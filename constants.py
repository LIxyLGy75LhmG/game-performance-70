from typing import Final, Tuple

# Color constants
BLACK: Final[Tuple[int, int, int]] = (0, 0, 0)
WHITE: Final[Tuple[int, int, int]] = (255, 255, 255)
RED: Final[Tuple[int, int, int]] = (255, 0, 0)
GREEN: Final[Tuple[int, int, int]] = (0, 255, 0)
BLUE: Final[Tuple[int, int, int]] = (0, 0, 255)

# Screen dimensions constants
SCREEN_WIDTH: Final[int] = 800
SCREEN_HEIGHT: Final[int] = 600

# Frame rate constants
FPS: Final[int] = 60

# Game state constants
game_states: Final[dict[str, int]] = {
    'MENU': 0,
    'PLAYING': 1,
    'PAUSED': 2,
    'GAMEOVER': 3
}

def get_color(name: str) -> Tuple[int, int, int]:
    """Retrieve RGB color based on name.

    Args:
        name (str): The name of the color.

    Returns:
        Tuple[int, int, int]: RGB representation of the color.
    """
    colors = {
        'black': BLACK,
        'white': WHITE,
        'red': RED,
        'green': GREEN,
        'blue': BLUE,
    }
    return colors.get(name.lower(), BLACK)  # Default to black if color not found
