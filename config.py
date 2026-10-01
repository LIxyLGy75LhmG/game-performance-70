import json
import os
from typing import Any, Dict

class GameConfig:
    DEFAULT_SETTINGS = {
        "resolution": [1920, 1080],
        "vsync": True,
        "target_fps": 144,
        "shaders_quality": "high"
    }

    def __init__(self, path: str = "settings.json"):
        self.path = path
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            self._save_defaults()
            return self.DEFAULT_SETTINGS.copy()
        
        try:
            with open(self.path, 'r') as f:
                user_data = json.load(f)
            return {**self.DEFAULT_SETTINGS, **user_data}
        except (json.JSONDecodeError, IOError):
            return self.DEFAULT_SETTINGS.copy()

    def _save_defaults(self):
        with open(self.path, 'w') as f:
            json.dump(self.DEFAULT_SETTINGS, f, indent=4)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def __repr__(self):
        return f"<GameConfig path='{self.path}' keys={list(self.data.keys())}>"