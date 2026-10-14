# Kronos V12: Institutional Symbol Tear Sheet — `COST`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.87%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`40.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.5% / -1.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-14 01:00` | `2026-09-16 01:00` | 48.0h | `$910.6911` | `$901.0417` | **-1.09%** | **-1.09%** | +1.2% | -1.0% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-22 05:00` | `2026-09-23 17:00` | 36.0h | `$904.9868` | `$900.0941` | **-0.56%** | **-0.56%** | +0.3% | -1.1% | `stall_bailout` |
| 3 | Book 2 | `2026-09-28 13:00` | `2026-09-30 01:00` | 36.0h | `$930.0293` | `$921.3409` | **-0.94%** | **-0.95%** | +0.1% | -1.8% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `2` | `0.0%` | **`-1.5%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `COST`

* **Total Candidate Breakouts Filtered (Vetoed):** `57`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `57` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+192.9%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+192.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `53` | `93.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `1.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `1.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `1.8%` |
| `Core 3: Min Turnover Velocity` | `1` | `1.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*