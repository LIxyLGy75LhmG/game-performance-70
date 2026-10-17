import json
import os
from typing import Any, Dict

def load_game_config(file_path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Merges file-based configuration with provided defaults using dict expansion."""
    config = defaults.copy()
    
    if not os.path.exists(file_path):
        return config

    try:
        with open(file_path, 'r') as f:
            user_config = json.load(f)
            if isinstance(user_config, dict):
                config = {**config, **user_config}
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def patch_config(target: Dict[str, Any], overrides: Dict[str, Any]) -> Dict[str, Any]:
    """In-place patch mechanism for runtime performance tuning."""
    for key, value in overrides.items():
        if key in target:
            target[key] = value
    return target

if __name__ == "__main__":
    # Example usage for high-performance settings
    defaults = {"fps_limit": 60, "vsync": True, "quality": "high"}
    active_config = load_game_config("settings.json", defaults)
    print(f"Active config state: {active_config}")