from typing import List, Dict, Any

class Game:
    def __init__(self, name: str, players: List[str]) -> None:
        """Initialize a Game instance with a name and players."""
        self.name = name
        self.players = players
        self.scores: Dict[str, int] = {player: 0 for player in players}

    def update_score(self, player: str, points: int) -> None:
        """Update the score of a player."""
        if player in self.scores:
            self.scores[player] += points
        else:
            raise ValueError(f"Player {player} not found in game.")

    def get_winner(self) -> str:
        """Determine the winner of the game based on scores."""
        winner = max(self.scores, key=self.scores.get)
        return winner

    def game_summary(self) -> Dict[str, Any]:
        """Return a summary of the game with scores."""
        return {
            'name': self.name,
            'scores': self.scores,
            'winner': self.get_winner()
        }

# Example of how Game class can be used:
if __name__ == '__main__':
    game = Game("Ultimate Battle", ["Alice", "Bob", "Charlie"])
    game.update_score("Alice", 10)
    game.update_score("Bob", 15)
    game.update_score("Charlie", 12)
    summary = game.game_summary()
    print(summary)
