from typing import Final, Dict, List, Tuple

# Graphics performance presets for low-to-high configurations
RENDER_MODES: Final[Dict[str, int]] = {
    "potato": 720,
    "balanced": 1080,
    "cinematic": 2160
}

# Frame latency thresholds in milliseconds
LATENCY_THRESHOLDS: Final[Tuple[float, float, float]] = (16.6, 33.3, 50.0)

# Reserved engine buffer segments
BUFFER_KEYS: Final[List[str]] = ["vertex", "index", "shadow", "post_process"]

class EngineLimits:
    """Static performance boundaries for the game engine."""
    MAX_DRAWCALLS: Final[int] = 10000
    MAX_TEXTURE_SIZE: Final[int] = 4096
    THREAD_POOL_SIZE: Final[int] = 8

def get_buffer_metrics(mode: str = "balanced") -> Dict[str, float]:
    """Calculates performance constraints based on active resolution mode."""
    scale: float = RENDER_MODES.get(mode, 1080) / 1080
    return {
        "vram_usage": 1024.0 * scale,
        "draw_budget": float(EngineLimits.MAX_DRAWCALLS) * (1.0 / scale)
    }