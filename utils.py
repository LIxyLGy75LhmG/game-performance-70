import json
import os

def load_game_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Game data file not found: {file_path}")
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def save_game_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def update_game_data(file_path, updates):
    data = load_game_data(file_path)
    data.update(updates)
    save_game_data(file_path, data)

class GameDataException(Exception):
    pass

# Example usage
if __name__ == '__main__':
    try:
        game_data = load_game_data('game_data.json')
        print(game_data)
        update_game_data('game_data.json', {'score': 100})
    except GameDataException as e:
        print(f"Error handling game data: {e}")