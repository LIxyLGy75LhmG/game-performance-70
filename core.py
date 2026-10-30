from typing import Any, Dict, Generator, NamedTuple, Optional


class RenderMetrics(NamedTuple):
    frame_id: int
    frametime_ms: float
    draw_calls: int


class PerformanceCore:
    VALIDATORS = {
        "frame_id": lambda x: isinstance(x, int) and x >= 0,
        "frametime_ms": lambda x: isinstance(x, (int, float)) and 0.1 <= x <= 1000.0,
        "draw_calls": lambda x: isinstance(x, int) and 0 <= x <= 1_000_000,
    }

    def __init__(self) -> None:
        self.telemetry_log: list[RenderMetrics] = []
        self.anomaly_count: int = 0

    def validate_payload(self, payload: Dict[str, Any]) -> Optional[RenderMetrics]:
        """Validate frame payload using functional predicate map."""
        if not isinstance(payload, dict):
            return None
        if not all(rule(payload.get(field)) for field, rule in self.VALIDATORS.items()):
            return None
        return RenderMetrics(
            frame_id=payload["frame_id"],
            frametime_ms=float(payload["frametime_ms"]),
            draw_calls=payload["draw_calls"],
        )

    def process_stream(self, stream: Generator[Dict[str, Any], None, None]) -> None:
        """Main processing loop with inline payload assertion filter."""
        for raw_frame in stream:
            if (metrics := self.validate_payload(raw_frame)) is not None:
                self.telemetry_log.append(metrics)
            else:
                self.anomaly_count += 1
