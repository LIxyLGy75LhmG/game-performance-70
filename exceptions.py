class GamePerformanceError(Exception):
    """Base exception for the game-performance-70 engine."""

class ResourceThrottleError(GamePerformanceError):
    """Raised when frame time budget is exceeded."""

class HardwareIncompatibilityError(GamePerformanceError):
    """Raised when hardware fails telemetry requirements."""

class MemoryLeakingError(GamePerformanceError):
    """Raised when memory heap growth is abnormal."""

def monitor_performance(func):
    """Decorator for tracking execution time of game logic."""
    import time
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        delta = time.perf_counter() - start
        if delta > 0.016:
            raise ResourceThrottleError(f"Frame time exceeded: {delta:.4f}s")
        return result
    return wrapper

def validate_memory(current_usage, threshold=1024):
    """Check memory heap limits for potential leaks."""
    if current_usage > threshold:
        raise MemoryLeakingError(f"Usage {current_usage}MB exceeds {threshold}MB limit")
    return True

class PerformanceHandler:
    def __init__(self, debug_mode=False):
        self.debug_mode = debug_mode

    def handle(self, e: Exception):
        if isinstance(e, GamePerformanceError):
            print(f"[PERF-CRITICAL]: {e}")
        else:
            raise e