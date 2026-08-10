import random

class GameError(Exception):
    pass

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.level = 1

    def take_damage(self, amount):
        if amount < 0:
            raise GameError('Damage amount must be positive')
        self.health -= amount
        if self.health < 0:
            self.health = 0
        return self.health

    def heal(self, amount):
        if amount < 0:
            raise GameError('Healing amount must be positive')
        self.health += amount
        if self.health > 100:
            self.health = 100
        return self.health

class Game:
    def __init__(self):
        self.players = []

    def add_player(self, name):
        if not name:
            raise GameError('Player name cannot be empty')
        self.players.append(Player(name))

    def deal_damage(self, player_name, damage):
        player = self.find_player(player_name)
        if player:
            return player.take_damage(damage)
        return None

    def find_player(self, name):
        for player in self.players:
            if player.name == name:
                return player
        raise GameError('Player not found')

    def heal_player(self, player_name, heal_amount):
        player = self.find_player(player_name)
        if player:
            return player.heal(heal_amount)
        return None


# Example usage
if __name__ == '__main__':
    game = Game()
    game.add_player('Player1')
    try:
        game.deal_damage('Player1', 20)  # Reduces health
        game.heal_player('Player1', 10)  # Increases health
    except GameError as e:
        print(f'Error: {e}')