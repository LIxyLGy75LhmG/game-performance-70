import time
from collections import deque
from typing import Callable, Any, Dict, List


class DynamicFrameOptimizer:
    """Adapts task execution frequency based on frame render time budget."""
    __slots__ = ('target_fps', 'budget_sec', '_history', '_tasks', '_tick_count')

    def __init__(self, target_fps: float = 144.0, window_size: int = 60):
        self.target_fps = target_fps
        self.budget_sec = 1.0 / target_fps
        self._history: deque = deque(maxlen=window_size)
        self._tasks: List[tuple[int, Callable[[], Any]]] = []
        self._tick_count = 0

    def register_task(self, cadence_divider: int, task: Callable[[], Any]) -> None:
        """Register background task with a target frame cadence divisor."""
        self._tasks.append((max(1, cadence_divider), task))

    def measure_frame(self, frame_duration: float) -> None:
        """Track current frame timing and calculate moving delta."""
        self._history.append(frame_duration)

    @property
    def current_load_factor(self) -> float:
        if not self._history:
            return 0.0
        avg_time = sum(self._history) / len(self._history)
        return min(3.0, avg_time / self.budget_sec)

    def step(self) -> List[Any]:
        """Execute registered tasks adapted to current frame budget overhead."""
        self._tick_count += 1
        results = []
        load = self.current_load_factor

        effective_scale = max(1, round(load))
        for base_divider, task in self._tasks:
            adjusted_divider = base_divider * effective_scale
            if self._tick_count % adjusted_divider == 0:
                results.append(task())
        return results


def optimize_event_loop(optimizer: DynamicFrameOptimizer, render_func: Callable[[], None], ticks: int = 100) -> Dict[str, Any]:
    """Runs frame loop demonstrating dynamic frame budget adjustment."""
    executed_tasks = 0
    start_time = time.perf_counter()

    for _ in range(ticks):
        frame_start = time.perf_counter()
        render_func()
        frame_elapsed = time.perf_counter() - frame_start
        
        optimizer.measure_frame(frame_elapsed)
        task_results = optimizer.step()
        executed_tasks += len(task_results)

    total_time = time.perf_counter() - start_time
    return {
        "ticks": ticks,
        "total_time_ms": round(total_time * 1000, 2),
        "executed_subtasks": executed_tasks,
        "final_load_factor": round(optimizer.current_load_factor, 3)
    }
