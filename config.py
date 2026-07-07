from typing import Dict, Any

class Config:
    """
    Class to manage game configuration settings.
    """
    def __init__(self) -> None:
        self.settings: Dict[str, Any] = {}

    def load(self, filepath: str) -> None:
        """
        Load configuration settings from a given file.
        
        Args:
            filepath (str): Path to the configuration file.
        """
        with open(filepath, 'r') as file:
            self.settings = eval(file.read())  # Replace with a safe parser in production

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get the value of a configuration key.
        
        Args:
            key (str): The key for the desired configuration value.
            default (Any): Default value to return if the key is not found.
        
        Returns:
            Any: The value from the settings or the default.
        """
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Set a configuration key to a new value.
        
        Args:
            key (str): The key to set.
            value (Any): The value to assign to the key.
        """
        self.settings[key] = value

    def save(self, filepath: str) -> None:
        """
        Save the current settings to a file.
        
        Args:
            filepath (str): Path to save the configuration file.
        """
        with open(filepath, 'w') as file:
            file.write(str(self.settings))

config = Config()