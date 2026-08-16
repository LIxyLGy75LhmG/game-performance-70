import re

class InputValidator:
    def __init__(self):
        self.patterns = {
            'username': re.compile(r'^[a-zA-Z0-9]{3,}$'),
            'email': re.compile(r'^[\w\.-]+@[a-zA-Z\.-]+\.[a-zA-Z]{2,}$'),
            'password': re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$')
        }

    def validate_username(self, username: str) -> bool:
        return bool(self.patterns['username'].match(username))

    def validate_email(self, email: str) -> bool:
        return bool(self.patterns['email'].match(email))

    def validate_password(self, password: str) -> bool:
        return bool(self.patterns['password'].match(password))

    def validate_all(self, username: str, email: str, password: str) -> dict:
        return {
            'username': self.validate_username(username),
            'email': self.validate_email(email),
            'password': self.validate_password(password)
        }

# Example validation usage
if __name__ == '__main__':
    validator = InputValidator()
    result = validator.validate_all('user1', 'user@example.com', 'pass123')
    print(result)