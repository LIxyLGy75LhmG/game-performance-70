import json
from typing import Any, Dict, List


def load_game_data(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path: str, data: List[Dict[str, Any]]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def filter_high_scores(data: List[Dict[str, Any]], threshold: int) -> List[Dict[str, Any]]:
    return [record for record in data if record.get('score', 0) > threshold]


def average_score(data: List[Dict[str, Any]]) -> float:
    scores = [record['score'] for record in data if 'score' in record]
    return sum(scores) / len(scores) if scores else 0.0


def most_frequent_item(data: List[Dict[str, Any]], key: str) -> Any:
    frequency = {}
    for record in data:
        item = record.get(key)
        if item:
            frequency[item] = frequency.get(item, 0) + 1
    return max(frequency, key=frequency.get) if frequency else None