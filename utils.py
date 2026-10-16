import functools
import random
import time
from typing import Any, Callable, Tuple, Type


class NetworkSyncError(Exception):
    """Raised when game state or telemetry payload fails to synchronize."""
    pass


def frame_budget_backoff(max_retries: int = 4, base_frame_ms: float = 0.016):
    """Yields retry delays scaled around target frame rates (e.g. 16ms for 60 FPS)."""
    for attempt in range(max_retries):
        multiplier = 2 ** attempt
        jitter = random.uniform(0.75, 1.25)
        yield base_frame_ms * multiplier * jitter


def retry_network_dispatch(
    max_retries: int = 4,
    catch_exceptions: Tuple[Type[Exception], ...] = (ConnectionError, TimeoutError)
) -> Callable:
    """Decorator wrapping unreliable network payloads with frame-paced exponential retries."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delays = frame_budget_backoff(max_retries=max_retries)
            for attempt_idx, delay in enumerate(delays, start=1):
                try:
                    return func(*args, **kwargs)
                except catch_exceptions as error:
                    if attempt_idx == max_retries:
                        raise NetworkSyncError(
                            f"Network operation '{func.__name__}' failed after {max_retries} attempts."
                        ) from error
                    time.sleep(delay)
        return wrapper
    return decorator


@retry_network_dispatch(max_retries=3)
def transmit_telemetry_packet(packet_id: int, payload: dict) -> bool:
    """Simulates sending performance telemetry data to game server."""
    if random.random() < 0.5:
        raise ConnectionError(f"Packet {packet_id} transmission timed out")
    return True
