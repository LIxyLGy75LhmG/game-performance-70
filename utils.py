import json
import os

class GameData:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.data = json.load(file)

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def update_score(self, player_id, score):
        if player_id not in self.data:
            self.data[player_id] = {'score': 0}
        self.data[player_id]['score'] += score
        self.save_data()

    def get_score(self, player_id):
        return self.data.get(player_id, {}).get('score', 0)

    def reset_scores(self):
        self.data = {}
        self.save_data()