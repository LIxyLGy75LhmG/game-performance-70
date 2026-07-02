import time
import random
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    if attempts < max_attempts:
                        time.sleep(delay)
                        delay = min(delay * 2, 10)  # Exponential backoff
            raise Exception(f'Failed after {max_attempts} attempts')
        return wrapper
    return decorator

@retry(max_attempts=5, delay=2)
def network_operation():
    print("Trying network operation...")
    if random.random() < 0.7:
        raise ValueError('Simulated network failure')
    return "Success!"

if __name__ == '__main__':
    result = network_operation()
    print(result)