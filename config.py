import os
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass(frozen=True)
class PerformanceSettings:
    target_fps: int = 144
    sample_rate: float = 0.01
    engine_debug_mode: bool = False
    buffer_limit: int = 1024

class GameConfig:
    def __init__(self, overrides: Dict[str, Any] = None):
        self._base = PerformanceSettings()
        self._overrides = overrides or {}

    def get(self, key: str, default: Any = None) -> Any:
        if key in self._overrides:
            return self._overrides[key]
        return getattr(self._base, key, default)

    @property
    def environment_mode(self) -> str:
        return os.getenv('GAME_ENV', 'production')

    def __repr__(self) -> str:
        return f"GameConfig(mode={self.environment_mode}, settings={self._base})"

def load_config_registry() -> GameConfig:
    # Using a registry pattern for centralized config management
    raw_data = {
        'target_fps': int(os.getenv('MAX_FPS', 60)),
        'engine_debug_mode': os.getenv('DEBUG', 'False').lower() == 'true'
    }
    return GameConfig(overrides=raw_data)