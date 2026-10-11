import time
import functools
import logging

logger = logging.getLogger('game-performance-70')

def retry_operation(max_attempts=3, backoff=0.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    wait_time = backoff * (2 ** (attempt - 1))
                    logger.warning(f'Attempt {attempt} failed: {e}. Retrying in {wait_time}s...')
                    time.sleep(wait_time)
            logger.error(f'Operation failed after {max_attempts} attempts')
            raise last_exception
        return wrapper
    return decorator

class NetworkState:
    def __init__(self):
        self.latency_buffer = []

    @retry_operation(max_attempts=4, backoff=1.0)
    def fetch_server_ping(self, endpoint):
        # Simulation of jittery network hardware interaction
        import random
        if random.random() < 0.7:
            raise ConnectionError('Packet loss detected')
        return {'status': 'ok', 'latency': random.randint(10, 50)}