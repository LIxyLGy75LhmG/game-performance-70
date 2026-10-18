import os
import json
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any], path: str = 'settings.json'):
        self.path = path
        self._data = defaults.copy()
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                try:
                    user_cfg = json.load(f)
                    self._data.update({k: v for k, v in user_cfg.items() if k in self._data})
                except json.JSONDecodeError:
                    pass

    def __getattr__(self, name: str) -> Any:
        if name in self._data:
            return self._data[name]
        raise AttributeError(f'Config has no attribute {name}')

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def __repr__(self) -> str:
        return f'<GameConfig {list(self._data.keys())}>'

def get_config():
    defaults = {
        'fps_cap': 144,
        'vsync': True,
        'resolution': [1920, 1080],
        'gpu_accelerated': True
    }
    return ConfigLoader(defaults)