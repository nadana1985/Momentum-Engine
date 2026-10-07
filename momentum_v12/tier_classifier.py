"""
Kronos V12: Core 2 - Dynamic Point-in-Time Tier Classifier
Segments 725-shard universe into Tier 1 (Macro Crypto) and Tier 2 (Mid-Cap Crypto),
excluding synthetic tokenized equities, stablecoins, and micro-cap dead books.
"""

from pathlib import Path
from typing import Dict, List, Optional, Tuple
import pandas as pd
from momentum_v12.config import TierConfig

_CACHED_TIER_DF: Optional[pd.DataFrame] = None


def find_asset_tiers_path() -> Path:
    """Locates asset_tiers.parquet with fallbacks."""
    candidates = [
        Path(__file__).resolve().parent.parent / "data" / "asset_tiers.parquet",
        Path(__file__).resolve().parent.parent.parent / "scratch" / "asset_tiers.parquet",
        Path("data/asset_tiers.parquet"),
        Path("scratch/asset_tiers.parquet"),
    ]
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError("asset_tiers.parquet not found in expected locations.")


def load_tier_table(path: Optional[Path] = None) -> pd.DataFrame:
    """Loads and filters the universe tier DataFrame."""
    global _CACHED_TIER_DF
    if _CACHED_TIER_DF is not None:
        return _CACHED_TIER_DF

    p = path or find_asset_tiers_path()
    df = pd.read_parquet(p)
    _CACHED_TIER_DF = df
    return df


def get_universe_tiers(
    tier_cfg: TierConfig = TierConfig(),
    tier_df: Optional[pd.DataFrame] = None,
    return_tier3: bool = False
) -> Tuple:
    """
    Classifies universe into Tier 1, Tier 2, and metadata dictionary.
    Excludes tokenized equities and illiquid books.
    """
    df = tier_df if tier_df is not None else load_tier_table()
    excluded = set(tier_cfg.excluded_symbols)

    crypto_df = df[~df['asset'].isin(excluded)].copy()

    # Tier 1: Macro Crypto ($15M+ OI, $15M+ Vol, 0.35+ BTC Corr, 180d+ History)
    t1_mask = (
        (crypto_df['med_oi_30d_m'] >= (tier_cfg.tier1_min_oi_usd / 1e6)) &
        (crypto_df['med_vol_30d_m'] >= (tier_cfg.tier1_min_vol_usd / 1e6)) &
        (crypto_df['corr_btc'] >= tier_cfg.tier1_min_corr_btc) &
        (crypto_df['hist_days'] >= tier_cfg.tier1_min_hist_days)
    )
    t1_assets = crypto_df[t1_mask]['asset'].tolist()

    # Tier 2: Mid-Cap Crypto ($2.5M+ OI, $2.5M+ Vol, 0.25+ BTC Corr, 90d+ History)
    t2_mask = (
        ~crypto_df['asset'].isin(t1_assets) &
        (crypto_df['med_oi_30d_m'] >= (tier_cfg.tier2_min_oi_usd / 1e6)) &
        (crypto_df['med_vol_30d_m'] >= (tier_cfg.tier2_min_vol_usd / 1e6)) &
        (crypto_df['corr_btc'] >= tier_cfg.tier2_min_corr_btc) &
        (crypto_df['hist_days'] >= tier_cfg.tier2_min_hist_days)
    )
    t2_assets = crypto_df[t2_mask]['asset'].tolist()

    # Tier 3: Micro-Cap Crypto ($250k+ OI floor)
    t3_mask = (
        ~crypto_df['asset'].isin(t1_assets) &
        ~crypto_df['asset'].isin(t2_assets) &
        (crypto_df['med_oi_30d_m'] >= (tier_cfg.tier3_min_oi_usd / 1e6))
    )
    t3_assets = crypto_df[t3_mask]['asset'].tolist()

    meta_dict: Dict[str, dict] = {}
    for _, row in crypto_df.iterrows():
        a = str(row['asset'])
        t = "Tier 1" if a in t1_assets else ("Tier 2" if a in t2_assets else ("Tier 3" if a in t3_assets else "Excluded"))
        meta_dict[a] = {
            'tier': t,
            'med_oi_30d_m': float(row.get('med_oi_30d_m', 0.0)),
            'med_vol_30d_m': float(row.get('med_vol_30d_m', 0.0)),
            'corr_btc': float(row.get('corr_btc', 0.0)),
            'hist_days': float(row.get('hist_days', 0.0)),
            'last_price': float(row.get('last_price', 0.0)),
        }

    if return_tier3:
        return t1_assets, t2_assets, t3_assets, meta_dict
    return t1_assets, t2_assets, meta_dict


def get_all_universe_tiers(
    tier_cfg: TierConfig = TierConfig(),
    tier_df: Optional[pd.DataFrame] = None
) -> Tuple[List[str], List[str], List[str], Dict[str, dict]]:
    """Convenience function returning (Tier 1, Tier 2, Tier 3, metadata)."""
    return get_universe_tiers(tier_cfg, tier_df, return_tier3=True)


def get_asset_tier(
    asset: str,
    tier_cfg: TierConfig = TierConfig(),
    tier_df: Optional[pd.DataFrame] = None
) -> str:
    """Returns 'Tier 1', 'Tier 2', 'Tier 3', or 'Excluded' for a single asset."""
    t1, t2, t3, _ = get_universe_tiers(tier_cfg, tier_df, return_tier3=True)
    clean = asset.upper().replace("1000", "").replace("USDT", "")
    if asset in t1 or clean in t1 or f"1000{clean}" in t1:
        return "Tier 1"
    if asset in t2 or clean in t2 or f"1000{clean}" in t2:
        return "Tier 2"
    if asset in t3 or clean in t3 or f"1000{clean}" in t3:
        return "Tier 3"
    return "Excluded"
