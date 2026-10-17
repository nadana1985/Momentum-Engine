"""
Kronos V12: Canonical Configuration & Frozen Dataclasses (Cores 1-6)
Implements strict typing, frozen contracts, and interface compliance.
"""

from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True)
class MacroConfig:
    """Core 1: 200-Day BTC Macro Bear Veto Configuration"""
    btc_symbol: str = "BTC"
    ema_hours: int = 4800          # 200 days * 24h
    return_hours: int = 720        # 30 days * 24h
    require_bull: bool = True
    enable_decoupling_override: bool = False  # STRICTLY DISABLED: Clean-room proved bear decoupling bleeds -64.5%
    ath_tier2_protection_pct: float = 0.85
    enable_cycle_spring: bool = True          # Study S-Y: Cycle Bottom Spring (Days 180+ below EMA & 30d base)
    cycle_spring_min_days: float = 180.0      # Minimum consecutive days below EMA required to unlock spring
    cycle_spring_require_base: bool = True    # Requires positive 30d BTC return (downside exhaustion)
    enable_rs_btc_extension_veto: bool = True # Study S-Z: 14d RS_BTC Over-Extension Climax Clamp
    max_rs_btc_extension: float = 0.20        # Vetoes exhausted late-climax breakout traps (> +20.0% vs BTC)

    def __post_init__(self):
        assert self.ema_hours > 0, "ema_hours must be positive"
        assert self.return_hours > 0, "return_hours must be positive"
        assert 0.0 < self.ath_tier2_protection_pct <= 1.0, "ath_tier2_protection_pct must be in (0, 1]"
        assert self.cycle_spring_min_days > 0, "cycle_spring_min_days must be positive"
        assert self.max_rs_btc_extension > 0.0, "max_rs_btc_extension must be positive"


@dataclass(frozen=True)
class TierConfig:
    """Core 2: Dynamic Point-in-Time Tier Classifier Thresholds"""
    tier1_min_oi_usd: float = 15_000_000.0   # $15M median OI
    tier1_min_vol_usd: float = 15_000_000.0  # $15M median volume
    tier1_min_corr_btc: float = 0.0          # Clean-Room Decoupled: 0 penalty on BTC correlation
    tier1_min_hist_days: float = 180.0

    tier2_min_oi_usd: float = 2_500_000.0    # $2.5M median OI
    tier2_min_vol_usd: float = 2_500_000.0   # $2.5M median volume
    tier2_min_corr_btc: float = 0.0          # Clean-Room Decoupled: 0 penalty on BTC correlation
    tier2_min_hist_days: float = 90.0

    # Core 2c: Tier 3 Micro-Cap Low-Float Universe
    enable_tier3: bool = True
    tier3_min_oi_usd: float = 250_000.0      # $250k min OI floor to filter zero-liquidity zombies
    tier3_enable_book1: bool = False         # STRICTLY DISABLED: No trend breakouts on micro-caps
    tier3_enable_book2: bool = True          # ENABLED: Squeeze breakouts only
    tier2_enable_book4: bool = False         # STRICTLY DISABLED: Book 4 restricted to Tier 1 alone
    tier3_enable_book4: bool = False         # STRICTLY DISABLED: Book 4 restricted to Tier 1 alone

    excluded_symbols: Tuple[str, ...] = (
        'AAPL', 'AMZN', 'GOOGL', 'MSFT', 'NVDA', 'TSLA', 'META', 'AMD', 'INTC',
        'ARM', 'AVGO', 'MU', 'QCOM', 'SPY', 'QQQ', 'XAU', 'XAG', 'CL', 'BZ',
        'ASTS', 'PLTR', 'COIN', 'MSTR', 'SNDK', 'MRVL', 'EWY', 'KORU', 'AAOI',
        'AMAT', 'ANTHROPIC', 'OPENAI', 'SPCX', 'SKHYNIX', 'SAMSUNG', 'SOXL',
        'DRAM', 'BMNR', 'TQQQ', 'USDC'
    )

    def __post_init__(self):
        assert self.tier1_min_oi_usd > self.tier2_min_oi_usd, "Tier 1 OI must exceed Tier 2"
        assert 0.0 <= self.tier1_min_corr_btc <= 1.0, "Correlation must be in [0, 1]"
        assert 0.0 <= self.tier2_min_corr_btc <= 1.0, "Correlation must be in [0, 1]"


