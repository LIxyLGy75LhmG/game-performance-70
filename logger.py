import sys
import time
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

class FrameAwareFormatter(logging.Formatter):
    """Formats log records with frame delta timing for game performance tracing."""
    def __init__(self, fmt: str = None):
        super().__init__(fmt or "%(asctime)s [%(levelname)s] [dt:%(delta_ms)06.2fms] %(message)s")
        self._last_tick = time.perf_counter()

    def format(self, record: logging.LogRecord) -> str:
        now = time.perf_counter()
        record.delta_ms = (now - self._last_tick) * 1000.0
        self._last_tick = now
        return super().format(record)

def setup_performance_logger(
    log_dir: str = "logs",
    filename: str = "telemetry.log",
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 3
) -> logging.Logger:
    """Configures a rotating performance logger tuned for high-frequency telemetry."""
    target_path = Path(log_dir)
    target_path.mkdir(parents=True, exist_ok=True)
    log_file = target_path / filename

    logger = logging.getLogger("game_performance")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    formatter = FrameAwareFormatter()

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

perf_logger = setup_performance_logger()
