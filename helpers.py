import random

def generate_random_number(minimum, maximum):
    if not isinstance(minimum, int) or not isinstance(maximum, int):
        raise ValueError('Minimum and maximum must be integers.')
    if minimum >= maximum:
        raise ValueError('Minimum must be less than maximum.')
    return random.randint(minimum, maximum)


def is_valid_input(user_input):
    return isinstance(user_input, int) and user_input >= 1


def get_user_input():
    while True:
        try:
            user_input = int(input('Enter a positive integer: '))
            if is_valid_input(user_input):
                return user_input
            else:
                print('Invalid input. Try again.')
        except ValueError:
            print('Please enter a valid integer.')


def main_loop():
    while True:
        user_number = get_user_input()
        print(f'You entered: {user_number}')
        # Simulating game tick with random number generation
        random_number = generate_random_number(1, 100)
        print(f'Random number generated: {random_number}')
        
        continue_game = input('Do you want to continue? (y/n): ').strip().lower()
        if continue_game != 'y':
            break

if __name__ == '__main__':
    main_loop()