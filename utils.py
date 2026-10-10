import time
import functools
import random

def retry_network_ops(retries=3, backoff=0.5):
    """decorator for exponential backoff network resilience"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempt += 1
                    if attempt == retries:
                        raise e
                    sleep_time = (backoff * (2 ** (attempt - 1))) + (random.random() * 0.1)
                    time.sleep(sleep_time)
            return None
        return wrapper
    return decorator

class NetworkCircuitBreaker:
    """stateful gatekeeper for failing network calls"""
    def __init__(self, threshold=5):
        self.failures = 0
        self.threshold = threshold
        self.is_open = False

    def execute(self, func, *args, **kwargs):
        if self.is_open:
            raise RuntimeError("circuit breaker is open, blocking calls")
        try:
            result = func(*args, **kwargs)
            self.failures = 0
            return result
        except Exception as e:
            self.failures += 1
            if self.failures >= self.threshold:
                self.is_open = True
            raise e