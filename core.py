import time
from typing import Callable, Any, Dict

def throttle(interval: float):
    def decorator(func: Callable):
        last_called = [0.0]
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            if now - last_called[0] >= interval:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def memoize_with_ttl(ttl: float):
    cache: Dict[tuple, tuple] = {}
    def decorator(func: Callable):
        def wrapper(*args):
            now = time.time()
            if args in cache:
                result, timestamp = cache[args]
                if now - timestamp < ttl:
                    return result
            result = func(*args)
            cache[args] = (result, now)
            return result
        return wrapper
    return decorator

def frame_budget(limit_ms: float):
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = (time.perf_counter() - start) * 1000
            if elapsed > limit_ms:
                print(f'warning: frame budget exceeded by {elapsed - limit_ms:.2f}ms')
            return result
        return wrapper
    return decorator

def clamp(val: float, min_val: float, max_val: float) -> float:
    return max(min_val, min(val, max_val))