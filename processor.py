import logging
import functools

class GamePerformanceError(Exception):
    pass

def robust_performance_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, ZeroDivisionError) as e:
            logging.error(f'performance anomaly detected: {e}')
            return {'status': 'degraded', 'fps': 0, 'reason': str(e)}
        except Exception as e:
            logging.critical(f'unrecoverable game state: {e}')
            raise GamePerformanceError('hard reset required') from e
    return wrapper

@robust_performance_check
def calculate_frame_delta(render_time, target_ms):
    if render_time < 0:
        raise ValueError('negative time delta encountered')
    return (target_ms - render_time) / render_time

def process_frame_batch(batches):
    results = []
    for batch in batches:
        results.append(calculate_frame_delta(batch.get('time', 0), 16.6))
    return results

if __name__ == '__main__':
    data = [{'time': 8.3}, {'time': 0}, {'time': -5}]
    processed = process_frame_batch(data)
    print(processed)