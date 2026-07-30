import logging

class GameLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        handler = logging.FileHandler('game.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_performance(self, func):
        import time
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.logger.info(f'Performance: {func.__name__} took {end_time - start_time:.4f} seconds')
            return result
        return wrapper

# Example usage
# logger = GameLogger('MyGame')  
# @logger.log_performance
# def some_game_function():
#     # Game logic here
  
# some_game_function()