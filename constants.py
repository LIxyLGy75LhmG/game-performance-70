SCORE_MULTIPLIER = 1.5
LEVELS = {'easy': 1, 'medium': 2, 'hard': 3}
WEAPON_TYPES = ['sword', 'bow', 'magic']
ITEMS = {
    'health_potion': {'restore': 50, 'quantity': 10},
    'mana_potion': {'restore': 30, 'quantity': 5},
    'stamina_potion': {'restore': 20, 'quantity': 8}
}
POWER_UPS = [
    {'type': 'speed', 'duration': 30},
    {'type': 'strength', 'duration': 20},
    {'type': 'invisibility', 'duration': 15}
]
DEFAULT_PLAYER_STATS = {
    'health': 100,
    'mana': 50,
    'stamina': 70,
    'level': LEVELS['easy'],
    'score': 0
}
MAX_INVENTORY_SIZE = 20