import json
import random
from typing import List, Dict

class GameDataProcessor:
    @staticmethod
    def normalize_scores(scores: List[int]) -> List[float]:
        max_score = max(scores) if scores else 0
        return [(score / max_score) if max_score > 0 else 0 for score in scores]

    @staticmethod
    def average_score(scores: List[int]) -> float:
        return sum(scores) / len(scores) if scores else 0.0

    @staticmethod
    def generate_match_report(data: Dict[str, List[int]]) -> str:
        report = {
            'average_scores': {player: GameDataProcessor.average_score(scores) for player, scores in data.items()},
            'normalized_scores': {player: GameDataProcessor.normalize_scores(scores) for player, scores in data.items()}
        }
        return json.dumps(report, indent=4)

    @staticmethod
    def random_event_trigger(chance: float) -> bool:
        return random.random() < chance

    @staticmethod
    def combine_report_data(report1: str, report2: str) -> str:
        combined = json.loads(report1)
        additional = json.loads(report2)
        combined.update(additional)
        return json.dumps(combined, indent=4)