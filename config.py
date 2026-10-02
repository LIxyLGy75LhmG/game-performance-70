import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, file_path: str, defaults: Dict[str, Any]):
        self.path = file_path
        self.defaults = defaults
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            self._write(self.defaults)
            return self.defaults
        with open(self.path, 'r') as f:
            try:
                user_data = json.load(f)
                return {**self.defaults, **user_data}
            except json.JSONDecodeError:
                return self.defaults

    def _write(self, data: Dict[str, Any]) -> None:
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

def initialize_game_config(file: str = 'settings.json') -> ConfigLoader:
    defaults = {
        "fps_cap": 60,
        "vsync": True,
        "resolution": [1920, 1080],
        "graphics_preset": "ultra"
    }
    return ConfigLoader(file, defaults)