import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.user_config = { }

    def load(self, filepath):
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:
                self.user_config = json.load(file)

    def get(self, key):
        return self.user_config.get(key, self.default_config.get(key))

    def get_all(self):
        combined_config = self.default_config.copy()
        combined_config.update(self.user_config)
        return combined_config

if __name__ == '__main__':
    defaults = {'difficulty': 'normal', 'sound_volume': 50, 'resolution': '1920x1080'}
    config_loader = ConfigLoader(defaults)
    config_loader.load('user_config.json')
    print(config_loader.get_all())