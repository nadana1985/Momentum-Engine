---
name: pre_pump_coil_scanner
description: Instructions and standard procedure for screening the cryptocurrency universe for pre-pump coiled squeeze setups, retest traps, and Bar 0 ignition shocks across the 6 core futures metrics.
---

# Pre-Pump Coiled Squeeze & Ignition Scanner (The 6-Metric Architecture) Skill

This skill teaches the AI agent how to detect and screen for explosive coiled short-squeeze candidates, retest traps, and instantaneous Bar 0 ignition shocks using the deterministic production tool [`scripts/scan_pre_pump_coils.py`](file:///f:/kronos_v1_alt/scripts/scan_pre_pump_coils.py).

---

## 1. When to Use This Skill
Activate this skill whenever the user asks to:
- Scan for tokens that are "ready before the pump" or "coiling at t=0" like OGN did on Oct 7.
- Screen the universe for impending short squeezes, retest short traps, or Bar 0 ignition volume shocks.
- Analyze assets using the 6 Core Futures Metrics: Trade Count, Volume, Taker Buy Flow, Open Interest, Funding Rate, and Whale L/S.
- Check whether a specific asset has the "OGN pre-pump trait" or "CTSI retest trap" or "KAIA ignition shock".

---

## 2. Deterministic Command-Line Execution
Agents must **NEVER** write ad-hoc scanning loops. Always use the canonical tool:

```bash
# 1. Scan the current live universe (outputs separated Tier 1 LEADING and Tier 2 LAGGING tables):
python scripts/scan_pre_pump_coils.py --scan

# 2. Filter exclusively for LEADING candidates (200-EMA Merged & Reclaimed - true OGN/ARPA/BAT flyers):
python scripts/scan_pre_pump_coils.py --scan --tier leading

# 3. Filter exclusively for LAGGING candidates (Below 1D 200-EMA - ERA/WAL counter-trend scalps):
python scripts/scan_pre_pump_coils.py --scan --tier lagging

# 4. Inspect a specific symbol at current tape (e.g. ERA or CTSI):
python scripts/scan_pre_pump_coils.py --symbol ERA
python scripts/scan_pre_pump_coils.py --symbol CTSI

# 5. Historical verification at a specific point-in-time timestamp:
python scripts/scan_pre_pump_coils.py --symbol OGN --as-of "2026-10-07 22:00:00"

# 6. Machine-readable JSON output:
python scripts/scan_pre_pump_coils.py --symbol ERA --json
```

---

## 3. The 6 Core Futures Metrics & The Invariant Laws

Empirically verified across 725 liquid shards and deep forensic audits of OGN, KAIA, CTSI, and US:

1. **Trade Count Velocity (`count / 24h median count`):**
   - The algorithmic canary. In OGN (Oct 8 08:00), trade count exploded 17.4x (6.9k $\rightarrow$ 120k). In KAIA (Oct 9 08:00), it exploded 211x (1.6k $\rightarrow$ 354k).
2. **Total Volume ($) & Volume Shock (`vol_1h / 24h median vol`):**
   - Instantaneous 5x to 25x volume shock confirming institutional participation.
3. **Taker Market Buy Ratio (`taker_buy_quote_volume / quote_volume`):**
   - Measures whether aggressive market orders are absorbing passive sell walls ($\ge 48\% - 50\%$).
4. **Open Interest Dynamics & The Bar 0 Flat-OI Law:**
   - **The Law:** At Bar 0 of an explosive breakout, **Open Interest does NOT expand** (OGN: 85.9M $\rightarrow$ 84.9M; KAIA: 60.3M $\rightarrow$ 60.0M) because existing limit orders are wiped out.
   - Massive OI expansion ($2\times$ to $5\times$) only occurs in **Bar 1 and Bar 2** as trapped counter-trend shorters flood in.
5. **8h Funding Rate (Negative Carry Fuel):**
   - $\le -0.02\%$ to $-0.50\%$ carrying penalty forcing trapped shorts to liquidate.
6. **Whale Long/Short Ratio & Contraction:**
   - Top Trader Whale L/S collapsing ($\Delta L/S < -0.20$ or $L/S \le 1.50$) as large accounts build net short exposure into the shelf.

---

## 4. Multi-Regime Classification Matrix

| Regime Status | Core Indicators | Prototype Asset |
| :--- | :--- | :--- |
| **`PRIME_COIL (PRE_IGNITION_SQUEEZE)`** | $\text{Funding} \le -0.05\%$, $\text{Shelf} \le 25\%$, $\text{Ret}_{24\text{h}} \le +8\%$, $\Delta L/S < 0$ | **`OGN`** (Oct 7) / **`ERA`** (Current) |
| **`ACTIVE_SQUEEZE_SHELF (RETEST TRAP)`** | $\text{Funding} \le -0.10\%$, $\Delta \text{OI}_{24\text{h}} \ge +25\%$, $\text{Turnover} \ge 4\times$, Higher-low shelf | **`CTSI`** (Current $0.0365 shelf) |
| **`BAR_0_IGNITION_SHOCK`** | $\text{Trade Count Velocity} \ge 8\times$, $\text{Vol Shock} \ge 8\times$, $\text{Ret}_{1\text{h}} \ge +4\%$ | **`KAIA`** (Oct 9 08:00) |
| **`COILING (HIGH_PRESSURE)`** | Total Score $\ge 65/100$ | Primary Watchlist |

---

## 5. Empirical Quantile Architecture (The OGN Baseline Invariants)

The scanner operates in pure **Empirical Quantile space**, evaluating each asset's real-time metrics against its historical empirical CDF (up to 8,760 hours / 1 year trailing baseline), calibrated from the deep forensic audit of OGN's 48,385-hour history:

| Metric | OGN Pre-Pump ($t-1$) | OGN Bar 0 Ignition ($t=0$) | OGN Retest Trap ($t+12$) | Empirical Quantile Threshold |
| :--- | :--- | :--- | :--- | :--- |
| **8h Funding Rate** | **P01.8 - P02.5** ($-0.15\%$) | **P02.3** ($-0.10\%$) | **P11.5** ($-0.04\%$) | $\le \text{P05}$ (Bottom 5% Carry Squeeze) |
| **Whale L/S 24h Delta** | **P01.6** ($-0.80$) | **P02.3** ($-0.68$) | **P00.2** ($-1.65$) | $\le \text{P05}$ (Severe Whale Short Dumping) |
| **Whale L/S Ratio** | **P17.6** ($1.92$) | **P21.4** ($1.99$) | **P00.05** ($0.45$) | $\le \text{P01}$ (Whale Crowded Short Trap) |
| **Trade Count Velocity** | **P66.9** ($1.16\times$) | **P99.70** ($18.9\times$) 🚀 | **P96.5** ($3.57\times$) | $\ge \text{P95}$ (Top 5% Algorithmic Canary) |
| **Volume Shock** | **P80.5** ($1.62\times$) | **P99.72** ($37.8\times$) 🚀 | **P92.9** ($3.13\times$) | $\ge \text{P95}$ (Top 5% Institutional Shock) |
| **Taker Buy Ratio** | **P94.4** ($59.6\%$) | **P61.5** ($50.4\%$) | **P60.9** ($51.7\%$) | $\ge \text{P85}$ (Stealth Aggressive Absorption) |
| **24h Delta OI %** | **P85.6 - P91.4** ($+7.2\%$) | **P88.3** ($+8.8\%$) | **P99.95** ($+879\%$) 💣 | $\ge \text{P90}$ (Institutional Short Piling) |

---

## 6. Empirical Quantile Scoring Rubric (0 to 100 Points)

* **Funding Carry Penalty (Max 30 pts):**  
  $\le \text{P01}$ OR raw $\le -0.50\%$ (30 pts) \| $\le \text{P03}$ OR raw $\le -0.20\%$ (25 pts) \| $\le \text{P05}$ OR raw $\le -0.05\%$ (20 pts) \| $\le \text{P15}$ OR raw $< 0.0\%$ (12 pts)
* **Shelf & Support Structure (Max 20 pts):**  
  $\le \text{P15}$ OR raw $\le 10\%$ (20 pts) \| $\le \text{P30}$ OR raw $\le 18\%$ (16 pts) \| raw $\le 26\%$ (12 pts) \| Retest shelf with trapped shorts $\le 48\%$ + $\text{Funding} \le \text{P05}$ (10 pts)
* **Whale Short Trap (Max 20 pts):**  
  Whale L/S $\le \text{P01}$ or $< 0.85$ (12 pts) \| $\le \text{P05}$ or $< 1.50$ (8 pts) \| $\le \text{P20}$ or $< 2.00$ (4 pts) + Falling delta ($\le \text{P02}$: +8 pts, $\le \text{P05}$: +5 pts, $< 0$: +3 pts)
* **Flow & Canary Ignition (Max 15 pts):**  
  Trade count OR volume shock $\ge \text{P99}$ (15 pts) \| $\ge \text{P95}$ (12 pts) \| $\ge \text{P85}$ or turnover $\ge 5\times$ (8 pts) \| Taker buy ratio $\ge \text{P85}$ (5 pts)
* **Open Interest Expansion & Liquidity (Max 15 pts):**  
  24h $\Delta \text{OI} \ge \text{P98}$ (8 pts) \| $\ge \text{P85}$ (5 pts) \| Bar 0 Flat-OI Anomaly (7 pts) \| Liquid asset bonus $\ge \$1\text{M}$ OI (7 pts)

---

## 7. Full Lifecycle Evaluation: Entry vs. Mid-Run Hold vs. Climax Exit

For the complete hour-by-hour forensic table of `OGN/USDT` (Oct 5 – Oct 10, 2026), always consult [`references/OGN_LIFECYCLE_ENTRY_EXIT_REFERENCE.md`](file:///f:/kronos_v1_alt/.agents/skills/pre_pump_coil_scanner/references/OGN_LIFECYCLE_ENTRY_EXIT_REFERENCE.md).

### A. How to Distinguish a Mid-Run Shakeout Dip (HOLD / ADD) from a Climax Top (EXIT)
| Diagnostic Dimension | Mid-Run Shakeout (`OGN Oct 8 15:00` @ \$0.0388) $\rightarrow$ **HOLD / ADD** | Climax Peak (`OGN Oct 8 20:00–21:00` @ \$0.0536) $\rightarrow$ **FULL EXIT** |
| :--- | :--- | :--- |
| **Candle Upper Wick** | Moderate ($35\% - 46\%$) | **Extreme Pinbar Rejection ($80\% - 85\%$)** 🚨 |
| **Token Open Interest** | **Expanding to New Highs** ($398\text{M} \rightarrow 456.5\text{M}$) | **Lower High Divergence** ($433\text{M}$) $\rightarrow$ **$-38\%$ Unwind** 🚨 |
| **Whale L/S Trajectory** | **Still Falling Sharply** ($0.59 \rightarrow 0.52$, shorts adding) | **Bottoms ($0.42$) and Turns UP** ($0.42 \rightarrow 0.82$, shorts covering) 🚨 |
| **8h Funding Rate** | **Extreme Negative Carry** ($-0.893\% \rightarrow -0.400\%$) | **Collapses 10x Toward Zero** ($-0.037\% \rightarrow -0.019\%$) 🚨 |
| **Volume vs. Prior Wave** | Sustained ($48\times - 71\times$ median) | **$-62\%$ Bearish Divergence** ($3.1\times \rightarrow 0.9\times$ median) 🚨 |

### B. The 6 Quantitative Climax Exit Alarms (Trigger Full Exit when $\ge 3$ Fire on an Extended Runner)
1. **85% Climax Pinbar Wick:** Upper wick $\ge 75\%$ at a new cycle high (`OGN` printed 85% at \$0.0536 and 80% on the \$0.0495 retest).
2. **Bearish Volume & Trade Count Divergence:** Higher price high on $\ge 50\%$ lower 1h volume than Wave 1 (`OGN` dropped -62%: \$116.5M $\rightarrow$ \$44.2M).
3. **Token OI Bearish Divergence:** Higher price high while Token OI fails to beat its prior peak (`456.5M` $\rightarrow$ `433.0M`).
4. **10x Funding Rate Collapse:** Extreme negative funding ($\le -0.40\%$) suddenly snaps near zero ($\ge -0.04\%$) at the top (`-0.400%` $\rightarrow$ `-0.037%`).
5. **Taker Buy Breakdown ($< 49.5\%$) + Sub-1.2x Volume Collapse** on the immediate follow-through bar.
6. **Whale L/S Floor Inflection:** Whale L/S stops falling, bottoms ($0.42$), and rises while Token OI bleeds and price drops (whales covering profitable top-shorts).

