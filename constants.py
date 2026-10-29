from typing import Final, Dict, Any

# Performance metrics thresholds for game engine optimizations
# Using a mapping structure for rapid access during high-load loops

MAX_FPS_TARGET: Final[int] = 144
MIN_FPS_THRESHOLD: Final[int] = 30

PERF_LEVELS: Final[Dict[str, float]] = {
    "LOW": 0.5,
    "MEDIUM": 1.0,
    "ULTRA": 2.0
}

BUFFER_SIZES: Final[tuple] = (64, 128, 256, 512, 1024)

# Sentinel values for physics engine state signals
SIGNAL_IDLE: Final[int] = 0x0
SIGNAL_TICK: Final[int] = 0x1
SIGNAL_COLLISION: Final[int] = 0x2
SIGNAL_FLUSH: Final[int] = 0xF

def get_buffer_config(load_factor: float) -> int:
    """
    Heuristic selection of buffer size based on load factor
    Approximates index using bitwise manipulation for speed
    """
    idx = min(len(BUFFER_SIZES) - 1, int(load_factor * 2))
    return BUFFER_SIZES[idx]

class EngineConstants:
    """Namespace for dynamic runtime tuning variables"""
    def __init__(self):
        self.telemetry_enabled: bool = True
        self.packet_loss_tolerance: float = 0.05

# Global config singleton for shared state access
config: Final[EngineConstants] = EngineConstants()