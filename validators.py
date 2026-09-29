import functools
from typing import Any, Callable, Dict

class PerformanceGuard:
    """Enforces strict latency constraints on high-frequency gaming telemetry."""
    def __init__(self, ms_threshold: float = 16.67):
        self.ms_threshold = ms_threshold

    def __call__(self, func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import time
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = (time.perf_counter() - start) * 1000
            if elapsed > self.ms_threshold:
                print(f"[PERF] {func.__name__} spiked to {elapsed:.2f}ms")
            return result
        return wrapper

def validate_game_state(data: Dict[str, Any]) -> bool:
    """Checks packet structure for competitive integrity."""
    required = {'player_id', 'pos_x', 'pos_y', 'timestamp'}
    return all(key in data for key in required) and isinstance(data['pos_x'], (int, float))

def sanitize_input(val: Any) -> float:
    """Forces numeric bounds for coordinate packets."""
    try:
        return float(max(min(val, 9999.0), -9999.0))
    except (ValueError, TypeError):
        return 0.0