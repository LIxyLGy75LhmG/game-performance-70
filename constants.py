import json
import os

def load_config(filename='config.json', defaults=None):
    if defaults is None:
        defaults = {}
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            config = json.load(f)
        config = {**defaults, **config}
    else:
        config = defaults
    return config

# Default configuration
DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 75,
    'difficulty': 'normal'
}

# Load configuration
CONFIG = load_config('config.json', DEFAULT_CONFIG)  
