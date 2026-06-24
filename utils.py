import json
import random

class GameDataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_player_score(self, player_id):
        return self.data.get(player_id, {}).get('score', 0)

    def update_player_score(self, player_id, score):
        if player_id not in self.data:
            self.data[player_id] = {'score': 0}
        self.data[player_id]['score'] += score
        self.save_data()

    def add_random_event(self):
        event = random.choice(['found_item', 'defeated_enemy', 'completed_task'])
        for player_id in self.data.keys():
            if event == 'found_item':
                self.data[player_id]['score'] += 10
            elif event == 'defeated_enemy':
                self.data[player_id]['score'] += 20
            else:
                self.data[player_id]['score'] += 5
        self.save_data()

