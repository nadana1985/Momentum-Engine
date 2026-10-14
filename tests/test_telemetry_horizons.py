"""
Unit tests for Kronos V12.4 Counterfactual Telemetry In-Flight Horizon Handling.
Verifies that:
1. Records with < 72 forward bars are flagged as in-flight (is_complete_72h = False).
2. Dodged bullet flag cannot be prematurely asserted on in-flight vetoes.
3. Veto alpha summary segregates completed vs in-flight vetoes.
"""

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pytest
import numpy as np
import pandas as pd
from momentum_v12.telemetry_v12 import TelemetryCollector, TelemetryRecord


def test_telemetry_incomplete_horizon_flags():
    """Verify that a recent veto with only 6 forward bars is flagged as in-flight."""
    dates = pd.date_range('2026-10-09 00:00:00', periods=14, freq='h')
    shard_df = pd.DataFrame({
        'open': [0.078] * 14,
        'high': [0.079] * 7 + [0.08062] + [0.079] * 6,
        'low': [0.077] * 7 + [0.07361] + [0.077] * 6,
        'close': [0.07835] * 7 + [0.07824] * 7,
        'volume': [1000.0] * 14,
    }, index=dates)

    # Veto at Bar 7 (2026-10-09 07:00:00) -> 6 subsequent bars available (Bars 8 to 13)
    rec = TelemetryRecord(
        timestamp=pd.Timestamp('2026-10-09 07:00:00'),
        asset='MAGIC',
        tier='Tier 3',
        status='VETOED',
        veto_gate='Core 4: Whale Firewall',
        candidate_setup='Continuation Breakout',
        price=0.07835,
        turnover=3.85,
        ls_ratio=1.53,
        funding_rate=0.00005,
        btc_macro_bull=True
    )

    collector = TelemetryCollector()
    collector.log_signal(rec)
    df_tel = collector.to_dataframe()

    enriched = TelemetryCollector.enrich_forward_returns(df_tel, shard_df)

    assert len(enriched) == 1
    row = enriched.iloc[0]

    # Verify horizon tracking
    assert row['fwd_hours_elapsed'] == 6
    assert bool(row['is_complete_72h']) is False
    assert bool(row['is_complete_24h']) is False
    assert bool(row['is_in_flight']) is True

    # Crucial: Must NOT prematurely assert Dodged Bullet on in-flight incomplete horizon!
    assert bool(row['is_dodged_bullet']) is False

    # Summary segregation test
    summary = TelemetryCollector.compute_veto_alpha_summary(enriched)
    assert summary['total_vetoes'] == 1
    assert summary['completed_vetoes'] == 0
    assert summary['in_flight_vetoes'] == 1
    assert summary['dodged_bullets'] == 0


def test_telemetry_complete_horizon():
    """Verify that a veto with >= 72 forward bars is properly marked complete."""
    dates = pd.date_range('2026-01-01 00:00:00', periods=100, freq='h')
    shard_df = pd.DataFrame({
        'open': [10.0] * 100,
        'high': [10.5] * 100,
        'low': [8.0] * 100,
        'close': [9.0] * 100,
        'volume': [1000.0] * 100,
    }, index=dates)

    rec = TelemetryRecord(
        timestamp=pd.Timestamp('2026-01-01 05:00:00'),
        asset='TEST',
        tier='Tier 1',
        status='VETOED',
        veto_gate='Core 1: Macro Bear Veto',
        candidate_setup='Continuation Breakout',
        price=10.0,
        turnover=2.0,
        ls_ratio=1.0,
        funding_rate=0.0001,
        btc_macro_bull=True
    )

    collector = TelemetryCollector()
    collector.log_signal(rec)
    df_tel = collector.to_dataframe()

    enriched = TelemetryCollector.enrich_forward_returns(df_tel, shard_df)
    row = enriched.iloc[0]

    assert row['fwd_hours_elapsed'] >= 72
    assert bool(row['is_complete_72h']) is True
    assert bool(row['is_complete_24h']) is True
    assert bool(row['is_in_flight']) is False
    assert bool(row['is_dodged_bullet']) is True  # Price dropped from 10 to 9 (-10%)
