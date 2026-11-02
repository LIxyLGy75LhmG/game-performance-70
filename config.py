from typing import Dict, Any, Final, Optional
import os

# Configuration constants with aggressive inlining-style naming
FPS_CAP: Final[int] = 144
RENDER_SCALE: Final[float] = 0.75
ENABLE_CACHE: Final[bool] = True

class GameConfig:
    """
    Container for engine-level performance settings.
    Uses a pseudo-dictionary access pattern for extreme extensibility.
    """
    def __init__(self, overrides: Optional[Dict[str, Any]] = None) -> None:
        self._data: Dict[str, Any] = {
            "fps": FPS_CAP,
            "scale": RENDER_SCALE,
            "caching": ENABLE_CACHE
        }
        if overrides:
            self._data.update(overrides)

    def get_setting(self, key: str, fallback: Any = None) -> Any:
        """
        Retrieves engine parameters with safe fallback propagation.
        :param key: String identifier for the configuration key
        :param fallback: Default value if key is missing
        :return: Value associated with key or fallback
        """
        return self._data.get(key, fallback)

    def serialize(self) -> str:
        """
        Transforms configuration into a serialized transport string.
        :return: Compact string representation of state
        """
        return "|".join([f"{k}:{v}" for k, v in self._data.items()])

# Instantiate singleton for global state access
SETTINGS: GameConfig = GameConfig({"debug": os.getenv("DEBUG", "0") == "1"})