class GameError(Exception):
    """Base class for game-related exceptions."""
    pass

class PlayerNotFoundError(GameError):
    """Exception raised when a player is not found."""
    def __init__(self, player_id):
        super().__init__(f'Player with ID {player_id} not found.')
        self.player_id = player_id

class GameOverError(GameError):
    """Exception raised when game is over."""
    def __init__(self, reason):
        super().__init__(f'Game is over: {reason}')
        self.reason = reason

class InvalidMoveError(GameError):
    """Exception raised for invalid moves in the game."""
    def __init__(self, move):
        super().__init__(f'Invalid move: {move}')
        self.move = move

class ResourceNotFoundError(GameError):
    """Exception raised when requested resource is not found."""
    def __init__(self, resource_id):
        super().__init__(f'Resource {resource_id} not found.')
        self.resource_id = resource_id