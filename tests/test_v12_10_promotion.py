import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pytest
import pandas as pd
from momentum_v12.config import V12Config, Book5Config, MicrostructureConfig, ExitConfig

def test_v12_10_config_invariants():
    b5 = Book5Config()
    assert b5.discount_pct == 0.08
    assert b5.max_ls == 0.85
    assert b5.min_d_oi_tokens == 0.40
    assert b5.ttl_hours == 72
    
    micro = MicrostructureConfig()
    assert hasattr(micro, "enable_front_running_purge")
    
    exit_cfg = ExitConfig()
    assert hasattr(exit_cfg, "enable_euphoria_climax_harvest")

def test_canonical_v12_10_vault_integrity():
    p_parq = ROOT / "data" / "canonical" / "canonical_v12_10_tape.parquet"
    assert p_parq.exists(), "canonical_v12_10_tape.parquet must exist in vault"
    df = pd.read_parquet(p_parq)
    assert len(df) == 3810, f"Expected exactly 3,810 records, got {len(df)}"
    assert (df['is_open'] == False).all(), "All canonical trades must be closed"
    assert set(df['book'].unique()) == {
        'Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5 (Shelf Absorption Squeeze)'
    }
    
    # Assert Log Profit Factor and Net Log
    w = df[df['log_ret'] > 0]['log_ret'].sum()
    l = abs(df[df['log_ret'] <= 0]['log_ret'].sum())
    log_pf = w / l
    net_log = df['log_ret'].sum() * 100.0
    wr = (df['log_ret'] > 0).mean() * 100.0
    
    assert log_pf >= 2.33, f"Expected Log PF >= 2.33, got {log_pf:.3f}"
    assert net_log >= 13800.0, f"Expected Net Log >= 13,800%, got {net_log:.1f}%"
    assert wr >= 61.0, f"Expected Win Rate >= 61.0%, got {wr:.2f}%"
