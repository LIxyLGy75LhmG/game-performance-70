import numpy as np

class GameProcessor:
    def __init__(self, initial_state):
        self.state = np.array(initial_state)

    def apply_action(self, action):
        if action == 'move_left':
            self.state[0] -= 1
        elif action == 'move_right':
            self.state[0] += 1
        elif action == 'jump':
            self.state[1] += 1
        elif action == 'duck':
            self.state[1] -= 1

    def get_current_state(self):
        return self.state.tolist()

    def reset(self, new_state=None):
        if new_state is None:
            self.state = np.array([0, 0])  # Reset to origin
        else:
            self.state = np.array(new_state)

    def is_game_over(self):
        return self.state[1] < 0  # Example condition for game over

    def score_multiplier(self, score):
        if self.state[0] > 10:
            return score * 2
        return score

