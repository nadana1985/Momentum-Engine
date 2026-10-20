# Kronos Quantitative Knowledge Base & Migration Architecture (KNOWLEDGE.md)
## Sovereign Pipeline Protocol, Version Promotion SOP & Zero-Reversion Invariants

* **Version:** Canonical Production V13.3 (Master Unified Multi-Book Production Architecture + Temporal Calendar Firewall)
* **Scope:** All Autonomous Agents, Quantitative Engineers, Pipeline Scripts, and Dashboard Services
* **Mandate:** Zero-Reversion Guarantee — Clean-room discoveries MUST natively propagate through the pipeline without static band-aids or cache desynchronization.

---

## 1. Executive Context & The Post-Mortem (Why This File Exists)

### The Failure Modes Observed & Solved:
1. **The Static File-Copy Fallacy:**
   When Study S-BC/S-BD (V12.7) and Study S-BE (V12.8) were proven in the clean room, an agent copied the output CSV into `v12_standalone/data/all_tapes/v12_production/master_raw_tape.csv`.
2. **The Immediate Reversion on Next Pipeline Run:**
   When pipeline scripts executed `build_v12_tape.py`, if it pointed to an outdated matrix, it regenerated older trades directly from raw shards, overwriting production files.
3. **The Two-Tranche Shadowing Bug (V12.11 Post-Mortem):**
   In `v12_standalone/momentum_v12/engine_v12.py`, Book 4 target logic at lines 341–344 previously had a legacy single-tranche target cut (`exit_triggered = True; exit_reason = 'target_reclaim'`). This blocked execution from reaching line 412 (the Two-Tranche S-BE engine), prematurely terminating macro runners like `SUSDT` (`S`) at +15% instead of locking 50% in Tranche A and trailing 50% in Tranche B. **Lines 341–344 have been purged, permanently activating the unshadowed Two-Tranche engine.**
4. **V13.2 Synthesis (Book 6 3-SARE Integration):**
   Integrated Book 6 (3-Stage Asymmetric Reclaim Engine) natively into `engine_v12.py`, `features_v12.py`, and `build_v12_tape.py`, capturing orderflow accumulation breakout reclaims at $\text{AVWAP}_\tau$ across 30-day cyclical bases with 50% resting limit absorption and volume liquidation bailout.
5. **V13.3 Promotion (Temporal Calendar Boundary Firewall - Study S-BV & S-BX):**
   Natively integrates `CalendarConfig` into `engine_v12.py` and `build_v12_tape.py`. Eliminates opening new positions on Monday, Month-End, and Month-Start across all books, and Book 1 on Sunday. Converts Book 2 Sunday setups to 7-Day High Breakout conditional triggers while preserving high-WR Sunday absorption entries for Books 3, 4, 5, and 6. Elevates Master Portfolio Win Rate to **`64.85%`** (from 62.69%) and surges Log Profit Factor to **`2.707`** (from 2.458) across 3,937 closed trades.

### Immutable Iron Law:
> **Never apply static file-copy patches to production tape directories.**
> **The sovereign pipeline runner (`pipeline_v12_11.ps1` / `build_v12_tape.py`) MUST be the native generator of the canonical production tape from the ground up, with live forward mark-to-market evaluation on active open positions.**

---

## 2. Sovereign Pipeline Runner Architecture (`pipeline_v12_11.ps1`)

The production pipeline is unified into the root executable:
`f:\kronos_v1_alt\pipeline_v12_11.ps1`

```powershell
# Standard execution (uses cached 1h shards up to latest snapshot, exports to v13_production):
.\pipeline_v12_11.ps1

# Full live ingestion execution (fetches newest candles from Binance Futures first):
.\pipeline_v12_11.ps1 -Ingest

# Custom output tape directory:
.\pipeline_v12_11.ps1 -TapeDir "data/all_tapes/my_custom_run"
```

### 3-Step Execution Pipeline:
1. **Step [1/3] Master Runner (`build_v12_tape.py`):** Loads canonical V13.2 tape (`canonical_v13_2_tape.parquet`), performs live forward mark-to-market on active positions (`is_open == True`), automatically scans rolling 168h candles to append fresh candidate setups/vetoes to the Flight Recorder (`veto_telemetry.parquet`), and mirrors telemetry to both `telemetry/` and tape directories.
2. **Step [2/3] Strict Compounding Splitter (`build_csv.py`):** Partitions `trades.parquet`, `open_trades.parquet`, `closed_trades.parquet`, and precomputes 551 individual symbol scorecards in strict log-return space.
3. **Step [3/3] Executive Artifacts (`generate_artifacts.py`):** Publishes all Markdown tear sheets and open ledgers (`v13_production_tear_tape.md`, `v13_production_open_trades.md`).

