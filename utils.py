import time
import random

def retry(operation, retries=3, delay=1, backoff=2):
    attempts = 0
    while attempts < retries:
        try:
            return operation()
        except Exception as e:
            attempts += 1
            if attempts == retries:
                print(f'Operation failed after {retries} attempts. Exception: {e}')
                raise
            print(f'Attempt {attempts} failed: {e}. Retrying in {delay} seconds...')
            time.sleep(delay)
            delay *= backoff

# Example Operation  
def network_operation():
    # Simulate random network failure
    if random.choice([True, False]):
        raise ConnectionError('Simulated connection failure')
    return 'Network operation succeeded!'

# Execute with retry logic
if __name__ == '__main__':
    result = retry(network_operation)
    print(result)
