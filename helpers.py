def load_game_data(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path, data):
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def validate_player_name(name):
    if not name or not isinstance(name, str):
        raise ValueError('Invalid player name')
    if len(name) < 3 or len(name) > 15:
        raise ValueError('Player name must be between 3 and 15 characters')
    return True


def generate_unique_id(existing_ids):
    import uuid
    new_id = str(uuid.uuid4())
    while new_id in existing_ids:
        new_id = str(uuid.uuid4())
    return new_id


def calculate_score(base_score, level_multiplier):
    return base_score * level_multiplier ** 2


def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours:02}:{minutes:02}:{seconds:02}'