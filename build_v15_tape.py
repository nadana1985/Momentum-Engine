"""
Kronos V15: Root Forwarder for build_v15_tape.py
Delegates deterministically to v15_standalone/build_v15_tape.py to prevent code divergence.
"""
import sys
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
V15_DIR = ROOT / "v15_standalone"
TARGET = V15_DIR / "build_v15_tape.py"

spec = importlib.util.spec_from_file_location("v15_build_v15_tape", TARGET)
_mod = importlib.util.module_from_spec(spec)
sys.modules["v15_build_v15_tape"] = _mod
spec.loader.exec_module(_mod)

main = _mod.main
process_asset = _mod.process_asset
get_runtime_config = _mod.get_runtime_config
RAW_DIR = _mod.RAW_DIR
EXOTIC_DIR = _mod.EXOTIC_DIR
TAPE_DIR = _mod.TAPE_DIR

if __name__ == "__main__":
    main()
