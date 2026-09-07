import json
import os
from typing import Any, Dict

class ConfigProcessor:
    def __init__(self, path: str = "config.json", defaults: Dict[str, Any] = None):
        self.path = path
        self.defaults = defaults or {}
        self.settings = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            self._save(self.defaults)
            return self.defaults
        try:
            with open(self.path, "r") as f:
                loaded = json.load(f)
                return {**self.defaults, **loaded}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def _save(self, data: Dict[str, Any]) -> None:
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def get(self, key: str, fallback: Any = None) -> Any:
        return self.settings.get(key, fallback)

    def patch(self, key: str, value: Any) -> None:
        self.settings[key] = value
        self._save(self.settings)

if __name__ == "__main__":
    # Example usage for performance tunings
    engine_cfg = ConfigProcessor("engine.json", {"fps_cap": 144, "vsync": False})
    print(f"Current FPS limit: {engine_cfg.get('fps_cap')}")