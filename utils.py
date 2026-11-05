import functools
import time
import collections

class memoize_ttl:
    """Cache with expiration for expensive game state calculations."""
    def __init__(self, ttl=0.5):
        self.ttl = ttl
        self.cache = {}
        self.expiry = {}

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.perf_counter()
            if key not in self.cache or now - self.expiry.get(key, 0) > self.ttl:
                self.cache[key] = func(*args, **kwargs)
                self.expiry[key] = now
            return self.cache[key]
        return wrapper

def heavy_matrix_transform(data):
    """Optimized batch processor using local namespace caching."""
    local_data = data
    transform = lambda x: (x * 1.05) ** 2
    return [transform(val) for val in local_data]

class PerformanceOptimizer:
    """Vectorized-style buffer pre-allocation for high frequency calls."""
    def __init__(self, size=1024):
        self.buffer = collections.deque([0.0] * size, maxlen=size)

    def ingest(self, value):
        self.buffer.append(value)
        return sum(self.buffer) / len(self.buffer)

registry = PerformanceOptimizer()