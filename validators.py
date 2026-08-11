import re

class InputValidator:
    @staticmethod
    def validate_username(username):
        if not isinstance(username, str) or len(username) < 3:
            raise ValueError('Username must be a string with at least 3 characters')
        if not re.match('^[a-zA-Z0-9_]+$', username):
            raise ValueError('Username can only contain alphanumeric characters and underscores')
        return True

    @staticmethod
    def validate_score(score):
        if not isinstance(score, int) or score < 0:
            raise ValueError('Score must be a non-negative integer')
        return True

    @staticmethod
    def validate_level(level):
        if level not in ['easy', 'medium', 'hard']:
            raise ValueError('Level must be one of the following: easy, medium, hard')
        return True