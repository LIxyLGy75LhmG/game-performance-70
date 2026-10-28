import time
import functools
import random
import logging

logger = logging.getLogger('game-performance-70')

def retry_network_op(max_attempts=3, base_delay=0.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f'Op failed after {max_attempts} tries: {e}')
                        raise
                    jitter = random.uniform(0, 0.1 * base_delay)
                    sleep_time = (base_delay * (2 ** (attempts - 1))) + jitter
                    time.sleep(sleep_time)
            return None
        return wrapper
    return decorator

@retry_network_op(max_attempts=4)
def fetch_server_metrics(endpoint):
    # Simulate volatile network state
    if random.random() < 0.7:
        raise ConnectionError('Packet loss detected')
    return {'fps': 144, 'ping': 20}