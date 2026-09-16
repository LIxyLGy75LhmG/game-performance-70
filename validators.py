import functools
from typing import Any, Callable, Dict

def validate_telemetry(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        data = args[0] if args else kwargs.get('data', {})
        if not isinstance(data, dict):
            raise ValueError('Telemetry payload must be a mapping')
        required = {'fps', 'latency', 'gpu_temp'}
        if not required.issubset(data.keys()):
            missing = required - data.keys()
            raise KeyError(f'Missing telemetry fields: {missing}')
        return func(*args, **kwargs)
    return wrapper

class PerformanceSchema:
    """Validator for exotic game frame data structures"""
    @staticmethod
    @validate_telemetry
    def sanitize(payload: Dict[str, Any]) -> Dict[str, Any]:
        # Clamp values to logical engine bounds
        return {
            'fps': max(0, min(999, payload.get('fps', 60))),
            'latency': max(0, payload.get('latency', 0)),
            'gpu_temp': max(20, min(120, payload.get('gpu_temp', 50))),
            'meta': payload.get('meta', 'standard_frame')
        }

def frame_validator(func: Callable) -> Callable:
    return lambda *args, **kwargs: func(PerformanceSchema.sanitize(args[0]), **kwargs)