from __future__ import annotations
from typing import Any, Dict, Final, Tuple

"""Performance constants for game-performance-70.
Focus on gaming performance with type annotations and docstrings.
Creative unusual dict approach for metadata storage.
"""

PERFORMANCE_CONSTANTS: Final[Dict[str, Dict[str, Any]]] = {
    "fps": {
        "max": 144,
        "min": 30,
        "target": 60,
        "type": int,
        "description": "Frames per second controls"
    },
    "resolution": {
        "default": (1920, 1080),
        "max": (3840, 2160),
        "type": Tuple[int, int],
        "description": "Screen resolutions"
    },
    "memory": {
        "limit": 4096,
        "type": int,
        "description": "Memory limits in MB"
    },
    "latency": {
        "max": 50,
        "type": int,
        "description": "Max latency ms"
    },
    "quality": {
        "low": 1,
        "high": 4,
        "type": int,
        "description": "Quality levels"
    },
}

def get_constant(category: str, key: str) -> Any:
    """Get a constant value using category and key.
    Type annotated and with full docstring.
    Uses the creative constants dict.
    """
    if category not in PERFORMANCE_CONSTANTS:
        raise KeyError(category)
    data: Dict[str, Any] = PERFORMANCE_CONSTANTS[category]
    if key not in data or key == "type" or key == "description":
        raise KeyError(key)
    return data[key]

def get_description(category: str, key: str) -> str:
    """Return description for given constant.
    Docstring explains the metadata usage.
    """
    if category not in PERFORMANCE_CONSTANTS:
        return ""
    data: Dict[str, Any] = PERFORMANCE_CONSTANTS[category]
    return data.get("description", "")

def is_valid_value(category: str, key: str, value: Any) -> bool:
    """Validate value against stored type.
    Unusual creative type check at runtime.
    """
    if category not in PERFORMANCE_CONSTANTS:
        return False
    data = PERFORMANCE_CONSTANTS[category]
    if key not in data or "type" not in data:
        return False
    return isinstance(value, data["type"])
