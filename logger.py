import logging
import os

class GameLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(f'logs/{name}.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_event(self, event):
        self.logger.info(event)

    def log_error(self, error):
        self.logger.error(error)

    def log_warning(self, warning):
        self.logger.warning(warning)

    def close(self):
        for handler in self.logger.handlers:
            handler.close()
            self.logger.removeHandler(handler)

# Example usage
if __name__ == '__main__':
    os.makedirs('logs', exist_ok=True)  
    game_logger = GameLogger('game_session')
    try:
        game_logger.log_event('Game started')
        # Game logic here
        raise ValueError('An example error')
    except Exception as e:
        game_logger.log_error(str(e))
    finally:
        game_logger.log_event('Game ended')
        game_logger.close()