from typing import Any, Dict


def is_valid_score(score: int) -> bool:
    """Check if the score is within valid range.

    Args:
        score (int): Score to validate.

    Returns:
        bool: True if score is valid, False otherwise.
    """
    return 0 <= score <= 100


def has_required_fields(data: Dict[str, Any], required_fields: list) -> bool:
    """Check if the required fields are present in the data.

    Args:
        data (Dict[str, Any]): Dictionary containing data to check.
        required_fields (list): List of required field names.

    Returns:
        bool: True if all required fields are present, False otherwise.
    """  
    return all(field in data for field in required_fields)


def is_valid_username(username: str) -> bool:
    """Validate the username according to specific rules.

    Args:
        username (str): Username to validate.

    Returns:
        bool: True if the username is valid, False otherwise.
    """  
    return username.isalnum() and 3 <= len(username) <= 20