import time
import random

def retry(func, max_retries=5, delay=1):
    """Retry a function call a specified number of times with a delay."""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            print(f'Attempt {attempt + 1} failed: {e}')
            if attempt < max_retries - 1:
                time.sleep(delay)
            else:
                print('All attempts failed.')
                raise


def network_operation():
    """Simulate a network operation that may fail randomly."""
    if random.choice([True, False]):
        raise Exception('Network error occurred.')
    return 'Success!'

# Example usage
if __name__ == '__main__':
    try:
        result = retry(network_operation)
        print(result)
    except Exception:
        print('Unable to complete the network operation.')