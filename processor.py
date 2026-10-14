import functools
import gc

class EntityProcessor:
    def __init__(self):
        self._cache = {}
        self.active_pool = set()

    @functools.lru_cache(maxsize=128)
    def _compute_state(self, entity_id: int, transform_hash: int) -> dict:
        return {"id": entity_id, "data": "precomputed_vector_frame"}

    def optimize_garbage_collection(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            gc.disable()
            try:
                return func(*args, **kwargs)
            finally:
                gc.enable()
        return wrapper

    @optimize_garbage_collection
    def process_frame(self, entities: list) -> list:
        processed = []
        for entity in entities:
            e_id = id(entity)
            t_hash = hash(str(entity))
            processed.append(self._compute_state(e_id, t_hash))
        return processed

    def clear_stale_data(self):
        self._compute_state.cache_clear()
        self.active_pool.clear()