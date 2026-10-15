import statistics
from typing import List, Dict, Any, Generator

class GamingFrameProcessor:
    """Processes raw telemetry frame times into performance metrics using generator windows."""
    
    def __init__(self, target_fps: float = 60.0):
        self.target_frame_time = 1000.0 / target_fps
        
    def extract_frame_windows(
        self, frame_times_ms: List[float], window_size: int = 100
    ) -> Generator[List[float], None, None]:
        """Yields overlapping sliding windows of frame times."""
        if len(frame_times_ms) < window_size:
            yield frame_times_ms
            return
        for i in range(len(frame_times_ms) - window_size + 1):
            yield frame_times_ms[i:i + window_size]

    def compute_stutter_index(self, window: List[float]) -> float:
        """Calculates a custom stutter metric based on deviation from target frame time."""
        if not window:
            return 0.0
        deviations = [max(0.0, ft - self.target_frame_time) ** 2 for ft in window]
        return (sum(deviations) / len(window)) ** 0.5

    def analyze_telemetry(self, raw_frame_times: List[float]) -> Dict[str, Any]:
        """Generates FPS metrics including 1% and 0.1% lows."""
        if not raw_frame_times:
            return {"fps_avg": 0.0, "fps_1percent_low": 0.0, "fps_01percent_low": 0.0, "stutter_score": 0.0}

        sorted_times = sorted(raw_frame_times)
        total_frames = len(sorted_times)

        avg_frame_time = statistics.mean(raw_frame_times)
        fps_avg = 1000.0 / avg_frame_time if avg_frame_time > 0 else 0.0

        idx_1pct = max(0, int(total_frames * 0.99) - 1)
        idx_01pct = max(0, int(total_frames * 0.999) - 1)

        time_1pct = sorted_times[idx_1pct]
        time_01pct = sorted_times[idx_01pct]

        fps_1pct = 1000.0 / time_1pct if time_1pct > 0 else 0.0
        fps_01pct = 1000.0 / time_01pct if time_01pct > 0 else 0.0

        window_stutters = [
            self.compute_stutter_index(w) 
            for w in self.extract_frame_windows(raw_frame_times, 60)
        ]
        avg_stutter = statistics.mean(window_stutters) if window_stutters else 0.0

        return {
            "fps_avg": round(fps_avg, 2),
            "fps_1percent_low": round(fps_1pct, 2),
            "fps_01percent_low": round(fps_01pct, 2),
            "stutter_score": round(avg_stutter, 4),
            "total_frames_analyzed": total_frames
        }
