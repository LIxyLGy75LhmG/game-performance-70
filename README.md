# game-performance-70

`game-performance-70` is a lightweight Python toolkit designed to monitor and optimize system resource allocation for high-demand gaming sessions. It provides real-time metrics and automated process prioritization to reduce frame drops and input latency.

## Features

*   **Priority Orchestration:** Automatically elevates the CPU priority of active game processes while throttling background services to prevent stuttering.
*   **Thermal Monitoring:** Tracks GPU and CPU junction temperatures in real-time to alert users before thermal throttling triggers frame rate degradation.
*   **Resource Profiling:** Generates detailed CSV logs of RAM utilization and VRAM saturation to help identify memory-hungry background applications.
*   **Instant Optimization:** A single-command toggle that clears standby cache and suspends non-essential Windows tasks during gameplay.

## Installation

Ensure you have Python 3.8+ installed. It is recommended to use a virtual environment for better dependency management.

```bash
# Clone the repository
git clone https://github.com/Developer/game-performance-70.git
cd game-performance-70

# Install required dependencies
pip install -r requirements.txt
```

## Usage

To monitor system performance and enable auto-optimization for your active process, run the main module with administrative privileges:

```bash
# Run with elevated permissions to allow process management
sudo python main.py --optimize --monitor
```

Once running, the application will detect the active fullscreen process and begin resource allocation. Press `Ctrl+C` to stop the service and restore standard system priority.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.