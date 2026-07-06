import time
import random
from typing import Callable, Any

def retry(operation: Callable[..., Any], retries: int = 3, delay: int = 2, backoff: float = 1.5) -> Any:
    attempt = 0
    while attempt < retries:
        try:
            return operation()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            attempt += 1
            if attempt >= retries:
                print("All attempts failed, raising exception.")
                raise
            time.sleep(delay)
            delay *= backoff

# Example usage with a network operation simulation

def mock_network_operation():
    if random.choice([True, False]):
        raise ConnectionError("Network error occurred")
    return "Success!"

if __name__ == "__main__":
    try:
        result = retry(mock_network_operation)
        print(result)
    except Exception as e:
        print(f"Final exception: {e}")
