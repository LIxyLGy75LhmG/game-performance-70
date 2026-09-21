import os
from typing import Final

# Performance constants for game-performance-70
TARGET_FPS: Final[int] = 144
BUFFER_SIZE_BYTES: Final[int] = 1024 * 64
MAX_MEMORY_THRESHOLD_MB: Final[int] = 2048

# Graphics-specific tweaks
RENDER_SCALE_QUALITY: Final[str] = 'ultra'
USE_VULKAN_BACKEND: Final[bool] = True

# Network optimization
PACKET_LOSS_TOLERANCE: Final[float] = 0.005
DEFAULT_LATENCY_MS: Final[int] = 25

# Environmental configuration
GAME_ASSETS_PATH: Final[str] = os.getenv('ASSET_PATH', './assets')
IS_DEBUG_MODE: Final[bool] = os.getenv('DEBUG', 'False').lower() == 'true'

class PerformanceTier:
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    ULTRA = 3

# Dictionary mapping for quick lookups
TIER_CONFIGS: Final[dict] = {
    PerformanceTier.LOW: {'draw_dist': 500, 'shadows': False},
    PerformanceTier.MEDIUM: {'draw_dist': 1000, 'shadows': True},
    PerformanceTier.HIGH: {'draw_dist': 2000, 'shadows': True},
    PerformanceTier.ULTRA: {'draw_dist': 5000, 'shadows': True}
}