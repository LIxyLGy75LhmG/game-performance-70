import json
import os
import multiprocessing
from typing import Any, Dict

class GameConfig(dict):
    """A dictionary-backed configuration loader that dynamically adjusts
    performance presets based on detected CPU cores and local JSON overrides."""

    PRESETS: Dict[str, Dict[str, Any]] = {
        "potato": {"target_fps": 30, "shadows": False, "render_scale": 0.75, "threads": 1},
        "standard": {"target_fps": 60, "shadows": True, "render_scale": 1.0, "threads": 2},
        "hardcore": {"target_fps": 144, "shadows": True, "render_scale": 1.25, "threads": 4}
    }

    def __init__(self, config_path: str = "settings.json"):
        super().__init__()
        self.config_path = config_path
        self._apply_preset(self._detect_hardware_profile())
        self.load_from_file()

    def _detect_hardware_profile(self) -> str:
        try:
            cores = multiprocessing.cpu_count()
            if cores <= 2:
                return "potato"
            elif cores <= 6:
                return "standard"
            return "hardcore"
        except Exception:
            return "standard"

    def _apply_preset(self, preset_name: str):
        preset = self.PRESETS.get(preset_name, self.PRESETS["standard"])
        self.update(preset)

    def load_from_file(self):
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    user_data = json.load(f)
                    self.update(user_data)
            except (json.JSONDecodeError, IOError):
                pass

    def __getattr__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError:
            raise AttributeError(f"Configuration key '{name}' not found.")

    def save(self):
        try:
            with open(self.config_path, "w") as f:
                json.dump(dict(self), f, indent=4)
        except IOError:
            pass