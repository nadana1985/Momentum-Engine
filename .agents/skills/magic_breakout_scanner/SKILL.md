---
name: magic_breakout_scanner
description: Instructions and standard procedure for screening the cryptocurrency universe for MAGIC-type organic volume shock breakouts, post-breakout consolidation flags, and mid-run whale counter-short supernova metamorphoses across the 6 core futures metrics.
---

# MAGIC-Type Supernova & Organic Breakout Scanner Skill

This skill teaches the AI agent how to detect, analyze, and screen for **MAGIC-type organic breakouts** and **mid-run whale counter-short supernova metamorphoses** using the deterministic production tool [`scripts/scan_magic_breakouts.py`](file:///f:/kronos_v1_alt/scripts/scan_magic_breakouts.py) (alias [`scripts/scan_magic_type.py`](file:///f:/kronos_v1_alt/scripts/scan_magic_type.py)).

---

## 1. When to Use This Skill
Activate this skill whenever the user asks to:
- Find "the next MAGIC" or check if an asset has the "MAGIC type" breakout DNA (e.g., `C98`, `STRK`, `BAT`, `S`).
- Screen the universe for Book 1 organic volume breakouts that are transforming into short squeezes as whales attempt to top-short the rally.
- Contrast an organic volume-shock breakout against a pre-pump negative-funding coil (`OGN` / `CTSI` / `ERA`).
- Evaluate whether whales are fading/counter-shorting an active uptrend ($\Delta L/S \le -0.30$, $\Delta \text{OI} \ge +30\%$).

---

## 2. Deterministic Command-Line Execution
Agents must **NEVER** write ad-hoc scanning loops. Always use the canonical tool:

```bash
# 1. Scan the entire liquid universe for MAGIC-type setups (separated into LEADING & LAGGING tiers):
python scripts/scan_magic_breakouts.py --scan

# 2. Filter exclusively for LEADING candidates (200-EMA Merged & Reclaimed - true MAGIC/C98/LUMIA flyers):
python scripts/scan_magic_breakouts.py --scan --tier leading

# 3. Filter exclusively for LAGGING candidates (Below 1D 200-EMA - counter-trend scalps):
python scripts/scan_magic_breakouts.py --scan --tier lagging

# 4. Inspect a specific symbol at current tape (e.g. MAGIC, C98, ORDI):
python scripts/scan_magic_breakouts.py --symbol MAGIC
python scripts/scan_magic_breakouts.py --symbol C98

# 5. Historical verification at a specific point-in-time timestamp (e.g. MAGIC Stage 1 Ignition):
python scripts/scan_magic_breakouts.py --symbol MAGIC --as-of "2026-10-09 06:00:00"

# 6. Machine-readable JSON output:
python scripts/scan_magic_breakouts.py --symbol C98 --json
```

---

## 3. The 3-Stage MAGIC Metamorphosis Lifecycle

Unlike `OGN` or `CTSI` (which begin with deep negative funding at the bottom of a compressed range), **MAGIC-type runners begin as pure Book 1 Organic Breakouts with normal positive funding (+0.005% to +0.010%) and transform into short squeezes mid-flight**:

1. **Stage 1: Organic Launchpad Ignition (`STAGE_1_BREAKOUT`):**
   - **Trigger:** Violent Bar 0 institutional volume shock ($\ge 5\times - 25\times$ median, $\ge \text{P95}$) and trade count canary explosion ($\ge 5\times - 15\times$ median, $\ge \text{P95}$).
   - **Funding:** Normal baseline positive carry ($+0.0050\%$ to $+0.0100\%$).
   - **Bar 0 Flat-OI Law:** Open Interest remains flat on Bar 0 ($-5\%$ to $+5\%$) as aggressive market buys wipe out resting sell walls (`MAGIC` Oct 9 06:00: Vol jumped 20.5x to \$4.24M while OI stayed flat at \$3.91M).
2. **Stage 2: High-Shelf Consolidation Flag (`CONSOLIDATION_FLAG`):**
   - Price coils tightly ($72\text{h range} \le 22\%$) above the breakout level while turnover velocity remains elevated ($\ge 2.0\times - 3.0\times$).
   - Top Trader Whales begin fading the rally, causing $L/S$ to drop ($\Delta L/S \le -0.20$) while Open Interest climbs $+25\%$ to $+65\%$.
3. **Stage 3: Supernova Squeeze Metamorphosis (`SUPERNOVA_ACTIVE`):**
   - Whales aggressively attempt to top-short the breakout ($L/S$ collapses from $\sim 2.0$ down to $< 1.00$; `MAGIC` hit **0.63** / 61.4% net short!).
   - Trapped counter-trend shorts fuel a $2\times$ to $4\times$ Open Interest explosion (`MAGIC` OI surged **+344.9%** from \$3.9M to \$17.81M).
   - Turnover velocity crosses $5\times$ to $20\times$, propelling price $+100\%$ to $+150\%$ higher.

---

## 4. Multi-Regime Classification Matrix

| Regime Status | Score | Core Quantitative Criteria | Prototype Benchmark |
| :--- | :--- | :--- | :--- |
| **`SUPERNOVA_ACTIVE`** | **$\ge 75/100$** | $\text{Turnover} \ge 5\times$, $L/S \le 1.00$ ($\Delta L/S \le \text{P02}$), $\Delta \text{OI}_{24\text{h}} \ge +50\%$ | **`MAGIC`** (Oct 9 18:00 – Oct 10 01:00) |
| **`STAGE_1_BREAKOUT`** | **$60 - 74/100$** | $\text{Vol/Trade Shock} \ge \text{P95}$, $\text{Ret}_{24\text{h}} \in [+10\%, +40\%]$, $\Delta L/S \le \text{P05}$, $\Delta \text{OI} \ge +25\%$ | **`MAGIC`** (Oct 9 06:00) / **`C98`** (Current) |
| **`CONSOLIDATION_FLAG`** | **$48 - 59/100$** | $\text{Shelf} \le 22\%$, $\text{Ret}_{24\text{h}} \ge +8\%$, $\text{Turnover} \ge 1.8\times$ | **`MAGIC`** (Oct 9 08:00 – 13:00) |
| **`DEVELOPING_MOMENTUM`** | **$48 - 59/100$** | Active flow expansion with wider range structure | Secondary Watchlist |
| **`NOT_READY`** | **$< 35/100$** | Low volume velocity ($< 1.5\times$), stagnant OI, seller-dominated tape | **`ORDI`** (Current) |

---

## 5. Empirical Quantile Benchmark: The MAGIC Forensic Trajectory

Calibrated from `MAGIC/USDT`'s 8,760-hour empirical baseline across its October 9–10 supernova lifecycle:

| Metric | Pre-Pump Baseline (Oct 8) | Stage 1 Ignition (Oct 9 06:00) | Mid-Shelf Flag (Oct 9 10:00) | Stage 2 Supernova (Oct 10 01:00) |
| :--- | :--- | :--- | :--- | :--- |
| **Price ($)** | \$0.0645 | **\$0.0763** (+15.1% 1h) | **\$0.0782** (+21% shelf) | **\$0.1403** (+107.4% 24h) |
| **Trade Count (1h)** | 4,660 (1.0x) | **54,320 (10.2x / P99.1)** 🚀 | 56,340 (6.5x / P98.2) | **359,177 (P94.0 of surged tape)** |
| **Volume 1h ($)** | \$186k (1.0x) | **\$4.24M (20.5x / P99.3)** 🚀 | \$3.75M (5.8x / P97.5) | **\$30.94M (\$365.9M 24h Vol)** |
| **Turnover Velocity** | 1.15x | **2.73x** | **4.10x** | **20.55x** 🔥 |
| **Whale L/S Ratio** | 1.92 (65.8% Long) | **2.02** ($\Delta: +0.13$) | **1.53** ($\Delta: -0.37$ / P03.1) | **0.63** ($\Delta: -1.23$ / **P00.0**) 💣 |
| **Open Interest ($)** | \$4.00M | **\$3.91M** (+0.5% Flat Bar 0) | **\$6.66M** (+68.2% / P99.1) | **\$17.81M** (+344.9% / **P100.0**) |
| **8h Funding Rate** | +0.0050% | **+0.0050%** (Organic Carry) | +0.0050% | -0.0090% $\rightarrow$ +0.0016% |

---

## 6. Scoring Rubric (0 to 100 Points)

1. **Flow & Algorithmic Canary Shock (Max 25 pts):**
   - Trade Count Velocity $\ge \text{P99}$ or $\ge 8\times$ (15 pts) \| $\ge \text{P95}$ or $\ge 4\times$ (10 pts) \| $\ge \text{P85}$ or $\ge 2\times$ (6 pts)
   - Volume Shock $\ge \text{P99}$ or $\ge 8\times$ (10 pts) \| $\ge \text{P95}$ or $\ge 4\times$ (7 pts) \| $\ge \text{P85}$ or $\ge 2\times$ (4 pts)
2. **Momentum Acceleration & Turnover Velocity (Max 25 pts):**
   - 24h Turnover Velocity $\ge 5.0\times$ (12 pts) \| $\ge 3.0\times$ (9 pts) \| $\ge 1.8\times$ (6 pts) \| $\ge 1.0\times$ (3 pts)
   - 24h Price Return $\in [+10\%, +40\%]$ [Sweet-Spot Launchpad] (13 pts) \| $(+40\%, +120\%]$ [Supernova] (10 pts) \| $[+5\%, +10\%)$ (7 pts)
3. **Whale Counter-Short Trap & Fading Dynamics (Max 25 pts):**
   - 24h $\Delta \text{Whale L/S} \le \text{P02}$ or $\le -0.40$ (15 pts) \| $\le \text{P05}$ or $\le -0.20$ (10 pts) \| $\le -0.10$ (5 pts)
   - Absolute Whale L/S $\le 1.00$ [Whales Net-Short] (10 pts) \| $\le 1.40$ (7 pts) \| $\le 1.80$ (4 pts)
4. **Open Interest Fuel & Carrier Flow (Max 25 pts):**
   - 24h $\Delta \text{OI} \ge +50\%$ (12 pts) \| $\ge +25\%$ (9 pts) \| $\ge +10\%$ (6 pts) \| Bar 0 Flat-OI Anomaly ($[-5\%, +5\%]$ with Vol Shock $\ge 5\times$) (7 pts)
   - Taker Buy Ratio $\ge 52\%$ (8 pts) \| $\ge 48\%$ (5 pts)
   - Institutional Liquidity Bonus: $\text{OI} \ge \$2.0\text{M}$ (5 pts) \| $\ge \$1.0\text{M}$ (3 pts)

---

## 7. Architectural Contrast: OGN/CTSI Type vs. MAGIC/C98 Type

| Feature | Book 2 Coiled Squeeze (`scan_pre_pump_coils.py`) | Book 1 $\rightarrow$ Supernova (`scan_magic_breakouts.py`) |
| :--- | :--- | :--- |
| **Prototype Assets** | `OGN`, `CTSI`, `ERA` | `MAGIC`, `C98`, `STRK` |
| **Starting Funding Rate** | Deeply Negative ($\le -0.05\%$ to $-0.58\%$) | Normal / Positive ($+0.005\%$ to $+0.010\%$) |
| **Where Shorts Enter** | At the bottom / floor before the pump | **Into the rally** (whales trying to fade/top-short the breakout) |
| **Primary Ignition Signal** | Extreme negative carry + tight 72h compression | **P95–P99 Volume & Trade Count Shock + Turnover Velocity $\ge 3\times$** |
