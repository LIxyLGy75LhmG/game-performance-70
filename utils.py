import time
import random
from functools import wraps
from typing import Callable, Any, Tuple


class NetworkGlitchError(Exception):
    """Raised when game frame network sync fails."""
    pass


def _calculate_jitter_delay(attempt: int, base_delay: float, max_delay: float) -> float:
    """Calculate exponential backoff with pseudo frame-tick jitter."""
    raw_delay = base_delay * (2 ** (attempt - 1))
    jitter = random.uniform(0.85, 1.25)
    return min(raw_delay * jitter, max_delay)


def retry_net_op(
    exceptions: Tuple[type[Exception], ...] = (ConnectionError, TimeoutError, NetworkGlitchError),
    max_attempts: int = 4,
    base_delay: float = 0.05,
    max_delay: float = 1.0
) -> Callable:
    """Decorator providing backoff retries for game network packets."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    last_error = exc
                    if attempt < max_attempts:
                        delay = _calculate_jitter_delay(attempt, base_delay, max_delay)
                        time.sleep(delay)
            if last_error:
                raise last_error
        return wrapper
    return decorator


@retry_net_op(max_attempts=3, base_delay=0.02)
def sync_player_frame(frame_id: int, packet_data: dict) -> bool:
    """Simulate network transmission for game state sync."""
    if random.random() < 0.4:
        raise NetworkGlitchError(f"Frame {frame_id} lost in transit")
    return True
