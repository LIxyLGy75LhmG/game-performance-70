import logging

class InputProcessor:
    def __init__(self):
        self.valid_keys = {'w', 'a', 's', 'd', 'space', 'esc'}
        self.logger = logging.getLogger('game-performance-70')

    def validate_input(self, raw_data):
        if not isinstance(raw_data, dict):
            return False, 'invalid data type'
        if 'key' not in raw_data or raw_data['key'] not in self.valid_keys:
            return False, 'unsupported key input'
        if not isinstance(raw_data.get('timestamp', 0), (int, float)):
            return False, 'invalid timestamp format'
        return True, None

    def run_process_loop(self, event_stream):
        for event in event_stream:
            try:
                is_valid, reason = self.validate_input(event)
                if not is_valid:
                    self.logger.warning(f'packet rejection: {reason}')
                    continue
                
                self._apply_physics_update(event)
            except Exception as e:
                self.logger.error(f'critical loop interrupt: {e}')
                break

    def _apply_physics_update(self, data):
        # Niche game-performance-70 calculation logic
        state = data.get('key')
        performance_mod = hash(str(data['timestamp'])) % 10
        return state, performance_mod