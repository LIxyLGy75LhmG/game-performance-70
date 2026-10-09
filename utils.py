import time
import functools
from typing import Callable, Any, Dict

class PerformanceMetrics:
    def __init__(self):
        self.telemetry = {}

    def record(self, func_name: str, duration: float):
        self.telemetry[func_name] = self.telemetry.get(func_name, []) + [duration]

    def average_latency(self, func_name: str) -> float:
        data = self.telemetry.get(func_name, [0])
        return sum(data) / len(data)

metrics_engine = PerformanceMetrics()

def benchmark_frame_op(func: Callable):
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        metrics_engine.record(func.__name__, time.perf_counter() - start_time)
        return result
    return wrapper

def pack_entity_data(entity_id: int, state: Dict[str, Any]) -> bytes:
    header = entity_id.to_bytes(4, byteorder='big')
    payload = str(state).encode('utf-8')
    return header + b'|' + payload

def unpack_entity_data(raw_data: bytes) -> Dict[str, Any]:
    _, payload = raw_data.split(b'|', 1)
    return eval(payload.decode('utf-8'))