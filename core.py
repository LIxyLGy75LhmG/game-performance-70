import time
import random

class GameInputError(Exception):
    pass

def validate_packet(packet):
    if not isinstance(packet, dict):
        raise GameInputError("Malformatted input structure")
    if 'seq' not in packet or not isinstance(packet['seq'], int):
        raise GameInputError("Missing or invalid sequence identifier")
    if packet.get('latency', 0) > 500:
        raise GameInputError("Packet latency spike detected")

def game_loop():
    print("Starting performance-optimized processing cycle...")
    for _ in range(100):
        try:
            raw_input = {"seq": random.randint(1, 1000), "latency": random.randint(10, 600)}
            validate_packet(raw_input)
            process_tick(raw_input)
        except GameInputError as e:
            print(f"Input rejection: {e}")
            continue
        time.sleep(0.01)

def process_tick(data):
    # Simulate high-performance game logic
    pass

if __name__ == "__main__":
    game_loop()