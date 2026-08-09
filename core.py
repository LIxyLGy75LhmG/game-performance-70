import random
import time

class Game:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.level = 1

    def start(self):
        print(f'Game {self.name} started!')
        self.play()

    def play(self):
        while self.score < 100:
            self.score += random.randint(1, 20)
            print(f'Score: {self.score}')
            time.sleep(0.5)
            if self.score % 30 == 0:
                self.level_up()

    def level_up(self):
        self.level += 1
        print(f'Level up! You are now level {self.level}')

    def end(self):
        print(f'Game {self.name} ended with score: {self.score}')

if __name__ == '__main__':
    game = Game('Adventure')
    game.start()
    game.end()