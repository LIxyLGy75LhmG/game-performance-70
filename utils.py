import time
import random
import requests

def retry_network_operation(operation, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = operation()
            if response.ok:
                return response.json()
            else:
                print(f"Attempt {attempt + 1}: Received non-200 response: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1}: Network error: {e}")
        time.sleep(delay)
    raise Exception(f"Failed after {retries} attempts.")

# Example operation function

def fetch_data():
    url = "https://api.example.com/data"
    return requests.get(url)

# Usage
if __name__ == '__main__':
    try:
        data = retry_network_operation(fetch_data)
        print(data)
    except Exception as e:
        print(e)