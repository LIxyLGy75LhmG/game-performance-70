import logging

class GameLogger:
    def __init__(self, log_file='game.log'):
        logging.basicConfig(filename=log_file, level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def log_info(self, message):
        logging.info(message)

    def log_warning(self, message):
        logging.warning(message)

    def log_error(self, message):
        logging.error(message)

    def log_debug(self, message):
        logging.debug(message)

    def validate_input(self, user_input):
        if not isinstance(user_input, str) or not user_input:
            self.log_error('Invalid input received')
            return False
        return True

    def process_input(self, user_input):
        if self.validate_input(user_input):
            self.log_info(f'Processing input: {user_input}')
            # Process the input here
            return True
        return False

if __name__ == '__main__':
    logger = GameLogger()
    sample_inputs = ['', 'valid_input', 123]
    for input_value in sample_inputs:
        logger.process_input(input_value)