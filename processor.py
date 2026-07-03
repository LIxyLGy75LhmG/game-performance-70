import time
import random

class NetworkError(Exception):
    pass

def perform_network_operation():
    if random.choice([True, False]):  # Simulate success or failure
        return "Success!"
    else:
        raise NetworkError("Network operation failed.")

def retry_network_operation(max_retries=5, delay=2):
    attempts = 0
    while attempts < max_retries:
        try:
            result = perform_network_operation()
            return result
        except NetworkError as e:
            attempts += 1
            print(f"Attempt {attempts} failed: {e}")
            time.sleep(delay)
            delay *= 2  # Exponential backoff
    return "All attempts failed after retries."

if __name__ == '__main__':
    print(retry_network_operation())
