import gc
import time
import psutil
from typing import Callable, Any

class MemorySanitizer:
    """aggressive memory cleanup for high-frame rate gaming"""
    def __init__(self, threshold_mb: int = 500):
        self.threshold = threshold_mb

    def run_gc_sweep(self) -> None:
        collected = gc.collect()
        process = psutil.Process()
        mem_info = process.memory_info().rss / (1024 * 1024)
        if mem_info > self.threshold:
            print(f"[System] High memory usage detected: {mem_info:.2f}MB. Scrubbing objects...")

    @staticmethod
    def performance_gate(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start) * 1000
            if duration > 16.6:
                print(f"[Warning] {func.__name__} took {duration:.2f}ms (frametime spike)")
            return result
        return wrapper

class ResourceRegistry:
    """singleton registry for engine assets"""
    _registry: dict[str, Any] = {}

    @classmethod
    def register(cls, key: str, resource: Any) -> None:
        cls._registry[key] = resource

    @classmethod
    def flush(cls) -> None:
        cls._registry.clear()
        gc.collect()