---

## 3. Mandatory 6-Step SOP for Version Promotions

Whenever research verifies a new breakthrough that passes all 6 SPEC Acceptance Gates, the agent MUST execute the following 6 steps in strict sequential order. **DO NOT SKIP ANY STEP.**

### Step 1: Clean-Room Quantitative Verification
* Verify all 6 SPEC §6 Acceptance Gates:
  1. $\Delta \text{Net Log} > 0$
  2. $\text{Log PF} \ge \text{Baseline}$
  3. $\text{Win Rate} \ge \text{Baseline}$
  4. $\text{Max Drawdown} \le \text{Baseline}$
  5. 2022 Bear Market Preservation ($\text{Log PnL}_{2022} \ge +54.0\%$)
  6. Statistical Significance ($t > 3.00, p < 0.001$)
* **Taguchi Robustness & Noise Injection Gate (MANDATORY for all new books/logic):**
  Run the automated stress battery on the candidate tape:
  `python v12_standalone/scripts/run_taguchi_stress_test.py`
  Must satisfy all 3 Taguchi Quality Engineering thresholds:
  1. **Stress Survival Ratio:** $P_{10} / |P_{50}| \ge 0.85$ (At least 85% of alpha survives across 1,000 block-bootstrap paths).
  2. **Normalized Percentile Spread:** $(P_{90} - P_{10}) / |P_{50}| \le 0.35$ (Tight dispersion under noise).
  3. **Friction Resilience:** With $+25\text{ bps}$ roundtrip slippage/fee drag, Portfolio Log PF retention MUST be $\ge 85\%$ and individual book retention $\ge 80\%$.
* Produce `clean_room/STUDY_S_XX_VERDICT.md`.

### Step 2: Canonical Vaulting in `v12_standalone/`
* Deposit the audited candidate tape into the canonical directory:
  `v12_standalone/data/canonical/canonical_v13_2_tape.parquet` and `.csv`.
* Ensure this file is checked into version control.

### Step 3: Wire `build_v12_tape.py` to the New Version
* Point `build_v12_tape.py` canonical path pointer to `canonical_v13_2_tape.parquet`.
* Ensure the **Live Forward-Evaluation Loop** is armed for mark-to-market.

### Step 4: Pipeline Execution via `pipeline_v12_11.ps1`
* Run: `.\pipeline_v12_11.ps1`
* Verify console output reports exact expected trade counts, Log PF, and active open positions.

### Step 5: Full Automated Regression Test Suite
* Run the test suite:
  ```powershell
  pytest v12_standalone/tests/
  ```

### Step 6: Cyber Dashboard Verification & Process Restart
* Restart Dashboard on Port 8056 to clear in-memory cache:
  ```powershell
  Get-Process -Id (Get-NetTCPConnection -LocalPort 8056 -State Listen).OwningProcess | Stop-Process -Force
  python v12_standalone/dashboard.py
  ```

---

## 4. Architectural Invariants Ledger (Do Not Violate)

