import time
import random

class NetworkError(Exception):
    pass

def retry_on_failure(func, retries=3, delay=2):
    for attempt in range(retries):
        try:
            return func()
        except NetworkError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                wait_time = delay + random.uniform(0, 1)
                print(f"Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
            else:
                print("All attempts failed.")
                raise

# Example function to simulate network operation
def network_operation():
    if random.choice([True, False]):
        raise NetworkError("Simulated network failure")
    return "Network operation successful!"

# Usage:
# result = retry_on_failure(network_operation)