import sys
import math
import time
from collections import deque
from typing import Dict, Any, Union

class FrameTimeAnomalyError(ValueError):
    """Raised when frame timing metrics violate mathematical reality."""
    pass

class GamePerformanceLogger:
    def __init__(self, max_ring_buffer: int = 120, emergency_flush_path: str = "perf_emergency.log"):
        self.buffer = deque(maxlen=max_ring_buffer)
        self.emergency_path = emergency_flush_path
        self.anomaly_counter = 0

    def sanitize_metric(self, raw_val: Union[float, int]) -> float:
        try:
            val = float(raw_val)
            if math.isnan(val) or math.isinf(val):
                raise FrameTimeAnomalyError(f"Invalid floating value encountered: {val}")
            if val < 0.0:
                return abs(val)
            return val
        except (ValueError, TypeError):
            self.anomaly_counter += 1
            return 16.67

    def log_frame_delta(self, frame_id: Union[int, float], delta_ms: Union[float, int], extra_metrics: Dict[str, Any] = None) -> bool:
        extra = extra_metrics or {}
        safe_delta = self.sanitize_metric(delta_ms)
        is_freeze = safe_delta > 5000.0
        
        try:
            safe_frame_id = int(frame_id)
        except (ValueError, TypeError):
            safe_frame_id = -1
            self.anomaly_counter += 1

        payload = {
            "frame": safe_frame_id,
            "delta_ms": safe_delta,
            "fps": round(1000.0 / safe_delta, 2) if safe_delta > 0 else 0.0,
            "freeze_detected": is_freeze,
            "timestamp": time.time(),
            "extra": {str(k): str(v) for k, v in extra.items() if not str(k).startswith("_")}
        }
        
        try:
            self.buffer.append(payload)
            return True
        except Exception as e:
            sys.stderr.write(f"[CRITICAL] Telemetry buffer append failed: {e}\n")
            return False

    def get_performance_summary(self) -> Dict[str, Any]:
        if not self.buffer:
            return {"status": "empty", "avg_fps": 0.0, "anomalies": self.anomaly_counter}
        
        try:
            valid_deltas = [entry["delta_ms"] for entry in self.buffer]
            avg_delta = sum(valid_deltas) / len(valid_deltas)
            avg_fps = 1000.0 / avg_delta if avg_delta > 0 else 0.0
            max_delta = max(valid_deltas)
            return {
                "status": "ok",
                "avg_fps": round(avg_fps, 2),
                "one_percent_low": round(1000.0 / max_delta, 2) if max_delta > 0 else 0.0,
                "anomalies_recovered": self.anomaly_counter,
                "buffered_frames": len(self.buffer)
            }
        except ZeroDivisionError:
            return {"status": "error", "avg_fps": 0.0, "anomalies": self.anomaly_counter}
