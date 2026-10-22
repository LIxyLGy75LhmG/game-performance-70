import sys
import logging
from datetime import datetime

class PerformanceLogger:
    def __init__(self, log_file='game_perf.log'):
        self.log_file = log_file

    def log_event(self, event_name, data):
        try:
            if not isinstance(data, dict):
                raise ValueError('Payload must be a dictionary')
            
            timestamp = datetime.utcnow().isoformat()
            log_entry = f'[{timestamp}] EVENT: {event_name} | DATA: {data}\n'
            
            with open(self.log_file, 'a') as f:
                f.write(log_entry)
        except (IOError, PermissionError) as e:
            self._emergency_fallback(e, event_name)
        except Exception as e:
            sys.stderr.write(f'Catastrophic logger failure: {e}\n')

    def _emergency_fallback(self, error, event_name):
        fallback_file = 'emergency_log.txt'
        try:
            with open(fallback_file, 'a') as f:
                f.write(f'CRITICAL: {event_name} failed due to {error}\n')
        except Exception:
            pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.log_event('CRITICAL_EXCEPTION', {'error': str(exc_val)})