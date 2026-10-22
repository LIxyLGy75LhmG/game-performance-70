import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from collections import deque

class TelemetryBurstHandler(RotatingFileHandler):
    """Rotating log handler with high-frequency ring buffer for gaming telemetry."""
    
    def __init__(self, filename, maxBytes=524288, backupCount=3, burst_capacity=50):
        super().__init__(filename, maxBytes=maxBytes, backupCount=backupCount, encoding="utf-8")
        self._ring_buffer = deque(maxlen=burst_capacity)
        self.low_fps_threshold = 30.0

    def emit(self, record):
        fps = getattr(record, "fps", None)
        if fps is not None and fps < self.low_fps_threshold:
            record.msg = f"[PERF DROP {fps:.1f} FPS] {record.msg}"
            record.levelno = max(record.levelno, logging.WARNING)
            record.levelname = logging.getLevelName(record.levelno)
            self.flush_burst()
        
        self._ring_buffer.append(record)
        if len(self._ring_buffer) >= self._ring_buffer.maxlen or record.levelno >= logging.WARNING:
            self.flush_burst()

    def flush_burst(self):
        while self._ring_buffer:
            rec = self._ring_buffer.popleft()
            super().emit(rec)


def setup_game_logger(name="game_perf", log_file="telemetry.log", level=logging.INFO):
    """Configures telemetry logger with frame-burst rotating file handler."""
    os.makedirs("logs", exist_ok=True)
    path = os.path.join("logs", log_file)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False
    
    if not logger.handlers:
        handler = TelemetryBurstHandler(path, maxBytes=512 * 1024, backupCount=3)
        formatter = logging.Formatter(
            "[%(asctime)s.%(msecs)03d] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s",
            datefmt="%H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        console = logging.StreamHandler(sys.stdout)
        console.setFormatter(formatter)
        logger.addHandler(console)
        
    return logger
