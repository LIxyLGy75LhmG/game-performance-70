import time
import random

class NetworkError(Exception):
    pass


def perform_network_operation():
    if random.choice([True, False]):  # Simulate success or failure
        print('Operation succeeded.')
        return 'Success'
    else:
        raise NetworkError('Network operation failed.')


def retry_operation(retries=5, delay=2):
    for attempt in range(retries):
        try:
            return perform_network_operation()
        except NetworkError as e:
            print(e)
            print(f'Attempt {attempt + 1} failed, retrying...')
            time.sleep(delay)
    print('All attempts failed.')
    return None


if __name__ == '__main__':
    result = retry_operation()
    if result:
        print('Final result:', result)
    else:
        print('Operation could not be completed.')