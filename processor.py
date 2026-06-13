import json
import random

class GameProcessor:
    def __init__(self):
        self.valid_inputs = {'start', 'stop', 'pause', 'resume'}

    def get_user_input(self):
        return input("Enter command (start/stop/pause/resume): ").strip().lower()

    def validate_input(self, command):
        if command not in self.valid_inputs:
            raise ValueError(f'Invalid command: {command}')

    def process_commands(self):
        while True:
            command = self.get_user_input()
            try:
                self.validate_input(command)
                self.handle_command(command)
            except ValueError as e:
                print(e)

    def handle_command(self, command):
        if command == 'start':
            print("Game started!")
        elif command == 'stop':
            print("Game stopped.")
            exit()
        elif command == 'pause':
            print("Game paused.")
        elif command == 'resume':
            print("Game resumed.")

if __name__ == '__main__':
    processor = GameProcessor()
    processor.process_commands()