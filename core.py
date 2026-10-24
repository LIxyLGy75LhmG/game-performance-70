from typing import Dict, List, Optional, Final

CACHE_SIZE: Final[int] = 1024

class FrameProcessor:
    """Calculates performance metrics from raw frame telemetry data."""

    def __init__(self, target_fps: int = 60) -> None:
        self.target_fps: int = target_fps
        self.history: List[float] = []

    def ingest_frame_time(self, ms: float) -> None:
        """Adds a new frame duration in milliseconds to the history buffer."""
        self.history.append(ms)
        if len(self.history) > CACHE_SIZE:
            self.history.pop(0)

    def get_avg_latency(self) -> float:
        """Computes the arithmetic mean of cached frame latencies."""
        if not self.history:
            return 0.0
        return sum(self.history) / len(self.history)

    def assess_health(self, threshold_ms: float = 16.6) -> Dict[str, bool]:
        """Evaluates if current performance adheres to frame time budget."""
        avg = self.get_avg_latency()
        return {"stable": avg <= threshold_ms, "jitter": avg > threshold_ms * 1.5}

def process_stream(data: List[float]) -> Optional[float]:
    """Batch analysis of frame telemetry streams."""
    if not data:
        return None
    return float(sum(data) / len(data))

# Dynamic frame analysis initialization
engine = FrameProcessor(target_fps=144)