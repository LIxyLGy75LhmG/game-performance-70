import random

class GameError(Exception):
    pass

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def update_score(self, points):
        if not isinstance(points, int):
            raise GameError('Points must be an integer')
        if points < 0:
            raise GameError('Points cannot be negative')
        self.score += points

def play_game(player):
    try:
        action = random.choice(['score', 'fail'])
        if action == 'score':
            points = random.randint(1, 100)
            player.update_score(points)
            print(f'{player.name} scored {points} points.')
        else:
            print(f'{player.name} failed this round.')
    except GameError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    player1 = Player('Alice')
    for _ in range(5):
        play_game(player1)
    print(f'{player1.name} final score: {player1.score}')