import functools
import time

class PerformanceEngine:
    def __init__(self, cache_size=128):
        self.cache = {}
        self.cache_size = cache_size
        self.hits = 0
        self.misses = 0

    def memoize_frame(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in self.cache:
                self.hits += 1
                return self.cache[key]
            result = func(*args, **kwargs)
            if len(self.cache) >= self.cache_size:
                self.cache.pop(next(iter(self.cache)))
            self.cache[key] = result
            self.misses += 1
            return result
        return wrapper

def calculate_physics_vector(force, mass, time_delta):
    return (force / mass) * (time_delta ** 2)

engine = PerformanceEngine()
optimized_physics = engine.memoize_frame(calculate_physics_vector)

def process_frame_batch(entities, dt):
    results = []
    for entity in entities:
        state = optimized_physics(entity['force'], entity['mass'], dt)
        results.append(state)
    return results

if __name__ == '__main__':
    mock_data = [{'force': 10.0, 'mass': 1.0} for _ in range(1000)]
    output = process_frame_batch(mock_data, 0.016)
    print(f'Computed {len(output)} vectors with {engine.hits} cache hits.')