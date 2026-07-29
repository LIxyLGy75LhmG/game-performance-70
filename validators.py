import re

def is_valid_username(username):
    if not isinstance(username, str):
        return False
    return 3 <= len(username) <= 20 and re.match('^[a-zA-Z0-9_]+$', username) is not None


def is_valid_password(password):
    if not isinstance(password, str):
        return False
    return (8 <= len(password) <= 16 and 
            any(c.isdigit() for c in password) and 
            any(c.isalpha() for c in password) and 
            any(c in '!@#$%^&*()' for c in password))


def is_valid_email(email):
    if not isinstance(email, str):
        return False
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None


def validate_user_data(username, password, email):
    return (is_valid_username(username) and 
            is_valid_password(password) and 
            is_valid_email(email))
