import logging
import functools
import time

# Custom high-performance performance logger
def performance_tracker(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        if elapsed > 16.67:
            logging.warning(f"Slow frame in {func.__name__}: {elapsed:.2f}ms")
        return result
    return wrapper

def get_logger(name: str):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

# Static instance for module-level usage
engine_logger = get_logger("game-engine")