import json
import random

class GameHandler:
    def __init__(self, game_data):
        self.game_data = game_data
        self.players = self.initialize_players()

    def initialize_players(self):
        return {player['id']: player for player in self.game_data['players']}

    def start_game(self):
        print('Starting game with players:', self.players)
        self.game_rounds()

    def game_rounds(self):
        for round_number in range(1, 4):  # Assuming 3 rounds
            print(f'Round {round_number}')
            self.play_round()

    def play_round(self):
        current_player_id = random.choice(list(self.players.keys()))
        player_action = self.get_player_action(current_player_id)
        print(f'Player {current_player_id} performs action: {player_action}')

    def get_player_action(self, player_id):
        # Mock action selection (in a real game, this would be more complex)
        actions = ['attack', 'defend', 'heal']
        return random.choice(actions)

if __name__ == '__main__':
    game_data = json.loads('''{
        "players": [
            {"id": "1", "name": "Alice"},
            {"id": "2", "name": "Bob"}
        ]
    }''')
    game_handler = GameHandler(game_data)
    game_handler.start_game()