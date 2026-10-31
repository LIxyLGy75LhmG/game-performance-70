from typing import Any, Dict

class InputSanitizer:
    def __init__(self, schema: Dict[str, type]):
        self.schema = schema

    def validate(self, payload: Any) -> bool:
        if not isinstance(payload, dict):
            return False
        return all(k in payload and isinstance(payload[k], t) for k, t in self.schema.items())

def process_frame(input_data: Any):
    sanitizer = InputSanitizer({"x": int, "y": int, "action": str})
    if not sanitizer.validate(input_data):
        raise ValueError("malformed input stream detected")
    return f"processing {input_data['action']} at {input_data['x']},{input_data['y']}"

if __name__ == "__main__":
    game_loop = [{"x": 10, "y": 20, "action": "jump"}, "invalid", {"x": 0, "y": 0, "action": "idle"}]
    for frame in game_loop:
        try:
            print(process_frame(frame))
        except ValueError:
            print("skipped corrupted packet")