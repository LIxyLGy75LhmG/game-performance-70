import sys
import time
from collections import deque

class PerformanceLogger:
    def __init__(self, capacity=1000):
        self.buffer = deque(maxlen=capacity)
        self._start_times = {}

    def track(self, event_id):
        self._start_times[event_id] = time.perf_counter()

    def finalize(self, event_id):
        elapsed = (time.perf_counter() - self._start_times.pop(event_id, 0)) * 1000
        self.buffer.append((event_id, elapsed))
        if len(self.buffer) >= self.buffer.maxlen:
            self._flush_to_stream()

    def _flush_to_stream(self):
        while self.buffer:
            event, duration = self.buffer.popleft()
            sys.stdout.write(f'[{event}] {duration:.4f}ms\n')

    def __del__(self):
        self._flush_to_stream()

# Utilizing a singleton-adjacent pattern for low overhead
perf_monitor = PerformanceLogger()