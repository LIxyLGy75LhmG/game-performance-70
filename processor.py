from collections import deque
from typing import Dict, List, Optional, TypeAlias

FrameTimeMs: TypeAlias = float
FPSMetrics: TypeAlias = Dict[str, float]


class FrameTimeProcessor:
    """Real-time gaming frame telemetry analyzer using a dynamic sliding window.

    Computes instantaneous FPS, 1% low, 0.1% low, and micro-stutter index
    from incoming frame render intervals.
    """

    def __init__(self, window_size: int = 120) -> None:
        self._window_size: int = max(10, window_size)
        self._buffer: deque[FrameTimeMs] = deque(maxlen=self._window_size)

    def ingest_frame(self, frame_time_ms: FrameTimeMs) -> Optional[FPSMetrics]:
        """Pushes a new frame rendering time into the window buffer.

        Args:
            frame_time_ms: Elapsed time to render frame in milliseconds.

        Returns:
            Calculated FPS performance metrics if buffer is sufficiently full.
        """
        if frame_time_ms <= 0.0:
            return None

        self._buffer.append(frame_time_ms)
        if len(self._buffer) < (self._window_size // 2):
            return None

        return self._calculate_metrics()

    def _calculate_metrics(self) -> FPSMetrics:
        """Evaluates percentiles and stutter statistics using dynamic sorting."""
        sorted_times: List[FrameTimeMs] = sorted(self._buffer)
        total_frames: int = len(sorted_times)

        avg_ms: float = sum(sorted_times) / total_frames
        avg_fps: float = 1000.0 / avg_ms if avg_ms > 0 else 0.0

        idx_1pct: int = max(0, int(total_frames * 0.99) - 1)
        idx_01pct: int = max(0, int(total_frames * 0.999) - 1)

        low_1pct_fps: float = 1000.0 / sorted_times[idx_1pct]
        low_01pct_fps: float = 1000.0 / sorted_times[idx_01pct]

        variance: float = sum((t - avg_ms) ** 2 for t in sorted_times) / total_frames
        stutter_index: float = (variance ** 0.5) / avg_ms if avg_ms > 0 else 0.0

        return {
            "avg_fps": round(avg_fps, 1),
            "low_1pct_fps": round(low_1pct_fps, 1),
            "low_01pct_fps": round(low_01pct_fps, 1),
            "stutter_index": round(stutter_index, 4),
        }
