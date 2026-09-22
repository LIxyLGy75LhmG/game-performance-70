import time
import functools
import random
from typing import Callable, Any

def jitter_retry(retries: int = 3, delay: float = 1.0):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_ex = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_ex = e
                    wait = delay * (2 ** attempt) + random.uniform(0, 0.5)
                    time.sleep(wait)
            raise last_ex
        return wrapper
    return decorator

class NetworkProcessor:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    @jitter_retry(retries=3, delay=0.5)
    def fetch_game_data(self, request_id: int):
        # Simulate unstable network connection for game telemetry
        if random.random() < 0.7:
            raise ConnectionError(f"Latency spike at {self.endpoint}")
        return {"id": request_id, "status": "success", "timestamp": time.time()}

if __name__ == "__main__":
    proc = NetworkProcessor("https://api.game-perf.io")
    try:
        data = proc.fetch_game_data(42)
        print(f"Payload acquired: {data}")
    except ConnectionError:
        print("Operation failed after max retries")