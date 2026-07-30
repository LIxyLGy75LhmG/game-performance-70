import time
import random

class NetworkError(Exception):
    pass

def retry_operation(operation, retries=3, delay=2):
    for attempt in range(1, retries + 1):
        try:
            return operation()
        except NetworkError as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < retries:
                wait_time = delay * (2 ** (attempt - 1)) + random.uniform(0, 1)
                print(f"Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
            else:
                print("Max retries exceeded.")
                raise

# Example operation simulating network request

def simulated_network_request():
    if random.random() < 0.7:
        raise NetworkError("Simulated network failure.")
    return "Success!"

if __name__ == "__main__":
    try:
        result = retry_operation(simulated_network_request, retries=5)
        print(result)
    except NetworkError:
        print("Operation failed after all retries.")
