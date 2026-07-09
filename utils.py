import json
import os

def load_game_data(file_path):
    """Load game data from a JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path, data):
    """Save game data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_game_data(file_path, updates):
    """Update specific attributes in game data."""
    data = load_game_data(file_path)
    data.update(updates)
    save_game_data(file_path, data)


if __name__ == '__main__':
    sample_data = {'score': 100, 'level': 1}
    save_game_data('game_data.json', sample_data)
    print(load_game_data('game_data.json'))
    update_game_data('game_data.json', {'score': 150})
    print(load_game_data('game_data.json'))