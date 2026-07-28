import time

class GameEngine:
    def __init__(self):
        self.fps = 60
        self.last_update_time = time.time()
        self.delta_time = 0

    def update(self):
        current_time = time.time()
        self.delta_time = current_time - self.last_update_time
        if self.delta_time >= 1 / self.fps:
            self.process_game_logic()
            self.last_update_time = current_time

    def process_game_logic(self):
        # Game logic and updates happen here
        print('Game logic updated')

    def run(self):
        while True:
            self.update()

if __name__ == '__main__':
    engine = GameEngine()
    engine.run()