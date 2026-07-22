import random
import math


def roll_dice(sides=6, times=1):
    return [random.randint(1, sides) for _ in range(times)]


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def lerp(start, end, t):
    return start + (end - start) * t


def distance(point_a, point_b):
    return math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)


def is_power_of_two(n):
    return (n & (n - 1)) == 0 and n > 0


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def choose(n, k):
    if k == 0:
        return 1
    return factorial(n) // (factorial(k) * factorial(n - k))


def shuffle_list(items):
    random.shuffle(items)
    return items


def get_random_choice(choices):
    return random.choice(choices)