@dataclass(frozen=True)
class MicrostructureConfig:
    """Core 3 & 4: Orderbook Turnover Velocity & Whale Firewall Gates"""
    min_turnover_velocity: float = 0.25
    max_turnover_velocity: float = 15.0       # Book 1 max turnover velocity (P98 of universe)
    b2_max_turnover_velocity: float = 5.0     # Book 2 max turnover velocity (retail euphoria protection)
    min_toptrader_ls: float = 0.85
    tier1_max_funding: float = 0.00030       # +0.030% per 8h
    tier2_max_funding: float = 0.00030       # +0.030% per 8h (harmonized with Tier 1)

    # Revamped Book 2: Coiled Squeeze Breakout Engine (Reverse-Engineered from Pure Shards)
    enable_book2: bool = True
    b2_max_ls: float = 0.95                    # Whales are net short
    b2_max_shelf_range: float = 0.25           # Tight 72h compression shelf <= 25%
    b2_max_ret_7d: float = 0.30                # Not already parabolically extended <= +30%
    b2_max_d_oi_usd_24h: float = 0.20          # OI not hyper-inflated <= +20%
    b2_max_dist_72h_low: float = 0.22          # Breakout not blown out <= +22% from shelf floor
    b2_max_taker_ratio: float = 0.52           # Passive smart money absorption
    b2_min_vol_shock: float = 2.0              # Clean volume expansion >= 2.0x
    b2_cooldown_hours: float = 72.0            # 72h cooldown
    b2_max_initial_risk: float = 0.08          # 8.0% structural stop clamp

    # Study S-Z2: Trapped-Short Squeeze Ignition Override
    enable_sqz_turnover_override: bool = True
    sqz_override_max_funding: float = -0.00030 # Negative funding <= -0.030% / 8h (-33% APR)
    sqz_override_max_ls: float = 1.25          # Whales not heavily long (trapped short squeeze fuel)

    # Study S-Z3: High-Turnover Trapped-Whale Squeeze Exception
    enable_whale_trap_override: bool = True
    whale_trap_min_turnover: float = 5.0      # Active orderbook turnover
    whale_trap_max_funding: float = 0.00005   # Flat or negative funding <= +0.005% / 8h

    # Study S-R: Microstructure De-Guillotining (Canonical Production Architecture)
    enable_funding_sqz_exception: bool = True   # Unlocks high funding if whales net short (L/S < 0.95)
    funding_sqz_max_ls: float = 0.95            # Max Top Trader L/S for funding squeeze unlock
    enable_turnover_scaling: bool = True        # Unlocks turnover > 15.0x with continuous size scaling

    # Study S-BC & S-BD: Modern Quant Microstructure Upgrades (Canonical Production V12.7)
    book2_sub_200d_only: bool = True            # Study S-BC: Coiled Squeezes restricted strictly to Sub-200d EMA (PF 2.281)
    enable_csmi_anti_chop: bool = True          # Study S-BD: Compensatory Anti-Chop Firewall
    csmi_anti_chop_threshold: float = -1.25     # Veto candidates with extreme negative confluence S <= -1.25

    # Study S-BI Pillar 2: Book 2 Whale Front-Running Purge (engine-native re-test; default OFF)
    enable_front_running_purge: bool = False
    front_run_min_d_ls_24h: float = 0.25        # Veto Book 2 coil if whales jumped long >= +25% in 24h

    # V13.0 / Study S-BP: Book 2 Inverted Carry Conviction Multiplier
    enable_b2_inverted_carry_sizing: bool = True
    b2_inverted_carry_multiplier: float = 1.25  # Sizing multiplier on negative funding (FR <= 0.0) + trapped shorts
    b2_inverted_carry_max_ls: float = 1.05

    def __post_init__(self):
        assert self.min_turnover_velocity > 0.0, "min_turnover must be positive"
        assert self.max_turnover_velocity > self.min_turnover_velocity, "max_turnover must exceed min"
        assert self.min_toptrader_ls > 0.0, "min_toptrader_ls must be positive"
        assert self.sqz_override_max_funding < 0.0, "sqz_override_max_funding must be negative"
        assert self.whale_trap_min_turnover > 0.0, "whale_trap_min_turnover must be positive"
        assert 0.0 < self.funding_sqz_max_ls <= 2.0, "funding_sqz_max_ls must be in (0, 2]"


