import random
import time

class GameProcessor:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.is_running = True

    def start_game(self):
        print("Game starting...")
        while self.is_running:
            self.play_round()
            self.level_up()
            time.sleep(1)  # Simulate time between rounds

    def play_round(self):
        print(f"Level {self.level}: Playing round...")
        outcome = random.choice(['win', 'lose'])
        if outcome == 'win':
            self.update_score(10)
            print(f"You won! Score: {self.score}")
        else:
            print("You lost this round.")

    def update_score(self, points):
        self.score += points

    def level_up(self):
        if self.score >= self.level * 50:
            self.level += 1
            print(f"Congratulations! You've reached level {self.level}!")

    def stop_game(self):
        self.is_running = False
        print("Game stopped.")

if __name__ == '__main__':
    processor = GameProcessor()
    try:
        processor.start_game()
    except KeyboardInterrupt:
        processor.stop_game()