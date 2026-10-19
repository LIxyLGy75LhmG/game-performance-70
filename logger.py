import logging
from logging.handlers import RotatingFileHandler
import sys

def setup_game_logger(name: str = 'performance_monitor', log_file: str = 'game.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '[%(asctime)s] | %(levelname)8s | %(name)s | %(message)s',
        datefmt='%H:%M:%S'
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=1024 * 1024 * 5, 
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

log = setup_game_logger()