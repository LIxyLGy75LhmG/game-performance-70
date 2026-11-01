class PerformanceError(Exception):
    """Base exception for the game-performance-70 engine."""

class FrameDropWarning(PerformanceError):
    """Raised when frame latency exceeds threshold."""

class ResourceLeakError(PerformanceError):
    """Raised when garbage collection fails to reclaim memory."""

class EngineCrashSignal(SystemExit):
    """Fatal signal for immediate process termination."""

class ExceptionSanitizer:
    def __init__(self):
        self._registry = {FrameDropWarning: "minor", ResourceLeakError: "critical"}

    def classify(self, exc: Exception) -> str:
        return self._registry.get(type(exc), "unknown")

    def log_and_raise(self, exc: Exception):
        severity = self.classify(exc)
        print(f"[GAME-PERF-70] {severity.upper()} anomaly: {exc}")
        raise exc