import gc
import time
import logging

class PerformanceHandler:
    def __init__(self, threshold_ms=16.6):
        self.threshold = threshold_ms
        self.logger = logging.getLogger('game-performance-70')
        self.metrics = {'frame_times': [], 'gc_events': 0}

    def monitor_frame(self, frame_start_time):
        duration = (time.perf_counter() - frame_start_time) * 1000
        self.metrics['frame_times'].append(duration)
        
        if duration > self.threshold:
            self._trigger_cleanup(duration)

    def _trigger_cleanup(self, lag_spike):
        self.logger.warning(f'Lag spike detected: {lag_spike:.2f}ms. Initiating recovery.')
        
        gc.disable()
        self.metrics['gc_events'] += 1
        
        # Unconventional aggressive cleanup
        cleared = gc.collect(generation=2)
        
        gc.enable()
        self.logger.info(f'Recovery complete. Objects cleared: {cleared}')

    def get_status(self):
        return {
            'avg_frame_time': sum(self.metrics['frame_times'][-100:]) / 100 if self.metrics['frame_times'] else 0,
            'recovery_count': self.metrics['gc_events']
        }

def create_handler(threshold=16.6):
    return PerformanceHandler(threshold)