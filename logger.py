import logging
from logging.handlers import RotatingFileHandler
import os

def get_performance_logger(name='game-perf', log_file='game_metrics.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Unusual approach: using a filter to inject performance context
    class PerfFilter(logging.Filter):
        def filter(self, record):
            record.game_tick = getattr(record, 'game_tick', 'N/A')
            return True

    handler = RotatingFileHandler(
        log_file, 
        maxBytes=1024 * 1024 * 5, 
        backupCount=3
    )

    formatter = logging.Formatter(
        '[%(asctime)s] [TICK:%(game_tick)s] %(levelname)s: %(message)s'
    )
    
    handler.setFormatter(formatter)
    logger.addFilter(PerfFilter())
    logger.addHandler(handler)
    
    # Prevent duplicate handlers on re-import
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

if __name__ == '__main__':
    log = get_performance_logger()
    log.info('performance tracking initiated', extra={'game_tick': 0})