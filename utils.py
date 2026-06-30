import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class GameError(Exception):
    pass


def divide(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both arguments must be numbers.')
        return a / b
    except ZeroDivisionError:
        logging.error('Attempted to divide by zero.')
        raise GameError('Division by zero is not allowed.')
    except ValueError as ve:
        logging.error(f'ValueError: {ve}')
        raise GameError(f'Invalid input: {ve}')


def random_item_from_list(items):
    try:
        if not isinstance(items, list) or not items:
            raise ValueError('Input must be a non-empty list.')
        return random.choice(items)
    except ValueError as ve:
        logging.error(f'ValueError: {ve}')
        raise GameError(f'Cannot retrieve item: {ve}')


def game_score_calculator(scores):
    try:
        if not all(isinstance(score, (int, float)) for score in scores):
            raise ValueError('All scores must be numbers.')
        if len(scores) == 0:
            raise ValueError('Score list cannot be empty.')
        return sum(scores) / len(scores)
    except ValueError as ve:
        logging.error(f'ValueError: {ve}')
        raise GameError(f'Unable to calculate score: {ve}')
