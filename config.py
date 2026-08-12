import os

class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH = os.path.join(BASE_DIR, 'settings.json')

    @staticmethod
    def get_config_value(key):
        import json
        with open(Config.CONFIG_PATH) as config_file:
            config = json.load(config_file)
            return config.get(key, None)

    @staticmethod
    def set_config_value(key, value):
        import json
        with open(Config.CONFIG_PATH, 'r+') as config_file:
            config = json.load(config_file)
            config[key] = value
            config_file.seek(0)
            json.dump(config, config_file, indent=4)
            config_file.truncate()