import sys
import json
import time
from collections import deque
from typing import Dict, Any, Optional

class PerformanceLogger:
    """Edge-case resilient frame telemetry logger for game engine metrics."""

    def __init__(self, max_buffer: int = 100, output_file: str = "perf_metrics.jsonl"):
        self._buffer = deque(maxlen=max_buffer)
        self._output_file = output_file
        self._fallback_active = False

    def log_frame_metric(self, frame_id: int, fps: float, gpu_temp: float, extra: Optional[Dict[str, Any]] = None) -> bool:
        try:
            # Graceful recovery for non-numeric or corrupted values
            safe_fps = float(fps) if isinstance(fps, (int, float, str)) and str(fps).replace('.', '', 1).isdigit() else 0.0
            safe_temp = float(gpu_temp) if isinstance(gpu_temp, (int, float)) else -1.0
            
            payload = {
                "timestamp": time.time_ns(),
                "frame": int(frame_id) if isinstance(frame_id, (int, float)) else -1,
                "fps": round(safe_fps, 2),
                "gpu_temp_c": round(safe_temp, 1),
                "meta": extra if isinstance(extra, dict) else {"raw_extra": str(extra)}
            }
            
            self._buffer.append(payload)
            self._flush_payload(payload)
            return True

        except Exception as err:
            self._handle_edge_failure(err, frame_id)
            return False

    def _flush_payload(self, payload: Dict[str, Any]) -> None:
        if self._fallback_active:
            sys.stderr.write(f"[FALLBACK METRIC] {json.dumps(payload)}\n")
            return

        try:
            with open(self._output_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(payload) + "\n")
        except (IOError, OSError, PermissionError):
            self._fallback_active = True
            sys.stderr.write("[WARN] Primary stream failed. Dropping to emergency stderr.\n")
            sys.stderr.write(f"[FALLBACK METRIC] {json.dumps(payload)}\n")

    def _handle_edge_failure(self, error: Exception, frame_id: Any) -> None:
        sys.stderr.write(f"[LOG FATAL] Malformed telemetry frame '{frame_id}': {type(error).__name__} - {error}\n")

    def dump_ring_buffer(self) -> list:
        return list(self._buffer)