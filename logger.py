import sys
import time
import inspect
from datetime import datetime

class GameLogger:
    COLORS = {'DEBUG': '\033[94m', 'INFO': '\033[92m', 'WARN': '\033[93m', 'ERROR': '\033[91m', 'END': '\033[0m'}

    @staticmethod
    def _log(level, message):
        frame = inspect.stack()[2]
        caller = f"{frame.filename.split('/')[-1]}:{frame.lineno}"
        timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
        color = GameLogger.COLORS.get(level, '')
        output = f"{timestamp} [{level:^5}] {caller} | {message}"
        sys.stdout.write(f"{color}{output}{GameLogger.COLORS['END']}\n")

    @classmethod
    def debug(cls, msg): cls._log('DEBUG', msg)
    @classmethod
    def info(cls, msg): cls._log('INFO', msg)
    @classmethod
    def warn(cls, msg): cls._log('WARN', msg)
    @classmethod
    def error(cls, msg): cls._log('ERROR', msg)

def performance_monitor(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        GameLogger.info(f"call '{func.__name__}' took {elapsed:.2f}ms")
        return result
    return wrapper