class PerformanceThresholdExceeded(Exception):
    """Raised when game loop latency spikes above 16ms."""
    def __init__(self, latency, target=16.67):
        self.latency = latency
        self.message = f"Frame drop: {latency:.2f}ms exceeds {target}ms budget"
        super().__init__(self.message)

class ResourceAllocationError(Exception):
    """Raised when memory pool for assets is exhausted."""
    def __init__(self, requested, available):
        self.message = f"Memory exhaustion: {requested}MB requested, {available}MB free"
        super().__init__(self.message)

class GraphicsContextLost(Exception):
    """Raised during unexpected GPU context switch or crash."""
    def __init__(self):
        super().__init__("Hardware acceleration context invalidated")

def monitor_performance(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = (time.perf_counter() - start) * 1000
        if duration > 16.67:
            raise PerformanceThresholdExceeded(duration)
        return result
    return wrapper