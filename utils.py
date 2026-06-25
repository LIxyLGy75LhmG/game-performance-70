import json

def load_game_data(file_path):
    """Load game data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        return None


def save_game_data(file_path, data):
    """Save game data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        print(f"Error: Could not write to {file_path}.")


def update_game_scores(scores, player, score):
    """Update the game scores for a player."""
    scores[player] = scores.get(player, 0) + score


def get_top_scores(scores, n=5):
    """Return the top N scores as a list of tuples."""
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:n
}