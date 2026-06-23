def calculate_movement_speed(distance, time):
    """
    Calculate movement speed given distance and time.
    :param distance: float, the distance traveled
    :param time: float, the time taken
    :return: float, speed in units per second
    """
    if time <= 0:
        raise ValueError("Time must be greater than zero.")
    return distance / time


def clamp(value, min_value, max_value):
    """
    Constrain a value between a minimum and maximum.
    :param value: float, the value to clamp
    :param min_value: float, the minimum limit
    :param max_value: float, the maximum limit
    :return: float, clamped value
    """
    return max(min_value, min(value, max_value))


def linear_interpolation(start, end, factor):
    """
    Linearly interpolate between two values.
    :param start: float, the starting value
    :param end: float, the ending value
    :param factor: float, the interpolation factor (0-1)
    :return: float, interpolated value
    """
    if not (0 <= factor <= 1):
        raise ValueError("Factor must be between 0 and 1.")
    return start + (end - start) * factor


def random_choice_from_list(lst):
    """
    Return a random element from a non-empty list.
    :param lst: list, input list from which to choose
    :return: random element from the list
    """
    if not lst:
        raise ValueError("List cannot be empty.")
    from random import choice
    return choice(lst)