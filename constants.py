from typing import Final, Dict, Any

# Latency thresholds in milliseconds for telemetry tracking
LATENCY_TIERS: Final[Dict[str, float]] = {
    'EXCELLENT': 20.0,
    'GOOD': 50.0,
    'FAIR': 100.0,
    'POOR': 250.0
}

# Frame pacing targets for various game modes
FRAME_TARGETS: Final[Dict[str, int]] = {
    'COMPETITIVE': 144,
    'CINEMATIC': 60,
    'BATTERY_SAVER': 30
}

# Bitmask flags for engine state verification
ENGINE_FLAGS: Final[Dict[str, int]] = {
    'VSYNC_ENABLED': 1 << 0,
    'HDR_SUPPORTED': 1 << 1,
    'RAY_TRACING_ACTIVE': 1 << 2,
    'DLSS_UPSCALING': 1 << 3
}

def get_threshold_label(ms: float) -> str:
    """Determines latency tier via reverse dictionary lookup."""
    sorted_tiers = sorted(LATENCY_TIERS.items(), key=lambda x: x[1])
    for label, val in sorted_tiers:
        if ms <= val:
            return label
    return 'CRITICAL'

# System capacity constants
MAX_CONCURRENT_ENTITIES: Final[int] = 10000
BUFFER_SIZE_BYTES: Final[int] = 4096
NETWORK_TICK_RATE: Final[float] = 0.015