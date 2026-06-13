import time
import random

class NetworkError(Exception):
    pass

def retry(operation, retries=3, delay=2):
    for attempt in range(retries):
        try:
            return operation()
        except NetworkError as e:
            if attempt < retries - 1:
                print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                time.sleep(delay)
            else:
                print("All attempts failed.")
                raise

def network_operation():
    if random.choice([True, False]):
        raise NetworkError("Simulated network failure")
    return "Success!"

if __name__ == "__main__":
    try:
        result = retry(network_operation)
        print(result)
    except NetworkError:
        print("Operation failed after retries.")