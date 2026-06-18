from typing import Dict, Any, Optional

class Config:
    def __init__(self, settings: Optional[Dict[str, Any]] = None) -> None:
        """Initialize the Config with optional settings.

        Args:
            settings (Optional[Dict[str, Any]]): A dictionary of configuration settings.
        """
        self.settings = settings if settings else {}

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a config value by key, or default if not found.

        Args:
            key (str): The configuration key to retrieve.
            default (Any): The default value to return if key is not found.

        Returns:
            Any: The value associated with the key, or the default.
        """
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a value for a given config key.

        Args:
            key (str): The configuration key to set.
            value (Any): The value to associate with the key.
        """
        self.settings[key] = value

    def load(self, config_dict: Dict[str, Any]) -> None:
        """Load multiple configuration settings from a dictionary.

        Args:
            config_dict (Dict[str, Any]): A dictionary of settings to load.
        """
        self.settings.update(config_dict)

    def __repr__(self) -> str:
        """Return a string representation of the config settings.

        Returns:
            str: String representation of the settings.
        """
        return f"Config(settings={self.settings})"