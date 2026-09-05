class GamePerformanceError(Exception):
    """Base exception for game-performance-70 package."""

class DataStreamLatencyError(GamePerformanceError):
    """Raised when telemetry data arrival exceeds buffer limits."""

class FrameDropThresholdExceeded(GamePerformanceError):
    """Custom alert for hardware performance bottlenecks."""

def raise_if_bottleneck(fps, min_target=60):
    if fps < min_target:
        raise FrameDropThresholdExceeded(f"Performance drop detected: {fps} FPS")

def safe_data_process(data_stream):
    try:
        return [float(x) for x in data_stream]
    except (ValueError, TypeError) as e:
        raise DataStreamLatencyError(f"Corrupt telemetry packet: {e}")

class PerformanceSanitizer:
    def __init__(self, threshold):
        self.threshold = threshold
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is FrameDropThresholdExceeded:
            print(f"Warning: Performance intervention triggered: {exc_val}")
            return True