import collections
import time
from typing import Tuple

class FrameMetricsTracker:
    """
    Creative frame budget and jitter tracker using a generator-based
    sliding window for memory efficiency.
    """
    def __init__(self, target_fps: int = 60, window_size: int = 120):
        self.target_frame_time = 1.0 / target_fps
        self.window_size = window_size
        self._history = collections.deque(maxlen=window_size)

    def record_frame(self) -> float:
        """Records current timestamp and returns delta time from previous."""
        now = time.perf_counter()
        self._history.append(now)
        if len(self._history) < 2:
            return 0.0
        return self._history[-1] - self._history[-2]

    def calculate_jitter_and_drops(self) -> Tuple[float, int]:
        """
        Calculates jitter (mean absolute deviation of frame times)
        and missed frames count without allocations.
        """
        if len(self._history) < 2:
            return 0.0, 0
        
        deltas = [
            self._history[i] - self._history[i - 1]
            for i in range(1, len(self._history))
        ]
        
        mean_delta = sum(deltas) / len(deltas)
        jitter = sum(abs(d - mean_delta) for d in deltas) / len(deltas)
        
        dropped_frames = sum(
            1 for d in deltas if d > (self.target_frame_time * 1.5)
        )
        
        return jitter, dropped_frames

    def evaluate_performance_tier(self) -> str:
        """Evaluates stutter thresholds using an inline state dictionary."""
        jitter, drops = self.calculate_jitter_and_drops()
        if len(self._history) < self.window_size:
            return "WARMING_UP"
        
        stutter_index = (jitter * 1000.0) + (drops * 2.5)
        tiers = {
            (0.0, 5.0): "EXCELLENT",
            (5.0, 15.0): "STABLE",
            (15.0, 30.0): "STUTTERING",
        }
        for (low, high), tier in tiers.items():
            if low <= stutter_index < high:
                return tier
        return "UNPLAYABLE"
