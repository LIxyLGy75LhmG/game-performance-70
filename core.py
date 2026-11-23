import time
import functools
from typing import Callable, Any

def throttle_frame_rate(limit_hz: float):
    interval = 1.0 / limit_hz
    def decorator(func: Callable):
        last_exec = 0.0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_exec
            elapsed = time.perf_counter() - last_exec
            if elapsed >= interval:
                last_exec = time.perf_counter()
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator

def bitmask_check(val: int, flag: int) -> bool:
    return (val & flag) == flag

def interpolate(start: float, end: float, alpha: float) -> float:
    return start + (end - start) * min(max(alpha, 0.0), 1.0)

class PerformanceTracker:
    def __init__(self):
        self.snapshots = []

    def measure(self, func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            self.snapshots.append(time.perf_counter() - start)
            return result
        return wrapper

def vector_clamp(v: tuple[float, float], min_v: float, max_v: float) -> tuple[float, float]:
    return tuple(max(min(val, max_v), min_v) for val in v)