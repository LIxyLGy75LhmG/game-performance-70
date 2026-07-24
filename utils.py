import json
import random
from typing import List, Dict

def load_game_data(file_path: str) -> Dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'Error: {file_path} not found.')
        return {}
    except json.JSONDecodeError:
        print('Error: Failed to decode JSON.')
        return {}

def save_game_data(file_path: str, data: Dict) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def generate_random_event(events: List[str]) -> str:
    return random.choice(events)

# Example usage
if __name__ == '__main__':
    game_data = load_game_data('game_data.json')
    if game_data:
        event = generate_random_event(game_data.get('events', []))
        print(f'Random event triggered: {event}')