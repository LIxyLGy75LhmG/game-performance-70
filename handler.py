import random
import json

class GameHandler:
    def __init__(self):
        self.valid_commands = ['start', 'stop', 'pause', 'resume']
        self.state = 'stopped'

    def validate_input(self, command):
        if command not in self.valid_commands:
            raise ValueError(f"Invalid command: {command}")
        return command

    def process_command(self, command):
        command = self.validate_input(command)
        if command == 'start':
            self.state = 'running'
            return self._start_game()
        elif command == 'stop':
            self.state = 'stopped'
            return self._stop_game()
        elif command == 'pause':
            self.state = 'paused'
            return self._pause_game()
        elif command == 'resume':
            self.state = 'running'
            return self._resume_game()

    def _start_game(self):
        return json.dumps({'status': 'Game started', 'state': self.state})

    def _stop_game(self):
        return json.dumps({'status': 'Game stopped', 'state': self.state})

    def _pause_game(self):
        return json.dumps({'status': 'Game paused', 'state': self.state})

    def _resume_game(self):
        return json.dumps({'status': 'Game resumed', 'state': self.state})

if __name__ == '__main__':
    handler = GameHandler()
    for command in ['start', 'pause', 'resume', 'stop', 'invalid']:
        try:
            print(handler.process_command(command))
        except ValueError as e:
            print(e)