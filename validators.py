from typing import Union, Dict, Any, Optional

def validate_frame_rate(fps: Union[int, float]) -> bool:
    """Determines if the target frame rate is within standard gaming hardware bounds."""
    return 30 <= fps <= 360

def validate_config_schema(config: Dict[str, Any], required_keys: list) -> bool:
    """Checks if the game configuration object contains all mandatory performance keys."""
    return all(key in config for key in required_keys)

class PerformanceThreshold:
    """Engine constraint validator using a callback-style interface for frame latency."""
    def __init__(self, limit_ms: float = 16.67):
        self.limit_ms = limit_ms

    def is_within_spec(self, frame_time: float) -> bool:
        """Compares current frame delivery time against the initialized limit."""
        return frame_time <= self.limit_ms

def sanitize_input(user_input: Any) -> Optional[str]:
    """Normalizes input data strings, returning None for invalid game command types."""
    if isinstance(user_input, str) and len(user_input) < 128:
        return user_input.strip().lower()
    return None