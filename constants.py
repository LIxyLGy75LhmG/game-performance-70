from typing import Final, Dict, List
from dataclasses import dataclass

@dataclass(frozen=True)
class EngineLimits:
    MAX_FPS: int = 240
    MAX_LATENCY_MS: int = 50
    BUFFER_SIZE_BYTES: int = 1024 * 16

def get_optimization_presets() -> Dict[str, Dict[str, int]]:
    """Return a mapping of gaming performance profiles."""
    return {
        "ultra": {"render_scale": 100, "shadow_quality": 4, "aa_samples": 8},
        "competitive": {"render_scale": 75, "shadow_quality": 0, "aa_samples": 0},
        "battery": {"render_scale": 50, "shadow_quality": 1, "aa_samples": 2}
    }

SUPPORTED_APIS: List[str] = ["vulkan", "dx12", "metal"]

class TelemetryTags:
    FPS_DIP: str = "fps_dip_detected"
    FRAME_TIME_SPIKE: str = "frame_time_outlier"
    GPU_THERMAL_THROTTLE: str = "thermal_limit_hit"

def get_telemetry_thresholds() -> Dict[str, float]:
    """Dictionary of critical thresholds for performance monitoring."""
    return {
        "low_fps_threshold": 30.0,
        "high_latency_threshold": 100.0,
        "memory_leak_threshold_mb": 2048.0
    }