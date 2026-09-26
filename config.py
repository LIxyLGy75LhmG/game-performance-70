import json
from pathlib import Path
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any], path: str = 'config.json'):
        self.path = Path(path)
        self.data = defaults.copy()
        self._load()

    def _load(self) -> None:
        if self.path.exists():
            try:
                with open(self.path, 'r') as f:
                    user_data = json.load(f)
                    self._recursive_update(self.data, user_data)
            except (json.JSONDecodeError, IOError):
                pass

    def _recursive_update(self, target: Dict, source: Dict) -> None:
        for key, value in source.items():
            if isinstance(value, dict) and key in target and isinstance(target[key], dict):
                self._recursive_update(target[key], value)
            else:
                target[key] = value

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.data.get(key, fallback)

    def save(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)

def load_game_config(defaults: Dict[str, Any]) -> ConfigLoader:
    return ConfigLoader(defaults)