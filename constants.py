import enum
from dataclasses import dataclass
from typing import Final

@dataclass(frozen=True)
class EngineLimits:
    MAX_FPS: int = 240
    TARGET_LATENCY_MS: float = 16.6
    BUFFER_SIZE: int = 1024

class PerformanceTier(enum.Enum):
    POTATO = 0
    MID = 1
    ULTRA = 2

THRESHOLD_CONFIG: Final = {
    PerformanceTier.POTATO: {'draw_calls': 500, 'tex_quality': 'low'},
    PerformanceTier.MID: {'draw_calls': 2000, 'tex_quality': 'med'},
    PerformanceTier.ULTRA: {'draw_calls': 8000, 'tex_quality': 'high'}
}

CACHE_EXPIRY: Final[int] = 3600
SHUTDOWN_TIMEOUT: Final[float] = 5.5

def get_optimization_payload(tier: PerformanceTier) -> dict:
    return THRESHOLD_CONFIG.get(tier, THRESHOLD_CONFIG[PerformanceTier.POTATO])