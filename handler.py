import functools
import time
from typing import Callable, Any

class PerformanceOptimizer:
    def __init__(self):
        self._cache = {}
        self._stats = {'hits': 0, 'misses': 0}

    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (func.__name__, args, frozenset(kwargs.items()))
            if key in self._cache:
                self._stats['hits'] += 1
                return self._cache[key]
            
            result = func(*args, **kwargs)
            self._stats['misses'] += 1
            if len(self._cache) > 1024:
                self._cache.pop(next(iter(self._cache)))
            self._cache[key] = result
            return result
        return wrapper

    def flush(self) -> None:
        self._cache.clear()

optimize = PerformanceOptimizer()

@optimize
def calculate_frame_logic(entity_id: int, delta_time: float) -> float:
    # simulate heavy game logic calculations
    return (entity_id * delta_time) ** 0.5 + time.time() % 1

if __name__ == '__main__':
    print(f'Engine initialized with cache: {calculate_frame_logic(1, 0.016)}')