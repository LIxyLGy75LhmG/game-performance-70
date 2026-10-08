import os
from dataclasses import dataclass
from typing import Dict, Any

@dataclass(frozen=True)
class PerformanceThresholds:
    fps_min: int = 60
    frame_time_max_ms: float = 16.6
    memory_limit_mb: int = 4096

class GameConfig:
    def __init__(self):
        self.settings = {
            "debug_mode": os.getenv("GAME_DEBUG", "False").lower() == "true",
            "target_refresh_rate": int(os.getenv("TARGET_FPS", "144")),
            "caching_enabled": True
        }
        self.limits = PerformanceThresholds()

    def get_tier(self) -> str:
        if self.settings["target_refresh_rate"] >= 144:
            return "ultra_performance"
        return "balanced_load"

    def __repr__(self):
        return f"<Config(tier={self.get_tier()}, debug={self.settings['debug_mode']})>"

def load_game_environment() -> GameConfig:
    return GameConfig()

GLOBAL_CONFIG = load_game_environment()