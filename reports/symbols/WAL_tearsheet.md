# Kronos V12: Institutional Symbol Tear Sheet — `WAL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.279`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+6.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.89%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-13.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`50.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.0% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-15 01:00` | `2025-05-18 01:00` | 72.0h | `$0.6630` | `$0.6291` | **-5.12%** | **-5.25%** | +6.1% | -5.7% | `time_expiry` |
| 2 | Book 3 | `2025-07-01 13:00` | `2025-07-02 22:00` | 33.0h | `$0.3903` | `$0.4242` | **+8.70%** | **+8.34%** | +8.7% | -3.1% | `target_reclaim` |
| 3 | Book 3 | `2025-07-24 05:00` | `2025-07-26 15:00` | 58.0h | `$0.4171` | `$0.4840` | **+16.04%** | **+14.88%** | +16.6% | -1.4% | `target_reclaim` |
| 4 | Book 3 | `2025-07-29 14:00` | `2025-07-31 23:00` | 57.0h | `$0.4290` | `$0.3937` | **-8.23%** | **-8.59%** | +1.3% | -9.5% | `stop_loss` |
| 5 | Book 3 | `2025-08-11 11:00` | `2025-08-12 17:00` | 30.0h | `$0.4116` | `$0.4288` | **+4.17%** | **+4.08%** | +4.2% | -4.5% | `target_reclaim` |
| 6 | Book 3 | `2025-10-27 09:00` | `2025-10-28 19:00` | 34.0h | `$0.2480` | `$0.2276` | **-8.23%** | **-8.59%** | +0.2% | -9.0% | `stop_loss` |
| 7 | Book 3 | `2026-09-28 07:00` | `2026-10-01 07:00` | 72.0h | `$0.0337` | `$0.0341` | **+1.40%** | **+1.39%** | +4.8% | -3.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+27.3%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `2` | `50.0%` | **`-3.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `WAL`

* **Total Candidate Breakouts Filtered (Vetoed):** `98`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `80` (81.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+1,000.9%`
* **Missed Upside Forgone:** `-90.8%`
* **Net Veto Alpha:** `+910.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `56` | `57.1%` |
| `Core 1: Macro Bear Veto` | `23` | `23.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `12` | `12.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `7.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*