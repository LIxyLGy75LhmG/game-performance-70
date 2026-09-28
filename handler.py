import functools
import time

class FrameOptimizer:
    def __init__(self, cache_size=128):
        self.cache = {}
        self.cache_size = cache_size

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in self.cache:
                return self.cache[key]
            result = func(*args, **kwargs)
            if len(self.cache) >= self.cache_size:
                self.cache.pop(next(iter(self.cache)))
            self.cache[key] = result
            return result
        return wrapper

class PerformanceHandler:
    def __init__(self, target_fps=60):
        self.frame_time = 1.0 / target_fps
        self.last_sync = time.perf_counter()

    def throttle(self, logic_func):
        """Executes logic with high-precision frame throttling"""
        def inner(*args, **kwargs):
            start = time.perf_counter()
            result = logic_func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            sleep_time = self.frame_time - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)
            return result
        return inner

def batch_process_entities(entities, transform):
    return [transform(e) for e in entities if e.get('active', True)]

optimized_handler = PerformanceHandler()