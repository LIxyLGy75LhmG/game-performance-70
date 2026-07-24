import time
import random

class Game:
    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def run(self):
        start_time = time.perf_counter()
        self.update_entities()
        self.render_entities()
        end_time = time.perf_counter()
        print(f'Frame processed in {end_time - start_time:.4f} seconds')

    def update_entities(self):
        for entity in self.entities:
            entity.update()

    def render_entities(self):
        for entity in self.entities:
            entity.render()

class Entity:
    def __init__(self, id):
        self.id = id

    def update(self):
        # Simulated computation
        time.sleep(random.uniform(0, 0.1))

    def render(self):
        # Simulate rendering delay
        print(f'Rendering entity {self.id}')

if __name__ == '__main__':
    game = Game()
    for i in range(10):
        game.add_entity(Entity(i))
    while True:
        game.run()