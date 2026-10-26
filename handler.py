from functools import wraps
import math
import time
from typing import Callable, Any, Dict


class TelemetryFaultHandler:
    """Decorator and interceptor to handle anomalous gaming telemetry metrics."""

    def __init__(self, fallback_fps: float = 60.0, max_delta_sec: float = 0.5):
        self.fallback_fps = fallback_fps
        self.max_delta_sec = max_delta_sec
        self._last_valid_timestamp = time.perf_counter()
        self._history: list = []

    def safe_frame_sample(self, func: Callable[..., Dict[str, Any]]) -> Callable[..., Dict[str, Any]]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Dict[str, Any]:
            now = time.perf_counter()
            dt = now - self._last_valid_timestamp

            try:
                metrics = func(*args, **kwargs)
                if not isinstance(metrics, dict):
                    raise ValueError("Metrics output must be a dictionary")

                raw_fps = metrics.get("fps", self.fallback_fps)
                if not isinstance(raw_fps, (int, float)) or math.isnan(raw_fps) or raw_fps <= 0 or math.isinf(raw_fps):
                    metrics["fps"] = self._compute_moving_average()
                    metrics["telemetry_fault"] = "invalid_fps_repaired"
                else:
                    self._history.append(float(raw_fps))
                    if len(self._history) > 30:
                        self._history.pop(0)

                if dt <= 0 or dt > self.max_delta_sec:
                    metrics["frame_time_ms"] = round(1000.0 / metrics["fps"], 3)
                    metrics["timing_anomaly"] = True
                else:
                    metrics["frame_time_ms"] = round(dt * 1000.0, 3)

            except Exception as err:
                metrics = {
                    "fps": self.fallback_fps,
                    "frame_time_ms": round(1000.0 / self.fallback_fps, 3),
                    "gpu_load_pct": 0.0,
                    "telemetry_fault": f"recovered_{type(err).__name__.lower()}",
                    "timing_anomaly": True,
                }

            self._last_valid_timestamp = now
            return metrics

        return wrapper

    def _compute_moving_average(self) -> float:
        if not self._history:
            return self.fallback_fps
        return round(sum(self._history) / len(self._history), 2)


fault_handler = TelemetryFaultHandler()


@fault_handler.safe_frame_sample
def poll_gpu_telemetry() -> Dict[str, Any]:
    return {"fps": float("nan"), "gpu_load_pct": 98.4}
