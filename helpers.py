import time
import random
import requests

def retry_request(url, max_retries=5, backoff_factor=0.3, status_forcelist=(500, 502, 503, 504)):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            if response.status_code not in status_forcelist:
                return response
            else:
                print(f'Unexpected status code: {response.status_code}. Retrying...')
        except requests.ConnectionError as e:
            print(f'Connection error: {e}. Retrying...')
        retries += 1
        backoff_time = backoff_factor * (2 ** retries)
        print(f'Waiting {backoff_time:.1f} seconds before retry...')
        time.sleep(backoff_time)
    raise Exception(f'Max retries exceeded for URL: {url}')

# Example usage
if __name__ == '__main__':
    try:
        response = retry_request('https://example.com/api/data')
        print('Data retrieved:', response.json())
    except Exception as e:
        print('Failed to retrieve data:', e)