@dataclass(frozen=True)
class EntryConfig:
    """Core 5: Dual Entry Engine (Continuation Breakout + Bear-Trap Reclaim)"""
    breakout_lookback_bars: int = 504        # 21 days (504h)
    min_14d_ret: float = 0.15                # +15%
    min_rs_btc: float = 0.10                 # +10% relative strength
    max_dist_from_60d_low: float = 0.50      # +50% max distance from 60d base
    remediated_max_dist_60d: float = 0.60    # Firm ceiling for remediated squeeze overrides (seals 999.0 leak)
    max_dist_from_72h_low: float = 0.25      # Upstream Flagpole Clamp: <= +25% from 72h low
    max_oi_expansion_14d: float = 0.35       # +35% max OI expansion clamp
    cooldown_hours: int = 72                 # Study S-AV: 72h calibrated base horizon (lifts wealth +108.8Q x)

    # Bear Trap V-Reclaim (Study S-P)
    reclaim_min_hours: float = 12.0
    reclaim_max_hours: float = 144.0
    reclaim_max_pnl_loss: float = -0.14      # Within -14% stop flush
    reclaim_min_ret_14d: float = 0.10
    reclaim_max_dist_60d_t1: float = 1.10
    reclaim_max_dist_60d_t2: float = 0.90
    slippage: float = 0.0025                 # 25 bps slippage

    # Study S-U High-Shelf Continuation Engine
    enable_continuation: bool = False
    continuation_shelf_bars: int = 336          # 14 days (336h)
    continuation_max_shelf_range: float = 0.30  # <= 30% range compression
    continuation_min_vol_shock: float = 2.5     # >= 2.5x volume shock
    continuation_min_turnover: float = 1.5      # >= 1.5x turnover velocity
    continuation_min_toptrader_ls: float = 1.30 # >= 1.30 Top Trader L/S
    continuation_max_initial_risk: float = 0.08 # Max 8.0% initial stop loss clamp
    continuation_cooldown_hours: float = 72.0   # 72h minimum cooldown after prior exit (eliminates rapid churn)
    continuation_min_dist_60d: float = 0.40     # Must be >= 40% above 60d low (elevated continuation)
    continuation_min_rs_btc: float = 0.15       # Must be outperforming BTC by >= +15%
    continuation_min_14d_ret: float = 0.20      # Must have >= +20% 14d momentum base

    def __post_init__(self):
        assert self.min_14d_ret > 0.0, "min_14d_ret must be positive"
        assert self.reclaim_max_hours > self.reclaim_min_hours, "Invalid reclaim time window"
        assert 0.0 <= self.slippage <= 0.05, "Slippage must be in [0, 0.05]"
        assert 0.0 < self.continuation_max_initial_risk <= 0.15, "continuation_max_initial_risk must be in (0, 0.15]"
        assert self.max_dist_from_72h_low > 0.0, "max_dist_from_72h_low must be positive"
        assert self.remediated_max_dist_60d > 0.0, "remediated_max_dist_60d must be positive"


