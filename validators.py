from typing import Any, Dict, Optional

MAX_LATENCY_MS = 500
INPUT_FIELDS = {'tick_rate', 'frame_delta', 'input_buffer'}

class ValidationError(Exception):
    pass

def validate_game_payload(payload: Dict[str, Any]) -> bool:
    """Validate performance telemetry packets."""
    if not isinstance(payload, dict):
        raise ValidationError('payload must be a dictionary')
    
    if not INPUT_FIELDS.issubset(payload.keys()):
        missing = INPUT_FIELDS - payload.keys()
        raise ValidationError(f'missing telemetry fields: {missing}')

    if payload['tick_rate'] < 0 or payload['tick_rate'] > 1000:
        raise ValidationError('invalid tick rate frequency')

    if payload['frame_delta'] > MAX_LATENCY_MS:
        return False

    return True

def sanitize_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """Force numeric types for processing safety."""
    return {
        'tick_rate': float(data.get('tick_rate', 60)),
        'frame_delta': abs(float(data.get('frame_delta', 0))),
        'input_buffer': str(data.get('input_buffer', ''))[:256]
    }