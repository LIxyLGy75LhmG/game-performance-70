import re

def validate_email(email):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.com'
    if re.fullmatch(pattern, email):
        return True
    return False

def validate_username(username):
    if 3 <= len(username) <= 15 and username.isalnum():
        return True
    return False

def validate_password(password):
    if (len(password) >= 8 and
i = re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'[0-9]', password) and
i and
        re.search(r'[!@#$%^&*]', password)):
        return True
    return False

def validate_game_id(game_id):
    if isinstance(game_id, int) and game_id > 0:
        return True
    return False