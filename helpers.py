import time
import functools
from typing import Callable, Any

def performance_throttle(interval: float):
    def decorator(func: Callable):
        last_called = 0
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            nonlocal last_called
            now = time.perf_counter()
            if now - last_called >= interval:
                last_called = now
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator

class ResourcePool:
    def __init__(self, capacity: int = 1024):
        self._stack = [object() for _ in range(capacity)]
        self.capacity = capacity

    def acquire(self):
        return self._stack.pop() if self._stack else None

    def release(self, item: Any):
        if len(self._stack) < self.capacity:
            self._stack.append(item)

def format_frame_metrics(fps: float, latency: float) -> str:
    metrics = {
        "fps": round(fps, 2),
        "latency_ms": round(latency * 1000, 3),
        "timestamp": time.time_ns()
    }
    return " | ".join(f"{k}={v}" for k, v in metrics.items())