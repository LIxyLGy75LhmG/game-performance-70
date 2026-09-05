import logging
import random

class PerformanceError(Exception):
    pass

class FrameProcessor:
    def __init__(self, threshold=60):
        self.threshold = threshold
        self.logger = logging.getLogger('game-perf')

    def sanitize_fps(self, fps_value):
        try:
            if not isinstance(fps_value, (int, float)):
                raise ValueError(f'Invalid data type: {type(fps_value)}')
            
            if fps_value < 0:
                return 0
            if fps_value > 500:
                raise PerformanceError('Physics engine unstable at ultra-high framerates')
                
            return round(fps_value, 2)
        except (ValueError, PerformanceError) as e:
            self.logger.warning(f'Frame spike anomaly: {e}')
            return self.threshold

    def process_batch(self, frame_data):
        results = []
        for data in frame_data:
            clean_val = self.sanitize_fps(data)
            results.append(clean_val)
        return results

def run_optimization_cycle(data):
    proc = FrameProcessor()
    try:
        return proc.process_batch(data)
    except Exception:
        return [60] * len(data)