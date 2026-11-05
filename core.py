import time
import functools
import logging
from typing import Callable, Any

def performance_tracker(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'[PERF] {func.__name__} executed in {end_time - start_time:.6f}s')
        return result
    return wrapper

def frame_rate_limiter(target_fps: int) -> Callable:
    frame_duration = 1.0 / target_fps
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            sleep_time = frame_duration - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)
            return result
        return wrapper
    return decorator

def lazy_asset_loader(asset_path: str) -> dict:
    data = {'loaded': False, 'content': None}
    def loader():
        if not data['loaded']:
            data['content'] = f'raw_bytes_from_{asset_path}'
            data['loaded'] = True
        return data['content']
    return {'get': loader}

def clamp(val: float, min_val: float, max_val: float) -> float:
    return max(min_val, min(val, max_val))