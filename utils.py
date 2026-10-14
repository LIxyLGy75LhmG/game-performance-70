import time
import functools
from collections import deque

class FrameBuffer:
    def __init__(self, size=60):
        self.data = deque(maxlen=size)

    def record(self, delta_time):
        self.data.append(delta_time)

    @property
    def average_fps(self):
        if not self.data:
            return 0.0
        avg = sum(self.data) / len(self.data)
        return 1.0 / avg if avg > 0 else 0.0

def throttle_input(interval_ms):
    def decorator(func):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            if (now - last_called[0]) * 1000 >= interval_ms:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def normalize_vector(vec):
    magnitude = sum(x**2 for x in vec)**0.5
    return tuple(x / magnitude for x in vec) if magnitude > 0 else vec

def batch_process_entities(entities, callback, batch_size=100):
    for i in range(0, len(entities), batch_size):
        batch = entities[i:i + batch_size]
        for entity in batch:
            callback(entity)
        time.sleep(0.001)