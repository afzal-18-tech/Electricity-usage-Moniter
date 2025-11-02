# Electricity Usage Monitor

A simple project to collect, analyze, and visualize electricity consumption data for a household or small business. This repository contains scripts and examples to ingest readings (CSV or sensor), clean and aggregate data, produce summary statistics, and generate visualizations and reports.

Features
- Import electricity readings from CSV files or live sensors
- Parse, clean and validate time-series consumption data
- Produce summary statistics (hourly, daily, weekly, monthly)
- Visualizations for usage and cost over time (plots, dashboards)
- Configurable cost-per-kWh, timezone, and thresholds for alerts
- Extensible scripts to add sensors, storage backends, or alerting

Quick start

Prerequisites
- Python 3.8+
- pip
- Optional: Jupyter, matplotlib, pandas, numpy,Mysql,Tkinter(GUI)

Install
1. Clone the repo:
   git clone https://github.com/afzal-18-tech/electricity-usage-moniter.git
   cd electricity-usage-moniter

2. (Recommended) Create and activate a virtual environment:
   python -m venv .venv
   source .venv/bin/activate    # macOS / Linux
   .venv\Scripts\activate       # Windows (PowerShell/CMD)

3. Install dependencies (if a requirements file exists):
   pip install -r requirements.txt

Usage
- Scripts: Check the `scripts/` directory for data ingestion and analysis scripts. To run a script:
  python scripts/ingest.py --input data/readings.csv

- If there is an `app.py`:
  python app.py

- Notebooks: Open any notebooks in `notebooks/` with Jupyter to explore analyses interactively.

CSV data format example
Timestamp,Usage_kWh,Voltage,Current
2025-10-01 00:00:00,0.45,230,1.95
2025-10-01 00:15:00,0.50,231,2.10

Configuration
- Add a configuration file (e.g., config.yaml or .env) to store:
  - timezone
  - cost_per_kwh
  - CSV column mappings
  - alert thresholds

Project structure (suggested)
- data/            # sample CSVs and raw data
- scripts/         # ingestion, cleaning, and reporting scripts
- notebooks/       # exploratory analysis
- src/             # reusable modules
- tests/           # unit/integration tests

Contributing
- Contributions are welcome. Please open an issue to discuss major changes first.
- Workflow: fork -> branch -> PR. Add tests for new features where possible.

License
MIT — see LICENSE for details.

Maintainer
@afzal-18-tech

Notes
- I corrected the spelling of "moniter" to "Monitor" in this README. Consider renaming the repository from `electricity-usage-moniter` to `electricity-usage-monitor` for consistency, or keep the README name aligned with the repo name if you prefer the original spelling.
