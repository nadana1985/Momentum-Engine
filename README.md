# Kronos V15.0: Master Unified Production Architecture

> **Institutional-grade, causal quantitative momentum and microstructure trading engine for cryptocurrency perpetual futures.**

[![Version](https://img.shields.io/badge/Release-V15.0_Canonical-green.svg)](V15_0_PRODUCTION_RELEASE_NOTES.md)
[![Verification](https://img.shields.io/badge/Cold_Build-Rule_3_Certified-blue.svg)](v15_standalone/run_v15_0_fresh_build.py)
[![Heuristics](https://img.shields.io/badge/Microstructure-Rule_7_Studentized-purple.svg)](.agents/AGENTS.md)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](#)

---

## 1. Executive Summary & Production Performance

**Kronos V15.0** is the canonical production release of the Altcoin Momentum Engine, deployed across all **652 liquid perpetual shards** on Binance Futures. 

It synthesizes the **Rule 7 Dynamic Studentized Microstructure Governor** (Study S-CD), the **Asymmetric Capitalization Exit Law with Macro Convexity Preservation** (Study S-CI), and the **Two-Tranche Micro-Harvesting Engine for Micro-Caps (Book 7 MSSR)** into a unified, zero-lookahead, multi-book execution stack.

### Verified Full Universe Metrics (3,109 Closed Trades)
*All metrics verified via ground-up cold simulation (`run_v15_0_fresh_build.py`) with zero cached tape dependencies.*

| Performance Metric | Institutional Result |
| :--- | :--- |
| **Cumulative Net Log Return** | **`+4,043.1%`** ($3.62 \times 10^{17}\times$ Capital Multiple) |
| **Log Profit Factor** | **`1.449`** |
| **Win Rate** | **`51.85%`** (1,612 Wins / 1,497 Losses) |
| **Total Universe Breadth** | **652 Shards** (Tier 1: 63, Tier 2: 192, Tier 3: 397) |
| **Zero Lookahead Guarantee** | 100% Truncation Invariant down to $10^{-16}$ precision |

---

## 2. Multi-Book Architecture Breakdown

Kronos V15.0 operates 6 specialized, non-overlapping books orchestrated across asset tiers:

| Book | Strategy Archetype | Methodology | Target Tier | Net Log | Log PF | Win Rate |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| **Book 1** | **Continuation Breakout** | 3-Bar structural acceptance ($t = +1, +2, +3$), calibrated $+5.0\%$ target cap, and $-0.5\%$ cushion ratchet | Tier 1 & 2 | **+384.0%** | **1.882** | 37.88% |
| **Book 2** | **Coiled Squeeze** | 72h compression shelves ($\le 25\%$), Sunday high break confirmation trigger | Tier 1, 2, 3 | **+1,186.0%** | **2.053** | 39.41% |
| **Book 3** | **Shelf Absorption** | Passive limit bids into high-volume liquidity shelves during macro pullbacks | Tier 1 & 3 | **+1,297.3%** | **1.227** | 57.68% |
| **Book 4** | **Two-Tranche Reclaim** | 200d EMA reclaim with causal 23:00 UTC day close ($C_{23:00} \ge P_{\text{NB\_High}}$) + Toxic Long Firewall | Tier 1 (Macro) | **+779.9%** | **2.086** | 41.59% |
| **Book 6** | **3-SARE Orderflow Reclaim** | CUSUM-Anchored orderflow basis ($\text{AVWAP}_\tau$) across 30d accumulation bases with staged limit absorption | Tier 1 & 2 | **+351.7%** | **1.431** | 38.79% |
| **Book 7** | **MSSR Micro-Harvesting** | Two-Tranche Micro-Harvesting (+3% Tranche A / +3% BE ratchet / `MICRO_STALL` alert) + Negative Carry Gate | Tier 3 (Micro) | **+44.2%** | **1.218** | **82.71%** |

### Capitalization Tier Performance Attribution
* **Tier 1 (Deep Large-Caps / 63 Shards):** 591 trades | **+1,825.6% Net Log** | Log PF: **1.959** | Win Rate: **49.1%**
* **Tier 2 (Liquid Mid-Caps / 192 Shards):** 601 trades | **+902.4% Net Log** | Log PF: **1.693** | Win Rate: **37.8%**
* **Tier 3 (Micro-Caps / 397 Shards):** 1,917 trades | **+1,315.1% Net Log** | Log PF: **1.227** | Win Rate: **57.1%**

---

## 3. Core Quantitative Discoveries & Invariants

1. **The Dynamic Heuristic Microstructure Law (Rule 7 Certified):**
   Arbitrary static constants (e.g. `funding < -15%`, `L/S >= 2.80`) are permanently banned. Microstructure is evaluated using rolling 30-day studentized Z-scores ($z_{LS}, z_{\text{funding}}, z_{\text{OI}}$). Vetoing entries where retail is crowded long against trapped whales ($pct_{LS} \ge 80\% \land z_{LS} \ge 0.80\sigma$) eliminates 140 toxic fakeouts, protecting +337.5% in net alpha.
2. **The Asymmetric Capitalization Exit Law (Study S-CI):**
   Large-cap monster trends (`SOL`, `1000PEPE`, `AVAX`, `XLM`) require unconstrained 72h Donchian floor trails (`low_72h`) to capture fat-tail power laws (+738.7% MFE). Premature climax exits cut large-cap alpha by -338.2%. Conversely, micro-caps suffer from sudden liquidity evaporation and require immediate Micro-Harvesting (+3% Tranche A / +3% BE ratchet) which converts negative drag into an 82.71% win rate.
3. **The Clean-Room Truncation Invariance Invariant (Rule 4 Certified):**
   Every entry, stop-loss, and target calculated at timestamp $T$ produces identical values down to 16 decimal places when the dataset is sliced at $T$ (`df.loc[:T]`). Zero lookahead bias exists in the engine.

---

## 4. Quick Start & Execution

### Prerequisites
- Python 3.10+ (Recommended: Python 3.11)
- Install requirements:
  ```bash
  pip install -r requirements.txt
  ```

### 1. Run Cold Verification Build (Rule 3 Certified)
To regenerate the canonical production tape from raw candlestick shards with live mark-to-market accounting:
```powershell
# PowerShell
.\pipeline_v15.ps1
```
Or execute directly via Python:
```bash
python v15_standalone/run_v15_0_fresh_build.py
```
*Output Tape: `data/canonical/canonical_v15_0_tape.parquet` (3,109 closed trades).*

### 2. Launch the Interactive NiceGUI Dashboard
Monitor active trades, historical performance curves, trade logs, and live telemetry:
```bash
python v15_standalone/momentum_v15/dashboard_nicegui.py
```
*Dashboard opens at `http://localhost:8080`.*

### 3. Run Live Climax & Micro-Stall Tactical Scanners
Screen active market runners for climax exhaustion or micro-stall alerts:
```bash
python scripts/scan_climax_exits.py
python scripts/alert_climax_scanner.py
```

---

## 5. Repository Directory Layout

```text
├── .agents/                        # Sovereign pipeline rules (AGENTS.md) and agent knowledge
├── data/
│   └── canonical/                  # Canonical V15.0 production tape (CSV + Parquet)
├── docs/
│   └── legacy/                     # Archived V12 architecture specifications & verification logs
├── scripts/                        # Production scanners (Climax Exits, Tactical Alerting, Scanners)
├── tests/                          # Production unit tests and regression test suites
├── v15_standalone/                 # CANONICAL V15.0 PRODUCTION SUITE
│   ├── build_v15_tape.py           # Ground-up production tape builder with live MTM
│   ├── run_v15_0_fresh_build.py    # Zero-cache cold verification harness
│   └── momentum_v15/               # Sovereign V15.0 Engine Package
│       ├── config.py               # Studentized heuristics, Toxic Long Firewall, Book 7 configs
│       ├── engine_v12.py           # Core execution kernel (Books 1, 2, 3, 4, 6, 7)
│       ├── features_v12.py         # Causal indicator calculations & studentized Z-scores
│       ├── dashboard_nicegui.py    # Interactive production telemetry dashboard
│       └── tier_classifier.py     # Asset capitalization tiering (T1 / T2 / T3)
├── pipeline_v15.ps1                # Master production orchestration pipeline
├── V15_0_PRODUCTION_RELEASE_NOTES.md # Detailed V15.0 quantitative release notes
└── README.md                       # Repository master manual (this document)
```

---

## 6. Sovereign Pipeline Rules of Engagement

All contributors, researchers, and AI agents operating on this codebase must strictly adhere to the Sovereign Rules defined in [`.agents/AGENTS.md`](.agents/AGENTS.md):
1. **Rule 1 (Single-Kernel Iron Law):** Never write custom shard loops. All logic must reside causally inside the engine kernel.
2. **Rule 2 (Anti-Chaining Rule):** Downstream studies must simulate the entire universe from raw shards through the engine. No static CSV propagation.
3. **Rule 3 (Cold Ground-Up Verification Gate):** Every candidate promotion must be verified via cold ground-up tape generation with zero cached files.
4. **Rule 4 (Truncation Invariance):** Signals at timestamp $T$ must trigger with identical prices and stops when future data is truncated.
5. **Rule 7 (Dynamic Heuristic Law):** Zero arbitrary static constants. All volatility, orderflow, funding, and positioning thresholds must be studentized.
