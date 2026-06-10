import json
import os

DEFAULT_CONFIG = {
    'fullscreen': False,
    'resolution': '1920x1080',
    'volume': 0.5,
    'controls': {
        'move_left': 'A',
        'move_right': 'D',
        'jump': 'SPACE',
        'shoot': 'LEFT_MOUSE'
    }
}

class ConfigLoader:
    def __init__(self, custom_config_path=None):
        self.config = DEFAULT_CONFIG.copy()
        if custom_config_path:
            self.load_config(custom_config_path)

    def load_config(self, path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                custom_config = json.load(f)
                self._merge_configs(self.config, custom_config)
        else:
            print(f"Warning: Config file '{path}' not found. Using defaults.")

    def _merge_configs(self, default, custom):
        for key, value in custom.items():
            if isinstance(value, dict) and key in default:
                self._merge_configs(default[key], value)
            else:
                default[key] = value

    def get(self):
        return self.config

# Example usage
if __name__ == '__main__':
    loader = ConfigLoader('user_config.json')
    print(loader.get())