import time
import random

class Game:
    def __init__(self):
        self.state = 'initial'
        self.players = []

    def add_player(self, player_name):
        self.players.append(player_name)
        print(f'Player {player_name} added to the game.')

    def simulate_game(self):
        start_time = time.time()
        while self.state != 'end':
            action = self.random_action()
            self.perform_action(action)
            if len(self.players) >= 5:
                self.state = 'end'
        end_time = time.time()
        print(f'Game finished in {end_time - start_time:.2f} seconds.')

    def random_action(self):
        actions = ['move', 'attack', 'defend']
        return random.choice(actions)

    def perform_action(self, action):
        time.sleep(0.1)  # Simulating some processing time
        print(f'Performed action: {action}')  

if __name__ == '__main__':
    game = Game()
    for name in ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']:
        game.add_player(name)
    game.simulate_game()