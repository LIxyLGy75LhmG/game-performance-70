import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game.log', max_bytes=5 * 1024 * 1024, backup_count=3):
    logger = logging.getLogger('GameLogger')
    logger.setLevel(logging.DEBUG)

    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(handler)

    return logger

if __name__ == '__main__':
    log = setup_logger()
    log.debug('This is a debug message')
    log.info('Informational message logged')
    log.warning('A warning has occurred')
    log.error('An error occurred!', exc_info=True)
    log.critical('Critical issue detected')
