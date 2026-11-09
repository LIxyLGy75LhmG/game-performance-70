import time
import functools
from typing import Callable, Any

def frame_throttle(ms: int):
    def decorator(func: Callable):
        last_call = 0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_call
            now = time.perf_counter() * 1000
            if now - last_call >= ms:
                last_call = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def batch_process(items: list, size: int):
    for i in range(0, len(items), size):
        yield items[i:i + size]

def memory_cleanup(obj_dict: dict, threshold: int):
    if len(obj_dict) > threshold:
        keys = sorted(obj_dict.keys(), key=lambda k: getattr(obj_dict[k], 'last_used', 0))
        for i in range(len(obj_dict) - threshold):
            del obj_dict[keys[i]]

def calculate_fps(frame_times: list) -> float:
    if not frame_times:
        return 0.0
    return 1000.0 / (sum(frame_times) / len(frame_times))

class EntityProxy:
    def __init__(self, target):
        self._target = target
        self.last_used = time.time()

    def __getattr__(self, name):
        self.last_used = time.time()
        return getattr(self._target, name)