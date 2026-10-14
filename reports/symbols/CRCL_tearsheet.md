# Kronos V12: Institutional Symbol Tear Sheet — `CRCL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.190`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+3.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.08%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`90.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.0% / -8.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-05 01:00` | `2026-05-08 01:00` | 72.0h | `$125.5230` | `$113.5853` | **-8.12%** | **-8.47%** | +3.7% | -12.6% | `stagnation_cut` |
| 2 | Book 4 | `2026-08-20 08:00` | `2026-08-27 15:00` | 175.0h | `$83.1774` | `$95.6540` | **+22.50%** | **+20.29%** | +15.7% | -4.2% | `target_reclaim` |
| 3 | Book 3 | `2026-09-15 13:00` | `2026-09-16 13:00` | 24.0h | `$89.3854` | `$82.0290` | **-8.23%** | **-8.59%** | +4.5% | -9.0% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stagnation_cut` | `1` | `0.0%` | **`-8.5%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+20.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `CRCL`

* **Total Candidate Breakouts Filtered (Vetoed):** `70`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `29` (41.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+235.6%`
* **Missed Upside Forgone:** `-100.0%`
* **Net Veto Alpha:** `+135.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `66` | `94.3%` |
| `Core 4: Funding Rate Cap` | `3` | `4.3%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `1.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*