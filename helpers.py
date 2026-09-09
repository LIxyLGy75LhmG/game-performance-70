import time
from functools import wraps
from typing import Any, Callable, Dict

def frame_budget_guard(ms_limit: float = 16.67):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = (time.perf_counter() - start_time) * 1000
            if elapsed > ms_limit:
                print(f'[PERF] Warning: {func.__name__} exceeded budget: {elapsed:.2f}ms')
            return result
        return wrapper
    return decorator

class DataStreamOptimizer:
    def __init__(self, buffer_size: int = 10):
        self.cache: Dict[str, Any] = {}
        self.buffer_size = buffer_size

    def pack_game_state(self, entity_id: str, payload: Any) -> None:
        self.cache[entity_id] = (payload, time.time())
        if len(self.cache) > self.buffer_size:
            oldest = min(self.cache, key=lambda k: self.cache[k][1])
            del self.cache[oldest]

    def get_state_snapshot(self) -> Dict[str, Any]:
        return {k: v[0] for k, v in self.cache.items()}

def delta_compress(current: dict, previous: dict) -> dict:
    return {k: v for k, v in current.items() if previous.get(k) != v}

if __name__ == '__main__':
    optimizer = DataStreamOptimizer()
    optimizer.pack_game_state('player_1', {'x': 100, 'y': 200})
    print(f'Active state: {optimizer.get_state_snapshot()}')