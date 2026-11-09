# game-performance-70

`game-performance-70` is a high-precision telemetry and optimization suite designed to analyze hardware overhead during heavy gaming sessions. It provides real-time bottlenecks identification by monitoring CPU utilization, frame time consistency, and memory page faults.

## Features
* **Frame Time Analysis:** Calculates 1% and 0.1% low metrics to detect micro-stuttering that standard FPS counters miss.
* **Hardware Overhead Tracking:** Monitors background process interrupts that conflict with gaming threads using Python’s `psutil` integration.
* **Thermal Throttling Alerts:** Triggers system notifications if GPU/CPU junction temperatures exceed custom safety thresholds.
* **Report Export:** Generates structured `.csv` logs for post-session analysis or visualization in data tools like Grafana.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/game-performance-70.git
cd game-performance-70
pip install -r requirements.txt
```

*Note: Administrative/Sudo privileges are required to access low-level system process metrics.*

## Usage

To start a performance monitor session, run the core script with the PID of your gaming process:

```bash
# Monitor a specific process
python main.py --pid 4520 --interval 1.0 --output session_log.csv
```

You can also run it in global mode to capture aggregate system strain:

```bash
python main.py --global --duration 600
```

This will run the monitor for 10 minutes and automatically save the findings to the local `reports/` directory.

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.