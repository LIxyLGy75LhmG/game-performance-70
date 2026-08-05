import re

def validate_input(player_input):
    if not isinstance(player_input, str):
        raise ValueError('Input must be a string.')  
    player_input = player_input.strip()
    if len(player_input) == 0:
        raise ValueError('Input cannot be empty.')
    if not re.match('^[a-zA-Z0-9_]*$', player_input):
        raise ValueError('Input contains invalid characters. Only alphanumeric and underscores are allowed.')
    return player_input

if __name__ == '__main__':
    while True:
        try:
            user_input = input('Enter your command: ')
            validated_input = validate_input(user_input)
            print(f'Validated input: {validated_input}')
        except ValueError as e:
            print(f'Error: {e}')
            continue
        # Further processing with validated_input
