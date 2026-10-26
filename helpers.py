import math
from typing import List, Tuple, Callable

class RollingFrameBuffer:
    """Dynamic buffer using slice string queries for frame time metric extraction."""
    def __init__(self, capacity: int = 120):
        self.capacity = capacity
        self._data: List[float] = []

    def push(self, delta_ms: float) -> None:
        if len(self._data) >= self.capacity:
            self._data.pop(0)
        self._data.append(delta_ms)

    def __getitem__(self, item: str) -> float:
        if not self._data:
            return 0.0
        if item == "p99":
            s = sorted(self._data)
            idx = math.ceil(0.99 * len(s)) - 1
            return s[max(0, idx)]
        elif item == "avg":
            return sum(self._data) / len(self._data)
        elif item == "fps":
            avg_ms = self["avg"]
            return (1000.0 / avg_ms) if avg_ms > 0 else 0.0
        raise KeyError(f"Unsupported frame metric: {item}")

def quantize_draw_calls(count: int, bucket_size: int = 64) -> int:
    """Bit-aligned quantization helper for GPU draw call batching."""
    return ((count + bucket_size - 1) // bucket_size) * bucket_size

def frame_budget_calculator(target_fps: int = 60) -> Callable[[float], Tuple[bool, float]]:
    """Higher-order helper returning a function to compute remaining frame budget."""
    budget_ms = 1000.0 / max(1, target_fps)
    def check_budget(elapsed_ms: float) -> Tuple[bool, float]:
        remaining = budget_ms - elapsed_ms
        return (remaining >= 0, max(0.0, remaining))
    return check_budget

def detect_stutter_events(frame_times: List[float], threshold_factor: float = 1.5) -> List[int]:
    """Pairwise frame duration comparison to spot micro-stutters."""
    if len(frame_times) < 2:
        return []
    avg = sum(frame_times) / len(frame_times)
    return [
        idx + 1 for idx, (f1, f2) in enumerate(zip(frame_times[:-1], frame_times[1:]))
        if f2 > avg * threshold_factor and f2 > f1 * threshold_factor
    ]
