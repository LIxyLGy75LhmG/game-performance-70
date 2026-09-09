import logging
from logging.handlers import RotatingFileHandler
import os

def get_game_logger(name: str = 'game-perf') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not os.path.exists('logs'):
        os.makedirs('logs')

    log_path = os.path.join('logs', f'{name}.log')
    
    # Using a 5MB rotation threshold for rapid iteration
    handler = RotatingFileHandler(
        log_path, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    
    # Creative format for performance profiling logs
    formatter = logging.Formatter(
        '[%(asctime)s] | %(levelname)8s | %(name)s | %(message)s',
        datefmt='%H:%M:%S'
    )
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    # Console output for real-time monitoring
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)
    
    return logger

# Singleton-ish access point
logger = get_game_logger()