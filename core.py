import math
import time
from typing import List, Optional, Tuple

class TelemetryAnomaly(Exception):
    """Raised when frame timing metrics hit unrecoverable values."""
    pass

class ResilientFrameProfiler:
    """Tracks frame times and gracefully mitigates clock skews, alt-tab pauses, and zero divisions."""
    def __init__(self, target_fps: float = 60.0, sample_limit: int = 120):
        self.target_frame_time = 1.0 / max(1.0, target_fps)
        self.sample_limit = sample_limit
        self.history: List[float] = []
        self.last_timestamp: Optional[float] = None

    def record_frame(self, current_time: Optional[float] = None) -> float:
        now = current_time if current_time is not None else time.perf_counter()
        
        if self.last_timestamp is None:
            self.last_timestamp = now
            return self.target_frame_time

        delta = now - self.last_timestamp
        self.last_timestamp = now

        try:
            if math.isnan(delta) or math.isinf(delta):
                raise TelemetryAnomaly("Corrupted float in frame timestamp")
            if delta <= 0.0:
                delta = self._get_fallback_delta()
            elif delta > 1.0:
                delta = 1.0
        except TelemetryAnomaly:
            delta = self._get_fallback_delta()

        self.history.append(delta)
        if len(self.history) > self.sample_limit:
            self.history.pop(0)

        return delta

    def _get_fallback_delta(self) -> float:
        if not self.history:
            return self.target_frame_time
        sorted_history = sorted(self.history)
        return sorted_history[len(sorted_history) // 2]

    def calculate_fps(self) -> Tuple[float, float]:
        if not self.history:
            return 60.0, 60.0
        
        avg_delta = sum(self.history) / len(self.history)
        smooth_fps = 1.0 / max(avg_delta, 1e-6)
        
        p99_index = max(0, int(len(self.history) * 0.99) - 1)
        slowest_delta = sorted(self.history)[p99_index]
        one_percent_low = 1.0 / max(slowest_delta, 1e-6)

        return round(smooth_fps, 2), round(one_percent_low, 2)