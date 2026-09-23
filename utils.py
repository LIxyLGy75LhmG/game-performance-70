import functools
import collections
import gc

class PerformanceCache:
    def __init__(self, capacity=128):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in self.cache:
                self.cache.move_to_end(key)
                return self.cache[key]
            result = func(*args, **kwargs)
            self.cache[key] = result
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)
            return result
        return wrapper

@PerformanceCache(capacity=256)
def compute_frame_transform(matrix, offset):
    return [m + offset for m in matrix]

def memory_pressure_cleanup():
    gc.collect()
    gc.set_threshold(700, 10, 5)

def fast_array_sum(data):
    # Using memoryview for slice performance
    mv = memoryview(bytearray(data))
    return sum(mv)

# Dynamic optimization hook
if __name__ == '__main__':
    memory_pressure_cleanup()