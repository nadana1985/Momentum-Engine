"""
Kronos V15.0 Production Dashboard Entrypoint
Launches the Cyber Command Center on Port 8080 with full NiceGUI UI,
Plotly multi-pane charts, Quasar data tables, and real-time tactical alerts.

Usage:
    python dashboard.py
    (Accessible at http://localhost:8080)
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

if __name__ in {"__main__", "__mp_main__"}:
    import runpy
    dashboard_path = ROOT / "v15_standalone" / "momentum_v15" / "dashboard_nicegui.py"
    runpy.run_path(str(dashboard_path), run_name="__main__")
