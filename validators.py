from typing import Any, Dict


def validate_positive_integer(value: Any) -> int:
    """
    Validate that the provided value is a positive integer.
    
    Args:
        value (Any): The value to validate.
    
    Raises:
        ValueError: If the value is not a positive integer.
    
    Returns:
        int: The validated positive integer.
    """
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{value} is not a positive integer.")
    return value


def validate_non_empty_string(value: Any) -> str:
    """
    Validate that the provided value is a non-empty string.
    
    Args:
        value (Any): The value to validate.
    
    Raises:
        ValueError: If the value is not a non-empty string.
    
    Returns:
        str: The validated non-empty string.
    """
    if not isinstance(value, str) or not value:
        raise ValueError(f"{value} is not a non-empty string.")
    return value


def validate_settings(settings: Dict[str, Any]) -> None:
    """
    Validate the game settings to ensure they meet required criteria.
    
    Args:
        settings (Dict[str, Any]): The game settings dictionary to validate.
    
    Raises:
        ValueError: If any settings are invalid.
    """
    try:
        validate_positive_integer(settings['max_players'])
        validate_non_empty_string(settings['game_name'])
    except KeyError as e:
        raise ValueError(f'Missing required setting: {e}')

    
# Example usage:
if __name__ == '__main__':
    game_settings = {'max_players': 5, 'game_name': 'Survival Arena'}
    validate_settings(game_settings)
