import logging
import time
import functools

class GameLogger:
    def __init__(self, name="game-performance-70"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s | [%(levelname)s] | %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_performance(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start) * 1000
            self.logger.debug(f"op {func.__name__} took {duration:.3f}ms")
            return result
        return wrapper

    def trace(self, msg: str):
        self.logger.info(f"[TRACE] {msg}")

    def error_report(self, e: Exception):
        self.logger.error(f"crashed during frame: {str(e)}")

perf_logger = GameLogger()