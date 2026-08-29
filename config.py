import json
import os
from typing import Dict, Any
class GamePerformanceConfig:
    DEFAULTS = {
        "fps_limit": 60,
        "resolution_width": 1920,
        "resolution_height": 1080,
        "particle_count": 100,
        "audio_volume": 0.75,
        "vsync_enabled": True
    }
    def __init__(self, config_file="performance_config.json"):
        self.config_file = config_file
        self.settings = self._initialize_with_handling()
    def _initialize_with_handling(self):
        settings = self.DEFAULTS.copy()
        if not os.path.isfile(self.config_file):
            return settings
        try:
            with open(self.config_file, "r") as f:
                loaded_data = json.load(f)
            validated = {}
            for key, value in loaded_data.items():
                if key not in settings:
                    continue
                try:
                    if key in ["fps_limit", "particle_count", "resolution_width", "resolution_height"]:
                        num_val = int(value)
                        if num_val <= 0:
                            num_val = settings[key]
                        elif num_val > 10000:
                            num_val = settings[key] // 2
                        validated[key] = num_val
                    elif key == "audio_volume":
                        vol = float(value)
                        if not 0 <= vol <= 1:
                            vol = 0.5
                        validated[key] = vol
                    elif key == "vsync_enabled":
                        validated[key] = str(value).lower() in ["true", "1", "yes"]
                    else:
                        validated[key] = value
                except (ValueError, TypeError):
                    print(f"Glitch in setting {key}. Falling back.")
                    validated[key] = settings[key]
            return {**settings, **validated}
        except (json.JSONDecodeError, IOError, OSError):
            print("Config load failure. Engaging safe mode defaults.")
            return settings
        except Exception:
            print("Critical performance error.")
            return settings
    def get(self, key):
        try:
            return self.settings[key]
        except KeyError:
            return self.DEFAULTS.get(key)