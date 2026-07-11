from typing import List, Dict


def calculate_frame_rate(frames: int, duration: float) -> float:
    """
    Calculate the frames per second (FPS).
    
    Args:
        frames (int): The number of frames rendered.
        duration (float): The time duration in seconds.
    
    Returns:
        float: The calculated frames per second.
    """
    if duration <= 0:
        raise ValueError("Duration must be greater than zero.")
    return frames / duration


def get_high_scores(scores: List[int]) -> Dict[str, int]:
    """
    Generates a dictionary of high scores and their ranks.
    
    Args:
        scores (List[int]): A list of player scores.
    
    Returns:
        Dict[str, int]: A dictionary with ranks as keys and scores as values.
    """
    sorted_scores = sorted(set(scores), reverse=True)
    return {f'Rank {rank + 1}': score for rank, score in enumerate(sorted_scores)}


def format_time(milliseconds: int) -> str:
    """
    Convert milliseconds to a formatted time string.
    
    Args:
        milliseconds (int): Time in milliseconds.
    
    Returns:
        str: Formatted time string in "mm:ss".
    """
    seconds = milliseconds // 1000
    minutes, seconds = divmod(seconds, 60)
    return f'{minutes:02}:{seconds:02}'
