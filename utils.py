import logging
import functools
from typing import Callable, Any

logger = logging.getLogger('game-performance-70')

class PerformanceBoundaryError(Exception):
    """Raised when game metrics drift into unplayable zones."""
    pass

def robust_execution(default_value: Any = None):
    """Decorator to swallow engine-breaking edge cases with grace."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ZeroDivisionError, TypeError, ValueError) as e:
                logger.error(f'Edge case detected in {func.__name__}: {e}')
                return default_value
            except Exception as e:
                logger.critical(f'Critical system rupture: {e}')
                raise PerformanceBoundaryError(f'Engine state corrupted in {func.__name__}') from e
        return wrapper
    return decorator

@robust_execution(default_value=0.0)
def calculate_fps(frame_time_ms: float) -> float:
    """Calculate frames per second with division safety."""
    if frame_time_ms <= 0:
        raise ValueError('Frame time must be positive')
    return 1000.0 / frame_time_ms

def validate_resource_bounds(value: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
    """Clamp values to maintain stable game simulation states."""
    if not isinstance(value, (int, float)):
        return min_val
    return max(min_val, min(value, max_val))