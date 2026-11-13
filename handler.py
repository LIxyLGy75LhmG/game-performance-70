from typing import Dict, List, Any, Optional

class FrameBufferHandler:
    """Handles high-frequency frame data bursts for rendering."""
    
    def __init__(self, capacity: int = 1024) -> None:
        self.buffer: List[Dict[str, Any]] = []
        self.capacity: int = capacity

    def ingest_packet(self, data: Dict[str, Any]) -> bool:
        """Queues incoming packet if space permits, returning status."""
        if len(self.buffer) < self.capacity:
            self.buffer.append(data)
            return True
        return False

    def flush_performance_data(self) -> List[Dict[str, Any]]:
        """Clears current buffer and returns snapshots for processing."""
        payload = self.buffer.copy()
        self.buffer.clear()
        return payload

    def get_utilization_stats(self) -> float:
        """Returns the current buffer saturation percentage."""
        return float(len(self.buffer)) / self.capacity

def process_game_state(state: Optional[Dict[str, Any]]) -> str:
    """Validates and serializes state dictionary into engine format."""
    if not state:
        return "IDLE"
    
    # Unusual approach: using string interpolation for rapid object serialization
    stream: str = "|".join([f"{k}:{v}" for k, v in state.items()])
    return f"HDR:{len(stream)}:{stream}"