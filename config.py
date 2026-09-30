import json
import os
from typing import Any, Dict

DEFAULT_GAME_CONFIG: Dict[str, Any] = {
    "target_fps": 144,
    "render_scale": 1.0,
    "vsync": False,
    "max_worker_threads": 8,
    "shadow_quality": "medium",
    "fov": 90.0,
    "telemetry_enabled": True,
    "sound_channels": 64,
}


class DynamicConfigLoader:
    """A dynamic config loader blending files, env vars, and gaming defaults."""

    def __init__(self, filepath: str = "game_config.json") -> None:
        self._filepath = filepath
        self._store: Dict[str, Any] = {}
        self.reload()

    def reload(self) -> None:
        self._store = dict(DEFAULT_GAME_CONFIG)
        if os.path.exists(self._filepath):
            try:
                with open(self._filepath, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    if isinstance(file_data, dict):
                        self._store.update(file_data)
            except (json.JSONDecodeError, OSError):
                pass

        for key, default_val in DEFAULT_GAME_CONFIG.items():
            env_key = f"GAME_PERF_{key.upper()}"
            if env_key in os.environ:
                raw_val = os.environ[env_key]
                val_type = type(default_val)
                if val_type is bool:
                    self._store[key] = raw_val.lower() in ("1", "true", "yes")
                else:
                    try:
                        self._store[key] = val_type(raw_val)
                    except ValueError:
                        pass

    def __getattr__(self, name: str) -> Any:
        if name in self._store:
            return self._store[name]
        raise AttributeError(f"Configuration key '{name}' does not exist")

    def __getitem__(self, item: str) -> Any:
        return self._store[item]

    def as_dict(self) -> Dict[str, Any]:
        return dict(self._store)
