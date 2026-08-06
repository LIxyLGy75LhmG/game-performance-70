from typing import List, Dict, Any

class GameProcessor:
    """
    Class to handle game processing tasks.
    """
    def __init__(self, game_data: List[Dict[str, Any]]) -> None:
        """
        Initializes the GameProcessor with game data.
        
        :param game_data: List of dictionaries containing game information.
        """
        self.game_data = game_data

    def calculate_performance(self) -> Dict[str, float]:
        """
        Calculate the average performance metrics of the games.
        
        :return: Dictionary containing average FPS and memory usage.
        """
        total_fps = 0
        total_memory = 0
        num_games = len(self.game_data)

        for game in self.game_data:
            total_fps += game.get('fps', 0)
            total_memory += game.get('memory_usage', 0)

        return {
            'average_fps': total_fps / num_games if num_games > 0 else 0,
            'average_memory': total_memory / num_games if num_games > 0 else 0,
        }

    def filter_games(self, min_fps: float) -> List[Dict[str, Any]]:
        """
        Filter games based on minimum FPS requirement.
        
        :param min_fps: Minimum FPS threshold to filter games.
        :return: List of games that meet the FPS requirement.
        """
        return [game for game in self.game_data if game.get('fps', 0) >= min_fps]

    def compute_average_frame_time(self) -> float:
        """
        Compute the average frame time from the game data.
        
        :return: Average frame time in milliseconds.
        """
        total_frame_time = 0
        total_frames = 0

        for game in self.game_data:
            total_frame_time += game.get('frame_time', 0) * game.get('frame_count', 0)
            total_frames += game.get('frame_count', 0)

        return total_frame_time / total_frames if total_frames > 0 else 0
