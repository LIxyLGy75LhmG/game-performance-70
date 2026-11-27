import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Callable, Dict, Any

class FrameMetricsAdapter(logging.LoggerAdapter):
    """Injects dynamic frame timing and rendering context into log records."""
    def __init__(self, logger: logging.Logger, telemetry_fn: Callable[[], Dict[str, Any]] = None):
        super().__init__(logger, {})
        self.telemetry_fn = telemetry_fn or (lambda: {"fps": 60.0, "frame": 0})

    def process(self, msg: str, kwargs: Dict[str, Any]):
        metrics = self.telemetry_fn()
        frame_id = metrics.get("frame", 0)
        fps = metrics.get("fps", 0.0)
        formatted_msg = f"[F:{frame_id:07d} | {fps:5.1f} FPS] {msg}"
        return formatted_msg, kwargs

def configure_rotating_logger(
    log_path: str = "logs/perf_telemetry.log",
    max_megabytes: float = 5.0,
    backup_count: int = 3,
    telemetry_provider: Callable[[], Dict[str, Any]] = None
) -> FrameMetricsAdapter:
    log_dir = os.path.dirname(log_path)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger("game_performance")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    file_handler = RotatingFileHandler(
        filename=log_path,
        maxBytes=int(max_megabytes * 1024 * 1024),
        backupCount=backup_count,
        encoding="utf-8"
    )
    formatter = logging.Formatter(
        fmt="%(asctime)s.%(msecs)03d | %(levelname)-7s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return FrameMetricsAdapter(logger, telemetry_provider)