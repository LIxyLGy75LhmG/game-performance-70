import random

class CustomError(Exception):
    pass


def divide_numbers(numerator, denominator):
    try:
        if denominator == 0:
            raise CustomError('Denominator cannot be zero.')
        result = numerator / denominator
    except TypeError as e:
        raise CustomError(f'Invalid input type: {e}')
    return result


def random_choice(options):
    if not isinstance(options, list) or len(options) == 0:
        raise CustomError('Options must be a non-empty list.')
    return random.choice(options)


def safe_get(dictionary, key, default=None):
    try:
        return dictionary[key]
    except KeyError:
        return default
    except TypeError as e:
        raise CustomError(f'Invalid dictionary or key: {e}')