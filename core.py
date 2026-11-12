import gc
import time
import logging

class PerformanceOptimizer:
    def __init__(self, threshold=0.8):
        self.threshold = threshold
        self.logger = logging.getLogger('game-performance-70')

    def monitor_memory(self):
        import psutil
        mem = psutil.virtual_memory()
        if mem.percent > (self.threshold * 100):
            self.logger.warning(f"Memory saturation at {mem.percent}%. Triggering GC sweep.")
            gc.collect()
            return True
        return False

    def optimize_frame_budget(self, frame_time_limit=0.016):
        def decorator(func):
            def wrapper(*args, **kwargs):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                elapsed = time.perf_counter() - start
                if elapsed > frame_time_limit:
                    self.logger.debug(f"Frame spike detected: {elapsed:.4f}s")
                return result
            return wrapper
        return decorator

    @staticmethod
    def purge_stale_cache(cache_dict, max_size=1000):
        if len(cache_dict) > max_size:
            keys_to_delete = list(cache_dict.keys())[:int(max_size * 0.2)]
            for k in keys_to_delete:
                del cache_dict[k]
            return True
        return False