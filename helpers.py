from typing import Any, Dict, Optional

class InputSanitizer:
    def __init__(self, bounds: Dict[str, tuple]):
        self.bounds = bounds

    def validate(self, packet: Dict[str, Any]) -> bool:
        try:
            for key, (min_val, max_val) in self.bounds.items():
                val = packet.get(key)
                if not isinstance(val, (int, float)) or not (min_val <= val <= max_val):
                    return False
            return True
        except Exception:
            return False

def process_game_input(raw_data: Any, validator: InputSanitizer) -> Optional[Dict]:
    if not isinstance(raw_data, dict):
        return None
    
    if not validator.validate(raw_data):
        return None
        
    # Squashing high-frequency inputs into normalized coordinate space
    return {
        "x": round(raw_data.get("x", 0), 2),
        "y": round(raw_data.get("y", 0), 2),
        "meta": "validated"
    }

# Execution loop context
if __name__ == "__main__":
    bounds = {"x": (-1000, 1000), "y": (-1000, 1000)}
    sanitizer = InputSanitizer(bounds)
    mock_stream = [{"x": 50, "y": 20}, "corrupt", {"x": 9999, "y": 0}]
    
    results = [process_game_input(d, sanitizer) for d in mock_stream]
    print([r for r in results if r])