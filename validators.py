import functools

def validate_game_input(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        payload = kwargs.get('data') or (args[0] if args else None)
        if not isinstance(payload, dict) or 'input_code' not in payload:
            return {'status': 'error', 'message': 'malformed telemetry packet'}
        if not (0 <= payload.get('latency', 0) < 5000):
            return {'status': 'error', 'message': 'latency outlier detected'}
        return func(*args, **kwargs)
    return wrapper

class TelemetryProcessor:
    def __init__(self):
        self.buffer = []

    @validate_game_input
    def ingest(self, data):
        self.buffer.append(data)
        return {'status': 'success', 'data_points': len(self.buffer)}

def run_main_loop(processor, stream):
    for raw_packet in stream:
        response = processor.ingest(data=raw_packet)
        if response.get('status') == 'error':
            print(f"[CORE] Rejected packet: {response.get('message')}")
        else:
            print(f"[CORE] Accepted. Current buffer: {response.get('data_points')}")