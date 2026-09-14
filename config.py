import os
import logging

class ConfigError(Exception):
    pass

def get_performance_limit(key: str, default: int = 60) -> int:
    try:
        value = os.getenv(key)
        if value is None:
            return default
        parsed = int(value)
        if parsed <= 0:
            raise ValueError('non-positive limit')
        return parsed
    except (ValueError, TypeError) as e:
        logging.error(f'Invalid config for {key}: {e}. Falling back to {default}')
        return default

def validate_game_settings(settings: dict):
    required = ['fps_cap', 'render_scale']
    missing = [k for k in required if k not in settings]
    if missing:
        raise ConfigError(f'missing critical keys: {missing}')
    
    if not (0.1 <= settings.get('render_scale', 1.0) <= 2.0):
        settings['render_scale'] = 1.0
        logging.warning('render_scale out of bounds, reset to 1.0')

class GameConfig:
    def __init__(self, raw_data: dict):
        try:
            validate_game_settings(raw_data)
            self.fps = raw_data.get('fps_cap', 60)
            self.scale = raw_data.get('render_scale', 1.0)
        except ConfigError as e:
            logging.critical(f'failed to initialize config: {e}')
            self.fps = 30
            self.scale = 0.5