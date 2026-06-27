import json
import os

DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 75,
    'language': 'en',
}

def load_config(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            try:
                user_config = json.load(file)
                return {**DEFAULT_CONFIG, **user_config}
            except json.JSONDecodeError:
                print('Error decoding JSON, loading defaults.')
    return DEFAULT_CONFIG

if __name__ == '__main__':
    config = load_config('config.json')
    print(config)