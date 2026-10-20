---
name: best_sr_strategy
description: Instructions and standard procedure for calculating the institutional Support & Resistance Strategy (சிறந்த உத்தி) combining Price Action, Volume Profile, Open Interest (OI) dynamics, Top Trader Whale Long/Short ratio, and liquidation flush absorption.
---

# Institutional Support & Resistance Strategy (சிறந்த உத்தி) Skill

This skill teaches the AI agent how to extract and calculate institutional Support and Resistance levels and tactical execution blueprints ("சிறந்த உத்தி") for any cryptocurrency token across historical windows (e.g. 90-day / 3-month) using the deterministic tool [`scripts/calculate_best_sr_strategy.py`](file:///f:/kronos_v1_alt/scripts/calculate_best_sr_strategy.py).

---

## 1. When to Use This Skill
Activate this skill whenever the user asks to:
- Find the Support and Resistance of an asset (e.g. "EIGEN support resistance", "SOL S/R", etc.).
- Calculate the "சிறந்த உத்தி" (Best Strategy) for any given symbol.
- Analyze Open Interest (OI) and Whale Long/Short (Top Trader L/S) positioning alongside Price Action.
- Identify trapped supply overhead or liquidation flush absorption floors.
- Formulate a tactical trade blueprint (optimal entry zone, strict stop-loss invalidation, take-profit targets).

---

## 2. Deterministic Command-Line Execution
Agents must **NEVER** run ad-hoc multi-file loops or heuristic scripts. Use the verified production tool:

```bash
# 1. Standard 90-day (3-month) institutional tear-sheet
python scripts/calculate_best_sr_strategy.py --symbol <ASSET>

# 2. Custom lookback duration (e.g., 30 days, 60 days, 180 days)
python scripts/calculate_best_sr_strategy.py --symbol <ASSET> --days 30

# 3. Machine-readable JSON output for programmatic integration
python scripts/calculate_best_sr_strategy.py --symbol <ASSET> --json
```

---

## 3. Core Quantitative Methodology

### A. The Positioning-Price Duality
- **Pure Price Action Fallacy:** Traditional chartist lines (trendlines, double bottoms) ignore derivative leverage and are routinely hunted by institutional algorithms for liquidity.
- **Pure Derivatives Fallacy:** Open Interest and Long/Short ratios lack price units and cannot provide numerical support/resistance coordinates by themselves.
- **The Synthesis:** Volume Profile determines the **"WHERE"** (Point of Control POC, Value Area VAH/VAL, High Volume Shelves), while Open Interest + Top Trader L/S define the **"WHO & WHY"** (Who is trapped? Is this shelf an accumulation floor or a fragile exit wall?).

### B. Support Tiers (S1, S2, S3)
1. **S1 (Immediate Absorption Floor):**
   - Anchored to recent high-volume liquidation flush wicks ($\text{Vol} > 2.5\times$, $\Delta \text{OI} < 0$) where leveraged longs were wiped out and passive limit orders absorbed the selling.
   - Or the primary high-volume profile shelf immediately below current price.
2. **S2 (Major Structural Base):**
   - The heaviest multi-week volume consolidation shelf located in the lower 50% of the cyclical range (e.g. breakout launchpad).
3. **S3 (Macro Cycle Low):**
   - Absolute cyclical low across the lookback window (macro accumulation base / structural invalidation).

### C. Resistance Tiers (R1, R2, R3)
1. **R1 (Primary Trapped Supply Ceiling):**
   - Point of Control (POC) or the largest volume acceptance shelf above current price. When price trades below POC, traders who accumulated there are underwater, creating intense exit-supply friction on relief rallies.
2. **R2 (Exhaustion / Distribution Shelf):**
   - High-volume swing-high or double-top rejection where Whale L/S previously reached euphoria levels.
3. **R3 (Macro Cycle High):**
   - Absolute cyclical peak across the lookback window (climax exhaustion).

### D. Whale Positioning Matrix
- **$\text{Whale L/S} < 0.85$ (Whale Short Trap):** Institutional accounts are net short into high volume. If the S1/S2 shelf holds, a violent parabolic short squeeze is likely.
- **$\text{Whale L/S} > 2.20$ (Crowded Long Fragility):** Retail and institutional participants are heavily leveraged long. Elevated risk of cascade liquidations and air-pocket crashes on minor dips.
- **$0.85 \le \text{Whale L/S} \le 2.20$ (Balanced):** Organic trend distribution.

### E. Multi-Timeframe 200-EMA Convergence (`LEADING` vs. `LAGGING` Tier) & Macro Breakdown Magnets (`[M1]` / `[M2]`)
- **`LEADING` Tier (`200EMA_MERGED_ABOVE`):** `price_vs_ema200_1d_pct >= -3.0%` AND `ema_1h_vs_1d_gap_pct >= -15.0%`. All three `200 EMAs` (`1h`, `4h`, `1D`) have converged and price has reclaimed the Daily `200 EMA` (`OGN`, `MAGIC`, `GTC`, `CTSI`, `ARPA`, `BAT`, `LUMIA`). Unlocks open-sky parabolic expansion toward the **Sep 2025 Breakdown Low (`[M2]`)**.
- **`LAGGING` Tier (`SUB_1D_200EMA_LAGGING`):** `price_vs_ema200_1d_pct < -3.0%` OR `ema_1h_vs_1d_gap_pct < -15.0%`. Price is trapped below a descending `1D EMA 200` (`ERA`, `WAL`). Treat as a counter-trend scalp capped at the `1D 200 SMA / 1D 200 EMA` overhead wall.
- **Two-Stage Macro Breakdown Low Magnets:**
  - **`[M1] Nov 2025 Breakdown Low`:** Stage-1 structural gateway and post-climax support flip (`OGN` \$0.0325, `MAGIC` \$0.1000).
  - **`[M2] Sep 2025 Breakdown Low`:** Terminal blow-off target where multi-day short squeezes exhaust (`OGN` \$0.0538 vs \$0.0536 actual top; `MAGIC` \$0.1422 vs \$0.1442 actual top; `GTC` \$0.2586 vs \$0.2614 actual top).

---

## 4. Standard Response Format
When presenting the analysis to the user, include:
1. **Market Snapshot & 200-EMA Tier:** 90D High, 90D Low, Current Price, POC, OI, Whale L/S, Funding Rate, and `LEADING` vs. `LAGGING` 200-EMA Convergence status.
2. **Recent Liquidation Flush Alert:** If detected in the past 48 hours, mention the wick low, volume shock, and OI purge.
3. **Structured S/R Table (including `[M1] Nov 2025` & `[M2] Sep 2025` Breakdown Lows):** S1, S2, S3, R1, R2, R3, M1, M2 with prices and volume/microstructure rationale.
4. **Visual ASCII Ladder:** Clear price hierarchy diagram showing the asset's position relative to POC, 1D 200 EMA, and shelves.
5. **Tactical Blueprint (செயல் உத்தி):** Recommended Entry/Buy Zone, Strict Invalidation Stop-Loss, and Take-Profit Targets.

