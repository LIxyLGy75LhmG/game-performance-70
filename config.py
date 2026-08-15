import json
import os

class ConfigLoader:
    def __init__(self, default_config: dict, config_path: str = 'config.json'):
        self.default_config = default_config
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self) -> dict:
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as file:
                user_config = json.load(file)
            return {**self.default_config, **user_config}
        return self.default_config

    def get(self, key, default=None):
        return self.config.get(key, default)

# Sample default config
DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 75,
    'language': 'en'
}

if __name__ == '__main__':
    config_loader = ConfigLoader(DEFAULT_CONFIG)
    print(config_loader.get('resolution'))  # Output default resolution