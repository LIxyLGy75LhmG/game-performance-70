import time
import random

def retry_operation(max_retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < max_retries - 1:
                        wait_time = random.uniform(1, delay)
                        print(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time:.2f} seconds...")
                        time.sleep(wait_time)
                    else:
                        print(f"Attempt {attempt + 1} failed: {e}. No more retries.")
                        raise
        return wrapper
    return decorator

@retry_operation(max_retries=5, delay=5)
def network_request():
    if random.choice([True, False]):
        return "Success!"
    else:
        raise ConnectionError("Network issue occurred")
