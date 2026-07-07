import json
import os

DEFAULT_CONFIG = {
    'screen_width': 1024,
    'screen_height': 768,
    'full_screen': False,
    'volume': 0.5,
    'language': 'en',
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()  # Start with defaults
        self.load_config()

    def load_config(self):
        if os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as file:
                try:
                    user_config = json.load(file)
                    self.config.update(user_config)
                except json.JSONDecodeError:
                    print('Error loading config: Invalid JSON. Using defaults.')

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

# Example of usage
# loader = ConfigLoader()
# print(loader.get('volume'))
