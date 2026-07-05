import time
import numpy as np

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = np.zeros((height, width), dtype=int)
        self.score = 0

    def update_board(self):
        # Simulating game logic with NumPy for optimization
        new_blocks = np.random.randint(1, 5, size=(2, 2))
        self.board[0:2, 0:2] = new_blocks
        self.score += np.sum(new_blocks)

    def render(self):
        for row in self.board:
            print(' '.join(map(str, row)))
        print(f'Score: {self.score}')  

    def play_game(self, rounds):
        for _ in range(rounds):
            start_time = time.time()
            self.update_board()
            self.render()
            end_time = time.time()
            print(f'Round time: {end_time - start_time:.4f} seconds')

if __name__ == '__main__':
    game = Game(5, 5)
    game.play_game(3)