import json
import random
from typing import List, Dict

class GameData:
    def __init__(self, player_name: str, score: int, level: int):
        self.player_name = player_name
        self.score = score
        self.level = level

    def to_dict(self) -> Dict[str, any]:
        return {
            'player_name': self.player_name,
            'score': self.score,
            'level': self.level
        }

def save_game_data(players: List[GameData], filename: str) -> None:
    data = [player.to_dict() for player in players]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_game_data(filename: str) -> List[GameData]:
    with open(filename, 'r') as f:
        data = json.load(f)
    return [GameData(**item) for item in data]

def generate_random_game_data(num_players: int) -> List[GameData]:
    return [GameData(f'Player{str(i)}', random.randint(0, 100), random.randint(1, 10)) for i in range(num_players)]