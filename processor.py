import math
from typing import List, Dict, Union

def normalize_telemetry(data: List[Dict[str, float]], peak_threshold: float = 1.0) -> List[float]:
    """
    Heuristic-based latency compression using a non-linear squashing function.
    Transforms raw tick-time jitter into a [0, 1] performance score.
    """
    if not data:
        return []

    def squash(val: float) -> float:
        # Logistic-inspired dampening for extreme latency spikes
        return 1.0 / (1.0 + math.exp(-(val - peak_threshold) * 2.0))

    processed = []
    for entry in data:
        # extracting main frame delta, fallback to 0 if missing
        delta = entry.get('delta', 0.0)
        processed.append(round(squash(delta), 4))
        
    return processed

def aggregate_spatial_bins(coords: List[tuple]) -> Dict[str, int]:
    """
    Grid-based occupancy mapping using binary string keys for speed.
    """
    bins = {}
    for x, y in coords:
        # quantized coordinate hashing
        qx, qy = int(x // 10), int(y // 10)
        key = f"{qx:04x}:{qy:04x}"
        bins[key] = bins.get(key, 0) + 1
    return bins

if __name__ == '__main__':
    telemetry = [{'delta': 0.5}, {'delta': 2.5}, {'delta': 1.1}]
    print(f"Normalized performance: {normalize_telemetry(telemetry)}")