from typing import Tuple

# Game constants for better maintainability

# Screen dimensions
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600

# Colors
BLACK: Tuple[int, int, int] = (0, 0, 0)
WHITE: Tuple[int, int, int] = (255, 255, 255)
RED: Tuple[int, int, int] = (255, 0, 0)
GREEN: Tuple[int, int, int] = (0, 255, 0)
BLUE: Tuple[int, int, int] = (0, 0, 255)

# Game settings
FPS: int = 60

# Player settings
PLAYER_LIVES: int = 3
PLAYER_SPEED: float = 5.0

# Enemy settings
ENEMY_SPEED: float = 3.0

def get_screen_size() -> Tuple[int, int]:
    """Returns the screen width and height as a tuple."
    return SCREEN_WIDTH, SCREEN_HEIGHT

def get_color(name: str) -> Tuple[int, int, int]:
    """Returns the RGB tuple for a given color name."""
    colors = {'black': BLACK, 'white': WHITE, 'red': RED, 'green': GREEN, 'blue': BLUE}
    return colors.get(name.lower(), WHITE)  # Default to WHITE if not found
