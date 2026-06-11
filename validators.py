import re

class ValidationError(Exception):
    pass

def validate_username(username):
    if not isinstance(username, str):
        raise ValidationError('Username must be a string.')
    if len(username) < 3 or len(username) > 20:
        raise ValidationError('Username must be between 3 and 20 characters.')
    if not re.match('^[a-zA-Z0-9_]*$', username):
        raise ValidationError('Username can only contain letters, numbers, and underscores.')
    return True


def validate_email(email):
    if not isinstance(email, str):
        raise ValidationError('Email must be a string.')
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise ValidationError('Invalid email format.')
    return True


def validate_password(password):
    if not isinstance(password, str):
        raise ValidationError('Password must be a string.')
    if len(password) < 8:
        raise ValidationError('Password must be at least 8 characters.')
    if not any(char.isdigit() for char in password):
        raise ValidationError('Password must contain at least one digit.')
    if not any(char.isupper() for char in password):
        raise ValidationError('Password must contain at least one uppercase letter.')
    return True