| Component | Invariant Rule | Violation Penalty |
| :--- | :--- | :--- |
| **Book 1 (Breakouts)** | Uses Continuous CSMI Sizing ($w \in [0.50, 1.45]$), Anti-Chop Firewall ($S > -1.25$), 3-Bar Consolidation Hold, and Micro-Harvesting (+5% Tranche A, -0.5% breakeven cushion). **NEVER apply a binary 200 EMA gate.** | Binary 200 EMA gate destroys 62.1% of breakout alpha (-344.2% net log bleed). |
| **Book 2 (Coiled Squeezes)** | Restricted **strictly to sub-200d EMA assets** (`c < ema200_1d`) with Inverted Carry Conviction ($1.25\times$ when $FR \le 0$ & Whales Short). | Trading above-200d coils introduces 299 negative-expectancy stall trades (PF 0.954). |
| **Book 2 Veto Logic** | When an above-200d squeeze is vetoed, **DO NOT call `_try_arm_flush_bid`**. It is a clean veto, NOT a flush setup. | Injects 329 false Book 3 trades, collapsing portfolio PF. |
| **Book 3 (Flush Reclaim)** | Resting limit bids at structural volume shelf or static $-8.0\%$ discount. Active **only during confirmed BTC Macro Bull** ($\text{BTC} > \text{EMA}_{4800\text{h}}$). Exits 100% at $+8.70\%$ entry reclaim. | Trading flush bids in a macro bear results in catastrophic falling-knife liquidations. |
| **Book 4 (Two-Tranche Engine)** | Target exits **MUST be handled by Two-Tranche logic (Study S-BE)**: Tranche A (50%) locks target cap (+15% to +20%), Tranche B (50%) ratchets stop to breakeven cushion (`entry * 0.9985`) and trails rolling 72h Donchian floor. **NEVER re-introduce legacy single-tranche target blocks at lines 341-344.** | Truncates macro excursions on runners like `S` and `USELESS` by 50% to 75%. |
| **Book 4 (Whale Squeeze Immunity)** | When whales are trapped short ($L/S \le 0.95$ or $\Delta L/S < -0.10$), **climax exits are overridden**; position rides 72h Donchian floor into macro runs. | Prematurely exits forced short squeeze expansions (e.g. `USELESS` exiting after 3 hours instead of riding to Sept 7). |
| **Book 4 (Dual Confluence Multiplier)** | Concurrent reclaim of USD 200d EMA and synthetic `ALT/BTC` 200d EMA earns $1.35\times$ Maximum Conviction Sizing. | Dilutes sizing on macro market share rotation leaders. |
| **Book 5 (Shelf Absorption Squeeze)** | Trapped Whale short squeezes ($L/S \le 0.85$, OI $\ge +40\%$) enter via passive resting limit bids at $-8.0\%$ discount. | Market chasing leads to 45.8% WR; limit absorption yields 90.05% WR. |
| **Book 6 (3-SARE Orderflow Reclaim)** | Anchors $\text{AVWAP}_\tau$ on CUSUM ignition ($S_\tau^+ \ge 1.50$) within 30-day cyclical bases. Entry staged: 50% limit bid at $\text{AVWAP}_\tau$, 50% reclaim close. Dual-barrier stop with $\ge 3.0\times$ volume panic bailout. 3-Stage exits: Tranche A (+8%), Tranche B (+25%), Tranche C (72h Donchian trail). | Market chasing spikes reduces Win Rate; ignoring panic bailout causes catastrophic drawdowns. |
| **Metrics Space** | All Profit Factors and portfolio compounding MUST be calculated in **strict log-return space** ($\sum \ln(1+R)$). | Arithmetic addition ($\sum R\%$) creates mathematical illusions and obscures ruin risk. |
| **Taguchi Quality Gate** | Every candidate model/book **MUST undergo Taguchi Noise Injection** via `v12_standalone/scripts/run_taguchi_stress_test.py`. Minimum Survival Ratio $\ge 0.85$, Spread $\le 0.35$, $+25\text{ bps}$ PF Retention $\ge 85\%$. | Deploys overfit "clean-curve" strategies that evaporate under live slippage and execution jitter. |

---

## 5. Quick Verification Script (Run to Audit Sync)

To instantly verify that the live pipeline, production files, and dashboard are in 100% synchronization:

```python
from pathlib import Path
import pandas as pd
import numpy as np

p_tape = Path("v12_standalone/data/all_tapes/v13_production")
closed = pd.read_parquet(p_tape / "closed_trades.parquet")
opened = pd.read_parquet(p_tape / "open_trades.parquet")

tot_log = closed['log_ret'].sum() * 100.0
w = closed[closed['log_ret'] > 0]['log_ret'].sum()
l = abs(closed[closed['log_ret'] < 0]['log_ret'].sum())
log_pf = w / l if l > 0 else 0.0
mult = np.exp(closed['log_ret'].sum())

print("=" * 60)
print("KRONOS LIVE PRODUCTION SYNC AUDIT (V13.2)")
print("=" * 60)
print(f"Closed Trades:     {len(closed):,}")
print(f"Active Positions:  {len(opened):,}")
print(f"Total Net Log:     +{tot_log:.1f}%")
print(f"Strict Log PF:     {log_pf:.3f}")
print(f"Capital Multiple:  {mult:.2e}x")
print("=" * 60)
assert len(closed) == 5010, f"Desynchronized closed trades count: {len(closed)}"
assert len(opened) >= 20, f"Missing active open positions: {len(opened)}"
assert log_pf >= 2.45, f"Profit Factor degraded below 2.45: {log_pf}"
print("✅ SYNC STATUS: 100% CANONICAL V13.2 COMPLIANT")
```

