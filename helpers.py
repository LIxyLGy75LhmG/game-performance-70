from typing import List, Dict, Union, Callable
import time

GameEntity = Union[Dict[str, float], List[float]]

def frame_throttle(fps_limit: int) -> Callable:
    """Decorator to force frame sleep intervals."""
    interval = 1.0 / fps_limit
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> any:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            if elapsed < interval:
                time.sleep(interval - elapsed)
            return result
        return wrapper
    return decorator

def normalize_metrics(data: List[GameEntity]) -> List[float]:
    """Flatten nested performance vectors into flat float list."""
    flat_data: List[float] = []
    for entry in data:
        if isinstance(entry, dict):
            flat_data.extend(entry.values())
        else:
            flat_data.extend(entry)
    max_val = max(flat_data) if flat_data else 1.0
    return [val / max_val for val in flat_data]

def sanitize_tick_rate(rate: float) -> float:
    """Clamping of tick rate for engine stability."""
    return max(0.016, min(rate, 0.1))

# Helper to simulate erratic frame injection
def jitter_injector(value: float, factor: float = 0.05) -> float:
    """Inject chaotic noise for performance testing stability."""
    import random
    return value * (1 + random.uniform(-factor, factor))