@dataclass(frozen=True)
class ExitConfig:
    """Core 6: Dynamic Tier Donchian Floors & Climax Harvesting"""
    tier1_donchian_bars: int = 336           # 14 days (336h)
    tier2_donchian_bars: int = 168           # 7 days (168h)
    tier1_max_initial_risk: float = 0.15     # 15% initial stop clamp
    tier2_max_initial_risk: float = 0.12     # 12% initial stop clamp

    # Ratchets
    tier1_be_ratchet_mfe: float = 0.20       # Lock BE at +20% MFE
    tier1_trail_ratchet_mfe: float = 0.50    # Trail high * 0.75 at +50% MFE
    tier1_trail_floor_pct: float = 0.75

    tier2_be_ratchet_mfe: float = 0.15       # Lock BE at +15% MFE
    tier2_trail_ratchet_mfe: float = 0.30    # Trail high * 0.82 at +30% MFE
    tier2_trail_floor_pct: float = 0.82

    # Study S-AL / S-AX: Intra-Trade Higher-Low Preservation Retest Cushion Ratchet
    # Options: "baseline", "cushion_3pct", "cushion_1_5pct", "delayed_30pct", "volume_gated", "no_be_ratchet"
    be_ratchet_mode: str = "cushion_1_5pct"  # Promoted to Canonical Production (Study S-AL/S-AX: +160.6% Net Log, 4.98x Wealth)

    # Continuation Engine Exits
    continuation_be_ratchet_mfe: float = 0.15   # Breakeven lock at +15% MFE
    continuation_trail_mfe: float = 0.30        # Trail high * 0.85 when MFE >= +30%
    continuation_trail_floor_pct: float = 0.85
    continuation_climax_mfe: float = 0.30       # Trigger climax check at >= +30% MFE
    continuation_climax_wick: float = 0.40      # Upper wick >= 40%
    continuation_climax_shock: float = 4.0      # Vol shock >= 4.0x

    # Fast Decay Cuts
    tier1_fast_decay_hours: float = 48.0
    tier1_fast_decay_oi_leak: float = -0.05  # -5% OI leak
    tier2_fast_decay_hours: float = 36.0
    tier2_fast_decay_oi_leak: float = -0.03  # -3% OI leak

    # Climax Top Harvest
    tier1_climax_mfe: float = 0.50
    tier2_climax_mfe: float = 0.30
    climax_min_upper_wick: float = 0.40
    climax_min_vol_shock: float = 3.0
    climax_whale_dump_d_ls: float = -0.08
    climax_whale_dump_funding: float = 0.00040

    # Book 2 Climax Harvest & Time Cap
    b2_climax_mfe: float = 0.35
    b2_climax_wick: float = 0.40
    b2_climax_shock: float = 3.5
    b2_time_cap_hours: int = 168

    # Stagnation & Time Caps
    stagnation_hours: float = 72.0
    stagnation_max_mfe: float = 0.04
    time_cap_hours_t1: int = 504             # 21 days
    time_cap_hours_t2: int = 336             # 14 days

    # Study S-AA: 36-Hour Stagnation Stall-Out Bailout Engine
    enable_stall_bailout: bool = True
    stall_bailout_hours: float = 36.0        # 36h incubation checkpoint (Zero-Runner Loss Horizon)
    stall_bailout_max_mfe: float = 0.010     # Peak MFE must not have exceeded +1.0% (+0.010)

    # Study S-AY: Two-Tier Target Cap Routing (Law 4 & Law 5)
    enable_two_tier_targets: bool = True
    max_lagging_target_pct: float = 0.20     # Upper target cap for lagging candidates (+20.0%)
    min_lagging_target_pct: float = 0.15     # Default minimum target cap (+15.0%)

    # Study S-BI Pillar 3: Whale Euphoria Climax Harvest (engine-native, point-in-time; default OFF)
    # Applies to Book 1 / Book 2 / Continuation only (Book 4 keeps its Two-Tranche engine).
    enable_euphoria_climax_harvest: bool = False
    euphoria_min_mfe: float = 0.20
    euphoria_min_ls: float = 2.50

    def __post_init__(self):
        assert self.tier1_donchian_bars > self.tier2_donchian_bars, "Tier 1 floor must be wider than Tier 2"
        assert self.tier1_max_initial_risk >= self.tier2_max_initial_risk, "Tier 1 risk clamp must be >= Tier 2"
        assert self.stall_bailout_hours > 0.0, "stall_bailout_hours must be positive"
        assert 0.0 < self.stall_bailout_max_mfe < 0.10, "stall_bailout_max_mfe must be in (0, 0.10)"
        assert 0.0 < self.min_lagging_target_pct <= self.max_lagging_target_pct, "Invalid lagging target thresholds"


@dataclass(frozen=True)
class SizingConfig:
    """Core 7 / Study S-Q: Point-in-Time Kyle-Lambda Dynamic Position Sizing Overlay (Canonical Production)"""
    enable_lambda_sizing: bool = True        # Promoted to Canonical Production (Study S-Q / S-R Full Stack)
    base_weight: float = 1.50                # w = base_weight - pct_lambda
    min_weight: float = 0.50                 # Clamped minimum weight
    max_weight: float = 1.50                 # Clamped maximum weight
    lookback_bars: int = 72                  # Rolling covariance window (72h)
    history_min_bars: int = 2160             # Minimum 90 days of valid lambda to form percentile
    history_max_bars: int = 8760             # Trailing 1-year percentile window
    fee_haircut_bps: float = 10.0            # Conservative fee stress test penalty on excess leverage

    # Study S-AW / S-AX: Continuous Institutional Ticket Size Sizing Overlay (Canonical Production V12.4)
    enable_ticket_size_sizing: bool = True   # Promoted to Canonical Production (Study S-AX: +160.6% Net Log, 4.98x Wealth)
    ts_base_multiplier: float = 0.75
    ts_slope_multiplier: float = 0.50
    ts_min_multiplier: float = 0.75
    ts_max_multiplier: float = 1.25
    ts_lookback_bars: int = 168

    # Study S-AY: Continuous 200-EMA Sizing Overlay (Canonical Production V12.5+)
    enable_ema_sizing: bool = True           # Promoted to Canonical Production (Study S-AY: +23.3% Net Log Lift)
    ema_base_multiplier: float = 0.75
    ema_slope_multiplier: float = 0.50
    ema_min_multiplier: float = 0.75
    ema_max_multiplier: float = 1.25

    # Study S-BD: Unified Compensatory Squeeze & Momentum Index (CSMI) Sizing Overlay (Canonical Production V12.7)
    enable_csmi_sizing: bool = True          # Promoted to Canonical Production (Study S-BD: +299.8% Net Log Lift, 20.0x Wealth)
    csmi_base_weight: float = 0.50
    csmi_slope_weight: float = 1.00
    csmi_min_weight: float = 0.50
    csmi_max_weight: float = 1.45

    def __post_init__(self):
        assert self.min_weight > 0.0, "min_weight must be positive"
        assert self.max_weight >= self.min_weight, "max_weight must be >= min_weight"
        assert self.lookback_bars >= 12, "lookback_bars must be at least 12"
        assert self.history_max_bars > self.history_min_bars, "history_max_bars must exceed history_min_bars"
        assert self.ts_max_multiplier >= self.ts_min_multiplier > 0.0, "Invalid ticket size multipliers"
        assert self.csmi_max_weight >= self.csmi_min_weight > 0.0, "Invalid CSMI multipliers"
        assert self.ema_max_multiplier >= self.ema_min_multiplier > 0.0, "Invalid EMA size multipliers"