---

## 6. Mandatory Clean-Room Study Protocol & Causality Guardrails
> **All Future Agents:** To prevent the lookahead bias and static trade-chaining trap identified in the V13.3 Release Review (where Book 4 relied on forward 16-day future minimums and static CSV propagation), **ALL clean-room studies MUST strictly satisfy the 5-Step Clean-Room Checklist below before any results are published or promoted.**

### Summary Checklist for Future Clean-Room Studies

| Step | Gate Requirement | Verification Command |
| :--- | :--- | :--- |
| **1. Engine Uniformity** | Study runs directly via `run_v12_engine` (no standalone shard loop). | Inspect study imports: must call engine, not custom loop. |
| **2. Cold Ground-Up Run** | Results reproduced via `KRONOS_PROFILE=fresh python build_v12_tape.py` without cached parquet files. | Verify tape generator runs without `data/canonical/`. |
| **3. Truncation Invariance** | Signal at $T_{\text{entry}}$ persists when shard is sliced to `[:T_entry]`. | Automated unit test running engine on truncated window. |
| **4. Raw Data Compliance** | Firewalls (Core 0, funding, OI) match production settings. No synthetic backfilling. | Zero NaN-bypass switches. |
| **5. No Static Chaining** | Downstream studies (sizing, exits) generate candidate setups from raw shards. | Grep study scripts for `.read_csv('*trades*.csv')`. |
| **6. Dynamic Heuristic Iron Law** | Zero hardcoded constants (e.g. static % drops, fixed APR cutoffs, static L/S). Must use ATR multiples, rolling 30d percentiles, and studentized Z-scores. | Inspect code for static thresholds (e.g. `> -5%`, `L/S >= 2.80`). |

### Specific Protocol for Clean-Room Study: Dynamic BTC CUSUM Exhaustion ($S^+ > h_{\text{exhaust}}$)
When executing the clean-room study to mathematically detect Bitcoin macro regime tops and pre-emptively scale down altcoin book sizing before BTC crashes below the 200-day EMA:

1. **The Quantitative Problem (The Trend-Follower False Dichotomy):**
   * Trend-following models currently use binary BTC macro gating: $\text{BTC} > \text{EMA}_{4800\text{h}}$ (100% Bull sizing) vs $\text{BTC} < \text{EMA}_{4800\text{h}}$ (0% or 50% Bear sizing).
   * After vertical multi-month expansions (e.g., April 2021, March 2024), altcoins roll over and suffer massive drawdowns while BTC is still $+30\%$ to $+50\%$ above its 200-day EMA. The binary gate leaves altcoin books at 100% risk exposure during the most violent air-pocket liquidation tops.

2. **The CUSUM Exhaustion Formulation:**
   * Calculate recursive two-sided or upper CUSUM on BTC volume-weighted log return momentum:
     $$z_t = \frac{r_{t, 24\text{h}} - \mu_{168\text{h}}}{\sigma_{168\text{h}}}, \quad S_t^+ = \max\left(0, S_{t-1}^+ + z_t - k\right)$$
     Combined with Orderflow Climax Exhaustion:
     $$\text{Exhaustion Score } E_t = f\left(S_t^+, \frac{\Delta \text{OI}_{\text{BTC}, 24\text{h}}}{\text{Vol}_{24\text{h}}}, \text{RS}_{\text{ALT/BTC}}\right)$$
   * When $E_t \ge h_{\text{exhaust}}$, trigger pre-emptive continuous sizing decay on altcoins:
     $$w_{\text{macro}} = \text{clip}\left(1.0 - \alpha \cdot (E_t - h_{\text{exhaust}}), 0.20, 1.0\right)$$

