import os
from typing import Any, Dict

DEFAULT_SETTINGS: Dict[str, Any] = {
    "target_fps": 60,
    "unlocked_fps": False,
    "resolution_scale": 1.0,
    "shadow_quality": "medium",
    "threaded_rendering": True,
    "latency_reduction": True,
}

PRESETS: Dict[str, Dict[str, Any]] = {
    "potato": {
        "target_fps": 30,
        "resolution_scale": 0.75,
        "shadow_quality": "low",
        "threaded_rendering": False,
    },
    "competitive": {
        "target_fps": 240,
        "unlocked_fps": True,
        "resolution_scale": 0.9,
        "shadow_quality": "off",
        "latency_reduction": True,
    },
}

class PerformanceConfig:
    def __init__(self, preset_name: str = "balanced"):
        self._settings = DEFAULT_SETTINGS.copy()
        preset = preset_name.lower()
        if preset in PRESETS:
            self._settings.update(PRESETS[preset])
        self._user_overrides: Dict[str, Any] = {}

    def load_from_env(self) -> None:
        for key, default_val in self._settings.items():
            env_key = f"GAME_PERF_{key.upper()}"
            if env_key in os.environ:
                raw_val = os.environ[env_key]
                target_type = type(default_val)
                try:
                    if target_type is bool:
                        self._user_overrides[key] = raw_val.lower() in ("true", "1", "yes", "on")
                    else:
                        self._user_overrides[key] = target_type(raw_val)
                except ValueError:
                    pass

    def __getattr__(self, name: str) -> Any:
        if name in self._user_overrides:
            return self._user_overrides[name]
        if name in self._settings:
            return self._settings[name]
        raise AttributeError(f"Configuration option {name!r} is not defined")

    def __repr__(self) -> str:
        merged = {**self._settings, **self._user_overrides}
        return f"PerformanceConfig({merged!r})"