import logging
from typing import Any, Optional

class PerformanceOptimizer:
    def __init__(self, buffer_size: int = 1024):
        self.buffer = [None] * buffer_size
        self.cursor = 0

    def process_frame_data(self, data: Any) -> Optional[float]:
        try:
            if not isinstance(data, (int, float)):
                raise TypeError(f'Invalid data type: {type(data).__name__}')
            
            if data < 0:
                raise ValueError('Negative frame latency detected')
                
            self.buffer[self.cursor] = data
            self.cursor = (self.cursor + 1) % len(self.buffer)
            
            valid_data = [x for x in self.buffer if x is not None]
            return sum(valid_data) / len(valid_data)
            
        except (TypeError, ValueError) as e:
            logging.error(f'Frame processing anomaly: {e}')
            return None
        except IndexError:
            logging.critical('Buffer overflow in frame processor')
            self.cursor = 0
            return None
        except Exception as e:
            logging.warning(f'Unexpected performance jitter: {e}')
            return 0.0

def run_pipeline(stream: list) -> list:
    proc = PerformanceOptimizer()
    return [proc.process_frame_data(item) for item in stream]

if __name__ == '__main__':
    data_stream = [16.6, 17.2, -1, 'lag', 16.8]
    results = run_pipeline(data_stream)
    print(f'Processed metrics: {results}')