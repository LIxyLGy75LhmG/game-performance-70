import json
from collections import defaultdict

class GameDataHandler:
    def __init__(self):
        self.data = defaultdict(list)

    def add_game_data(self, game_id, metrics):
        self.data[game_id].append(metrics)

    def get_average_metrics(self, game_id):
        if game_id not in self.data:
            return None
        total_metrics = defaultdict(int)
        for metrics in self.data[game_id]:
            for key, value in metrics.items():
                total_metrics[key] += value
        avg_metrics = {key: total / len(self.data[game_id]) for key, total in total_metrics.items()}
        return avg_metrics

    def export_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    def import_from_json(self, filename):
        with open(filename, 'r') as f:
            self.data = json.load(f)

# Usage example:
# handler = GameDataHandler()
# handler.add_game_data('game_1', {'fps': 60, 'ping': 20})
# handler.add_game_data('game_1', {'fps': 55, 'ping': 25})
# print(handler.get_average_metrics('game_1'))
# handler.export_to_json('game_data.json')
# handler.import_from_json('game_data.json')