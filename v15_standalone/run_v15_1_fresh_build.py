import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["SCIPY_OPENBLAS64_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["KRONOS_PROFILE"] = "fresh"
os.environ["KRONOS_TAPE_DIR"] = "data/all_tapes/v15_1_production"

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import build_v15_tape

if __name__ == "__main__":
    build_v15_tape.main()
