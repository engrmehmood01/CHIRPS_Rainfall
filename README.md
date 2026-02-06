
# Punjab CHIRPS Rainfall GIF (Google Earth Engine, Python)

Generate a monthly rainfall animation (GIF) for Punjab, Pakistan using
CHIRPS Daily precipitation data from Google Earth Engine.

## Features
- Monthly rainfall totals (mm)
- Configurable via `config.yaml`
- Optional GIF labeling
- Supports exporting only selected months (e.g., July–August 2025)

## Quick Start
```bash
pip install -r requirements.txt
python scripts/01_make_monthly_gif.py
python scripts/02_label_gif.py
```
