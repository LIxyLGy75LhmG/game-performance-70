import json
import random

class GameException(Exception):
    pass

class InvalidPlayerError(GameException):
    pass

class Game:
    def __init__(self, players):
        self.players = players
        self.validate_players()

    def validate_players(self):
        if len(self.players) < 2:
            raise InvalidPlayerError("Must have at least 2 players.")
        if not all(isinstance(player, str) for player in self.players):
            raise InvalidPlayerError("All players must be strings.")

    def start_game(self):
        try:
            print(f'Starting game with players: {self.players}')
            self.simulate_game()
        except InvalidPlayerError as e:
            print(f'Error: {str(e)}')

    def simulate_game(self):
        winner = random.choice(self.players)
        print(f'The winner is: {winner}')

if __name__ == '__main__':
    players = ['Alice', 'Bob']  # Change this for testing
    game = Game(players)
    game.start_game()
