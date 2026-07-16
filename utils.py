import json

def load_game_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise Exception(f"Error decoding JSON from: {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")


def save_game_data(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise Exception(f"Failed to save data: {str(e)}")


def update_high_scores(scores, new_score):
    scores.append(new_score)
    return sorted(scores, reverse=True)[:10]


def validate_game_state(state):
    required_keys = ['level', 'score', 'lives']
    for key in required_keys:
        if key not in state:
            raise ValueError(f'Missing required key: {key}') 
    return True

