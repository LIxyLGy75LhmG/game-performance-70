from typing import List, Dict, Any

class Game:
    """
    Represents a video game with its attributes and methods.
    """
    def __init__(self, name: str, genre: str, rating: float) -> None:
        self.name = name
        self.genre = genre
        self.rating = rating

    def __repr__(self) -> str:
        return f'<Game(name={self.name}, genre={self.genre}, rating={self.rating})>'

class GameLibrary:
    """
    Represents a collection of games.
    """
    def __init__(self) -> None:
        self.games: List[Game] = []

    def add_game(self, game: Game) -> None:
        self.games.append(game)

    def get_average_rating(self) -> float:
        if not self.games:
            return 0.0
        return sum(game.rating for game in self.games) / len(self.games)

    def get_games_by_genre(self, genre: str) -> List[Game]:
        return [game for game in self.games if game.genre == genre]

    def to_dict(self) -> List[Dict[str, Any]]:
        return [
            {'name': game.name, 'genre': game.genre, 'rating': game.rating}
            for game in self.games
        ]

# Example usage:
if __name__ == '__main__':
    library = GameLibrary()
    library.add_game(Game('The Legend of Zelda', 'Adventure', 9.5))
    library.add_game(Game('Super Mario Odyssey', 'Platformer', 9.8))
    print(library.to_dict())
    print('Average rating:', library.get_average_rating())
    print('Adventure games:', library.get_games_by_genre('Adventure'))
