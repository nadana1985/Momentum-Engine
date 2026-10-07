"""
Kronos V12: Multi-Worker Runner Forwarder (momentum_v12/build_v12_tape.py)
Delegates deterministically to v12_standalone/build_v12_tape.py to ensure zero code divergence.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import build_v12_tape

process_asset = build_v12_tape.process_asset
get_runtime_config = build_v12_tape.get_runtime_config
main = build_v12_tape.main
CFG = build_v12_tape.CFG
TAPE_DIR = build_v12_tape.TAPE_DIR
TELEMETRY_DIR = build_v12_tape.TELEMETRY_DIR

if __name__ == "__main__":
    build_v12_tape.main()
