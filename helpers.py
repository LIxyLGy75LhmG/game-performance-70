import time
import random
import functools


def retry(max_attempts=3, delay=1, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    wait_time = delay * (backoff ** (attempts - 1))
                    print(f"Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
        return wrapper
    return decorator


@retry(max_attempts=5, delay=1, backoff=2)
def fetch_data_from_network():
    if random.random() < 0.7:
        raise Exception('Simulated network failure')
    return 'Data fetched successfully!'

if __name__ == '__main__':
    print(fetch_data_from_network())