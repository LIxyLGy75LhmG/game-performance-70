class PerformanceError(Exception):
    """Base exception for the game-performance-70 engine."""
    pass

class ResourceExhaustionError(PerformanceError):
    """Raised when game assets consume too much heap."""
    def __init__(self, asset_id, usage):
        super().__init__(f"Asset {asset_id} exploded memory usage to {usage}MB")
        self.asset_id = asset_id

class FrameDropWarning(PerformanceError):
    """Custom notification for stuttering frames."""
    def __init__(self, delta_time):
        super().__init__(f"Frame spike detected: {delta_time:.2f}ms")

class ShaderCompilationError(PerformanceError):
    """Specialized exception for GPU pipeline failures."""
    def __init__(self, shader_name, gl_error):
        self.shader_name = shader_name
        self.gl_error = gl_error
        super().__init__(f"Shader compilation failed: {shader_name} [{gl_error}]")

def raise_if_laggy(delta, threshold=16.6):
    """Check if current performance breaches frame budget."""
    if delta > threshold:
        raise FrameDropWarning(delta)

def sanitize_performance_metrics(func):
    """Decorator for wrapping performance critical calls with exception logic."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PerformanceError as e:
            print(f"[PERF-CRIT]: {e}")
            raise
    return wrapper