@dataclass(frozen=True)
class ShadowReclaimConfig:
    """Study S-P: Bear-Market Shadow Anchor Reclaim Configuration"""
    enable_bear_shadow_reclaims: bool = False  # Zero-regression default
    max_toptrader_ls: float = 0.95             # Whales must be net short (squeeze fuel)
    min_turnover_velocity: float = 3.50        # High orderbook turnover
    max_funding_rate: float = 0.00010          # Funding <= +0.010% / 8h
    reclaim_min_hours: float = 12.0            # Min shakeout duration
    reclaim_max_hours: float = 144.0           # 6-day max window
    max_initial_risk: float = 0.08             # Clamped at -8.0% max loss
    min_vol_shock: float = 2.0                 # Minimum volume shock on shadow anchor registration

    def __post_init__(self):
        assert 0.0 < self.max_toptrader_ls <= 1.5, "max_toptrader_ls must be in (0, 1.5]"
        assert self.min_turnover_velocity > 0.0, "min_turnover must be positive"
        assert self.reclaim_max_hours > self.reclaim_min_hours, "Invalid reclaim time range"
        assert 0.0 < self.max_initial_risk <= 0.15, "max_initial_risk must be in (0, 0.15]"
        assert self.min_vol_shock >= 1.0, "min_vol_shock must be >= 1.0"


