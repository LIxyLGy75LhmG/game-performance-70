import sys
import os
import time
import json
from typing import Any, Dict, Optional

class TelemetryLogger:
    def __init__(self, primary_path: str = "game_perf.log", max_retries: int = 3):
        self.primary_path = primary_path
        self.fallback_path = f"fallback_{int(time.time())}.log"
        self.max_retries = max_retries
        self._emergency_stream = sys.stderr

    def _safe_serialize(self, data: Dict[str, Any]) -> str:
        try:
            return json.dumps(data, default=lambda o: f"<unserializable {type(o).__name__}>")
        except Exception:
            return json.dumps({"status": "corrupt_payload", "timestamp": time.time()})

    def log_frame_metric(self, frame_id: int, fps: float, metrics: Optional[Dict[str, Any]] = None) -> bool:
        payload = {
            "frame": frame_id,
            "fps": max(0.0, float(fps)) if isinstance(fps, (int, float)) else 0.0,
            "ts": time.time(),
            "details": metrics or {}
        }
        
        serialized = self._safe_serialize(payload) + "\n"
        
        for attempt in range(self.max_retries):
            target = self.primary_path if attempt == 0 else self.fallback_path
            try:
                with open(target, "a", encoding="utf-8") as f:
                    f.write(serialized)
                    f.flush()
                return True
            except (IOError, OSError, PermissionError):
                if attempt == self.max_retries - 1:
                    try:
                        self._emergency_stream.write(f"[EMERGENCY_LOG] {serialized}")
                        self._emergency_stream.flush()
                        return True
                    except Exception:
                        return False
            except Exception:
                pass
        return False
