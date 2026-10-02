import os
import json
from pathlib import Path
from typing import Any, Dict, Union

DEFAULT_PROFILE: Dict[str, Any] = {
    "target_fps": 144,
    "max_rendered_frames": 2,
    "enable_dlss": True,
    "dlss_mode": "quality",
    "vsync": False,
    "thread_pool_size": 8,
    "gpu_memory_budget_mb": 6144,
    "resolution_scale": 1.0,
}

class ConfigLoader:
    """Dynamic game configuration overlay with environment variable injection."""
    
    def __init__(self, config_path: Union[str, Path] = "game_settings.json"):
        self.config_path = Path(config_path)
        self._data: Dict[str, Any] = {}
        self.reload()

    def reload(self) -> None:
        """Loads base configuration and overlays active defaults and ENV overrides."""
        base = DEFAULT_PROFILE.copy()
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    base.update(file_data)
            except (json.JSONDecodeError, OSError):
                pass
        
        for key in base:
            env_var = f"GAME_{key.upper()}"
            if env_var in os.environ:
                val = os.environ[env_var]
                base[key] = type(base[key])(val) if not isinstance(base[key], bool) else val.lower() == "true"
        
        self._data = base

    def __getattr__(self, name: str) -> Any:
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"Configuration key '{name}' is not registered.")

    def __setattr__(self, name: str, value: Any) -> None:
        if name in ("config_path", "_data"):
            super().__setattr__(name, value)
        else:
            self._data[name] = value

    def __repr__(self) -> str:
        return f"GameConfig({self._data})"

    def export(self) -> str:
        return json.dumps(self._data, indent=2)

config = ConfigLoader()
