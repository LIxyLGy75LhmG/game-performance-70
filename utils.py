import time
import functools
from typing import Callable, Any

def frame_budget_guard(ms_limit: float):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start) * 1000
            if duration > ms_limit:
                print(f'[WARN] {func.__name__} took {duration:.2f}ms, exceeding budget of {ms_limit}ms')
            return result
        return wrapper
    return decorator

class TelemetryBuffer:
    def __init__(self, capacity: int = 100):
        self.capacity = capacity
        self.buffer = []

    def ingest(self, entry: dict[str, Any]) -> None:
        self.buffer.append({**entry, 'ts': time.time()})
        if len(self.buffer) > self.capacity:
            self.buffer.pop(0)

    def flush_csv(self, filename: str = 'metrics.csv') -> None:
        if not self.buffer: return
        keys = self.buffer[0].keys()
        with open(filename, 'a') as f:
            f.write(','.join(keys) + '\n')
            for row in self.buffer:
                f.write(','.join(map(str, row.values())) + '\n')
        self.buffer.clear()

def normalize_vector(v: tuple[float, ...]) -> tuple[float, ...]:
    mag = sum(x**2 for x in v)**0.5
    return tuple(x / mag if mag > 0 else 0.0 for x in v)