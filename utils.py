import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger('game-performance-70')

def retry_network_op(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Adaptive exponential backoff for jittery network calls."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries - 1:
                        logger.error(f'Critical failure after {retries} attempts: {e}')
                        raise
                    logger.warning(f'Attempt {attempt + 1} failed, retrying in {current_delay}s...')
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

def pulse_connection(check_func: Callable):
    """Decorator that wraps networking in a resilience layer."""
    return retry_network_op(retries=5, delay=0.5)(check_func)