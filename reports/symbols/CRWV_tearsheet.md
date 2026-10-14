# Kronos V12: Institutional Symbol Tear Sheet — `CRWV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.47%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`88.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.7% / -3.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-25 13:00` | `2026-08-27 13:00` | 48.0h | `$89.9443` | `$87.6004` | **-2.71%** | **-2.75%** | +4.0% | -3.6% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-04 19:00` | `2026-09-11 19:00` | 168.0h | `$89.6034` | `$88.8174` | **-0.91%** | **-0.91%** | +16.7% | -1.8% | `time_cap` |
| 3 | Book 2 | `2026-09-22 13:00` | `2026-09-24 13:00` | 48.0h | `$88.3002` | `$87.6603` | **-0.75%** | **-0.75%** | +2.4% | -4.5% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-3.5%`** |
| `time_cap` | `1` | `0.0%` | **`-0.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `CRWV`

* **Total Candidate Breakouts Filtered (Vetoed):** `181`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `139` (76.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+1,438.2%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+1,438.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `181` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*