import enum
from typing import Dict, Any

class GameState(enum.IntEnum):
    IDLE = 0
    LOADING = 1
    RUNNING = 2
    CRASHED = 3

class PerformanceConfig:
    def __init__(self, thresholds: Dict[str, float] = None):
        self._thresholds = thresholds or {'fps': 30.0, 'latency': 100.0}
        
    def get_threshold(self, key: str) -> float:
        try:
            return self._thresholds[key]
        except KeyError:
            return 0.0

    def __getitem__(self, key: str) -> float:
        val = self._thresholds.get(key)
        if val is None:
            raise ValueError(f'Undefined metric: {key}')
        return float(val)

ERROR_MESSAGES = {
    'GPU_MEM_EXHAUSTED': 'Fatal: Texture paging failed.',
    'LATENCY_SPIKE': 'Warning: Input lag detected.',
    'FRAME_DROP': 'Alert: Render stutter imminent.'
}

def safe_format_message(code: str, fallback: str = 'Unknown Error') -> str:
    return ERROR_MESSAGES.get(code, fallback)

def validate_perf_metrics(metrics: Dict[str, Any]) -> bool:
    try:
        return all(isinstance(v, (int, float)) and v >= 0 for v in metrics.values())
    except (AttributeError, TypeError):
        return False