@dataclass(frozen=True)
class Book3FlushReclaimConfig:
    """Study S-AC / S-AN / S-AO: Bull-Market Flush Absorption & Reclaim Architecture (Satellite Sleeve)
    Passes all 6 SPEC Acceptance Gates (+5,047.2% Net Log PnL, WR 57.18%, PF 1.274, t=8.66).
    Tier-Calibrated: Tier 1 & Tier 3 at -8.0% discount or dynamic volume shelf.
    Optimized (V12.2): Tier 2 Mid-Caps disabled by default (enable_tier2=False) to purge -105.4% absorption drag.
    Canonical V12.3 (Study S-AN / S-AO Arm 1): Two-Tier Volume Profile Shelf Absorption with Static Fallback:
      - Searches point-in-time 90-day volume profile in [-15%, -4%] corridor for High-Volume Nodes (HVN >= 1.0x mean).
      - Places resting limit bid at structural volume shelf high if present; falls back to static -8.0% if absent.
      - 72h TTL & resting stop-market at -8.0% from fill price.
      - Generates +416.4% Net Log Delta, Log PF 1.435, and expands capital multiple 64.4x to 284.01 Quadrillion x.
    """
    enable_book3_flush_reclaim: bool = True    # Promoted to Canonical Production (Study S-AC Full Stack)
    enable_tier1: bool = True                  # Allow Tier 1 in Book 3 (PF 1.589, +432.8% log)
    enable_tier2: bool = False                 # Disabled: Purges Tier 2 Mid-Cap drag (PF 0.948, -105.4% log drag)
    enable_tier3: bool = True                  # Allow Tier 3 in Book 3 (PF 1.215, +1,554.3% log)
    flush_discount_pct: float = 0.080          # Resting limit bid discount for Tier 1 & Tier 3 (0.920 * P_0)
    tier2_flush_discount_pct: float = 0.120    # Calibrated Tier 2 Mid-Cap discount (0.880 * P_0)
    ttl_hours: int = 72                        # 72h time-to-live for resting limit order
    max_initial_risk: float = 0.080            # Resting stop loss from fill (-8.0% from fill)
    target_reclaim_pct: float = 0.087          # Exit 100% at P_0 (+8.70% from fill / entry reclaim)
    require_btc_macro_bull: bool = True        # Strictly bull market only

    # Study S-AN / S-AO: Two-Tier Volume Profile Shelf Absorption Configuration
    # Options: "shelf_fallback" (Canonical V12.3 default), "static_only" (V12.2 legacy baseline)
    book3_shelf_mode: str = "shelf_fallback"
    vp_lookback_bars: int = 2160               # 90 days lookback (2160h)
    vp_bins: int = 35                          # 35 volume profile price bins
    corridor_lo: float = 0.85                  # -15% corridor lower bound (0.85 * P_0)
    corridor_hi: float = 0.96                  # -4% corridor upper bound (0.96 * P_0)
    hvn_mult_support: float = 1.0              # High Volume Node volume multiplier (>= 1.0x mean bin volume)

    # Study S-BJ: allow Tier 2 Book 3 bids ONLY when armed by these veto gates (empty = production behavior)
    tier2_gate_whitelist: Tuple[str, ...] = ()

    def __post_init__(self):
        assert 0.0 < self.flush_discount_pct < 0.20, "flush_discount_pct must be in (0, 0.20)"
        assert 0.0 < self.tier2_flush_discount_pct < 0.25, "tier2_flush_discount_pct must be in (0, 0.25)"
        assert self.ttl_hours > 0, "ttl_hours must be positive"
        assert 0.0 < self.max_initial_risk <= 0.15, "max_initial_risk must be in (0, 0.15]"
        assert self.target_reclaim_pct > 0.0, "target_reclaim_pct must be positive"
        assert self.book3_shelf_mode in ("shelf_fallback", "static_only"), "Invalid book3_shelf_mode"
        assert self.vp_lookback_bars > 0, "vp_lookback_bars must be positive"
        assert self.vp_bins >= 10, "vp_bins must be at least 10"
        assert 0.50 <= self.corridor_lo < self.corridor_hi <= 1.0, "Invalid corridor bounds"
        assert self.hvn_mult_support > 0.0, "hvn_mult_support must be positive"


@dataclass(frozen=True)
class Book4Config:
    """Core Book 4: 200-Day EMA Higher-Low Retest & Reclaim Engine (Study S-BB Canonical Production V12.6)
    Generates +4,795.1% Net Log Return across 521 trades, Log PF 4.809, Win Rate 75.6%.
    """
    enable_book4: bool = True
    min_bars_below: int = 720              # Minimum 30 days below 200d EMA before touch (720h)
    touch_tolerance_pct: float = 0.015     # High >= 0.985 * EMA_200d
    max_retest_hours: int = 120            # Bottom of pullback formed within 5 days (120h)
    max_retest_dd: float = -0.20           # Pullback depth contained within -20.0%
    target_cap_pct: float = 0.20           # Two-Tier target cap (+15% to +20%)
    continuous_btc_sizing: bool = True     # 1.0x Bull / 0.50x Bear continuous sizing overlay
    bear_sizing_mult: float = 0.50         # 0.50x defensive sizing during BTC macro bear
    max_duration_hours: int = 720          # 30 days max duration
    stagnation_cut_hours: int = 168        # 7-day stagnation cut if MFE < 5%
    donchian_arm_mfe: float = 0.50         # Arm trailing floor at +50% MFE

    # Study S-BF: Continuous Anti-Chase Sizing Multiplier Engine (Canonical Production V12.9)
    enable_anti_chase_sizing: bool = True
    anti_chase_threshold: float = 1.50     # Threshold for body / ATR_24h
    anti_chase_decay_slope: float = 0.35   # Slope for reducing size
    anti_chase_min_multiplier: float = 0.50 # Floor multiplier
    anti_chase_max_multiplier: float = 1.20 # Ceiling / maximum conviction multiplier

    # Study S-BK: Dual 200d EMA Confluence Multiplier & Whale Squeeze Immunity (Canonical Production V12.11)
    enable_dual_confluence_sizing: bool = True
    confluence_conviction_mult: float = 1.35  # Sizing multiplier when both USD and ALT/BTC 200d EMAs are reclaimed
    enable_whale_squeeze_immunity: bool = True # Override premature climax exits when Whales trapped net short (L/S <= 0.95)
    whale_squeeze_max_ls: float = 0.95        # Threshold for identifying trapped whale shorts

    # Study S-CA: Day Close P_NB_High Structural Acceptance (Tier 1 certified)
    enable_p_nb_day_close_confirmation: bool = True
    enable_p_nb_microstructure_sizing: bool = True

    def __post_init__(self):
        assert self.min_bars_below > 0, "min_bars_below must be positive"
        assert 0.0 < self.touch_tolerance_pct < 0.10, "touch_tolerance_pct must be in (0, 0.10)"
        assert self.max_retest_hours > 0, "max_retest_hours must be positive"
        assert -0.50 < self.max_retest_dd < 0.0, "max_retest_dd must be in (-0.50, 0.0)"
        assert self.target_cap_pct > 0.0, "target_cap_pct must be positive"
        assert 0.0 < self.bear_sizing_mult <= 1.0, "bear_sizing_mult must be in (0.0, 1.0]"
        assert self.anti_chase_max_multiplier >= self.anti_chase_min_multiplier > 0.0, "Invalid anti-chase multipliers"
        assert self.anti_chase_threshold > 0.0, "anti_chase_threshold must be positive"
        assert self.confluence_conviction_mult >= 1.0, "confluence_conviction_mult must be >= 1.0"
        assert 0.0 < self.whale_squeeze_max_ls <= 1.5, "whale_squeeze_max_ls must be in (0, 1.5]"


