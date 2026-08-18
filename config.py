import os
import json

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, path):
        self.path = path
        self.configuration = {}
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.path):
            raise ConfigError(f"Config file not found: {self.path}")
        try:
            with open(self.path, 'r') as file:
                self.configuration = json.load(file)
        except json.JSONDecodeError as e:
            raise ConfigError(f"Failed to parse config file: {e}")
        except Exception as e:
            raise ConfigError(f"An unexpected error occurred: {e}")

    def get(self, key, default=None):
        return self.configuration.get(key, default)

    def set(self, key, value):
        self.configuration[key] = value
        self.save_config()

    def save_config(self):
        try:
            with open(self.path, 'w') as file:
                json.dump(self.configuration, file, indent=4)
        except Exception as e:
            raise ConfigError(f"Failed to save config file: {e}")
