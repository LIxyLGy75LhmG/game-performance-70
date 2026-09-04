class GamePerformanceError(Exception):
    """Base exception for all game performance metrics issues."""

class TelemetryDataError(GamePerformanceError):
    """Raised when incoming telemetry data is malformed or missing."""

class LatencySpikeDetected(GamePerformanceError):
    """Raised when frame latency exceeds defined threshold."""

class AssetLoadTimeout(GamePerformanceError):
    """Raised when critical game assets fail to load in time."""

class PerformanceConstraintViolation(GamePerformanceError):
    """Custom exception for hardware-specific threshold breaches."""

def raise_if_lagging(latency_ms: float, threshold: float = 16.6) -> None:
    if latency_ms > threshold:
        raise LatencySpikeDetected(f"Frame latency {latency_ms}ms exceeded {threshold}ms threshold")

def validate_telemetry_payload(data: dict) -> None:
    required = {'frame_time', 'fps', 'gpu_temp'}
    if not all(key in data for key in required):
        raise TelemetryDataError(f"Missing required keys: {required - data.keys()}")

class PerformanceGuard:
    def __init__(self, limit: float):
        self.limit = limit

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            return False
        return True