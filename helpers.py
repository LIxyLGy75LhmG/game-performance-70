import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Magic config loader with defensive defaults."""
    def __init__(self, defaults: Dict[str, Any]):
        self.defaults = defaults

    def load(self, path: str) -> Dict[str, Any]:
        if not os.path.exists(path):
            return self.defaults
        try:
            with open(path, 'r') as f:
                loaded = json.load(f)
            return self._merge(self.defaults, loaded)
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def _merge(self, base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        config = base.copy()
        for key, value in override.items():
            if key in config and isinstance(config[key], dict) and isinstance(value, dict):
                config[key] = self._merge(config[key], value)
            else:
                config[key] = value
        return config

def get_performance_config(path: str = 'settings.json') -> Dict[str, Any]:
    default_profile = {
        "frame_cap": 60,
        "vsync": True,
        "graphics": {
            "shadows": "medium",
            "textures": "high"
        }
    }
    loader = ConfigLoader(default_profile)
    return loader.load(path)