import logging
from logging.handlers import RotatingFileHandler
import os

def get_performance_logger(name: str = 'game_perf') -> logging.Logger:
    """Factory for rotatable logs for game engine metrics."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        log_dir = 'logs'
        os.makedirs(log_dir, exist_ok=True)
        
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s'
        )
        
        # Rolling logs at 5MB, keeping 3 old generations
        path = os.path.join(log_dir, f'{name}.log')
        handler = RotatingFileHandler(
            path, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        # Stream to console if in development environment
        if os.getenv('GAME_DEBUG', 'false').lower() == 'true':
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            logger.addHandler(console)
            
    return logger