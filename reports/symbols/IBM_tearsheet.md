# Kronos V12: Institutional Symbol Tear Sheet — `IBM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.077`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-1.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.66%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`102.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.0% / -2.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-27 14:00` | `2026-08-29 02:00` | 36.0h | `$238.8456` | `$235.4699` | **-1.41%** | **-1.42%** | +0.9% | -1.5% | `stall_bailout` |
| 2 | Book 2 | `2026-09-09 17:00` | `2026-09-16 17:00` | 168.0h | `$239.1263` | `$239.3900` | **+0.11%** | **+0.11%** | +7.1% | -2.9% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `1` | `0.0%` | **`-1.4%`** |
| `time_cap` | `1` | `100.0%` | **`+0.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `IBM`

* **Total Candidate Breakouts Filtered (Vetoed):** `20`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `10` (50.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+49.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+49.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `20` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*