import gc
import time
import logging
from typing import Any, Callable

logger = logging.getLogger('game-performance-70')

class PerformanceManager:
    """Context manager for resource cleanup during game cycles."""
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.purge_unused_assets()

    @staticmethod
    def purge_unused_assets() -> None:
        start = time.perf_counter()
        gc.collect()
        duration = time.perf_counter() - start
        logger.debug(f"garbage collection finished in {duration:.4f}s")

def throttle_calls(seconds: float = 0.1):
    """Decorator to prevent function spamming in the main loop."""
    def decorator(func: Callable):
        last_call = 0.0
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal last_call
            now = time.time()
            if now - last_call > seconds:
                last_call = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def sanitize_frame_delta(delta: float, cap: float = 0.5) -> float:
    """Ensures frame updates never exceed the cap."""
    return min(float(delta), cap)