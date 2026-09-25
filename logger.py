import logging
import os
from logging.handlers import RotatingFileHandler


class SparklineTelemetryFormatter(logging.Formatter):
    """Formats frame timings into visual sparklines alongside standard log info."""

    SPARKS = [" ", "▂", "▃", "▄", "▅", "▆", "▇", "█"]

    def format(self, record: logging.LogRecord) -> str:
        base_msg = super().format(record)
        frametime = getattr(record, "frametime_ms", None)
        if frametime is not None:
            clamped = max(0.0, min(float(frametime), 50.0))
            idx = int((clamped / 50.0) * (len(self.SPARKS) - 1))
            return f"[{self.SPARKS[idx]}] {base_msg}"
        return f"[ ] {base_msg}"


def setup_telemetry_logger(
    log_dir: str = "logs",
    max_bytes: int = 512 * 1024,
    backup_count: int = 3,
) -> logging.Logger:
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "telemetry.log")

    logger = logging.getLogger("game_perf_telemetry")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    if not logger.handlers:
        handler = RotatingFileHandler(
            filename=log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        fmt = "%(asctime)s | %(levelname)-7s | FPS: %(fps)s | %(message)s"
        formatter = SparklineTelemetryFormatter(fmt=fmt, datefmt="%H:%M:%S")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


if __name__ == "__main__":
    perf_log = setup_telemetry_logger()
    perf_log.info("Render loop started", extra={"fps": 144, "frametime_ms": 6.94})
    perf_log.warning("Stutter spike detected", extra={"fps": 24, "frametime_ms": 41.6})