import random
import logging

class GameError(Exception):
    pass

def load_resources(resource_files):
    resources = {}
    for file in resource_files:
        try:
            if not file.endswith('.png') and not file.endswith('.mp3'):
                raise GameError(f'Invalid resource type for {file}')
            resources[file] = open(file, 'rb').read()
        except FileNotFoundError:
            logging.error(f'Resource file not found: {file}')
        except GameError as ge:
            logging.error(str(ge))
        except Exception as e:
            logging.exception('Unexpected error while loading resources')
    return resources

# Function that randomly simulates player actions

def simulate_player_action(player_id, action):
    if action not in ['jump', 'run', 'shoot']:
        logging.warning(f'Unknown action: {action} by player {player_id}')
        return 'no action taken'
    try:
        outcome = random.choice(['success', 'fail'])
        if outcome == 'fail':
            raise GameError(f'Action {action} failed for player {player_id}')
        return f'Player {player_id} performed {action}'
    except GameError as ge:
        logging.error(str(ge))
        return 'failure'
    except Exception as e:
        logging.exception('Unexpected error during action simulation')
        return 'error'