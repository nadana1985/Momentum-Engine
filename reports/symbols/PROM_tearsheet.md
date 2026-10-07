# Kronos V12: Institutional Symbol Tear Sheet — `PROM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.808`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+7.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.48%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-3.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`113.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.9% / -7.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-05-30 18:00` | `2025-05-30 21:00` | 3.0h | `$5.5819` | `$5.2536` | **-5.88%** | **-6.06%** | +1.8% | -9.4% | `initial_stop` |
| 2 | Book 2 | `2025-07-15 07:00` | `2025-07-22 07:00` | 168.0h | `$7.7363` | `$9.1351` | **+18.08%** | **+16.62%** | +29.1% | -4.2% | `time_cap` |
| 3 | Book 2 | `2025-08-11 22:00` | `2025-08-18 22:00` | 168.0h | `$9.3493` | `$9.0613` | **-3.08%** | **-3.13%** | +10.8% | -7.2% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `50.0%` | **`+13.5%`** |
| `initial_stop` | `1` | `0.0%` | **`-6.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `PROM`

* **Total Candidate Breakouts Filtered (Vetoed):** `66`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (51.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+527.0%`
* **Missed Upside Forgone:** `-980.4%`
* **Net Veto Alpha:** `+-453.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `54` | `81.8%` |
| `Core 4: Defensible Whale Dump` | `12` | `18.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*