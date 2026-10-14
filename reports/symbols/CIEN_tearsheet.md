# Kronos V12: Institutional Symbol Tear Sheet — `CIEN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`2.610`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+11.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.12x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.70%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`88.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.9% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 17:00` | `2026-08-28 17:00` | 48.0h | `$402.1228` | `$382.2719` | **-5.14%** | **-5.27%** | +4.4% | -5.4% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-21 12:00` | `2026-09-23 12:00` | 48.0h | `$372.4488` | `$366.7808` | **-1.61%** | **-1.63%** | +1.2% | -4.1% | `fast_decay_cut` |
| 3 | Book 2 | `2026-09-30 12:00` | `2026-10-07 12:00` | 168.0h | `$360.9201` | `$426.9799` | **+19.60%** | **+18.00%** | +24.2% | -5.5% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-6.9%`** |
| `time_cap` | `1` | `100.0%` | **`+18.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `CIEN`

* **Total Candidate Breakouts Filtered (Vetoed):** `9`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `7` (77.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+56.1%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+56.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `8` | `88.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `11.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*