import os
import json
import logging

class ConfigLoader:
    def __init__(self, path='settings.json'):
        self.path = path
        self.settings = {}

    def load(self):
        try:
            if not os.path.exists(self.path):
                raise FileNotFoundError(f'Config file {self.path} missing')
            with open(self.path, 'r') as f:
                self.settings = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
            self.settings = self._fallback_defaults(e)
        return self.settings

    def _fallback_defaults(self, error):
        logging.error(f'Configuration failure: {error}. Falling back to low-latency defaults.')
        return {
            'fps_cap': 60,
            'texture_quality': 'low',
            'vsync': False,
            'render_path': 'safe_mode'
        }

def get_game_config():
    loader = ConfigLoader()
    return loader.load()

if __name__ == '__main__':
    cfg = get_game_config()
    print(f'Game engine initialized with: {cfg}')