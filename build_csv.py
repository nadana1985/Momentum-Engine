"""
Kronos V15: Root Forwarder for build_csv.py
Delegates deterministically to momentum_v15/build_csv.py to prevent code divergence.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v15.build_csv import main

if __name__ == "__main__":
    main()
