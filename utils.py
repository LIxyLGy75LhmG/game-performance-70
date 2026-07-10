import json

class GameDataHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def write_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def update_data(self, new_data):
        existing_data = self.read_data()
        existing_data.update(new_data)
        self.write_data(existing_data)

    def filter_data(self, condition):
        data = self.read_data()
        return {k: v for k, v in data.items() if condition(v)}

# Example usage
if __name__ == '__main__':
    handler = GameDataHandler('game_data.json')
    print(handler.read_data())
    handler.update_data({'player_score': 100})
    filtered = handler.filter_data(lambda x: x > 50)
    print(filtered)