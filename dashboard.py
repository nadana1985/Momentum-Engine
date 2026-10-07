"""
Kronos V12 Dashboard Root Entrypoint
Launches the Cyber Command Center on Port 8056 with full NiceGUI UI,
Plotly multi-pane charts, Quasar data tables, and /coin/{symbol} deep research.

Usage:
    python dashboard.py
    (Accessible at http://localhost:8056)
"""
import os
import sys
from pathlib import Path

# Ensure repo root is on sys.path
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

if __name__ in {"__main__", "__mp_main__"}:
    import runpy
    dashboard_path = ROOT / "momentum_v12" / "dashboard_nicegui.py"
    runpy.run_path(str(dashboard_path), run_name="__main__")
