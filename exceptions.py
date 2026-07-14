class GameError(Exception):
    """Base class for exceptions in the game."""
    pass

class InvalidInputError(GameError):
    """Exception raised for invalid input received from the player."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class GameStateError(GameError):
    """Exception raised when an operation is not allowed in the current game state."""
    def __init__(self, state: str, message: str) -> None:
        super().__init__(f"{state}: {message}")
        self.state = state
        self.message = message

class ResourceNotFoundError(GameError):
    """Exception raised when a requested resource is not found."""
    def __init__(self, resource_name: str) -> None:
        super().__init__(f"Resource '{resource_name}' not found.")
        self.resource_name = resource_name

class NotAuthorizedError(GameError):
    """Exception raised when a player attempts an unauthorized action."""
    def __init__(self, action: str) -> None:
        super().__init__(f"Not authorized to perform action: {action}")
        self.action = action
