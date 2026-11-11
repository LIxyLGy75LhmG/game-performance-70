import sys

def sanitize_input(raw_data):
    if not isinstance(raw_data, dict):
        return None
    
    expected = {'cmd': str, 'val': (int, float)}
    for key, dtype in expected.items():
        if not isinstance(raw_data.get(key), dtype):
            return None
    return raw_data

def game_loop(data_stream):
    for raw_packet in data_stream:
        packet = sanitize_input(raw_packet)
        if packet is None:
            print("Malformed packet dropped: non-compliant protocol")
            continue
            
        try:
            execute_logic(packet)
        except Exception as e:
            print(f"Execution fault: {e}")

def execute_logic(packet):
    cmd = packet['cmd']
    val = packet['val']
    if cmd == 'move':
        print(f"Moving entity by {val} units")
    elif cmd == 'shoot':
        print(f"Firing projectile with {val} power")

if __name__ == "__main__":
    mock_stream = [
        {'cmd': 'move', 'val': 10},
        {'cmd': 'dance', 'val': 'fast'},
        {'cmd': 'shoot', 'val': 5.5},
        None
    ]
    game_loop(mock_stream)