@dataclass(frozen=True)
class Book5Config:
    """Study S-BI Pillar 1: Trapped-Whale Shelf Absorption Squeeze Sleeve (engine-native re-test; default OFF).
    Trigger (point-in-time): Top Trader L/S <= max_ls AND token-denominated OI 24h change >= min_d_oi_tokens
    AND price rising over 24h. Execution: resting limit bid at (1 - discount) * P0, target P0, stop -max_initial_risk
    from fill, TTL ttl_hours. Fills only when no position is open.
    """
    enable_book5: bool = False
    max_ls: float = 0.85
    min_d_oi_tokens: float = 0.40
    require_price_up_24h: bool = True
    discount_pct: float = 0.08
    max_initial_risk: float = 0.08
    ttl_hours: int = 72
    cooldown_hours: float = 72.0

    def __post_init__(self):
        assert 0.0 < self.discount_pct < 0.25, "discount_pct must be in (0, 0.25)"
        assert 0.0 < self.max_initial_risk <= 0.15, "max_initial_risk must be in (0, 0.15]"
        assert self.ttl_hours > 0, "ttl_hours must be positive"


@dataclass(frozen=True)
class Book1Config:
    """V13.0 / Study S-BR & S-BS: Book 1 Regime Dormancy & AVWAP Retest Reclaim Engine.
    Requires asset to emerge from a 72h compressed dormant base (D_t >= 0.65),
    anchors AVWAP_tau at 21-day breakout ignition, and executes on Higher-Low
    retest reclaim with Two-Tranche profit harvesting.
    """
    enable_dormancy_filter: bool = False
    min_dormancy_72h: float = 0.65             # Prior 72h mean dormancy score >= 0.65
    enable_avwap_reclaim: bool = False         # Wait for pullback & reclaim of AVWAP_tau (armed in V13)
    max_retest_hours: int = 120                # Retest window horizon
    avwap_corridor_tolerance: float = 0.05     # Pullback within [0.95, 1.05] of AVWAP
    tranche_a_target_pct: float = 0.05         # Option 1 Micro-Harvest: +5.0% target cap for >= 40.2% WR
    tranche_b_cushion_pct: float = 0.005       # Tight -0.5% breakeven cushion ratchet upon Tranche A fill
    tranche_b_donchian_bars: int = 72          # Rolling 72h Donchian floor trail
    spot_absorption_mult: float = 1.35         # Conviction sizing when Token OI is flat/falling (Delta OI <= 0)
    max_token_oi_expansion: float = 0.30       # Veto retail leverage bubbles (> +30% 24h OI)
    max_funding_z: float = 1.00                # Veto crowded funding tops (F_z > 1.0)
    enable_3bar_consolidation_hold: bool = True # Study S-BU: Require price to hold upper half of breakout candle
    min_consolidation_bars: int = 3            # 3 consecutive bars required to confirm structural acceptance

    def __post_init__(self):
        assert 0.0 < self.min_dormancy_72h <= 1.0, "min_dormancy_72h must be in (0, 1]"
        assert self.max_retest_hours > 0, "max_retest_hours must be positive"
        assert self.tranche_a_target_pct > 0.0, "tranche_a_target_pct must be positive"
        assert self.spot_absorption_mult >= 1.0, "spot_absorption_mult must be >= 1.0"


