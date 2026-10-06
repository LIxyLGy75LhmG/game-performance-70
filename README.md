# game-performance-70

`game-performance-70` is a Python-based diagnostic toolkit designed to analyze and stabilize frame rates in PC gaming environments. By monitoring hardware utilization in real-time, the tool identifies resource bottlenecks that cause stuttering or input lag.

## Features

*   **Real-time Telemetry:** Tracks CPU/GPU utilization, VRAM usage, and frame-time consistency with high-resolution sampling.
*   **Bottleneck Detection:** Automatically flags thermal throttling, process priority conflicts, or memory leaks impacting active game processes.
*   **Performance Profiles:** Generate and save optimized system configuration reports to replicate stable settings across different game titles.
*   **Low-Overhead Logging:** Operates with minimal background impact, ensuring your gameplay experience remains unaffected by the diagnostic process.

## Installation

Ensure you have Python 3.9+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/game-performance-70.git
cd game-performance-70
pip install -r requirements.txt
```

## Usage

To start a performance capture session, run the main diagnostic script with administrator privileges to ensure access to hardware sensors:

```bash
sudo python main.py --target "GameName.exe" --duration 300
```

This will log data for 300 seconds and output a `performance_report.csv` file in the `/logs` directory. You can visualize the data using the integrated analysis module:

```bash
python analyzer.py --file ./logs/performance_report.csv --plot
```

## Contributing
We welcome pull requests for new hardware driver support and improved analysis algorithms. Please ensure all code passes `flake8` linting before submission.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.