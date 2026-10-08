import functools
import logging

logger = logging.getLogger('game-performance-70')

class PerformanceValidationError(Exception):
    """Custom exception for anomalous gaming metrics."""
    pass

def validate_telemetry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result is None:
                raise PerformanceValidationError('Empty frame data detected')
            if not isinstance(result, (int, float)):
                raise PerformanceValidationError('Non-numeric performance metric')
            if result < 0:
                raise PerformanceValidationError('Negative frame timing anomaly')
            return result
        except Exception as e:
            logger.error(f'Edge case failure in {func.__name__}: {e}')
            return 0.0
    return wrapper

@validate_telemetry
def calculate_frame_time(ms_delta):
    return float(ms_delta)

@validate_telemetry
def parse_fps_cap(val):
    return int(val) if val else None