"""
Kronos V15.0 Production Tape Builder Root Entrypoint
Generates the canonical V15.0 tape across all 652 liquid perpetual shards.

Usage:
    python build_tape.py
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

if __name__ in {"__main__", "__mp_main__"}:
    import runpy
    runner_path = ROOT / "v15_standalone" / "run_v15_0_fresh_build.py"
    runpy.run_path(str(runner_path), run_name="__main__")