@dataclass(frozen=True)
class Book6Config:
    """Study S-BP: Book 6 3-Stage Asymmetric Reclaim Engine (3-SARE).
    CUSUM-anchored orderflow base reclaim with staged resting limit absorption,
    dual-barrier panic liquidation bailouts, and 3-stage asymmetric profit harvesting.
    """
    enable_book6: bool = True
    cusum_threshold: float = 1.50             # Minimum CUSUM accumulation drift at breakout (S_tau^+ >= 1.5)
    cycle_base_days: int = 30                 # 30-day base duration (720h)
    cycle_base_max_dist: float = 0.40         # Distance to 90d low <= 40%
    retest_min_hours: int = 36                # Minimum cooling-off before reclaim
    retest_max_hours: int = 168               # Maximum retest window
    avwap_tolerance_low: float = 0.90         # Lower boundary of retest corridor
    avwap_tolerance_high: float = 1.03        # Upper boundary of retest corridor
    limit_bid_ratio: float = 0.50             # 50% resting limit bid at AVWAP_tau
    stop_retest_floor_buffer: float = 0.995   # Retest low * 0.995 stop
    max_stop_pct: float = 0.105               # Hard -10.5% cap from entry
    panic_bailout_vol_mult: float = 3.0       # Exit early if breaking floor with volume >= 3.0x
    tranche_a_mfe: float = 0.08               # Tranche A +8.0% quick lock
    tranche_a_cushion: float = 0.002          # Ratchet Tranche B & C stop to entry -0.2%
    tranche_b_mfe: float = 0.25               # Tranche B +25.0% swing target cap
    tranche_b_floor: float = 0.08             # Ratchet Tranche C stop to +8.0% guaranteed
    tranche_c_donchian_bars: int = 72         # Trailing Donchian floor for runner
    whale_frontrun_veto_delta: float = 0.25   # Veto setups where whales aggressive long front-run
    whale_squeeze_max_ls: float = 0.95        # Trapped whale shorts squeeze immunity threshold
    max_duration_hours: int = 720             # 30-day holding horizon limit

    def __post_init__(self):
        assert self.cusum_threshold > 0.0, "cusum_threshold must be positive"
        assert self.cycle_base_days > 0, "cycle_base_days must be positive"
        assert 0.0 < self.tranche_a_mfe < self.tranche_b_mfe, "tranche_a_mfe must be < tranche_b_mfe"
        assert self.max_duration_hours > 0, "max_duration_hours must be positive"


@dataclass(frozen=True)
class CalendarConfig:
    """Study S-BV & S-BX: Temporal Calendar Boundary Firewall Engine.
    V13.3 Production Protocol:
    - Veto new position openings on Monday (00:00 - 23:59 UTC).
    - Veto new position openings on Month-End (last calendar day of month).
    - Veto new position openings on Month-Start (first calendar day of month).
    - Veto new position openings on Sunday for Book 1.
    - Require 7-Day High Breakout conditional trigger for Book 2 on Sunday.
    - Maintain active direct Sunday entries for Books 3, 4, 5, and 6.
    """
    enable_calendar_firewall: bool = True
    veto_monday: bool = True
    veto_month_start: bool = True
    veto_month_end: bool = True
    book1_veto_sunday: bool = True
    book2_require_sunday_high_break: bool = True
    sunday_high_break_window_hours: int = 168

    def __post_init__(self):
        assert self.sunday_high_break_window_hours > 0, "sunday_high_break_window_hours must be positive"


@dataclass(frozen=True)
class V12Config:
    """Master Unified Configuration Dataclass (V13.3 Production)"""
    macro: MacroConfig = field(default_factory=MacroConfig)
    tier: TierConfig = field(default_factory=TierConfig)
    micro: MicrostructureConfig = field(default_factory=MicrostructureConfig)
    entry: EntryConfig = field(default_factory=EntryConfig)
    exit: ExitConfig = field(default_factory=ExitConfig)
    sizing: SizingConfig = field(default_factory=SizingConfig)
    shadow_reclaim: ShadowReclaimConfig = field(default_factory=ShadowReclaimConfig)
    book3_flush: Book3FlushReclaimConfig = field(default_factory=Book3FlushReclaimConfig)
    book4: Book4Config = field(default_factory=Book4Config)
    book5: Book5Config = field(default_factory=Book5Config)
    book1: Book1Config = field(default_factory=Book1Config)
    book6: Book6Config = field(default_factory=Book6Config)
    calendar: CalendarConfig = field(default_factory=CalendarConfig)



