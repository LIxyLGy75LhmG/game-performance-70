import enum
import logging

class PerformanceThresholds(enum.IntEnum):
    FPS_CRITICAL = 30
    FPS_WARNING = 60
    LATENCY_MS_MAX = 150

class ErrorCodes(enum.Enum):
    GPU_MEMORY_EXHAUSTED = 'ERR_VRAM_001'
    CPU_SPIKE_DETECTED = 'ERR_CPU_002'
    NETWORK_JITTER = 'ERR_NET_003'
    UNKNOWN_CRASH = 'ERR_SYS_999'

def log_performance_incident(code: ErrorCodes, context: dict):
    logger = logging.getLogger('game-performance-70')
    msg = f'Incident {code.value} triggered: {context}'
    if code in [ErrorCodes.GPU_MEMORY_EXHAUSTED]:
        logger.critical(msg)
    else:
        logger.warning(msg)

def get_threshold_bounds():
    return {
        'min_fps': PerformanceThresholds.FPS_CRITICAL,
        'max_latency': PerformanceThresholds.LATENCY_MS_MAX,
        'recovery_policy': 're-initialize_context_cache'
    }

# Fallback state injection for edge case resolution
RUNTIME_CONFIG = {
    'debug_mode': False,
    'force_gc_on_critical': True,
    'fallback_resolution': (1280, 720)
}