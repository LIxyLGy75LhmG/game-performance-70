import time
import functools
from typing import Callable, Any

class GamePerformanceLogger:
    def __init__(self, threshold_ms: float = 16.67):
        self.threshold = threshold_ms

    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = (time.perf_counter() - start) * 1000
            if elapsed > self.threshold:
                print(f'[FRAME DROPPED] {func.__name__} took {elapsed:.2f}ms')
            return result
        return wrapper

performance_monitor = GamePerformanceLogger()

def log_memory_usage(data: dict) -> None:
    total_size = sum(len(str(v)) for v in data.values())
    print(f'[MEMORY SNAPSHOT] heap state size: {total_size} bytes')

class TelemetryBuffer:
    def __init__(self, capacity: int = 100):
        self.buffer = []
        self.capacity = capacity

    def push(self, event: dict):
        self.buffer.append({**event, 'ts': time.time()})
        if len(self.buffer) > self.capacity:
            self.buffer.pop(0)

    def dump(self):
        return list(self.buffer)