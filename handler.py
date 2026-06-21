import json

def load_game_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_game_data(file_path, key, value):
    data = load_game_data(file_path)
    data[key] = value
    save_game_data(file_path, data)


def filter_game_data(file_path, condition):
    data = load_game_data(file_path)
    filtered_data = {k: v for k, v in data.items() if condition(k, v)}
    return filtered_data


def merge_game_data(file_path_1, file_path_2, output_path):
    data_1 = load_game_data(file_path_1)
    data_2 = load_game_data(file_path_2)
    merged_data = {**data_1, **data_2}
    save_game_data(output_path, merged_data)