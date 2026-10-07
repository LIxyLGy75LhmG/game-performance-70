import time
import functools
import collections

def throttle(interval):
    def decorator(func):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            if now - last_called[0] >= interval:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def memoize_lru(maxsize=128):
    return functools.lru_cache(maxsize=maxsize)

def frame_delta_calculator():
    history = collections.deque(maxlen=60)
    def get_delta():
        now = time.perf_counter()
        history.append(now)
        if len(history) < 2: return 0.0
        return (history[-1] - history[0]) / (len(history) - 1)
    return get_delta

def profile_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f'[PERF] {func.__name__} took {duration:.6f}s')
        return result
    return wrapper

def chunk_iterable(data, size):
    for i in range(0, len(data), size):
        yield data[i:i + size]