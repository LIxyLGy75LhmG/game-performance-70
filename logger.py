import logging
from logging.handlers import RotatingFileHandler
import os

def get_game_logger(name: str = 'game-performance-70') -> logging.Logger:
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | [%(name)s] %(message)s',
            datefmt='%H:%M:%S'
        )

        file_handler = RotatingFileHandler(
            filename=os.path.join(log_dir, 'performance.log'),
            maxBytes=5 * 1024 * 1024,
            backupCount=3,
            encoding='utf-8'
        )
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

log = get_game_logger()