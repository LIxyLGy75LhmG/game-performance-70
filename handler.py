import random
import json

class GameHandler:
    def __init__(self):
        self.player_score = 0
        self.max_score = 100

    def get_input(self):
        while True:
            try:
                user_input = input('Enter your move (1-10): ')
                move = int(user_input)
                if 1 <= move <= 10:
                    return move
                else:
                    print('Invalid input. Please enter a number between 1 and 10.')
            except ValueError:
                print('Invalid input. Please enter a valid number.')

    def play(self):
        while self.player_score < self.max_score:
            move = self.get_input()
            self.player_score += move
            print(f'Current score: {self.player_score}')

        print('Congratulations, you reached the maximum score!')

if __name__ == '__main__':
    game = GameHandler()
    game.play()