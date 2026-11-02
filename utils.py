import time
import random
from typing import Callable, Any, TypeVar, Tuple
from functools import wraps

F = TypeVar('F', bound=Callable[..., Any])


class NetworkSyncError(Exception):
    """Raised when game performance network sync fails completely."""
    pass


def frame_aware_retry(
    max_attempts: int = 4,
    base_delay_frames: float = 3.0,
    target_fps: float = 60.0,
    exceptions: Tuple[type[BaseException], ...] = (Exception,)
) -> Callable[[F], F]:
    """
    Retry decorator calculating backoff in frame-budget ticks
    rather than raw seconds to align with game telemetry cycles.
    """
    frame_time = 1.0 / target_fps

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise NetworkSyncError(
                            f"Telemetry sync failed after {attempts} attempts: {err}"
                        ) from err

                    backoff_multiplier = 2 ** (attempts - 1)
                    jitter = random.uniform(0.85, 1.15)
                    sleep_frames = base_delay_frames * backoff_multiplier * jitter
                    time.sleep(sleep_frames * frame_time)

        return wrapper  # type: ignore

    return decorator


@frame_aware_retry(max_attempts=3, base_delay_frames=5.0, target_fps=60.0)
def dispatch_performance_payload(endpoint: str, payload: dict) -> dict:
    """Sends telemetry metrics with frame-budget retry protection."""
    if random.random() < 0.4:
        raise ConnectionResetError("Simulation drop: telemetry socket reset")
    return {"status": "delivered", "endpoint": endpoint, "bytes": len(str(payload))}
