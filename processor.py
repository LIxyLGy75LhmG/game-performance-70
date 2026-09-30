import math
from typing import Dict, List, Union

class TelemetryProcessor:
    """Processes gaming frame metrics with highly resilient edge-case mitigation."""

    def __init__(self, baseline_fps: float = 60.0):
        self.baseline_fps = max(0.1, baseline_fps)

    def process_frame_deltas(self, raw_deltas: List[Union[int, float, None]]) -> Dict[str, float]:
        if not raw_deltas:
            return {"average_fps": self.baseline_fps, "stutter_index": 0.0, "low_1percent": self.baseline_fps}

        clean_deltas = []
        for d in raw_deltas:
            try:
                if d is None or not isinstance(d, (int, float)):
                    continue
                if math.isnan(d) or math.isinf(d) or d <= 0.0:
                    continue
                clean_deltas.append(float(d))
            except (ValueError, TypeError):
                continue

        if not clean_deltas:
            return {"average_fps": self.baseline_fps, "stutter_index": 0.0, "low_1percent": self.baseline_fps}

        # Convert delta times (seconds) to frame rates
        frame_rates = [1.0 / delta for delta in clean_deltas]
        avg_fps = sum(frame_rates) / len(frame_rates)

        # Edge case: Very small datasets for 1% low calculations
        sorted_rates = sorted(frame_rates)
        one_percent_idx = max(1, int(len(sorted_rates) * 0.01))
        low_1percent = sum(sorted_rates[:one_percent_idx]) / one_percent_idx

        # Calculate stutter index as standard deviation of frame times
        mean_delta = sum(clean_deltas) / len(clean_deltas)
        variance = sum((d - mean_delta) ** 2 for d in clean_deltas) / len(clean_deltas)
        stutter_index = math.sqrt(variance) * 1000.0  # Convert to ms deviation

        return {
            "average_fps": round(avg_fps, 2),
            "stutter_index": round(stutter_index, 3),
            "low_1percent": round(low_1percent, 2)
        }