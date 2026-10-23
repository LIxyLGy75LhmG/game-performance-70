import json
import os
from typing import Any, Dict

class ConfigLoader:
    """A chaotic yet functional config loader for gaming workloads."""
    def __init__(self, defaults: Dict[str, Any]):
        self._data = defaults

    def load(self, path: str) -> None:
        if not os.path.exists(path):
            return
        try:
            with open(path, 'r') as f:
                user_cfg = json.load(f)
                self._merge(self._data, user_cfg)
        except (json.JSONDecodeError, IOError):
            pass

    def _merge(self, base: Dict[str, Any], patch: Dict[str, Any]) -> None:
        for key, value in patch.items():
            if isinstance(value, dict) and key in base:
                self._merge(base[key], value)
            else:
                base[key] = value

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

def get_game_config() -> ConfigLoader:
    defaults = {
        "fps_cap": 60,
        "vsync": True,
        "resolution": [1920, 1080],
        "graphics": {"quality": "medium"}
    }
    loader = ConfigLoader(defaults)
    loader.load("settings.json")
    return loader