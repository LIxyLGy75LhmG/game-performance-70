import random
import math

def random_position(width, height):
    return random.randint(0, width), random.randint(0, height)


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def interpolate(a, b, t):
    return a + (b - a) * t


def normalize(v):
    length = math.sqrt(v[0] ** 2 + v[1] ** 2)
    return v[0] / length, v[1] / length if length > 0 else (0, 0)