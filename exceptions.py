class InputValidationError(Exception):
    pass

class GameProcessor:
    def __init__(self):
        self.valid_actions = ['move', 'jump', 'attack', 'defend']

    def validate_input(self, action):
        if action not in self.valid_actions:
            raise InputValidationError(f"Invalid action: {action}")

    def process_game_loop(self, input_actions):
        for action in input_actions:
            try:
                self.validate_input(action)
                self.execute_action(action)
            except InputValidationError as e:
                print(e)

    def execute_action(self, action):
        print(f"Executing action: {action}")

# Example of how the GameProcessor might be instantiated and used:
if __name__ == '__main__':
    game_processor = GameProcessor()
    actions = ['move', 'jump', 'run']  # 'run' is an invalid action
    game_processor.process_game_loop(actions)