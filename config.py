import os
import json
from typing import Any, Dict

class GameConfig:
    DEFAULT_SETTINGS = {
        "frame_rate_cap": 60,
        "enable_vsync": True,
        "texture_quality": "ultra",
        "audio_channels": 128
    }

    def __init__(self, config_path: str = "settings.json"):
        self.config_path = config_path
        self.settings = self.DEFAULT_SETTINGS.copy()
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    user_config = json.load(f)
                    self.settings.update({k: v for k, v in user_config.items() if k in self.DEFAULT_SETTINGS})
            except (json.JSONDecodeError, IOError):
                pass

    def __getitem__(self, key: str) -> Any:
        return self.settings.get(key)

    def __repr__(self) -> str:
        return f"<GameConfig settings={self.settings}>"

def get_config() -> GameConfig:
    if not hasattr(get_config, "_instance"):
        get_config._instance = GameConfig()
    return get_config._instance