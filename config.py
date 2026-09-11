import os
import json
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "target_fps": 60,
    "vsync": True,
    "dynamic_resolution": False,
    "max_threads": 4,
    "gpu_scheduling": "normal",
    "telemetry_enabled": True
}

class GameConfig:
    """Dynamic configuration loader with fallback defaults and environment overrides."""
    def __init__(self, config_path: str = "perf_config.json"):
        self._path = config_path
        self._raw_config: Dict[str, Any] = {}
        self.load()

    def load(self) -> None:
        if os.path.exists(self._path):
            try:
                with open(self._path, "r") as f:
                    self._raw_config = json.load(f)
            except (json.JSONDecodeError, OSError):
                self._raw_config = {}
        else:
            self._raw_config = {}

    def save(self) -> None:
        try:
            with open(self._path, "w") as f:
                json.dump(self._raw_config, f, indent=2)
        except OSError:
            pass

    def __getattr__(self, name: str) -> Any:
        env_key = f"GP70_{name.upper()}"
        if env_key in os.environ:
            val = os.environ[env_key]
            default_val = DEFAULT_CONFIG.get(name)
            if isinstance(default_val, bool):
                return val.lower() in ("true", "1", "yes")
            if isinstance(default_val, int):
                return int(val)
            return val

        if name in self._raw_config:
            return self._raw_config[name]

        if name in DEFAULT_CONFIG:
            return DEFAULT_CONFIG[name]

        raise AttributeError(f"Configuration option '{name}' is not defined")

    def update(self, key: str, value: Any) -> None:
        if key not in DEFAULT_CONFIG:
            raise ValueError(f"Cannot update unregistered config setting: {key}")
        expected_type = type(DEFAULT_CONFIG[key])
        if not isinstance(value, expected_type):
            raise TypeError(f"Expected type {expected_type} for {key}, got {type(value)}")
        self._raw_config[key] = value
        self.save()