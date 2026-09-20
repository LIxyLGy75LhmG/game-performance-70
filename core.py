import logging
import functools

class GamePerformanceError(Exception):
    pass

def fault_tolerant_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (MemoryError, AttributeError, ZeroDivisionError) as e:
            logging.error(f'Performance bottleneck in {func.__name__}: {e}')
            return None
        except Exception as e:
            logging.critical(f'Unexpected engine crash: {e}')
            raise GamePerformanceError('Core system failure') from e
    return wrapper

class FrameProcessor:
    def __init__(self):
        self.frame_buffer = []

    @fault_tolerant_execution
    def calculate_delta(self, frame_data):
        if not frame_data:
            raise ValueError('Empty frame data')
        return 1.0 / len(frame_data)

    @fault_tolerant_execution
    def stream_frame(self, data):
        self.frame_buffer.append(data)
        return True

    def clear(self):
        self.frame_buffer.clear()

if __name__ == '__main__':
    proc = FrameProcessor()
    proc.calculate_delta([])
    proc.stream_frame({'id': 1})