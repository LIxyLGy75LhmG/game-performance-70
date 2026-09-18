import functools
import time

def validate_frame_budget(ms_limit=16.67):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start) * 1000
            if duration > ms_limit:
                print(f'[PERF WARNING] {func.__name__} took {duration:.2f}ms')
            return result
        return wrapper
    return decorator

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

def is_power_of_two(n):
    return (n & (n - 1) == 0) and n > 0

def sanitize_input(value, default, type_cast=int):
    try:
        return type_cast(value)
    except (ValueError, TypeError):
        return default

def check_memory_overhead(obj, threshold_bytes=1024):
    import sys
    size = sys.getsizeof(obj)
    return size < threshold_bytes, size