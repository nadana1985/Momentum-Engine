# Kronos V12: Institutional Symbol Tear Sheet — `HK1810`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.251`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.39%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-3.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`60.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.2% / -2.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-24 01:00` | `2026-08-27 01:00` | 72.0h | `$27.8989` | `$28.1594` | **+0.93%** | **+0.93%** | +4.8% | -1.1% | `time_expiry` |
| 2 | Book 2 | `2026-09-14 01:00` | `2026-09-16 01:00` | 48.0h | `$26.9873` | `$26.0148` | **-3.64%** | **-3.71%** | +1.6% | -3.6% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-3.7%`** |
| `time_expiry` | `1` | `100.0%` | **`+0.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `HK1810`

* **Total Candidate Breakouts Filtered (Vetoed):** `6`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `3` (50.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+31.4%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+31.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `5` | `83.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `16.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*