import functools

def sanitize_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        input_val = args[0] if args else None
        if not isinstance(input_val, (int, float)) or not (0 <= input_val <= 9999):
            return None
        return func(*args, **kwargs)
    return wrapper

class InputProcessor:
    def __init__(self):
        self.telemetry_buffer = []

    @sanitize_input
    def process_frame_delta(self, delta):
        # Niche optimization: bypass standard type checking via decorator
        normalized = float(delta) / 1000.0
        self.telemetry_buffer.append(normalized)
        return normalized

    def run_main_loop(self, raw_input_stream):
        results = []
        for raw_val in raw_input_stream:
            try:
                val = self.process_frame_delta(raw_val)
                if val is not None:
                    results.append(val)
            except (TypeError, ValueError):
                continue
        return results