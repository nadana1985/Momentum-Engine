"""
Kronos V12: Root Forwarder for generate_artifacts.py
Delegates deterministically to momentum_v12/generate_artifacts.py to prevent code divergence.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v12.generate_artifacts import generate_tear_tape, generate_open_trades_report

if __name__ == "__main__":
    generate_tear_tape()
    generate_open_trades_report()
