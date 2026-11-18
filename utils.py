import time
import functools
import random
import logging

logger = logging.getLogger('game-performance-70')

def retry_network_op(max_attempts=3, base_delay=0.5, backoff=2.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = base_delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f'Critical network failure after {attempts} attempts')
                        raise e
                    
                    jitter = random.uniform(0, 0.1 * current_delay)
                    sleep_time = current_delay + jitter
                    logger.warning(f'Network retry {attempts}/{max_attempts} in {sleep_time:.2f}s')
                    time.sleep(sleep_time)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_network_op(max_attempts=4)
def fetch_game_data(endpoint):
    # Simulate volatile network state
    if random.random() < 0.7:
        raise ConnectionError('Packet loss detected')
    return {'status': 'success', 'endpoint': endpoint}