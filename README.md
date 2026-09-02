# game-performance-70

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

game-performance-70 is a Python toolkit that helps game developers profile and optimize their titles for high frame rates. It focuses on identifying inefficiencies in rendering pipelines and update cycles to deliver smooth gameplay experiences.

## Features
- Real-time FPS and frame time tracking with per-system breakdowns
- Automatic detection of slow functions and excessive draw calls
- Memory profiling for textures, audio, and other game assets
- JSON and HTML report generation for post-session analysis

## Installation

```bash
pip install game-performance-70
```

From source:

```bash
git clone https://github.com/Developer/game-performance-70.git
cd game-performance-70
pip install -e .
```

## Basic Usage

```python
from game_performance_70 import Profiler

profiler = Profiler(target_fps=70)
profiler.start()

# Game loop
while running:
    update()
    render()

profiler.stop()
profiler.save_report("performance.json")
```