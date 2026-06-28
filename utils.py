import json
import math
import random

def generate_random_player_stats(num_players):
    stats = []
    for _ in range(num_players):
        player = {
            'id': random.randint(1000, 9999),
            'level': random.randint(1, 100),
            'health': random.randint(50, 500),
            'strength': random.randint(10, 100),
            'agility': random.randint(5, 100),
            'intelligence': random.randint(1, 100)
        }
        stats.append(player)
    return stats


def calculate_distance(point1, point2):
    if len(point1) != 2 or len(point2) != 2:
        raise ValueError('Both points must be of the form [x, y]')
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def save_stats_to_json(file_path, stats):
    with open(file_path, 'w') as f:
        json.dump(stats, f, indent=4)


def load_stats_from_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)