import numpy as np

class GameProcessor:
    def __init__(self, entity_data):
        self.entity_data = np.array(entity_data)

    def optimize_entity_processing(self):
        active_entities_mask = self.entity_data[:, 0] == 1
        optimized_entities = self.entity_data[active_entities_mask]
        return self.process_entities(optimized_entities)

    def process_entities(self, entities):
        results = []
        for entity in entities:
            results.append(self.compute_entity_score(entity))
        return np.array(results)

    def compute_entity_score(self, entity):
        score = (entity[1] * 0.5) + (entity[2] * 0.3) + (entity[3] * 0.2)
        return score

if __name__ == '__main__':
    example_data = [
        [1, 10, 20, 30],
        [0, 15, 25, 35],
        [1, 20, 30, 40],
    ]
    processor = GameProcessor(example_data)
    print(processor.optimize_entity_processing())