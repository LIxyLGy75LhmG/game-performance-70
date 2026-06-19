import logging
from typing import Any, Optional

class GameLogger:
    """Handles logging for the game application."""

    def __init__(self, name: str, level: Optional[int] = logging.INFO) -> None:
        """Initialize the logger with a specific name and log level."""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log_info(self, message: str, *args: Any) -> None:
        """Log an informational message."""
        self.logger.info(message, *args)

    def log_warning(self, message: str, *args: Any) -> None:
        """Log a warning message."""
        self.logger.warning(message, *args)

    def log_error(self, message: str, *args: Any) -> None:
        """Log an error message."""
        self.logger.error(message, *args)

    def log_debug(self, message: str, *args: Any) -> None:
        """Log a debug message."""
        self.logger.debug(message, *args)
