import time
import random
import requests

class NetworkError(Exception):
    pass

def retry_decorator(retries=3, delay=2):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, NetworkError) as e:
                    print(f'Attempt {attempt + 1} failed: {e}')
                    time.sleep(delay)
            raise NetworkError('Max retries exceeded')
        return wrapped
    return wrapper

@retry_decorator(retries=5, delay=3)
def fetch_data(url):
    if random.choice([True, False]):  # Simulate random network failure
        raise requests.RequestException('Network is down')
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    try:
        data = fetch_data('https://api.example.com/data')
        print(data)
    except NetworkError as e:
        print(e)