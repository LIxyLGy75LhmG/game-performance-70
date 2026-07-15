import numpy as np

class GameProcessor:
    def __init__(self, frame_data):
        self.frame_data = np.array(frame_data)

    def optimize_frame_processing(self):
        dimensions = self.frame_data.shape
        if len(dimensions) == 3:
            return self.process_3d_frames()
        elif len(dimensions) == 2:
            return self.process_2d_frames()
        return None

    def process_3d_frames(self):
        optimized_frames = np.mean(self.frame_data, axis=0)
        return optimized_frames

    def process_2d_frames(self):
        optimized_frames = np.median(self.frame_data, axis=0)
        return optimized_frames

    def enhance_performance(self):
        return self.optimize_frame_processing() * 1.5

# Example usage
if __name__ == '__main__':
    fps = GameProcessor([[1, 2], [3, 4], [5, 6]])
    print(fps.enhance_performance())