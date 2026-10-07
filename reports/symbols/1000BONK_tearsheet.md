# Kronos V12: Institutional Symbol Tear Sheet — `1000BONK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `11` (`11` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`63.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.817`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+50.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.66x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.62%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-26.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`21.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.4% / -5.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-17 13:00` | `2024-02-20 13:00` | 72.0h | `$0.0127` | `$0.0130` | **+2.14%** | **+2.12%** | +5.1% | -2.6% | `time_expiry` |
| 2 | Book 3 | `2024-02-28 17:00` | `2024-02-28 22:00` | 5.0h | `$0.0148` | `$0.0169` | **+13.64%** | **+12.78%** | +19.4% | -10.6% | `target_reclaim` |
| 3 | Book 3 | `2024-03-05 16:00` | `2024-03-05 17:00` | 1.0h | `$0.0272` | `$0.0309` | **+13.64%** | **+12.78%** | +19.8% | -1.2% | `target_reclaim` |
| 4 | Book 3 | `2024-04-25 04:00` | `2024-04-25 14:00` | 10.0h | `$0.0229` | `$0.0260` | **+13.64%** | **+12.78%** | +20.6% | -0.4% | `target_reclaim` |
| 5 | Book 3 | `2024-05-30 06:00` | `2024-06-02 06:00` | 72.0h | `$0.0335` | `$0.0331` | **-1.10%** | **-1.10%** | +9.1% | -3.6% | `time_expiry` |
| 6 | Book 3 | `2024-10-01 17:00` | `2024-10-02 03:00` | 10.0h | `$0.0220` | `$0.0250` | **+13.64%** | **+12.78%** | +13.7% | -1.5% | `target_reclaim` |
| 7 | Book 3 | `2024-11-16 15:00` | `2024-11-16 21:00` | 6.0h | `$0.0399` | `$0.0453` | **+13.64%** | **+12.78%** | +15.8% | -3.4% | `target_reclaim` |
| 8 | Book 3 | `2024-11-18 18:00` | `2024-11-19 13:00` | 19.0h | `$0.0463` | `$0.0526` | **+13.64%** | **+12.78%** | +15.3% | -1.9% | `target_reclaim` |
| 9 | Book 3 | `2025-01-19 22:00` | `2025-01-20 00:00` | 2.0h | `$0.0341` | `$0.0313` | **-8.23%** | **-8.59%** | +3.5% | -13.8% | `stop_loss` |
| 10 | Book 1 | `2026-08-22 02:00` | `2026-08-22 05:00` | 3.0h | `$0.0033` | `$0.0029` | **-13.86%** | **-14.92%** | +11.9% | -14.3% | `initial_stop` |
| 11 | Book 1 | `2026-08-22 17:00` | `2026-08-24 05:00` | 36.0h | `$0.0033` | `$0.0032` | **-3.31%** | **-3.36%** | +2.2% | -8.4% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+76.7%`** |
| `time_expiry` | `2` | `50.0%` | **`+1.0%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-3.4%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `initial_stop` | `1` | `0.0%` | **`-14.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000BONK`

* **Total Candidate Breakouts Filtered (Vetoed):** `156`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `87` (55.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `70`
* **Saved Capital Losses Avoided:** `+1,481.1%`
* **Missed Upside Forgone:** `-2,911.6%`
* **Net Veto Alpha:** `+-1,430.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `94` | `60.3%` |
| `Core 1: Macro Bear Veto` | `60` | `38.5%` |
| `Core 4: Funding Rate Cap` | `2` | `1.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*