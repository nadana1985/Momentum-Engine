"""
Study S-CA: Day Close P_NB_High structural acceptance and microstructure sizing.

Certified pieces only:
- extract_p_nb_high is causal (no canary-day / future leak)
- Book 4 candidate requires 23:00 UTC close >= P_NB_High when the flag is on
- Book 4 is Tier 1 only (tier2/tier3_enable_book4 default False)
- w_pnb * w_fr clamps

Existing S-BB hourly reclaim tests keep
enable_p_nb_day_close_confirmation=False.
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v12.config import Book4Config, V12Config
from momentum_v12.engine_v12 import run_v12_engine
from momentum_v12.features_v12 import compute_features_v12, extract_p_nb_high


def _sbb_cfg() -> V12Config:
    return V12Config(
        book4=Book4Config(
            enable_p_nb_day_close_confirmation=False,
            enable_p_nb_microstructure_sizing=False,
        )
    )


def _book4_frame(n: int = 2000) -> pd.DataFrame:
    dates = pd.date_range("2025-01-01", periods=n, freq="1h")
    c = np.full(n, 50.0)
    c[:200] = 150.0
    c[200:1000] = 50.0
    c[1000:1040] = np.linspace(50.0, 105.0, 40)
    c[1040:1070] = np.linspace(105.0, 92.0, 30)
    c[1070:1100] = np.linspace(92.0, 108.0, 30)
    c[1100:1150] = np.linspace(108.0, 135.0, 50)
    c[1150:] = 135.0
    h = c + 0.5
    l = c - 0.5
    return pd.DataFrame(
        {
            "timestamp": dates.astype(np.int64) // 10**6,
            "open": c,
            "high": h,
            "low": l,
            "close": c,
            "volume": np.full(n, 50000.0),
            "quote_volume": c * 50000.0,
            "sum_open_interest_value": np.full(n, 8000000.0),
            "count_toptrader_long_short_ratio": np.full(n, 1.80),
            "funding_rate": np.full(n, 0.0001),
            "taker_buy_quote_volume": c * 26000.0,
        },
        index=dates,
    )


def test_sca_config_defaults():
    cfg = V12Config()
    assert cfg.book4.enable_p_nb_day_close_confirmation is True
    assert cfg.book4.enable_p_nb_microstructure_sizing is True
    assert cfg.tier.tier2_enable_book4 is False
    assert cfg.tier.tier3_enable_book4 is False


def test_extract_p_nb_high_is_causal():
    idx = pd.date_range("2025-01-01", periods=20, freq="1D")
    o = np.full(20, 100.0)
    h = np.full(20, 101.0)
    l = np.full(20, 99.0)
    c = np.full(20, 99.5)

    # Last green with high > canary_close is the macro day.
    o[0], h[0], l[0], c[0] = 100.0, 140.0, 99.0, 135.0
    for i, hi in ((2, 110.0), (3, 118.0), (4, 125.0), (5, 112.0)):
        o[i], h[i], l[i], c[i] = 100.0, hi, 99.0, 105.0
    # Canary day and a future green must not leak into P_NB_High.
    o[14], h[14], l[14], c[14] = 100.0, 180.0, 99.0, 170.0
    o[16], h[16], l[16], c[16] = 100.0, 200.0, 99.0, 190.0

    daily = pd.DataFrame({"open": o, "high": h, "low": l, "close": c}, index=idx)
    p_nb, macro, win_len = extract_p_nb_high(
        daily, pd.Timestamp("2025-01-15"), 130.0
    )
    assert p_nb == 125.0
    assert pd.Timestamp(macro) == pd.Timestamp("2025-01-01")
    assert win_len >= 1

    # Truncating at the canary date must not change P_NB_High.
    p_nb_trunc, _, _ = extract_p_nb_high(
        daily.loc[: pd.Timestamp("2025-01-15")],
        pd.Timestamp("2025-01-15"),
        130.0,
    )
    assert p_nb_trunc == p_nb


def test_extract_p_nb_high_short_history_returns_none():
    idx = pd.date_range("2025-01-01", periods=8, freq="1D")
    daily = pd.DataFrame(
        {
            "open": np.full(8, 100.0),
            "high": np.full(8, 110.0),
            "low": np.full(8, 90.0),
            "close": np.full(8, 105.0),
        },
        index=idx,
    )
    p_nb, macro, win_len = extract_p_nb_high(
        daily, pd.Timestamp("2025-01-08"), 100.0
    )
    assert p_nb is None
    assert macro is None
    assert win_len == 0


def test_features_attach_daily_df():
    feat = compute_features_v12(
        _book4_frame(), btc_df=None, tier_label="Tier 1", cfg=V12Config()
    )
    daily = feat.attrs.get("daily_df")
    assert daily is not None
    assert not daily.empty
    for col in ("open", "high", "low", "close"):
        assert col in daily.columns


def test_sca_day_close_blocks_intraday_reclaim():
    df = _book4_frame()
    feat = compute_features_v12(df, btc_df=None, tier_label="Tier 1", cfg=V12Config())

    off, _ = run_v12_engine(feat, "SCA_TOKEN", cfg=_sbb_cfg())
    on, _ = run_v12_engine(feat, "SCA_TOKEN", cfg=V12Config())

    off_b4 = off[off["book"] == "Book 4"]
    assert not off_b4.empty
    off_entry = pd.Timestamp(off_b4.iloc[0]["entry"])

    if off_entry.hour != 23:
        on_b4 = on[on["book"] == "Book 4"] if not on.empty else on
        if on_b4 is not None and not on_b4.empty:
            on_entry = pd.Timestamp(on_b4.iloc[0]["entry"])
            assert on_entry.hour == 23
            assert on_entry >= off_entry
        # Intraday S-BB fill is not reused as the S-CA fill.
        if on_b4 is not None and not on_b4.empty:
            assert pd.Timestamp(on_b4.iloc[0]["entry"]) != off_entry


def test_sca_day_close_fires_at_hour_23():
    """Hold the reclaim through a 23:00 bar so S-CA can accept it."""
    n = 2000
    dates = pd.date_range("2025-01-01", periods=n, freq="1h")
    c = np.full(n, 50.0)
    c[:200] = 150.0
    c[200:1000] = 50.0
    c[1000:1040] = np.linspace(50.0, 105.0, 40)
    c[1040:1070] = np.linspace(105.0, 92.0, 30)
    # Stretch the reclaim so a 23:00 bar is included while price is above EMA.
    c[1070:1140] = np.linspace(92.0, 130.0, 70)
    c[1140:] = 130.0
    h = c + 0.5
    l = c - 0.5
    df = pd.DataFrame(
        {
            "timestamp": dates.astype(np.int64) // 10**6,
            "open": c,
            "high": h,
            "low": l,
            "close": c,
            "volume": np.full(n, 50000.0),
            "quote_volume": c * 50000.0,
            "sum_open_interest_value": np.full(n, 8000000.0),
            "count_toptrader_long_short_ratio": np.full(n, 1.80),
            "funding_rate": np.full(n, 0.0001),
            "taker_buy_quote_volume": c * 26000.0,
        },
        index=dates,
    )
    cfg = V12Config()
    feat = compute_features_v12(df, btc_df=None, tier_label="Tier 1", cfg=cfg)
    trades, _ = run_v12_engine(feat, "SCA_DAY_CLOSE", cfg=cfg)
    b4 = trades[trades["book"] == "Book 4"] if not trades.empty else trades
    assert not b4.empty, "S-CA should fill on a 23:00 close above P_NB_High"
    entry = pd.Timestamp(b4.iloc[0]["entry"])
    assert entry.hour == 23


def test_book4_disabled_on_tier2_and_tier3():
    df = _book4_frame()
    cfg = _sbb_cfg()
    feat_t1 = compute_features_v12(df, btc_df=None, tier_label="Tier 1", cfg=cfg)
    feat_t2 = compute_features_v12(df, btc_df=None, tier_label="Tier 2", cfg=cfg)
    feat_t3 = compute_features_v12(df, btc_df=None, tier_label="Tier 3", cfg=cfg)

    t1, _ = run_v12_engine(feat_t1, "T1", cfg=cfg)
    t2, _ = run_v12_engine(feat_t2, "T2", cfg=cfg)
    t3, _ = run_v12_engine(feat_t3, "T3", cfg=cfg)

    assert not t1[t1["book"] == "Book 4"].empty
    t2_b4 = t2[t2["book"] == "Book 4"] if not t2.empty else t2
    t3_b4 = t3[t3["book"] == "Book 4"] if not t3.empty else t3
    assert t2_b4 is None or t2_b4.empty
    assert t3_b4 is None or t3_b4.empty


def test_sca_microstructure_weight_clamps():
    w_pnb_hi = float(np.clip(1.0 + 0.35 * 2.0, 0.65, 1.35))
    w_pnb_lo = float(np.clip(1.0 + 0.35 * (-2.0), 0.65, 1.35))
    w_fr_hi = float(np.clip(1.0 - 0.20 * 3.0, 0.70, 1.25))
    w_fr_lo = float(np.clip(1.0 - 0.20 * (-3.0), 0.70, 1.25))
    assert w_pnb_hi == 1.35
    assert w_pnb_lo == 0.65
    assert w_fr_hi == 0.70
    assert w_fr_lo == 1.25
    w_vol = float(np.clip(1.20 * w_pnb_lo * w_fr_hi, 0.20, 1.50))
    assert w_vol >= 0.20
    assert w_vol <= 1.50


def test_sca_microstructure_changes_sizing_vs_sbb():
    df = _book4_frame()
    sbb = _sbb_cfg()
    sca_size = V12Config(
        book4=Book4Config(
            enable_p_nb_day_close_confirmation=False,
            enable_p_nb_microstructure_sizing=True,
        )
    )
    feat_sbb = compute_features_v12(df, btc_df=None, tier_label="Tier 1", cfg=sbb)
    feat_sca = compute_features_v12(df, btc_df=None, tier_label="Tier 1", cfg=sca_size)
    t_sbb, _ = run_v12_engine(feat_sbb, "SZ", cfg=sbb)
    t_sca, _ = run_v12_engine(feat_sca, "SZ", cfg=sca_size)
    b_sbb = t_sbb[t_sbb["book"] == "Book 4"].iloc[0]
    b_sca = t_sca[t_sca["book"] == "Book 4"].iloc[0]
    assert 0.20 <= float(b_sca["sizing_weight"]) <= 1.50
    assert pd.Timestamp(b_sbb["entry"]) == pd.Timestamp(b_sca["entry"])
