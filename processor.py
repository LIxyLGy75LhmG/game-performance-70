import time
from typing import Any, Callable, Dict, List, Generator


class FrameValidationError(Exception):
    """Raised when frame telemetry input fails bounds or integrity checks."""
    pass


def sanitize_frame(raw_frame: Dict[str, Any]) -> Dict[str, float]:
    """Validates and normalizes raw telemetry inputs using a rule matrix."""
    rules: Dict[str, Callable[[Any], bool]] = {
        "frame_id": lambda v: isinstance(v, int) and v >= 0,
        "delta_ms": lambda v: isinstance(v, (int, float)) and 0.1 <= v <= 1000.0,
        "fps": lambda v: isinstance(v, (int, float)) and 1.0 <= v <= 1000.0,
        "gpu_temp_c": lambda v: isinstance(v, (int, float)) and 10.0 <= v <= 115.0,
        "draw_calls": lambda v: isinstance(v, int) and 0 <= v <= 500000,
    }

    validated: Dict[str, float] = {}
    for key, validator in rules.items():
        if key not in raw_frame:
            raise FrameValidationError(f"Missing mandatory telemetry field: '{key}'")
        val = raw_frame[key]
        if not validator(val):
            raise FrameValidationError(f"Invalid telemetry value for field '{key}': {val}")
        validated[key] = float(val)

    return validated


class TelemetryStreamProcessor:
    """Processes incoming stream of game telemetry with inline validation."""

    def __init__(self, buffer_size: int = 100):
        self.buffer_size = buffer_size
        self.processed_count = 0
        self.drop_count = 0

    def process_stream(self, stream: List[Dict[str, Any]]) -> Generator[Dict[str, float], None, None]:
        """Main processing loop with yield-based stream validation."""
        for raw_payload in stream:
            try:
                valid_frame = sanitize_frame(raw_payload)
                self.processed_count += 1
                yield valid_frame
            except FrameValidationError:
                self.drop_count += 1
                continue
