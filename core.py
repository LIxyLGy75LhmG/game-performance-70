import json
from pathlib import Path
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, path: str = 'settings.json', defaults: Dict[str, Any] = None):
        self.path = Path(path)
        self.data = defaults or {}
        self._load()

    def _load(self) -> None:
        if self.path.exists():
            try:
                with open(self.path, 'r') as f:
                    file_data = json.load(f)
                    self.data.update(file_data)
            except (json.JSONDecodeError, IOError):
                pass

    def __getitem__(self, key: str) -> Any:
        return self.data.get(key)

    def __repr__(self) -> str:
        return f"<ConfigLoader: {len(self.data)} keys loaded>"

    @property
    def settings(self) -> Dict[str, Any]:
        return self.data

def get_game_config(overrides: Dict[str, Any] = None) -> ConfigLoader:
    default_vals = {
        "resolution": "1920x1080",
        "vsync": True,
        "max_fps": 144,
        "quality": "ultra"
    }
    loader = ConfigLoader("config.json", default_vals)
    if overrides:
        loader.data.update(overrides)
    return loader