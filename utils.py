import time
import random
from functools import wraps

def retry(retries=3, backoff=1.0, max_delay=60):
    """Retry decorator with configurable parameters."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    if attempt < retries:
                        sleep_time = min(backoff * (2 ** (attempt - 1)), max_delay)
                        print(f'Attempt {attempt} failed: {e}, retrying in {sleep_time} seconds...')
                        time.sleep(sleep_time)
                    else:
                        print('All retries failed.')
                        raise
        return wrapper
    return decorator

@retry(retries=5, backoff=1)
def fetch_data_from_server(url):
    if random.choice([True, False]):  # Simulate success or failure
        raise ConnectionError('Simulated network failure.')
    return {'data': 'some data from ' + url}
