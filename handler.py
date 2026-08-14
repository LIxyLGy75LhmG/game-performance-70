import json

class GameDataHandler:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")
            return {}

    def save_data(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.data, file, indent=4)

    def update_data(self, key, value):
        self.data[key] = value
        self.save_data()

    def get_data(self, key, default=None):
        return self.data.get(key, default)

# Example usage:
if __name__ == '__main__':
    handler = GameDataHandler('game_data.json')
    handler.update_data('level', 5)
    print(handler.get_data('level'))
    print(handler.get_data('non_existent_key', 'Not Found'))