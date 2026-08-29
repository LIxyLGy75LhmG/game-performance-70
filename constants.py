from enum import Enum
from typing import Any, Dict, List

class PerformanceLevel(Enum):
    POOR = 1
    FAIR = 2
    GOOD = 3
    EXCELLENT = 4

class GamingConstants:
    FPS_LIMIT = 144
    MIN_ACCEPTABLE_FPS = 30
    MAX_RESOURCE_USAGE = 85
    BASE_SCORE = 50
    MAX_PING = 100
    DATA_FIELDS = ["fps", "cpu_usage", "gpu_usage", "memory_usage", "ping"]
    GAME_MODES = ["single", "multi", "coop"]
    RESOLUTIONS = [(1920, 1080), (2560, 1440), (3840, 2160)]

    @classmethod
    def get_all_constants(cls) -> Dict[str, Any]:
        return {
            "fps_limit": cls.FPS_LIMIT,
            "min_fps": cls.MIN_ACCEPTABLE_FPS,
            "max_resource": cls.MAX_RESOURCE_USAGE,
            "data_fields": cls.DATA_FIELDS,
            "game_modes": cls.GAME_MODES,
            "resolutions": cls.RESOLUTIONS
        }

    @staticmethod
    def calculate_performance_score(data: Dict[str, Any]) -> float:
        fps = float(data.get("fps", 0))
        cpu = float(data.get("cpu_usage", 0))
        gpu = float(data.get("gpu_usage", 0))
        memory = float(data.get("memory_usage", 0))
        ping = float(data.get("ping", GamingConstants.MAX_PING))
        fps_factor = min(1.0, fps / GamingConstants.FPS_LIMIT)
        resource_avg = (cpu + gpu + memory) / 3
        resource_factor = max(0.0, (GamingConstants.MAX_RESOURCE_USAGE - resource_avg) / GamingConstants.MAX_RESOURCE_USAGE)
        ping_factor = max(0.0, (GamingConstants.MAX_PING - ping) / GamingConstants.MAX_PING)
        score = (fps_factor * 50) + (resource_factor * 30) + (ping_factor * 20) + GamingConstants.BASE_SCORE
        return min(100.0, max(0.0, round(score, 1)))

    @staticmethod
    def handle_gaming_data(raw_entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        handled = []
        for entry in raw_entries:
            if not isinstance(entry, dict):
                continue
            score = GamingConstants.calculate_performance_score(entry)
            level_value = min(4, max(1, int(score / 25) + 1))
            level_name = PerformanceLevel(level_value).name
            processed_entry = entry.copy()
            processed_entry.update({
                "performance_score": score,
                "performance_level": level_name,
                "is_high_performance": score >= 70
            })
            numeric_sum = sum(float(v) for v in entry.values() if isinstance(v, (int, float)))
            processed_entry["data_checksum"] = int(numeric_sum) % 1000
            handled.append(processed_entry)
        return handled

    @staticmethod
    def get_high_performance_entries(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        handled = GamingConstants.handle_gaming_data(entries)
        return [e for e in handled if e.get("is_high_performance", False)]

    @staticmethod
    def compute_average_score(entries: List[Dict[str, Any]]) -> float:
        if not entries:
            return 0.0
        handled = GamingConstants.handle_gaming_data(entries)
        scores = [e["performance_score"] for e in handled]
        return round(sum(scores) / len(scores), 1)