3. **Clean-Room Implementation & Study Rules:**
   * Compute $E_t$ strictly inside `get_btc_macro()` in `features_v12.py` in causal point-in-time order.
   * **No Lookahead:** $E_t$ at timestamp $T$ can only use BTC and derivative data available up to timestamp $T$.
   * **Full-Universe Ablation:** Simulate across all 652 shards directly via `build_v12_tape.py` under:
     - `Arm 0`: Baseline V13.3 (Binary BTC Macro Gate).
     - `Arm 1`: Discrete Exhaustion Veto (Drop altcoin entries when $E_t > h_{\text{exhaust}}$).
     - `Arm 2`: Continuous Macro Sizing Decay ($w_{\text{macro}} \in [0.20, 1.0]$ based on $E_t$).
     - `Arm 3`: Continuous Sizing Decay + Ratchet Stop Tightening on active runners.
   * **Verification Gate:** Must reduce Master Max Drawdown by $\ge 15\%$ and lift Bear/Transition Log PF without reducing Bull Market runner MFE capture.

---

## 7. Mandatory Dynamic Heuristic Protocol (Zero Static Constants Iron Law)

> **All Agents, Models, and Research Scripts:** Static constants are permanently banned from all analytical, screening, and execution code across this repository.

### Why Static Constants are Banned:
1. **Cross-Asset Volatility Distortion:** A $-5.0\%$ flush in Bitcoin is an extreme $-3.0\sigma$ macro liquidation event, whereas in high-beta altcoins (`ZEREBRO`, `YB`) it is ordinary 15-minute spread noise.
2. **Structural Ratio Invariance:** An absolute Long/Short ratio of $2.80$ is an extreme $+3\sigma$ bubble peak for deep institutional assets (`BTC`, `ETH`, `ZIL`), but normal baseline for retail-heavy meme perps.
3. **Carry Distortion:** A $-15\%$ APR funding rate represents deep basis discount on low-yield majors, but negligible noise on hyper-volatile altcoins.

### Standardized Dynamic Heuristic Formulations:
Every quantitative scan, filter, and engine component MUST use the following self-referential dynamic formulations:

1. **Price Flushes & Swings:**
   $$\text{Flush}_{\text{ATR}} = \frac{P_{\text{peak}} - P_{\text{curr}}}{\text{ATR}_{24\text{h}}(t)}, \quad \text{Condition: } \text{Flush}_{\text{ATR}} \ge 2.0\times$$

2. **Funding Rate Basis Crowding:**
   $$\text{pct}_{\text{funding}} = \text{Rank}_{720\text{h}}(\text{FR}_t), \quad z_{\text{funding}} = \frac{\text{FR}_t - \mu_{\text{FR}, 720\text{h}}}{\sigma_{\text{FR}, 720\text{h}}}$$

3. **Whale Sentiment Positioning (Studentized Log-Ratio):**
   $$z_{\text{LS}} = \frac{\ln(\text{LS}_t) - \mu_{\ln(\text{LS}), 720\text{h}}}{\sigma_{\ln(\text{LS}), 720\text{h}}}, \quad \text{pct}_{\text{LS}} = \text{Rank}_{720\text{h}}(\text{LS}_t)$$

4. **Open Interest Orderflow Absorption:**
   $$z_{\text{OI}} = \frac{\Delta \text{OI}_{12\text{h}}}{\sigma_{\text{OI}, 168\text{h}} \cdot \sqrt{12}}$$

5. **Structural Floor Defense & Distance to Invalidation:**
   $$\text{Distance to Invalidation}_{\text{ATR}} = \frac{P_{\text{curr}} - \text{Floor}}{\text{ATR}_{24\text{h}}(t)}$$

---

## 8. The Supernova Squeeze & Whale Counter-Short Finite State Machine Engine (Study S-CE)

### Executive Discovery (October 2026 Universe Squeeze Super-Cycle):
Empirical research across 745 liquid perpetual shards in October 2026 (`Q` +995.0%, `AGT` +750.9%, `US` +622.5%, `DOS` +486.7%, `RLC` +322.8%, `GTC` +305.1%, `BTW` +218.5%, `MAGIC` +215.6%) revealed that multi-hundred-percent runs are not driven by crowded retail buying, but by **Top Trader Whale Counter-Short Traps**. Whales aggressively fade early volume breakouts, forcing margin-call feedback loops that propel price parabolic.

### The 3-State Causal Finite State Machine Architecture:

