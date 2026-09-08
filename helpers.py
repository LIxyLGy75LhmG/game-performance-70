from typing import List, Dict, Union, Optional, Callable
import time

Metric = Dict[str, Union[float, int]]

def calculate_fps_drop(frames: List[float], threshold: float = 0.5) -> float:
    """Calculate performance dips below target threshold based on frame delta times."""
    if not frames:
        return 0.0
    dips = [f for f in frames if f > threshold]
    return (len(dips) / len(frames)) * 100

def frame_timer(func: Callable) -> Callable:
    """Decorator for measuring execution time of engine render loops."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return result, end - start
    return wrapper

class PerformanceBuffer:
    """Circular buffer for storing frame timings."""
    def __init__(self, size: int = 60):
        self.size = size
        self.data: List[float] = []

    def push(self, delta: float) -> None:
        """Append frame time and maintain buffer capacity."""
        self.data.append(delta)
        if len(self.data) > self.size:
            self.data.pop(0)

    def get_average(self) -> float:
        """Return mean frame time."""
        if not self.data:
            return 0.0
        return sum(self.data) / len(self.data)