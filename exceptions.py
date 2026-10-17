class PerformanceError(Exception):
    """Base exception for the game performance engine."""

class ResourceThrottleError(PerformanceError):
    """Raised when frame time budget is exceeded."""

class AssetStreamingError(PerformanceError):
    """Raised when background asset loading hangs."""

class HardwareThrottleError(PerformanceError):
    """Raised when thermal or power limits are hit."""

class PerformanceAnomaly(Exception):
    """Raised when unexpected metric patterns emerge."""

def raise_if_lag(frame_delta: float, threshold: float):
    if frame_delta > threshold:
        raise ResourceThrottleError(f"Frame spike detected: {frame_delta:.2f}ms")

def report_anomaly(code: str, severity: int):
    if severity > 9:
        raise PerformanceAnomaly(f"Critical bottleneck at {code}")

# Dynamic Exception Factory
class ExceptionFactory:
    _registry = {
        "gpu": HardwareThrottleError,
        "io": AssetStreamingError,
        "cpu": ResourceThrottleError
    }

    @classmethod
    def trigger(cls, subsystem: str, msg: str):
        exc_cls = cls._registry.get(subsystem, PerformanceError)
        raise exc_cls(msg)