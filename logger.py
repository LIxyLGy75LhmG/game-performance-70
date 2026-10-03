import logging
from logging.handlers import RotatingFileHandler
import os

class PerformanceLogger:
    def __init__(self, log_path='performance.log', max_size=1024*1024*5, backups=3):
        self.logger = logging.getLogger('game-performance-70')
        self.logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | FPS-Tracker: %(message)s'
        )
        
        handler = RotatingFileHandler(
            log_path, 
            maxBytes=max_size, 
            backupCount=backups
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger

def setup_performance_logging():
    instance = PerformanceLogger()
    return instance.get_logger()

if __name__ == '__main__':
    log = setup_performance_logging()
    log.info('Engine initialized at 144Hz target')