import enum
import os

class PerformanceThreshold(enum.IntEnum):
    FPS_TARGET_60 = 60
    FPS_TARGET_144 = 144
    LATENCY_MAX_MS = 16
    MEMORY_LIMIT_MB = 2048

class ResourcePaths:
    ASSET_ROOT = os.getenv('GAME_ASSET_PATH', './assets')
    SHADER_CACHE = os.path.join(ASSET_ROOT, 'shaders/cache')
    TEXTURE_STREAM = os.path.join(ASSET_ROOT, 'textures/stream')

class OptimizationFlags:
    ENABLE_GPU_CULLING = True
    COMPRESS_TEXTURES = True
    DYNAMIC_LOD_SCALING = True
    THREAD_PRIORITY_BOOST = False

class GraphicsPreset(enum.Enum):
    LOW = {'draw_dist': 500, 'shadow_res': 512}
    MED = {'draw_dist': 1000, 'shadow_res': 1024}
    ULTRA = {'draw_dist': 2500, 'shadow_res': 4096}

VERSION_INFO = {
    'major': 0,
    'minor': 7,
    'patch': 0,
    'codename': 'speedy-polygon'
}

def get_preset_config(level: str) -> dict:
    try:
        return GraphicsPreset[level.upper()].value
    except KeyError:
        return GraphicsPreset.MED.value