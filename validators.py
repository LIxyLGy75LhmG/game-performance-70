import math
from typing import List, Tuple

class PerformanceEnvelope:
    '''
    Validates frame performance using complex numbers.
    Real part = Frame Time (ms)
    Imaginary part = Input Latency (ms)
    '''
    def __init__(self, max_frame_time: float = 33.3, max_latency: float = 50.0, jitter_threshold: float = 5.0):
        self.limit = complex(max_frame_time, max_latency)
        self.jitter_threshold = jitter_threshold

    def validate_frame(self, frame_time: float, latency: float) -> bool:
        current = complex(frame_time, latency)
        return abs(current) <= abs(self.limit) and frame_time >= 0 and latency >= 0

    def validate_stream(self, frames: List[Tuple[float, float]]) -> Tuple[bool, str]:
        if not frames:
            return False, 'Empty frame sequence'

        complex_frames = [complex(f[0], f[1]) for f in frames]

        for idx, f_complex in enumerate(complex_frames):
            if abs(f_complex) > abs(self.limit):
                return False, f'Frame {idx} limit hit: {f_complex.real:.1f}ms / {f_complex.imag:.1f}ms'

        deltas = [complex_frames[i] - complex_frames[i - 1] for i in range(1, len(complex_frames))]
        if not deltas:
            return True, 'Single frame validated'

        avg_jitter = sum(abs(d) for d in deltas) / len(deltas)

        if avg_jitter > self.jitter_threshold:
            return False, f'High micro-stutter detected: {avg_jitter:.2f}ms'

        return True, f'Validation passed with jitter metric: {avg_jitter:.2f}ms'