# Kronos V12: Institutional Symbol Tear Sheet — `ALGO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.673`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+4.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.50%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-5.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`103.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.1% / -3.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-01-08 23:00` | `2023-01-10 11:00` | 36.0h | `$0.1996` | `$0.1989` | **-0.44%** | **-0.44%** | +4.4% | -1.6% | `fast_decay_cut` |
| 2 | Book 2 | `2023-06-23 16:00` | `2023-06-26 01:00` | 57.0h | `$0.1328` | `$0.1313` | **-1.17%** | **-1.18%** | +6.1% | -1.8% | `fast_decay_cut` |
| 3 | Book 2 | `2023-07-13 17:00` | `2023-07-15 17:00` | 48.0h | `$0.1162` | `$0.1130` | **-2.73%** | **-2.77%** | +6.4% | -5.7% | `fast_decay_cut` |
| 4 | Book 2 | `2023-09-20 18:00` | `2023-09-25 17:00` | 119.0h | `$0.0989` | `$0.0982` | **-0.80%** | **-0.80%** | +4.3% | -3.5% | `fast_decay_cut` |
| 5 | Book 2 | `2023-10-23 22:00` | `2023-10-27 01:00` | 75.0h | `$0.0987` | `$0.0985` | **-0.30%** | **-0.30%** | +5.0% | -3.2% | `fast_decay_cut` |
| 6 | Book 1 | `2023-11-06 08:00` | `2023-11-07 22:00` | 38.0h | `$0.1240` | `$0.1233` | **-0.41%** | **-0.41%** | +4.9% | -4.6% | `fast_decay_cut` |
| 7 | Book 1 | `2025-04-21 05:00` | `2025-05-03 00:00` | 283.0h | `$0.2010` | `$0.2112` | **+5.19%** | **+5.06%** | +18.8% | -5.9% | `trail_stop` |
| 8 | Book 2 | `2026-05-05 05:00` | `2026-05-12 05:00` | 168.0h | `$0.1194` | `$0.1253` | **+4.93%** | **+4.81%** | +14.7% | -2.9% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `6` | `0.0%` | **`-5.9%`** |
| `time_cap` | `1` | `100.0%` | **`+4.8%`** |
| `trail_stop` | `1` | `100.0%` | **`+5.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALGO`

* **Total Candidate Breakouts Filtered (Vetoed):** `299`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `174` (58.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `72`
* **Saved Capital Losses Avoided:** `+2,322.5%`
* **Missed Upside Forgone:** `-2,418.0%`
* **Net Veto Alpha:** `+-95.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `105` | `35.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `95` | `31.8%` |
| `Core 1: Macro Bear Veto` | `82` | `27.4%` |
| `Core 4: Funding Rate Cap` | `17` | `5.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*