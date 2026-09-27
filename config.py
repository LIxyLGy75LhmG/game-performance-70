import json
import os
from collections import ChainMap
from pathlib import Path
from typing import Any, Dict

DEFAULT_PERFORMANCE_PROFILE: Dict[str, Any] = {
    "target_fps": 144,
    "max_frame_latency": 2,
    "resolution_scale": 1.0,
    "vsync": False,
    "gpu_memory_budget_mb": 4096,
    "render_threads": max(1, (os.cpu_count() or 4) - 2),
    "enable_dlss": True,
    "asset_streaming_bandwidth_mbps": 500.0,
}


class DynamicConfigLoader:
    """Cascading performance configuration loader for gaming runtime engines."""

    def __init__(self, config_path: str = "settings.json"):
        self.config_path = Path(config_path)
        self._store: ChainMap = ChainMap()
        self.reload()

    def reload(self) -> None:
        file_data: Dict[str, Any] = {}
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
            except (json.JSONDecodeError, OSError):
                file_data = {}

        env_overrides: Dict[str, Any] = {}
        for key in DEFAULT_PERFORMANCE_PROFILE:
            env_key = f"GAME_PERF_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                if val.lower() in ("true", "false"):
                    env_overrides[key] = val.lower() == "true"
                else:
                    try:
                        env_overrides[key] = int(val) if "." not in val else float(val)
                    except ValueError:
                        env_overrides[key] = val

        self._store = ChainMap(env_overrides, file_data, DEFAULT_PERFORMANCE_PROFILE)

    def __getattr__(self, name: str) -> Any:
        if name in self._store:
            return self._store[name]
        raise AttributeError(f"Performance config option '{name}' not found")

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)

    def export_effective_config(self) -> Dict[str, Any]:
        return dict(self._store)


sys_config = DynamicConfigLoader()
