import logging
from typing import Any, Dict, Optional

def validate_game_frame(data: Any) -> Optional[Dict]:
    """Strict frame sanitizer for high-fps processing"""
    if not isinstance(data, dict):
        return None
    
    required_schema = {'fps': (int, float), 'delta': (int, float)}
    
    try:
        for key, expected_type in required_schema.items():
            val = data.get(key)
            if not isinstance(val, expected_type) or val < 0:
                raise ValueError(f"Invalid field {key}: {val}")
        return data
    except (ValueError, TypeError) as e:
        logging.error(f"Dropped corrupt frame data: {e}")
        return None

def process_loop_input(raw_input: Any) -> None:
    """Entry point for main loop sanitation"""
    validated = validate_game_frame(raw_input)
    if validated:
        logging.info(f"Processing frame at {validated['fps']} FPS")
    else:
        logging.warning("Malformed frame packet bypassed sanity check")