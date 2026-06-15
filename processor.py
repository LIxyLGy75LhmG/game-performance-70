import time
import random
import requests

def retry_network_operation(operation, retries=3, delay=2):
    for attempt in range(retries):
        try:
            result = operation()
            return result
        except requests.ConnectionError as e:
            print(f"ConnectionError: {e}. Attempt {attempt + 1} of {retries}.")
            time.sleep(delay)
        except requests.Timeout as e:
            print(f"TimeoutError: {e}. Attempt {attempt + 1} of {retries}.")
            time.sleep(delay)
    raise Exception("Maximum retries exceeded.")

def fetch_data(url):
    print(f"Fetching data from {url}...")
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_network_operation(lambda: fetch_data(url))
        print(data)
    except Exception as e:
        print(f"Failed to fetch data: {e}")
