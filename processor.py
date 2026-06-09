import numpy as np

class GameProcessor:
    def __init__(self, frames_per_second=60):
        self.frames_per_second = frames_per_second
        self.delta_time = 1 / self.frames_per_second
    
    def process_frame(self, input_data):
        processed_data = self._transform_data(input_data)
        self._apply_physics(processed_data)
        return processed_data
    
    def _transform_data(self, data):
        return np.array(data) * 1.5  # Example transformation
    
    def _apply_physics(self, data):
        data += np.random.normal(0, 1, size=data.shape)  # Simulating physics
        return data

    @staticmethod
    def calculate_performance_metrics(start_time, end_time):
        elapsed_time = end_time - start_time
        fps = 1 / elapsed_time if elapsed_time > 0 else 0
        return {'elapsed_time': elapsed_time, 'fps': fps}

# Example usage
if __name__ == '__main__':
    processor = GameProcessor()
    input_data = [1, 2, 3, 4, 5]
    frame_start = time.time()
    processed_frame = processor.process_frame(input_data)
    frame_end = time.time()
    metrics = processor.calculate_performance_metrics(frame_start, frame_end)
    print(f'Processed Frame: {processed_frame}')
    print(f'Metrics: {metrics}')