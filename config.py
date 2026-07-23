import json
import os

def load_config(config_file='config.json', defaults=None):
    if defaults is None:
        defaults = {}
    
    if not os.path.exists(config_file):
        return defaults
    
    with open(config_file, 'r') as file:
        try:
            user_config = json.load(file)
        except json.JSONDecodeError:
            print('Error decoding JSON, using defaults')
            return defaults
    
    # Merge defaults with user config, prioritize user settings
    merged_config = {**defaults, **user_config}
    return merged_config

# Example default configuration
if __name__ == '__main__':
    defaults = {
        'resolution': '1920x1080',
        'fullscreen': True,
        'volume': 80
    }
    config = load_config(defaults=defaults)
    print(config)