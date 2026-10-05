import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any], filepath: str = 'settings.json'):
        self.defaults = defaults
        self.filepath = filepath
        self.config = self._load_and_merge()

    def _load_and_merge(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            return self.defaults
        
        try:
            with open(self.filepath, 'r') as f:
                user_data = json.load(f)
            return {**self.defaults, **user_data}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.config.get(key, fallback)

    def __getitem__(self, key: str) -> Any:
        return self.config[key]

    def __repr__(self) -> str:
        return f"<ConfigLoader: {len(self.config)} keys active>"

def load_game_config() -> ConfigLoader:
    default_settings = {
        "resolution": "1920x1080",
        "vsync": True,
        "max_fps": 144,
        "gamma": 1.0
    }
    return ConfigLoader(default_settings)