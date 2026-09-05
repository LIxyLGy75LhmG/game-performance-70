import logging
import sys
import functools
from datetime import datetime

class PerformanceLogger:
    def __init__(self, name: str = "game_perf"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def monitor(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except MemoryError as e:
                self.logger.critical(f"Memory blowout during {func.__name__}: {e}")
                raise
            except Exception as e:
                self.logger.error(f"Unexpected frame failure in {func.__name__}: {type(e).__name__} -> {e}")
                return None
        return wrapper

    def log_stall(self, duration: float):
        if duration > 0.016:
            self.logger.warning(f"Frame stall detected: {duration:.4f}s exceeds threshold")

log = PerformanceLogger()