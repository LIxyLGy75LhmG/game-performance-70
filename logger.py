import logging

class CustomFormatter(logging.Formatter):
    def format(self, record):
        record.msg = f'[GAME LOG] {record.msg}'
        return super().format(record)

class GameLogger:
    def __init__(self, name='GameLogger'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(CustomFormatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(ch)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

logger = GameLogger()