# game-performance-70

`game-performance-70` is a high-precision Python utility designed to monitor, log, and analyze frame-time data and hardware utilization for PC games. By providing granular telemetry, it helps developers and power users identify performance bottlenecks and stuttering issues in real-time.

## Features

*   **Real-time Telemetry:** Captures sub-millisecond frame time intervals and GPU/CPU utilization metrics via low-overhead hooks.
*   **Customizable Logging:** Exports performance reports to structured CSV or JSON formats for seamless integration with spreadsheet tools or graphing libraries.
*   **Dynamic Threshold Alerts:** Configure specific frame-time targets (e.g., <16.7ms for 60FPS) and receive immediate console alerts when targets are missed.
*   **Minimal Footprint:** Optimized asynchronous data collection ensures the monitoring tool itself does not induce performance overhead on the target application.

## Installation

Ensure you have Python 3.8+ installed. Install the package directly via pip:

```bash
git clone https://github.com/Developer/game-performance-70.git
cd game-performance-70
pip install -r requirements.txt
```

## Usage

To start monitoring a target process by its PID, run the following command:

```python
from monitor import PerformanceEngine

# Initialize the engine for a target process
engine = PerformanceEngine(pid=1234)

# Start tracking and log results to a file
engine.start_tracking(output="performance_log.csv", duration=60)
```

For a quick summary via CLI:

```bash
python main.py --pid 1234 --duration 30 --report
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.