from typing import Optional, Dict, Any

class PerformanceError(Exception):
    """Base exception class for game-performance-70 engine faults."""
    def __init__(self, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        self.context: Dict[str, Any] = context or {}
        super().__init__(f"{message} | Context: {self.context}")

class FrameDropWarning(PerformanceError):
    """Raised when frame delivery timings exceed budget threshold."""
    def __init__(self, fps: float, threshold: float) -> None:
        super().__init__("Critical frame drop detected", {"fps": fps, "threshold": threshold})

class ResourceExhaustionError(PerformanceError):
    """Triggered when heap allocation for assets hits limits."""
    def __init__(self, asset_id: str, mem_usage: int) -> None:
        super().__init__("GPU memory ceiling breached", {"asset": asset_id, "bytes": mem_usage})

class PipelineStallError(PerformanceError):
    """Raised when the command queue fails to flush."""
    def __init__(self, latency_ms: float) -> None:
        super().__init__("Render pipeline sync timeout", {"ms": latency_ms})

def handle_engine_fault(error: PerformanceError) -> None:
    """Standard entry point for logging engine-level exceptions."""
    payload: Dict[str, Any] = {"type": type(error).__name__, "data": error.context}
    print(f"[PERF_FAIL]: {payload}")