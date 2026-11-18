import time
import functools
import logging

def time_execution(func):
    """Decorator for tracking performance-critical game loops."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        if (duration := end - start) > 0.016:
            logging.warning(f"Slow frame {func.__name__}: {duration:.4f}s")
        return result
    return wrapper

def throttled(interval: float):
    """Prevents function flooding in real-time game logic."""
    def decorator(func):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if time.perf_counter() - last_called[0] > interval:
                last_called[0] = time.perf_counter()
                return func(*args, **kwargs)
        return wrapper
    return decorator

def clamp(value: float, min_val: float, max_val: float) -> float:
    """Restrict numerical values for game engine bounds."""
    return max(min_val, min(value, max_val))

def chunk_list(data: list, size: int):
    """Partition asset loading batches."""
    for i in range(0, len(data), size):
        yield data[i:i + size]