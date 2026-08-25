import json
import os
from copy import deepcopy
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "game": {
        "title": "Game Performance 70",
        "version": "0.1",
        "target_fps": 70,
        "window_size": [1280, 720],
        "fullscreen": False,
    },
    "rendering": {
        "quality_level": "medium",
        "enable_shadows": True,
        "anisotropic_filtering": 8,
        "draw_distance": 500,
    },
    "sound": {
        "master_volume": 0.85,
        "music_volume": 0.6,
        "effects_volume": 1.0,
        "spatial_audio": True,
    },
    "controls": {
        "mouse_sensitivity": 1.0,
        "invert_y_axis": False,
        "key_bindings": {"forward": "w", "jump": "space"},
    },
}

class ConfigLoader:
    def __init__(self, filepath: str = "settings.json"):
        self.filepath = filepath
        self.data: Dict[str, Any] = self._initialize_config()

    def _initialize_config(self) -> Dict[str, Any]:
        config = deepcopy(DEFAULT_CONFIG)
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as file:
                    loaded = json.load(file)
                config = self._recursive_merge(config, loaded)
            except Exception as err:
                print(f"Config load issue: {err}. Defaults applied.")
        return config

    def _recursive_merge(self, target: Dict[str, Any], source: Dict[str, Any]) -> Dict[str, Any]:
        for k, v in source.items():
            if k in target and isinstance(target[k], dict) and isinstance(v, dict):
                target[k] = self._recursive_merge(target[k], v)
            else:
                target[k] = v
        return target

    def get(self, dotted_path: str, fallback: Optional[Any] = None) -> Any:
        parts = dotted_path.split(".")
        current: Any = self.data
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return fallback
        return current

    def set(self, dotted_path: str, value: Any) -> None:
        parts = dotted_path.split(".")
        current = self.data
        for part in parts[:-1]:
            if part not in current or not isinstance(current[part], dict):
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value

    def save(self) -> bool:
        try:
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(self.data, file, indent=2)
            return True
        except Exception as err:
            print(f"Save failed: {err}")
            return False

    def reload(self) -> None:
        self.data = self._initialize_config()

# Usage example
if __name__ == "__main__":
    loader = ConfigLoader("game_performance_config.json")
    print("Target FPS:", loader.get("game.target_fps"))
    print("Quality:", loader.get("rendering.quality_level"))
    loader.set("rendering.draw_distance", 1000)
    loader.save()
    print("Updated draw distance:", loader.get("rendering.draw_distance"))