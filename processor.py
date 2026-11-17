import time
import random

def validate_input(data):
    if not isinstance(data, dict) or 'frame_id' not in data:
        raise ValueError('corrupt packet schema detected')
    if not (0 <= data.get('latency', 999) < 500):
        raise ValueError('latency threshold spike')
    return True

def process_game_tick(stream):
    for raw_packet in stream:
        try:
            if validate_input(raw_packet):
                print(f"processing tick: {raw_packet['frame_id']}")
        except (ValueError, TypeError) as e:
            print(f"discarding malformed input: {e}")
            continue

if __name__ == '__main__':
    mock_stream = [
        {'frame_id': 1, 'latency': 20},
        {'frame_id': 2, 'latency': 800},
        {'corrupted': 'data'},
        {'frame_id': 3, 'latency': 45}
    ]
    process_game_tick(mock_stream)