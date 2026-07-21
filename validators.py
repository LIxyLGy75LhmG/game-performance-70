import re

def validate_player_name(name):
    if not isinstance(name, str):
        raise ValueError('Player name must be a string')
    if not (3 <= len(name) <= 20):
        raise ValueError('Player name must be between 3 and 20 characters')
    if not re.match('^[a-zA-Z0-9_]*$', name):
        raise ValueError('Player name can only contain letters, numbers, and underscores')
    return True

def validate_score(score):
    if not isinstance(score, (int, float)):
        raise ValueError('Score must be a number')
    if score < 0:
        raise ValueError('Score cannot be negative')
    return True

def validate_match_history(history):
    if not isinstance(history, list):
        raise ValueError('Match history must be a list')
    if not all(isinstance(match, dict) for match in history):
        raise ValueError('Each match must be a dictionary')
    return True

# Example usage (for testing)
if __name__ == '__main__':
    try:
        assert validate_player_name('Player_1') == True
        assert validate_score(100) == True
        assert validate_match_history([{'match_id': 1}, {'match_id': 2}]) == True
        print('All validations passed.')
    except ValueError as e:
        print(e)