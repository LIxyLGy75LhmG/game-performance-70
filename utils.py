import random
import math

def generate_random_coordinates(x_range, y_range):
    return (random.uniform(*x_range), random.uniform(*y_range))


def normalize_vector(vector):
    magnitude = math.sqrt(sum(i ** 2 for i in vector))
    return tuple(i / magnitude for i in vector) if magnitude else (0, 0)


def lerp(start, end, t):
    return start + (end - start) * t


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def calculate_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))


def random_choice(choices):
    return random.choice(choices)