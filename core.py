import functools
import time

class EntityCache:
    _storage = {}
    _tick = 0

    @classmethod
    def get_frame_key(cls, entity_id):
        return f"{entity_id}:{cls._tick // 2}"

    @classmethod
    def memoize_state(cls, func):
        @functools.wraps(func)
        def wrapper(entity_id, *args, **kwargs):
            key = cls.get_frame_key(entity_id)
            if key not in cls._storage:
                cls._storage[key] = func(entity_id, *args, **kwargs)
            return cls._storage[key]
        return wrapper

    @classmethod
    def refresh(cls):
        cls._tick += 1
        if cls._tick > 100:
            cls._storage.clear()
            cls._tick = 0

@EntityCache.memoize_state
def calculate_physics_vector(entity_id):
    # Simulate expensive vector math
    time.sleep(0.01)
    return [0.0, 9.8, 0.0]

def process_game_loop(entities):
    results = []
    for e in entities:
        results.append(calculate_physics_vector(e))
    EntityCache.refresh()
    return results

if __name__ == '__main__':
    ids = [1, 2, 3, 4, 5]
    # Fast call on second loop
    print(process_game_loop(ids))
    print(process_game_loop(ids))