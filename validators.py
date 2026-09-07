import time
import functools
import random
import logging

logger = logging.getLogger('game-performance-70')

def jitter_retry(retries=3, delay=1.0, backoff=2.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            current_delay = delay
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f'failed after {retries} attempts')
                        raise e
                    
                    sleep_time = current_delay + random.uniform(0, 0.1 * current_delay)
                    logger.warning(f'attempt {attempt} failed, retrying in {sleep_time:.2f}s')
                    time.sleep(sleep_time)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

class NetworkValidator:
    @staticmethod
    @jitter_retry(retries=5, delay=0.5)
    def validate_connection(endpoint):
        # simulate network flap
        if random.random() < 0.7:
            raise ConnectionError('packet loss spike')
        return True