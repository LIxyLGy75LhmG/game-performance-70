import random


def generate_random_position(bounds):
    """Generate a random position within given bounds."""
    x = random.uniform(bounds['x_min'], bounds['x_max'])
    y = random.uniform(bounds['y_min'], bounds['y_max'])
    return {'x': x, 'y': y}


def is_within_bounds(position, bounds):
    """Check if a position is within specified bounds."""
    return (bounds['x_min'] <= position['x'] <= bounds['x_max'] and
            bounds['y_min'] <= position['y'] <= bounds['y_max'])


def clamp(value, min_value, max_value):
    """Clamp a value between min and max limits."""
    return max(min_value, min(value, max_value))


def calculate_distance(point_a, point_b):
    """Calculate the Euclidean distance between two points."""
    return ((point_a['x'] - point_b['x']) ** 2 + (point_a['y'] - point_b['y']) ** 2) ** 0.5


def lerp(start, end, t):
    """Linear interpolation between two values based on t."""
    return start + (end - start) * t
