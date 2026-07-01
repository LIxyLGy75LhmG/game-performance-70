class GameError(Exception):
    """Base class for game exceptions."""
    pass

class InvalidDataError(GameError):
    """Exception raised for invalid input data."""
    def __init__(self, message="Invalid data provided."):
        self.message = message
        super().__init__(self.message)

class PlayerNotFoundError(GameError):
    """Exception raised when a player is not found."""
    def __init__(self, player_id):
        self.message = f'Player with ID {player_id} not found.'
        super().__init__(self.message)

class GameStateError(GameError):
    """Exception raised for invalid game state transitions."""
    def __init__(self, state):
        self.message = f'Cannot proceed from the current game state: {state}!'
        super().__init__(self.message)

class InvalidActionError(GameError):
    """Exception raised for illegal actions in the game."""
    def __init__(self, action):
        self.message = f'Action "{action}" is not allowed.'
        super().__init__(self.message)