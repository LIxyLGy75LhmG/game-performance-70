import time
import random
from functools import wraps

def resilient_network(max_attempts=3, backoff=0.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    sleep_time = backoff * (2 ** (attempts - 1)) + random.uniform(0, 0.1)
                    time.sleep(sleep_time)
        return wrapper
    return decorator

@resilient_network(max_attempts=5)
def fetch_game_data(endpoint):
    # Simulate volatile network state
    if random.random() < 0.7:
        raise ConnectionError('Packet drop in game-performance-70 cluster')
    return {'status': 'success', 'data': 'payload'}