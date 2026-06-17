from typing import Tuple

# Game constants

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
FPS: int = 60

COLOR_BLACK: Tuple[int, int, int] = (0, 0, 0)
COLOR_WHITE: Tuple[int, int, int] = (255, 255, 255)
COLOR_RED: Tuple[int, int, int] = (255, 0, 0)
COLOR_GREEN: Tuple[int, int, int] = (0, 255, 0)
COLOR_BLUE: Tuple[int, int, int] = (0, 0, 255)

# Game States

class GameState:
    MENU: str = "menu"
    PLAYING: str = "playing"
    PAUSED: str = "paused"
    GAME_OVER: str = "game_over"

    @staticmethod
    def all_states() -> Tuple[str, ...]:
        return (GameState.MENU, GameState.PLAYING, GameState.PAUSED, GameState.GAME_OVER)

# Difficulty Levels

class Difficulty:
    EASY: int = 1
    MEDIUM: int = 2
    HARD: int = 3

    @staticmethod
    def levels() -> Tuple[int, int, int]:
        return (Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD)
