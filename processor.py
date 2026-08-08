import json
from typing import List, Dict

class GameDataProcessor:
    def __init__(self, data: List[Dict]):
        self.data = data

    def normalize_scores(self) -> List[Dict]:
        max_score = max(item['score'] for item in self.data)
        for item in self.data:
            item['normalized_score'] = item['score'] / max_score
        return self.data

    def filter_by_player(self, player_name: str) -> List[Dict]:
        return [item for item in self.data if item['player'] == player_name]

    def to_json(self) -> str:
        return json.dumps(self.data, indent=4)

# Example usage
if __name__ == '__main__':
    sample_data = [
        {'player': 'Alice', 'score': 150},
        {'player': 'Bob', 'score': 100},
        {'player': 'Alice', 'score': 200},
    ]
    processor = GameDataProcessor(sample_data)
    print(processor.normalize_scores())
    print(processor.filter_by_player('Alice'))
    print(processor.to_json())