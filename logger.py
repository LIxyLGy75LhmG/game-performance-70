import logging
import os
from logging.handlers import RotatingFileHandler

def get_performance_logger(name: str = 'game-perf') -> logging.Logger:
    """
    Orchestrates a rotating logger that keeps game performance
    metrics sane by capping file bloat at 5MB per file.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        log_dir = 'logs'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        handler = RotatingFileHandler(
            filename=os.path.join(log_dir, f'{name}.log'),
            maxBytes=5 * 1024 * 1024,
            backupCount=3,
            encoding='utf-8'
        )
        
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        # Add a stream handler for local development visibility
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)
    
    return logger