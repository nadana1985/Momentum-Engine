# Kronos V12: Institutional Symbol Tear Sheet — `CRWV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.074`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-3.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.04%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`77.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.7% / -3.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-25 13:00` | `2026-08-27 13:00` | 48.0h | `$89.9443` | `$87.6004` | **-2.61%** | **-2.64%** | +4.0% | -3.6% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-04 19:00` | `2026-09-10 12:00` | 137.0h | `$89.6034` | `$89.8263` | **+0.25%** | **+0.25%** | +16.7% | -1.8% | `breakeven_ratchet` |
| 3 | Book 2 | `2026-09-22 13:00` | `2026-09-24 13:00` | 48.0h | `$88.3002` | `$87.6603` | **-0.72%** | **-0.73%** | +2.4% | -4.5% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-3.4%`** |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `CRWV`

* **Total Candidate Breakouts Filtered (Vetoed):** `22`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `14` (63.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+156.5%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+156.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `22` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*