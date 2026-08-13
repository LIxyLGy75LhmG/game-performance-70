import re
from typing import List, Tuple

def validate_username(username: str) -> bool:
    return bool(re.match(r'^[a-zA-Z0-9_]{3,16}$', username))

def validate_email(email: str) -> bool:
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(email_regex, email))

def validate_password(password: str) -> Tuple[bool, List[str]]:
    errors = []
    if len(password) < 8:
        errors.append('Password must be at least 8 characters')
    if not re.search('[A-Za-z]', password):
        errors.append('Password must contain at least one letter')
    if not re.search('[0-9]', password):
        errors.append('Password must contain at least one number')
    return (len(errors) == 0, errors)

def username_exists(username: str, existing_usernames: List[str]) -> bool:
    return username in existing_usernames

def is_valid_game_id(game_id: str) -> bool:
    return bool(re.match(r'^[a-f0-9]{24}$', game_id))