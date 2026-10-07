# Kronos V12: Institutional Symbol Tear Sheet — `CHZ`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.696`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-5.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.84%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-10.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`99.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.7% / -5.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-01-12 17:00` | `2023-01-18 16:00` | 143.0h | `$0.1290` | `$0.1264` | **-1.73%** | **-1.75%** | +12.1% | -5.8% | `fast_decay_cut` |
| 2 | Book 2 | `2023-07-13 17:00` | `2023-07-15 17:00` | 48.0h | `$0.0823` | `$0.0814` | **-1.14%** | **-1.15%** | +3.6% | -5.7% | `fast_decay_cut` |
| 3 | Book 2 | `2023-10-21 03:00` | `2023-10-28 03:00` | 168.0h | `$0.0598` | `$0.0648` | **+8.22%** | **+7.90%** | +15.0% | -1.7% | `time_cap` |
| 4 | Book 1 | `2023-11-05 23:00` | `2023-11-07 11:00` | 36.0h | `$0.0803` | `$0.0770` | **-3.34%** | **-3.40%** | +2.0% | -5.0% | `fast_decay_cut` |
| 5 | Book 2 | `2026-05-05 09:00` | `2026-05-12 09:00` | 168.0h | `$0.0420` | `$0.0436` | **+3.77%** | **+3.71%** | +12.6% | -4.4% | `time_cap` |
| 6 | Book 1 | `2026-09-22 23:00` | `2026-09-24 11:00` | 36.0h | `$0.0172` | `$0.0156` | **-9.85%** | **-10.37%** | +1.1% | -11.2% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `4` | `0.0%` | **`-16.7%`** |
| `time_cap` | `2` | `100.0%` | **`+11.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CHZ`

* **Total Candidate Breakouts Filtered (Vetoed):** `250`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `118` (47.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `41`
* **Saved Capital Losses Avoided:** `+1,437.0%`
* **Missed Upside Forgone:** `-2,469.4%`
* **Net Veto Alpha:** `+-1,032.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `97` | `38.8%` |
| `Core 1: Macro Bear Veto` | `92` | `36.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `56` | `22.4%` |
| `Core 4: Funding Rate Cap` | `5` | `2.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*