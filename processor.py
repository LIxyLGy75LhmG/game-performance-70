import random
import json

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) < 1:
        raise ValueError('Input cannot be empty')
    if len(user_input) > 100:
        raise ValueError('Input must not exceed 100 characters')
    return True

def main_processing_loop():
    while True:
        user_input = input('Enter your command (or type exit): ')
        if user_input.lower() == 'exit':
            break
        try:
            validate_input(user_input)
            # Simulate processing the command
            print(f'Processing command: {user_input}')
            response = {'response': f'Command {user_input} processed successfully'}
            print(json.dumps(response))
        except ValueError as e:
            print(e)
        except Exception as e:
            print('An unexpected error occurred:', str(e))

if __name__ == '__main__':
    main_processing_loop()