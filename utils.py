import math
from collections import deque
from typing import Dict, List


class FrameTelemetryBuffer:
    """A rolling window buffer for calculating gaming metrics like 1% low and 0.1% low FPS."""

    def __init__(self, max_samples: int = 1000):
        self.max_samples = max_samples
        self._frame_times: deque = deque(maxlen=max_samples)
        self._gpu_loads: deque = deque(maxlen=max_samples)

    def push_frame(self, frame_time_ms: float, gpu_load_pct: float) -> None:
        """Record frame duration in milliseconds and current GPU utilization."""
        if frame_time_ms <= 0:
            return
        self._frame_times.append(frame_time_ms)
        self._gpu_loads.append(max(0.0, min(100.0, gpu_load_pct)))

    def calculate_percentiles(self) -> Dict[str, float]:
        """Derive average FPS, 1% low FPS, 0.1% low FPS, and GPU bottleneck index."""
        if not self._frame_times:
            return {"avg_fps": 0.0, "low_1pct_fps": 0.0, "low_01pct_fps": 0.0, "gpu_bound_score": 0.0}

        sorted_ft = sorted(self._frame_times)
        count = len(sorted_ft)

        p1_index = max(0, count - math.ceil(count * 0.01))
        p01_index = max(0, count - math.ceil(count * 0.001))

        avg_ft = sum(sorted_ft) / count
        avg_fps = 1000.0 / avg_ft if avg_ft > 0 else 0.0

        p1_ft = sum(sorted_ft[p1_index:]) / len(sorted_ft[p1_index:])
        p01_ft = sum(sorted_ft[p01_index:]) / len(sorted_ft[p01_index:])

        low_1pct_fps = 1000.0 / p1_ft if p1_ft > 0 else 0.0
        low_01pct_fps = 1000.0 / p01_ft if p01_ft > 0 else 0.0

        gpu_avg = sum(self._gpu_loads) / len(self._gpu_loads)
        bottleneck_score = round((gpu_avg / 100.0) * (avg_fps / (low_1pct_fps + 1e-5)), 3)

        return {
            "avg_fps": round(avg_fps, 2),
            "low_1pct_fps": round(low_1pct_fps, 2),
            "low_01pct_fps": round(low_01pct_fps, 2),
            "gpu_bound_score": min(1.0, bottleneck_score),
        }


def quantify_stutter_index(frame_deltas: List[float], threshold_ms: float = 16.67) -> float:
    """Computes a custom non-linear stutter score based on variance over target threshold."""
    if len(frame_deltas) < 2:
        return 0.0
    spikes = [max(0.0, ft - threshold_ms) ** 1.5 for ft in frame_deltas]
    return round(sum(spikes) / len(frame_deltas), 4)
