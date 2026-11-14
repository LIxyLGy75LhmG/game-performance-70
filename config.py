import json
import os
from collections import ChainMap
from typing import Any, Dict


class DynamicConfigLoader:
    """Cascading game performance config loader with environmental fallbacks."""

    DEFAULTS: Dict[str, Any] = {
        "target_fps": 60,
        "max_render_threads": 4,
        "vsync": True,
        "resolution": [1920, 1080],
        "shadow_quality": "medium",
        "texture_budget_mb": 2048,
        "resolution_scale": 1.0,
    }

    def __init__(self, config_file: str = "settings.json"):
        self._config_file = config_file
        self._user_overrides: Dict[str, Any] = {}
        self._env_overrides: Dict[str, Any] = {}
        self.reload()

    def reload(self) -> None:
        if os.path.exists(self._config_file):
            try:
                with open(self._config_file, "r", encoding="utf-8") as f:
                    self._user_overrides = json.load(f)
            except (json.JSONDecodeError, OSError):
                self._user_overrides = {}

        prefix = "GAME_PERF_"
        for key, val in os.environ.items():
            if key.startswith(prefix):
                clean_key = key[len(prefix) :].lower()
                self._env_overrides[clean_key] = self._cast_value(val)

        self._active_chain = ChainMap(
            self._env_overrides, self._user_overrides, self.DEFAULTS
        )

    @staticmethod
    def _cast_value(val: str) -> Any:
        if val.isdigit():
            return int(val)
        if val.lower() in ("true", "false"):
            return val.lower() == "true"
        try:
            return float(val)
        except ValueError:
            return val

    def __getattr__(self, name: str) -> Any:
        if name in self._active_chain:
            return self._active_chain[name]
        raise AttributeError(f"Config setting '{name}' not found")

    def apply_preset(self, preset_name: str) -> None:
        presets = {
            "low_spec": {"target_fps": 30, "shadow_quality": "low", "texture_budget_mb": 512},
            "high_fps": {"target_fps": 144, "shadow_quality": "low", "vsync": False},
            "ultra": {"target_fps": 60, "shadow_quality": "ultra", "texture_budget_mb": 8192},
        }
        if preset_name in presets:
            self._user_overrides.update(presets[preset_name])
            self.reload()
