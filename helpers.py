import time
from collections import defaultdict

class SimpleGameEntity:
    def __init__(self, x, y, vx=0.0, vy=0.0):
        self.x = float(x)
        self.y = float(y)
        self.vx = float(vx)
        self.vy = float(vy)
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

def spatial_bucket_cull(entities, cam_x, cam_y, view_radius, dt):
    if not entities:
        return 0
    bucket_size = 200
    buckets = defaultdict(list)
    for entity in entities:
        bx = int(entity.x // bucket_size)
        by = int(entity.y // bucket_size)
        buckets[(bx, by)].append(entity)
    cam_bx = int(cam_x // bucket_size)
    cam_by = int(cam_y // bucket_size)
    bucket_range = int(view_radius // bucket_size) + 2
    count = 0
    for bx in range(cam_bx - bucket_range, cam_bx + bucket_range + 1):
        for by in range(cam_by - bucket_range, cam_by + bucket_range + 1):
            key = (bx, by)
            if key in buckets:
                for entity in buckets[key]:
                    dx = entity.x - cam_x
                    dy = entity.y - cam_y
                    if dx * dx + dy * dy <= view_radius * view_radius:
                        entity.update(dt)
                        count += 1
    return count

def generate_entities(n):
    return [SimpleGameEntity((i % 50) * 20, (i // 50) * 20, 2.0, 1.0) for i in range(n)]

def run_performance_test():
    entities = generate_entities(500)
    start = time.perf_counter()
    for _ in range(100):
        spatial_bucket_cull(entities, 250, 250, 1000, 0.016)
    return time.perf_counter() - start