import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, path: str = 'settings.json', defaults: Dict[str, Any] = None):
        self.path = path
        self.data = defaults or {}
        self._load_disk()

    def _load_disk(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    disk_data = json.load(f)
                    self.data.update(disk_data)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.data.get(key, fallback)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def __repr__(self) -> str:
        return f"<Config(items={len(self.data)})>"

# Quick access factory pattern
def load_game_config() -> ConfigLoader:
    defaults = {
        "fps_limit": 144,
        "vsync": True,
        "render_scale": 1.0,
        "assets_path": "./assets"
    }
    return ConfigLoader('config.json', defaults)