import functools
import time

def validate_frame_rate(fps_limit: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            target = 1.0 / fps_limit
            if duration < target:
                time.sleep(target - duration)
            return result
        return wrapper
    return decorator

def validate_asset_path(path: str) -> bool:
    allowed_ext = ('.png', '.json', '.wav', '.obj')
    return path.lower().endswith(allowed_ext) and '..' not in path

def validate_memory_usage(limit_mb: float):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import os
            import psutil
            process = psutil.Process(os.getpid())
            mem_before = process.memory_info().rss / 1024 / 1024
            result = func(*args, **kwargs)
            mem_after = process.memory_info().rss / 1024 / 1024
            if (mem_after - mem_before) > limit_mb:
                print(f"Warning: {func.__name__} exceeded memory threshold")
            return result
        return wrapper
    return decorator