"""
Core Test 3: Errors Surface Test
As specified in Issues-identified.pdf:
Feeds corrupt data to process_asset and asserts that the run fails loudly
with the coin explicitly named, proving that silent exception swallowing is eliminated.
"""

import sys
from pathlib import Path
import pytest
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import build_v15_tape


def test_corrupt_coin_surfaces_error_with_coin_named(tmp_path, monkeypatch):
    """Verify that process_asset raises RuntimeError naming the coin when data is corrupt."""
    corrupt_asset = "CORRUPT_TOKEN"
    
    # Create a corrupted parquet shard
    raw_dir = tmp_path / "raw_shards"
    raw_dir.mkdir(parents=True)
    corrupt_file = raw_dir / f"{corrupt_asset}_USDT_1h.parquet"
    corrupt_file.write_bytes(b"MALFORMED_NON_PARQUET_GARBAGE_BYTES")

    # Point build_v15_tape RAW_DIR to the corrupt directory
    monkeypatch.setattr(build_v15_tape._mod, "RAW_DIR", raw_dir)
    monkeypatch.setattr(build_v15_tape, "RAW_DIR", raw_dir)

    with pytest.raises(RuntimeError) as exc_info:
        build_v15_tape.process_asset((corrupt_asset, "Tier 1"))

    err_str = str(exc_info.value)
    assert corrupt_asset in err_str, f"Asset name '{corrupt_asset}' must be present in the exception message: {err_str}"
