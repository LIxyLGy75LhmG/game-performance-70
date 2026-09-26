import math
from typing import Dict, List, Tuple

class FastEntityGrid:
    """
    Z-Order curve (Morton space filling) spatial partitioner for O(1) proximity lookups.
    Avoids slow Euclidean distance loops for 2D gaming coordinate comparisons.
    """
    __slots__ = ('resolution', 'cell_size', 'grid')

    def __init__(self, cell_size: int = 32, resolution: int = 1024):
        self.cell_size = cell_size
        self.resolution = resolution
        self.grid: Dict[int, List[Tuple[int, float, float]]] = {}

    def _morton_encode(self, x: int, y: int) -> int:
        # Interleave bits of 16-bit coordinates to create a 1D spatial index hash
        x = (x | (x << 8)) & 0x00FF00FF
        x = (x | (x << 4)) & 0x0F0F0F0F
        x = (x | (x << 2)) & 0x33333333
        x = (x | (x << 1)) & 0x55555555

        y = (y | (y << 8)) & 0x00FF00FF
        y = (y | (y << 4)) & 0x0F0F0F0F
        y = (y | (y << 2)) & 0x33333333
        y = (y | (y << 1)) & 0x55555555

        return x | (y << 1)

    def insert(self, entity_id: int, x: float, y: float) -> None:
        gx = max(0, min(int(x // self.cell_size), self.resolution - 1))
        gy = max(0, min(int(y // self.cell_size), self.resolution - 1))
        
        morton_key = self._morton_encode(gx, gy)
        if morton_key not in self.grid:
            self.grid[morton_key] = []
        self.grid[morton_key].append((entity_id, x, y))

    def clear(self) -> None:
        self.grid.clear()

    def get_neighbors(self, x: float, y: float) -> List[Tuple[int, float, float]]:
        gx = max(0, min(int(x // self.cell_size), self.resolution - 1))
        gy = max(0, min(int(y // self.cell_size), self.resolution - 1))
        
        neighbors = []
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                nx, ny = gx + dx, gy + dy
                if 0 <= nx < self.resolution and 0 <= ny < self.resolution:
                    m_key = self._morton_encode(nx, ny)
                    if m_key in self.grid:
                        neighbors.extend(self.grid[m_key])
        return neighbors