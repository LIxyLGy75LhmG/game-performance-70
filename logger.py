import time
import threading
from collections import deque

class PerformanceLogger:
    def __init__(self, max_buffer=1000):
        self.buffer = deque(maxlen=max_buffer)
        self.lock = threading.Lock()
        self.start_times = {}

    def track(self, event_name):
        self.start_times[event_name] = time.perf_counter()

    def report(self, event_name):
        end = time.perf_counter()
        start = self.start_times.pop(event_name, end)
        duration = (end - start) * 1000
        with self.lock:
            self.buffer.append((event_name, duration))

    def get_stats(self):
        with self.lock:
            if not self.buffer: return {}
            data = list(self.buffer)
            return {
                "avg": sum(d for _, d in data) / len(data),
                "max": max(d for _, d in data),
                "count": len(data)
            }

perf_logger = PerformanceLogger()