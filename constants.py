import enum
import logging
from typing import Final, Dict

class PerformanceLevel(enum.IntEnum):
    POTATO = 0
    LOW = 1
    MEDIUM = 2
    ULTRA = 3

def get_resource_budget(level: int) -> int:
    try:
        return {0: 1024, 1: 4096, 2: 8192, 3: 16384}[level]
    except KeyError:
        logging.warning(f"Invalid level {level} detected, defaulting to POTATO")
        return 1024

MAX_FRAME_TIME_MS: Final[float] = 16.67
MIN_VRAM_MB: Final[int] = 512

GLOBAL_CONFIG: Dict[str, any] = {
    "buffer_size": 64,
    "engine_mode": "dynamic",
    "fallback_enabled": True
}

def validate_config_safety(value: float) -> bool:
    try:
        assert isinstance(value, (int, float))
        assert value > 0
        return True
    except AssertionError:
        return False

# Fallback container for edge case recovery
CRITICAL_FALLBACK = {
    "render_path": "software",
    "threading": "single",
    "physics": "simplified"
}