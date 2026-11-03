import time
from functools import wraps
from typing import Any, Callable, Dict

class GameMetricCollector:
    def __init__(self):
        self.telemetry: Dict[str, list] = {}

    def record(self, key: str, value: float):
        if key not in self.telemetry:
            self.telemetry[key] = []
        self.telemetry[key].append((time.perf_counter(), value))

    def get_avg(self, key: str) -> float:
        data = [v for _, v in self.telemetry.get(key, [])]
        return sum(data) / len(data) if data else 0.0

    def purge(self):
        self.telemetry.clear()

def frame_budget_guard(ms_limit: float):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start) * 1000
            if duration > ms_limit:
                print(f"Warning: {func.__name__} exceeded {ms_limit}ms: {duration:.2f}ms")
            return result
        return wrapper
    return decorator

def serialize_state(data: Dict[str, Any]) -> str:
    return "|".join(f"{k}:{v}" for k, v in sorted(data.items()))

class RollingBuffer:
    def __init__(self, size: int):
        self.size = size
        self.buffer = [0.0] * size
        self.idx = 0

    def push(self, val: float):
        self.buffer[self.idx] = val
        self.idx = (self.idx + 1) % self.size

    def mean(self) -> float:
        return sum(self.buffer) / self.size