import json
from typing import Any, Dict

class GameDataHandler:
    def __init__(self, data: Dict[str, Any]):
        self.data = data

    def to_json(self) -> str:
        return json.dumps(self.data)

    def from_json(self, json_str: str) -> None:
        self.data = json.loads(json_str)

    def extract_attribute(self, key: str) -> Any:
        return self.data.get(key, None)

    def update_attribute(self, key: str, value: Any) -> None:
        self.data[key] = value

    def get_summary(self) -> Dict[str, Any]:
        return {key: self.data[key] for key in self.data if isinstance(self.data[key], (int, float))}

if __name__ == '__main__':
    sample_data = {'score': 100, 'level': 3, 'player': 'John', 'items': ['sword', 'shield']}
    handler = GameDataHandler(sample_data)
    print(handler.to_json())
    handler.update_attribute('score', 150)
    print(handler.get_summary())