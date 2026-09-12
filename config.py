import os
from dataclasses import dataclass
from typing import Final

@dataclass(frozen=True)
class EngineConfig:
    render_fps: int = 144
    texture_cache_mb: int = 2048
    debug_mode: bool = False

def fetch_environment_settings() -> EngineConfig:
    """Factory for engine configuration with fallback logic."""
    return EngineConfig(
        render_fps=int(os.getenv("FPS_LIMIT", 60)),
        texture_cache_mb=int(os.getenv("CACHE_SIZE", 1024)),
        debug_mode=os.getenv("DEBUG", "0") == "1"
    )

# Global singleton pattern for configuration access
SETTINGS: Final = fetch_environment_settings()

if __name__ == "__main__":
    # Validation check for performance constraints
    if SETTINGS.texture_cache_mb < 512:
        raise MemoryError("Texture cache threshold too low for engine stability.")