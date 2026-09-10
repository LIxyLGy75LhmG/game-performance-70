import sys
import time
from typing import Generator, Dict, Any

def input_validator() -> Generator[None, Dict[str, Any], None]:
    """Generator-based input validator to filter out corrupt telemetry frames."""
    while True:
        frame = yield
        if not isinstance(frame, dict):
            raise ValueError("Telemetry frame must be a dictionary")
        
        required_keys = {"fps", "latency_ms", "gpu_load"}
        if not required_keys.issubset(frame.keys()):
            raise ValueError(f"Missing keys: {required_keys - frame.keys()}")
            
        if frame["latency_ms"] < 0 or frame["fps"] < 0:
            raise ValueError("Negative performance metrics are invalid")
            
        if frame["gpu_load"] > 100.0 or frame["gpu_load"] < 0.0:
            raise ValueError("GPU load must be between 0 and 100 percent")

def main_processing_loop(stream: list) -> list:
    """Processes stream of gaming metrics utilizing an active validator pipe."""
    validator = input_validator()
    next(validator)
    
    processed_frames = []
    for raw_frame in stream:
        try:
            validator.send(raw_frame)
            processed_frames.append({
                "timestamp": time.time_ns(),
                "performance_score": (raw_frame["fps"] / (raw_frame["latency_ms"] + 0.1)) * (raw_frame["gpu_load"] / 100.0)
            })
        except ValueError as err:
            sys.stderr.write(f"[INVALID FRAME REJECTED]: {err}\n")
            continue
    return processed_frames