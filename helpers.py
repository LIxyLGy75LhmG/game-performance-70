import functools
import time
import collections

def frame_rate_throttle(limit=60):
    interval = 1.0 / limit
    last_call = [0.0]
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.perf_counter() - last_call[0]
            if elapsed < interval:
                time.sleep(interval - elapsed)
            result = func(*args, **kwargs)
            last_call[0] = time.perf_counter()
            return result
        return wrapper
    return decorator

class DataCache:
    def __init__(self, max_size=128):
        self._cache = collections.OrderedDict()
        self.max_size = max_size

    def get_or_compute(self, key, compute_func):
        if key in self._cache:
            self._cache.move_to_end(key)
            return self._cache[key]
        
        val = compute_func()
        self._cache[key] = val
        self._cache.move_to_end(key)
        if len(self._cache) > self.max_size:
            self._cache.popitem(last=False)
        return val

def fast_math_inv_sqrt(n):
    if n <= 0: return 0
    return 1.0 / (n ** 0.5)

memoized_calculations = DataCache(256)