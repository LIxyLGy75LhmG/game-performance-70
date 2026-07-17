import random
import time

class Game:
    def __init__(self, players):
        self.players = players
        self.scores = {player: 0 for player in players}

    def play_round(self):
        print("Starting a new round...")
        for player in self.players:
            score = self.roll_dice()  # Simulate rolling a dice
            self.scores[player] += score
            print(f"{player} rolled a {score}, total score: {self.scores[player]}")
        print("Round finished.")

    @staticmethod
    def roll_dice():
        return random.randint(1, 6)

    def display_scores(self):
        for player, score in self.scores.items():
            print(f"{player}: {score} points")

    def start_game(self, rounds):
        for _ in range(rounds):
            self.play_round()
            time.sleep(1)  # Simulating delay between rounds
        self.display_scores()

if __name__ == "__main__":
    game = Game(players=["Alice", "Bob", "Charlie"])
    game.start_game(rounds=5)