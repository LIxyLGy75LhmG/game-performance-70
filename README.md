[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# game-performance-70

`game-performance-70` is a lightweight Python telemetry engine designed to monitor low-level system graphics metrics and optimize frame pacing during active gaming sessions. It actively tracks 1% low FPS, GPU thermal throttling events, and system RAM allocation to help maintain a rock-solid 70+ FPS performance profile.

## Features

- **Sub-millisecond Frametime Tracking:** Hooks into low-level graphics APIs to capture frame render times and flag micro-stutters in real time.
- **Dynamic Process Balancer:** Automatically adjusts OS thread priorities for non-essential background tasks whenever a configured game executable launches.
- **Thermal & Power Throttling Detection:** Monitors GPU core clocks and ambient temperatures, logging hardware throttling triggers directly to session data.
- **Automated Analytics Export:** Generates lightweight JSON and CSV reports summarizing average FPS, 0.1% lows, and hardware utilization curves.

## Installation

Ensure you have Python 3.9+ installed on your system.

```bash
git clone https://github.com/Developer/game-performance-70.git
cd game-performance-70
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Quick Start

Run a basic tracking session targeted at a specific game process:

```python
from game_performance_70 import TelemetryEngine, MonitorConfig

# Define session parameters
config = MonitorConfig(
    process_name="Cyberpunk2077.exe",
    target_fps=70,
    sample_rate_ms=250,
    auto_balance_cpu=True
)

# Initialize engine and start logging
engine = TelemetryEngine(config)
engine.start()

# Stop tracking and write session report upon exit
session_summary = engine.stop_and_export(output_dir="./logs")
print(f"Session complete. Average FPS: {session_summary.avg_fps}")
```

To run the live terminal overlay, execute the CLI entry point:

```bash
python -m game_performance_70 --target "eldenring.exe" --overlay
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.