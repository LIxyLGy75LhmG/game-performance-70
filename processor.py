class GameProcessor:
    def __init__(self, game_data):
        self.game_data = game_data

    def process_game(self):
        try:
            self.validate_data()
            result = self.calculate_performance()
            self.log_result(result)
            return result
        except Exception as e:
            self.handle_error(e)

    def validate_data(self):
        if not isinstance(self.game_data, dict):
            raise ValueError('Game data must be a dictionary')
        if 'frames' not in self.game_data or 'time' not in self.game_data:
            raise KeyError('Missing required game metrics')

    def calculate_performance(self):
        frames = self.game_data['frames']
        time = self.game_data['time']
        if time <= 0:
            raise ValueError('Time must be greater than zero')
        return frames / time

    def log_result(self, result):
        print(f'Performance: {result} FPS')

    def handle_error(self, error):
        print(f'An error occurred: {error}')