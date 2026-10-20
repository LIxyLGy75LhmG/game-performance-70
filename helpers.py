import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('game-performance-70')

def retry_network_call(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f'failed after {attempts} attempts: {e}')
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

# usage for jittery game connections
def robust_fetch(func):
    return retry_network_call(max_attempts=5, delay=0.5)(func)