import time
from typing import Dict, Any, Generator, Tuple

class MetricBoundary:
    FPS_LIMITS = (1.0, 360.0)
    FRAMETIME_MS_LIMITS = (1.0 / 360.0 * 1000.0, 1000.0)
    GPU_TEMP_LIMITS = (20.0, 105.0)

class FrameDataValidator:
    @staticmethod
    def validate_frame(raw_data: Any) -> Tuple[bool, int]:
        if not isinstance(raw_data, dict):
            return False, 0b10000

        flags = 0
        fps = raw_data.get('fps')
        ft = raw_data.get('frametime_ms')
        temp = raw_data.get('gpu_temp')

        if not isinstance(fps, (int, float)) or not (MetricBoundary.FPS_LIMITS[0] <= fps <= MetricBoundary.FPS_LIMITS[1]):
            flags |= 0b00001
        if not isinstance(ft, (int, float)) or not (MetricBoundary.FRAMETIME_MS_LIMITS[0] <= ft <= MetricBoundary.FRAMETIME_MS_LIMITS[1]):
            flags |= 0b00010
        if not isinstance(temp, (int, float)) or not (MetricBoundary.GPU_TEMP_LIMITS[0] <= temp <= MetricBoundary.GPU_TEMP_LIMITS[1]):
            flags |= 0b00100

        return flags == 0, flags

def frame_telemetry_loop(raw_stream: Generator[Any, None, None]) -> Generator[Dict[str, Any], None, None]:
    validator = FrameDataValidator()
    frame_counter = 0
    
    for raw_payload in raw_stream:
        is_valid, error_mask = validator.validate_frame(raw_payload)
        
        if not is_valid:
            ts = raw_payload.get('timestamp', time.time()) if isinstance(raw_payload, dict) else time.time()
            yield {
                'timestamp': ts,
                'status': 'REJECTED',
                'error_mask': bin(error_mask),
                'dropped': True
            }
            continue

        frame_counter += 1
        yield {
            'frame_id': frame_counter,
            'timestamp': raw_payload.get('timestamp', time.time()),
            'status': 'ACCEPTED',
            'fps': float(raw_payload['fps']),
            'frametime_ms': float(raw_payload['frametime_ms']),
            'gpu_temp': float(raw_payload['gpu_temp'])
        }
