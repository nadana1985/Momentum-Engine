# Version 10
"""Canonical configuration for the unified momentum engine.

Single source of truth for every knob that previously drifted between copies:
shock gate (percentile vs fixed), 1-year baseline strictness, dormant-book
definition, taker filter, consecutive-flag dedup, outcome horizons, CTA
execution semantics.

Old-file drift map (see README.md):
  shock gate default      -> p99 (was: fixed 15x in scanners, 5x in CTA)
  year baseline           -> strict 8760 by default, lax 720 optional
  dormant book            -> mode 'relative' default (was 4 definitions)
  taker filter            -> strict flag toggles it (was: absent in tape copy)
  dedup consecutive flags -> first_of_run option (was: only unified scanner)
  outcome window          -> t+1..t+N, entry bar excluded (was: unified scanner included it)
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# One data root for shards, state and tapes. Defaults to <repo>/data;
# set V10_DATA_ROOT to point at a data directory elsewhere.
DATA_ROOT = Path(os.environ.get('V10_DATA_ROOT') or (ROOT / 'data')).resolve()
SHARD_DIR = DATA_ROOT / 'raw_shards'
EXOTIC_DIR = DATA_ROOT / 'exotic_shards'
TAPE_DIR = DATA_ROOT / 'all_tapes' / 'v10_production'
L5_PATH = DATA_ROOT / 'l5_ranking.parquet'
BARS_24H = 24
BARS_4H = 4
BARS_30D = 720
BARS_1YR = 8760
HORIZONS = (3, 6, 24, 168)
RET_HORIZON = 168  # close-to-close return at t+168
DORMANT_MODES = ('relative', 'abs_usd', 'volume')
TAKER_BUFFER = 0.0

# ---------------------------------------------------------------------------
# V10.2 FROZEN closed-book spec (2026-09-20). Do not retune without a new
# pre-registered hypothesis class. pit_study rejected rise-vetoes and
# early-path exits. The lottery is unfilterable: take every CONTINUATION,
# Donchian the winners, eat the ~-6% structural-stop tax.
# Isolated to engine == "CONTINUATION". Never IGNITION / PHOENIX / squeeze.
# Trigger is CLOSE, not low. Stop never decreases.
# ---------------------------------------------------------------------------
DONCHIAN_BARS = 504            # 21d of 1h bars; asset-level low.shift(1).rolling
DONCHIAN_ARM_MFE = 0.50        # arm only after peak MFE >= 50%
DONCHIAN_ENGINE = 'CONTINUATION'
DONCHIAN_COL = 'donchian_low_504'


@dataclass(frozen=True)
class FeatureConfig:
    """Feature/enrichment configuration shared by every consumer."""
    # shock gate: exactly one of the two is used
    shock_percentile: float | None = 99.0   # trailing-1yr p99 of own shock_mult
    shock_mult: float | None = None         # fall back to a fixed multiplier (e.g. 15)

    # 1-year baseline strictness: 8760 = full year required (strict),
    # 720 = partial-year allowed (lax, matches the old tape generator)
    year_min_periods: int = BARS_1YR

    # dormant book: 'relative' = 30d notional median < 1yr notional median
    #               'abs_usd'  = 30d notional median < max_notional_usd
    #               'volume'   = trailing-24h avg volume < 30d volume median
    dormant_mode: str = 'relative'
    max_notional_usd: float = 150_000.0    # used only by 'abs_usd'

    # taker aggression filter (strict dual-tier ignition)
    require_taker: bool = True
    taker_buffer: float = TAKER_BUFFER

    # emit only the first flag of a consecutive-hour run
    first_of_run: bool = False

    l5_ranking_path: Path | None = L5_PATH

    def gate_label(self) -> str:
        if self.shock_mult is not None:
            return f'fixed {self.shock_mult:g}x'
        return f'trailing-1yr p{self.shock_percentile:g} of own shock_mult'

    def year_label(self) -> str:
        return 'strict (full 8760h)' if self.year_min_periods >= BARS_1YR else 'lax (>=720h)'


@dataclass(frozen=True)
class OutcomeConfig:
    """Forward-outcome (post-hoc label) configuration."""
    horizons: tuple = HORIZONS            # MFE/MAE windows in hours (t+1..t+N)
    ret_horizon: int = RET_HORIZON        # close-to-close return at t+N
    low_hold_hours: int = 24              # trigger-low hold window


@dataclass(frozen=True)
class CtaConfig:
    """Consolidated CTA execution semantics (one canonical behavior).

    Canonical choices (killing the CTA-family drifts):
      - trail_4h_low excludes the current bar (shift before rolling)
      - the working stop is a strict monotonic ratchet (never moves down)
      - no same-bar re-entry after a stop-out
      - exits trigger intrabar when low/high pierces the working stop
      - the dead-book filter is always applied (dormant_mode decides its form)

    V10.2 freeze: Donchian 21d floor is CONTINUATION-only (see DONCHIAN_*).
    trail_activation_pct is unused by CONTINUATION (squeeze still hardcodes +5%/25%).
    Changing donchian_bars / donchian_arm_mfe / donchian_engine is a new engine.
    """
    bars_per_24h: int = BARS_24H
    bars_per_4h: int = BARS_4H
    volume_shock_mult: float = 5.0          # CTA preset gate (raw engine, not ignition p99)
    hard_stop_pct: float = 0.03
    trail_activation_pct: float = 0.05      # UNUSED by CONTINUATION; squeeze +5% is hardcoded
    donchian_bars: int = DONCHIAN_BARS
    donchian_arm_mfe: float = DONCHIAN_ARM_MFE
    donchian_engine: str = DONCHIAN_ENGINE
    allow_short: bool = True
    dormant_mode: str = 'abs_usd'
    max_notional_usd: float = 150_000.0
    min_lookback: int = BARS_30D            # drop rows before this much history
    max_ignition_wick_ratio: float = 0.65   # Upper wick firewall (vetoes >65% rejection wicks)
    max_unconfirmed_extension: float = 2.0  # Volatility-normalized extension threshold (in units of 24h ATR)
    oi_confirmation_ratio: float = 0.8      # Required fraction of rolling 30d P90 OI change when extended
    min_exhaustion_mfe: float = 0.15        # Minimum peak MFE required to call exhaustion near accumulation floor
    base_floor_multiple: float = 2.0        # Multiple of rolling 90d low defining accumulation base zone
    base_floor_percentile: float = 0.60     # Percentile of rolling 90d range defining accumulation base zone
    base_lookback_bars: int = 2160          # 90 days of 1h bars




