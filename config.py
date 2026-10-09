import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any], path: str = 'settings.json'):
        self.path = path
        self.data = defaults
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    loaded = json.load(f)
                    self.data.update(loaded)
            except (json.JSONDecodeError, IOError):
                pass

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.data.get(key, fallback)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def save(self) -> None:
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def __repr__(self) -> str:
        return f"<ConfigLoader loaded_keys={list(self.data.keys())}>"

# Usage example for performance-70 tweaks
DEFAULT_SETTINGS = {
    "fps_cap": 144,
    "vsync": False,
    "render_scale": 1.0
}

settings = ConfigLoader(DEFAULT_SETTINGS)