class GameError(Exception):
    """Base class for game-related exceptions."""
    pass

class InputError(GameError):
    """Raised for invalid input error in game."""
    def __init__(self, message):
        super().__init__(message)

class ConnectionError(GameError):
    """Raised when a network connection fails."""
    def __init__(self, message):
        super().__init__(message)

class ResourceNotFoundError(GameError):
    """Raised when a game resource is not found."""
    def __init__(self, resource_name):
        message = f'Resource {resource_name} not found.'
        super().__init__(message)

# Function to simulate resource fetching

def fetch_game_resource(resource_name):
    available_resources = ['level1', 'level2', 'character1']
    if resource_name not in available_resources:
        raise ResourceNotFoundError(resource_name)
    return f'Fetched {resource_name}'

# Example usage with error handling

def main():
    try:
        print(fetch_game_resource('level1'))
        print(fetch_game_resource('level3'))
    except ResourceNotFoundError as e:
        print(e)
    except GameError as e:
        print(f'Game error occurred: {e}')  

if __name__ == '__main__':
    main()