import json
import os

class ConfigProcessor:
    DEFAULTS = {
        "game": {
            "performance": {
                "fps_limit": 60,
                "resolution_width": 1920,
                "resolution_height": 1080,
                "enable_vsync": True,
                "graphics_quality": "high"
            },
            "audio": {
                "master_volume": 0.75,
                "sound_effects": True
            }
        }
    }

    def __init__(self, path="config.json"):
        self.path = path
        self.data = {}
        self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path) as f:
                user_data = json.load(f)
        else:
            user_data = {}
        self.data = self._merge_defaults(self.DEFAULTS, user_data)

    def _merge_defaults(self, defaults, user):
        result = {}
        stack = [(defaults, user, result)]
        while stack:
            def_dict, usr_dict, res_dict = stack.pop()
            all_keys = set(def_dict.keys()) | set(usr_dict.keys())
            for key in all_keys:
                if key in def_dict and key in usr_dict and isinstance(def_dict[key], dict) and isinstance(usr_dict[key], dict):
                    res_dict[key] = {}
                    stack.append((def_dict[key], usr_dict[key], res_dict[key]))
                elif key in usr_dict:
                    res_dict[key] = usr_dict[key]
                else:
                    res_dict[key] = def_dict[key]
        return result

    def get(self, key_path):
        keys = key_path.split(".")
        current = self.data
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        return current

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=4)