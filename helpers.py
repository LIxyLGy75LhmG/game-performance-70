from typing import NamedTuple, List

class PerformanceMetrics(NamedTuple):
    avg_fps: float
    one_percent_low: float
    zero_point_one_percent_low: float
    stutter_count: int
    smoothness_score: float

def analyze_frame_deltas(frame_times_ms: List[float], stutter_threshold_ms: float = 16.67) -> PerformanceMetrics:
    """Processes raw frame render deltas (in ms) using percentile isolation
    to evaluate real-time framerate stability and stutter occurrences.
    """
    if not frame_times_ms:
        return PerformanceMetrics(0.0, 0.0, 0.0, 0, 0.0)

    sorted_times = sorted(frame_times_ms)
    count = len(sorted_times)

    idx_99 = max(0, int(count * 0.99) - 1)
    idx_99_9 = max(0, int(count * 0.999) - 1)

    p99_frame_time = sorted_times[idx_99]
    p99_9_frame_time = sorted_times[idx_99_9]

    total_time = sum(frame_times_ms)
    avg_fps = (count / total_time * 1000.0) if total_time > 0 else 0.0
    one_percent_low = (1000.0 / p99_frame_time) if p99_frame_time > 0 else 0.0
    zero_point_one_percent_low = (1000.0 / p99_9_frame_time) if p99_9_frame_time > 0 else 0.0

    median_time = sorted_times[count // 2]
    dynamic_stutter_threshold = max(stutter_threshold_ms * 1.5, median_time * 2.0)
    
    stutters = sum(1 for ft in frame_times_ms if ft > dynamic_stutter_threshold)
    
    variance = sum((ft - median_time) ** 2 for ft in frame_times_ms) / count
    smoothness_score = max(0.0, min(100.0, 100.0 - (variance ** 0.5)))

    return PerformanceMetrics(
        avg_fps=round(avg_fps, 2),
        one_percent_low=round(one_percent_low, 2),
        zero_point_one_percent_low=round(zero_point_one_percent_low, 2),
        stutter_count=stutters,
        smoothness_score=round(smoothness_score, 2)
    )

def quantize_fps_stream(raw_timestamps: List[float]) -> List[float]:
    """Transforms raw epoch render timestamps into millisecond frame deltas."""
    return [
        (t2 - t1) * 1000.0
        for t1, t2 in zip(raw_timestamps[:-1], raw_timestamps[1:])
        if t2 > t1
    ]