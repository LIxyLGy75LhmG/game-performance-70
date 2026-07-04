import json

DEFAULT_CONFIG = {
    'window_size': {'width': 800, 'height': 600},
    'fps': 60,
    'music_enabled': True,
    'difficulty': 'normal',
}

class ConfigLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_config(self):
        try:
            with open(self.filepath, 'r') as file:
                user_config = json.load(file)
                return self._merge_configs(DEFAULT_CONFIG, user_config)
        except (FileNotFoundError, json.JSONDecodeError):
            return DEFAULT_CONFIG

    def _merge_configs(self, defaults, user):
        for key, value in user.items():
            if isinstance(value, dict) and key in defaults:
                defaults[key] = self._merge_configs(defaults[key], value)
            else:
                defaults[key] = value
        return defaults

if __name__ == '__main__':
    loader = ConfigLoader('config.json')
    config = loader.load_config()
    print(config)