from typing import Dict, Any

class GameConfig:
    """
    Class to handle game configuration settings.
    """
    def __init__(self, settings: Dict[str, Any]) -> None:
        """
        Initialize the GameConfig with a dictionary of settings.
        
        :param settings: A dictionary containing game configuration settings.
        """
        self.settings = settings

    def get_setting(self, key: str) -> Any:
        """
        Retrieve the value of the specified setting.
        
        :param key: The key of the setting to retrieve.
        :return: The value of the setting, or None if not found.
        """
        return self.settings.get(key, None)

    def set_setting(self, key: str, value: Any) -> None:
        """
        Set the value of the specified setting.
        
        :param key: The key of the setting to update.
        :param value: The new value for the setting.
        """
        self.settings[key] = value

    def all_settings(self) -> Dict[str, Any]:
        """
        Retrieve all settings.
        
        :return: A dictionary of all settings.
        """
        return self.settings.copy()
