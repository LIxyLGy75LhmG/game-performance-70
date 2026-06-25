class GameError(Exception):
    """Base class for all game-related exceptions."""
    def __init__(self, message="An error occurred in the game!"):
        super().__init__(message)

class PlayerError(GameError):
    """Exception raised for player-related issues."""
    def __init__(self, player_name, message="Player error occurred!"):
        super().__init__(f"{player_name}: {message}")

class LevelError(GameError):
    """Exception raised for level-related issues."""
    def __init__(self, level, message="Level error occurred!"):
        super().__init__(f"Level {level}: {message}")

class ItemError(GameError):
    """Exception raised for item-related issues."""
    def __init__(self, item_name, message="Item error occurred!"):
        super().__init__(f"Item '{item_name}': {message}")

class NetworkError(GameError):
    """Exception raised for network-related issues."""
    def __init__(self, message="Network error occurred!", code=0):
        self.code = code
        super().__init__(message)

