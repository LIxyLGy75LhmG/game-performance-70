import time
import random
import requests

class NetworkError(Exception):
    pass

def retry(operation, retries=3, delay=2):
    for i in range(retries):
        try:
            return operation()
        except NetworkError as e:
            print(f"Attempt {i + 1} failed: {e}")
            if i < retries - 1:
                time.sleep(delay)
    raise NetworkError("All attempts failed")

def fetch_data(url):
    if random.choice([True, False]):  # Simulating network error
        raise NetworkError("Failed to fetch data")
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    url = "https://api.example.com/data"
    try:
        data = retry(lambda: fetch_data(url))
        print("Data fetched successfully:", data)
    except NetworkError:
        print("Could not fetch data after multiple attempts")