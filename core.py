import time
import random
import functools
import logging

logger = logging.getLogger("game_net")

def adaptive_retry(max_retries=4, base_delay=0.1, max_delay=2.0, backoff_factor=2.0):
    """Decorator applying dynamic jittered backoff for game network calls."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay = base_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    if attempt == max_retries:
                        logger.error(f"Network call {func.__name__} failed after {max_retries} attempts: {err}")
                        raise
                    jitter = random.uniform(0.8, 1.2)
                    sleep_time = min(max_delay, delay * jitter)
                    logger.warning(f"Attempt {attempt} failed ({err}). Retrying in {sleep_time:.3f}s...")
                    time.sleep(sleep_time)
                    delay *= backoff_factor
        return wrapper
    return decorator

class GameNetworkClient:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        self.connection_drops = 0

    @adaptive_retry(max_retries=3, base_delay=0.05, max_delay=0.5)
    def sync_telemetry(self, state_payload: dict) -> bool:
        """Simulates sending game state frame over unstable network."""
        if random.random() < 0.6:
            self.connection_drops += 1
            raise ConnectionError(f"Packet drop on {self.endpoint}")
        return True
