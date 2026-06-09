import time
import random

class NetworkError(Exception):
    pass

def request_with_retry(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = fake_network_request(url)
            return response
        except NetworkError:
            if attempt < retries - 1:
                print(f'Retrying... Attempt {attempt + 2}/{retries}')
                time.sleep(delay)
            else:
                raise

def fake_network_request(url):
    if random.choice([True, False]):  # Simulate network success or failure
        return {"status": "success", "url": url}
    else:
        raise NetworkError(f'Failed to connect to {url}')

# Example usage:
if __name__ == '__main__':
    try:
        result = request_with_retry('http://example.com')
        print(result)
    except NetworkError as e:
        print(e)