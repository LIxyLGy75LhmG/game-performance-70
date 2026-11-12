class GamePerformanceError(Exception):
    """Base exception for the game-performance-70 engine."""
    pass

class FrameDropWarning(GamePerformanceError):
    """Raised when frame time exceeds thresholds."""
    pass

class AssetLoadTimeout(GamePerformanceError):
    """Raised when async asset streaming hangs."""
    pass

class HardwareThrottleSignal(GamePerformanceError):
    """Raised when thermal throttling is detected."""
    pass

def raise_if_laggy(frame_time: float, threshold: float = 0.0166):
    if frame_time > threshold:
        raise FrameDropWarning(f"Frame time {frame_time:.4f}s exceeds {threshold}s limit")

def wrap_performance_check(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if isinstance(e, GamePerformanceError):
                raise
            raise GamePerformanceError(f"Performance engine anomaly: {str(e)}") from e
    return wrapper

class PerformanceGuard:
    def __init__(self, limit: float):
        self.limit = limit

    def __enter__(self):
        import time
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.perf_counter() - self.start
        if elapsed > self.limit:
            raise FrameDropWarning(f"Context block took {elapsed:.4f}s")