```
[ STATE A: DORMANT COIL ] ──(Bar 0 Ignition Shock)──> [ STATE B: IGNITION TRAP ] ──(Squeeze Confirmation)──> [ STATE C: SUPERNOVA RUNNER ]
      │                                                         │                                                   │
      │ (Iceberg Bids, Vol Comp, OI Retention)                  │ (Vol Shock ≥ 5x, 4h dOI ≥ 10%, dLS/dt ≤ -0.20)     │ (Whale L/S < 0.60, Negative Carry)
      └─────────────────────────────────────────────────────────┴───────────────────────────────────────────────────┴──> [ CLIMAX EXHAUSTION HARVEST ]
                                                                                                                             (Upper Wick ≥ 0.55, Dist > +8 ATR)
```

### The 6 Minute Microstructure Signatures (Rule 7 Certified):

1. **The "Iceberg Limit Absorption" Fingerprint (Raw Shards):**
   $$\text{Absorption Fingerprint} = (\text{TBR}_{24\text{h}} \le 0.48) \land \left(\frac{\text{AvgTradeSize}_{24\text{h}}}{\text{AvgTradeSize}_{30\text{d}}} \ge 1.20\right) \land \left(\left|\frac{\Delta P}{\text{ATR}_{24\text{h}}}\right| \le 1.0\right)$$
   *Mechanism:* Takers are actively market-selling ($\text{TBR} < 0.48$), but price refuses to print new lows because institutional resting limit bids absorb the volume at elevated trade sizes.

2. **The Volatility Compression Coil (Raw Shards):**
   $$\text{Volatility Coil} = \frac{\text{ATR}_{24\text{h}}}{\text{ATR}_{30\text{d}}} \le 0.65 \quad \text{for } \ge 48\text{ consecutive hours}$$
   *Mechanism:* Flags historical true range exhaustion prior to explosive regime shifts.

3. **The Orderflow Retention Ratio (Exotic Shards):**
   $$\text{OI Retention} = \left(\frac{P_t - P_{\text{high}, 7\text{d}}}{\text{ATR}_{24\text{h}}} \le -10.0\sigma\right) \land (\Delta \text{OI}_{\text{tok}, 7\text{d}} \ge 0.0\%)$$
   *Mechanism:* Proves sell-side panic volume is being absorbed into newly minted contracts rather than liquidation un-leveraging.

4. **The Bar-0 Volume Shock Multiplier (Raw Shards):**
   $$\text{Ignition Volume Shock} = \frac{\text{Volume}_{\text{bar}, t}}{\mu_{\text{vol}, 30\text{d\_hourly}}} \ge 5.0\times \quad \land \quad C_t > \text{EMA}_{200\text{h}}$$
   *Mechanism:* Confirms institutional liquidity ignition crossing key structural moving averages.

5. **The Instantaneous Whale Inversion Derivative ($\frac{\partial LS}{\partial t}$, Exotic Shards):**
   $$\text{Whale Inversion Trap} = (\Delta P_{4\text{h}} \ge +2.0 \text{ ATR}) \land (\Delta LS_{4\text{h}} \le -0.20 \text{ or } \Delta z_{LS, 4\text{h}} \le -1.2\sigma)$$
   *Mechanism:* Distinguishes genuine structural short squeezes from ordinary pump-and-dumps. If whales buy the pump, it fades; if whales counter-short the breakout, it squeezes.

6. **The Terminal Climax Exhaustion Fingerprint (Raw + Exotic Shards):**
   $$\text{Climax Top Alert} = (\text{Upper Wick Ratio} \ge 0.55) \land (P_t \ge \text{EMA}_{200\text{h}} + 8.0 \text{ ATR}) \land (LS_t < 0.65)$$
   *Mechanism:* Rejection pin-bars leaving $\ge 55\%$ upper wicks after an $+8\text{ ATR}$ run with whales pinned net short signal final forced covering into institutional distribution.

### Production Execution & Canonical Tooling:
All screening, monitoring, and historical audits MUST use the canonical production tool:
[`scripts/scan_supernova_squeezes.py`](file:///f:/kronos_v1_alt/scripts/scan_supernova_squeezes.py)
Supported by the Agent Skill: [`.agents/skills/supernova_squeeze_scanner/SKILL.md`](file:///f:/kronos_v1_alt/.agents/skills/supernova_squeeze_scanner/SKILL.md).



