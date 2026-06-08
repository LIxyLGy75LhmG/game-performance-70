import json
import os

DEFAULT_CONFIG = {
    'volume': 50,
    'resolution': '1920x1080',
    'fullscreen': True,
    'language': 'en',
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                try:
                    user_config = json.load(f)
                except json.JSONDecodeError:
                    print('Error decoding JSON, using defaults.')
                    return DEFAULT_CONFIG
            return {**DEFAULT_CONFIG, **user_config}
        else:
            return DEFAULT_CONFIG

    def get(self, key):
        return self.config.get(key, DEFAULT_CONFIG.get(key))

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

config_loader = ConfigLoader()