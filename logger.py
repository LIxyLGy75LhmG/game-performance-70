import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game.log', max_bytes=10*1024*1024, backup_count=5):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logger = logging.getLogger('game_logger')
    logger.setLevel(logging.DEBUG)

    handler = RotatingFileHandler(os.path.join('logs', log_file), maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

logger = setup_logger()  
logger.info('Logger is set up and ready.')