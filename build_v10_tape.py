import os
# --- Thread-count firewall: must be set BEFORE numpy/pandas are imported ---
# Without this, each ProcessPoolExecutor worker spawns its own OpenBLAS pool.
# On a 16-core machine: 16 workers × 16 threads = 256 threads → deadlock / thrash.
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("SCIPY_OPENBLAS64_NUM_THREADS", "1")   # bundled scipy-openblas64 (NumPy 2.1.1+)
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")


import pandas as pd

from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing

from momentum_v10.config import FeatureConfig, CtaConfig
from momentum_v10.universe_generator import load_with_oi
from momentum_v10.cta_dual import compute_features, run_cta

def process_asset(file_path):
    asset = file_path.stem.split("_")[0]
    if asset == "USDC": return None
    try:
        df10 = load_with_oi(asset, file_path.parent)
        feat10 = compute_features(df10, FeatureConfig(), asset=asset)
        return run_cta(feat10, CtaConfig(), asset=asset)
    except Exception as e:
        print(f"Error on {asset}: {e}")
        return None

def main():
    shards_dir = Path("data/raw_shards")
    files = list(shards_dir.glob("*_USDT_1h.parquet"))
    
    v10_all = []
    workers = min(16, multiprocessing.cpu_count())
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(process_asset, f): f for f in files}
        for future in as_completed(futures):
            res = future.result()
            if res is not None and not res.empty: v10_all.append(res)
                
    if not v10_all: return
    df = pd.concat(v10_all, ignore_index=True)
    
    out_dir = Path("data/all_tapes/v10_production")
    out_dir.mkdir(parents=True, exist_ok=True)
    # Research replay only. Never replace the live closed ledger.
    df.to_csv(out_dir / "master_raw_tape.csv", index=False)
    
if __name__ == "__main__": main()