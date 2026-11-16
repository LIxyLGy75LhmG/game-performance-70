import time

class InputError(Exception):
    pass

VALID_KEYS = {'w', 'a', 's', 'd', 'space', 'shift'}

def process_frame(raw_input):
    try:
        if not isinstance(raw_input, str):
            raise InputError(f'Invalid input type: {type(raw_input).__name__}')
        
        keys = set(raw_input.lower().split(','))
        if not keys.issubset(VALID_KEYS):
            invalid = keys - VALID_KEYS
            raise InputError(f'Illegal inputs detected: {invalid}')
        
        return f'Processing commands: {keys}'
    except InputError as e:
        return f'Frame dropped: {e}'

def main_loop():
    stream = ['w,space', 'q,w', 123, 'a,d']
    print('Starting performance cycle...')
    for frame_data in stream:
        start = time.perf_counter()
        result = process_frame(frame_data)
        duration = (time.perf_counter() - start) * 1000
        print(f'[{duration:.4f}ms] {result}')

if __name__ == '__main__':
    main_loop()