import time
import functools

class PerformanceTracker:
    def __init__(self):
        self.execution_times = []

    def record_time(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.execution_times.append(end_time - start_time)
            print(f"{func.__name__} executed in {end_time - start_time:.6f} seconds")
            return result
        return wrapper

    def get_average_time(self):
        return sum(self.execution_times) / len(self.execution_times) if self.execution_times else 0

performance_tracker = PerformanceTracker()

@performance_tracker.record_time
def heavy_computation(x):
    result = 0
    for i in range(x):
        result += i ** 2
    return result

@performance_tracker.record_time
def another_heavy_task(x):
    time.sleep(x)  # Simulating long computation
    return x * 2

if __name__ == "__main__":
    heavy_computation(10000)
    another_heavy_task(2)
    print(f"Average execution time: {performance_tracker.get_average_time():.6f} seconds")