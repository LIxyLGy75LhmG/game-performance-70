import time
import functools
import random
from typing import Callable, Any

def throttler(interval: float):
    def decorator(func: Callable):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - last_called[0] >= interval:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def jitter_delay(base: float, variation: float = 0.2):
    time.sleep(base + random.uniform(-variation, variation))

def memoize_frames(func: Callable):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def unpack_entity(entity_data: dict, keys: list[str]) -> list[Any]:
    return [entity_data.get(k) for k in keys]

def byte_formatter(size_bytes: int) -> str:
    if size_bytes == 0: return "0B"
    units = ("B", "KB", "MB", "GB", "TB")
    i = int(min(len(units)-1, (size_bytes.bit_length() - 1) // 10))
    return f"{size_bytes / (1024**i):.2f}{units[i]}"