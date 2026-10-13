import math
from typing import Final

# Using precomputed lookup tables for expensive calculations
# This bypasses heavy trig overhead in the game engine loop
LOOKUP_TABLE_SIZE: Final[int] = 1024
SIN_LOOKUP: Final[list[float]] = [
    math.sin(2 * math.pi * i / LOOKUP_TABLE_SIZE) for i in range(LOOKUP_TABLE_SIZE)
]

# Memory-aligned constant buffer for game engine core
BUFFER_SIZE: Final[int] = 4096
MAX_THREAD_WORKERS: Final[int] = 8

def get_fast_sin(angle: float) -> float:
    """Quick approximation using precomputed sine values."""
    idx = int((angle % (2 * math.pi)) * (LOOKUP_TABLE_SIZE / (2 * math.pi)))
    return SIN_LOOKUP[idx]

# Cache frame time intervals for simulation stepping
TARGET_FPS: Final[int] = 144
DELTA_TIME: Final[float] = 1.0 / TARGET_FPS

# Network packet optimization constants
PACKET_SIZE_LIMIT: Final[int] = 1400
RECV_BUFFER_SIZE: Final[int] = 65536

# Physics constants for collision detection performance
EPSILON_COLLISION: Final[float] = 1e-6
SPATIAL_GRID_SIZE: Final[int] = 64