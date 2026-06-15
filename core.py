import numpy as np

def optimize_game_performance(data):
    unique_data = np.unique(data)
    filtered_data = [d for d in unique_data if d > 0]
    return filtered_data

class Game:
    def __init__(self, player_data):
        self.player_data = player_data
        self.optimized_data = self.optimize_data()
    
    def optimize_data(self):
        return optimize_game_performance(self.player_data)
    
    def play(self):
        print("Game started with optimized data:")
        print(self.optimized_data)

if __name__ == '__main__':
    player_scores = [10, 20, 20, 0, -5, 30, 10]  
    game = Game(player_scores)
    game.play()