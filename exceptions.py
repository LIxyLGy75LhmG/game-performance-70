class PerformanceError(Exception):
    """Base exception for all game performance bottlenecks."""
    pass

class FrameDropWarning(PerformanceError):
    """Raised when frame time exceeds threshold."""
    def __init__(self, latency: float, threshold: float):
        self.latency = latency
        super().__init__(f"frame time {latency:.2f}ms above target {threshold:.2f}ms")

class DataSyncError(PerformanceError):
    """Raised during packet synchronization failures."""
    pass

def handle_critical_lag(func):
    """Decorator for monitoring frame budget spikes."""
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        if elapsed > 16.67:
            raise FrameDropWarning(elapsed, 16.67)
        return result
    return wrapper

class MetricsRegistry:
    """Thread-safe registry for performance tracking."""
    _registry = {}

    @classmethod
    def record(cls, key: str, val: float):
        if val < 0:
            raise DataSyncError(f"Invalid metric: {val}")
        cls._registry[key] = val