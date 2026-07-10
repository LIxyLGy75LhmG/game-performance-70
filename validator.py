import re

def validate_username(username):
    if not isinstance(username, str):
        raise ValueError('Username must be a string')
    if not (3 <= len(username) <= 20):
        raise ValueError('Username must be between 3 and 20 characters')
    if not re.match('^[a-zA-Z0-9_]+$', username):
        raise ValueError('Username can only contain alphanumeric characters and underscores')
    return True

def validate_score(score):
    if not isinstance(score, int):
        raise ValueError('Score must be an integer')
    if score < 0:
        raise ValueError('Score must not be negative')
    return True


def validate_input_data(username, score):
    validate_username(username)
    validate_score(score)

if __name__ == '__main__':
    try:
        validate_input_data('player1', 100)
        print('Input validation succeeded.')
    except ValueError as e:
        print(f'Input validation failed: {e}')