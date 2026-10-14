# Kronos V12: Institutional Symbol Tear Sheet — `ADA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `19` (`19` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `19` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`52.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.041`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+130.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`3.70x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+6.88%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`90.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.7% / -5.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 14:00` | `2022-11-01 14:00` | 168.0h | `$0.3720` | `$0.4008` | **+9.42%** | **+9.07%** | +18.2% | -1.5% | `time_cap` |
| 2 | Book 2 | `2022-12-13 13:00` | `2022-12-15 01:00` | 36.0h | `$0.3159` | `$0.3019` | **-5.35%** | **-5.48%** | +0.9% | -4.6% | `stall_bailout` |
| 3 | Book 1 | `2023-01-13 21:00` | `2023-01-16 08:00` | 59.0h | `$0.3487` | `$0.3473` | **-0.33%** | **-0.33%** | +6.3% | -4.9% | `fast_decay_cut` |
| 4 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.3308` | `$0.3438` | **+4.38%** | **+4.29%** | +11.3% | -4.5% | `time_cap` |
| 5 | Book 4 | `2023-04-03 08:00` | `2023-04-10 08:00` | 168.0h | `$0.4021` | `$0.3866` | **-4.45%** | **-4.53%** | +0.7% | -6.7% | `stagnation_cut` |
| 6 | Book 2 | `2023-07-13 16:00` | `2023-07-16 19:00` | 75.0h | `$0.3190` | `$0.3134` | **-2.23%** | **-2.25%** | +19.0% | -2.9% | `breakeven_ratchet` |
| 7 | Book 1 | `2023-11-02 18:00` | `2023-11-04 19:00` | 49.0h | `$0.3249` | `$0.3233` | **-0.55%** | **-0.55%** | +1.7% | -4.1% | `fast_decay_cut` |
| 8 | Book 3 | `2023-11-13 14:00` | `2023-11-16 07:00` | 65.0h | `$0.3612` | `$0.3926` | **+8.70%** | **+8.34%** | +10.4% | -6.7% | `target_reclaim` |
| 9 | Book 3 | `2023-12-16 00:00` | `2023-12-18 10:00` | 58.0h | `$0.5935` | `$0.5446` | **-8.23%** | **-8.59%** | +5.5% | -8.4% | `stop_loss` |
| 10 | Book 3 | `2024-02-20 15:00` | `2024-02-20 21:00` | 6.0h | `$0.5952` | `$0.6200` | **+4.17%** | **+4.08%** | +5.9% | -1.0% | `target_reclaim` |
| 11 | Book 3 | `2024-02-28 17:00` | `2024-02-29 04:00` | 11.0h | `$0.6199` | `$0.6534` | **+5.40%** | **+5.26%** | +6.9% | -4.0% | `target_reclaim` |
| 12 | Book 3 | `2024-03-05 16:00` | `2024-03-05 19:00` | 3.0h | `$0.7298` | `$0.6698` | **-8.23%** | **-8.59%** | +4.2% | -24.6% | `stop_loss` |
| 13 | Book 3 | `2024-03-14 16:00` | `2024-03-15 09:00` | 17.0h | `$0.7396` | `$0.6787` | **-8.23%** | **-8.59%** | +3.5% | -9.7% | `stop_loss` |
| 14 | Book 4 | `2024-11-07 18:00` | `2024-11-09 23:00` | 53.0h | `$0.3947` | `$0.4736` | **+136.11%** | **+90.97%** | +26.4% | -1.2% | `target_reclaim` |
| 15 | Book 3 | `2024-12-02 10:00` | `2024-12-02 15:00` | 5.0h | `$1.0749` | `$1.1756` | **+9.37%** | **+8.95%** | +14.1% | -1.6% | `target_reclaim` |
| 16 | Book 2 | `2025-04-22 14:00` | `2025-04-29 14:00` | 168.0h | `$0.6605` | `$0.7133` | **+8.35%** | **+8.03%** | +12.9% | -1.7% | `time_cap` |
| 17 | Book 2 | `2025-05-08 03:00` | `2025-05-15 03:00` | 168.0h | `$0.7044` | `$0.7898` | **+12.19%** | **+11.51%** | +22.7% | -1.2% | `time_cap` |
| 18 | Book 1 | `2025-07-10 17:00` | `2025-07-11 13:00` | 20.0h | `$0.6591` | `$0.7525` | **+25.66%** | **+23.27%** | +15.6% | -3.2% | `target_reclaim` |
| 19 | Book 4 | `2026-09-21 09:00` | `2026-10-08 15:00` | 414.0h | `$0.2394` | `$0.2316` | **-4.03%** | **-4.10%** | +18.0% | -4.0% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+140.9%`** |
| `time_cap` | `4` | `100.0%` | **`+32.9%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-0.9%`** |
| `stall_bailout` | `1` | `0.0%` | **`-5.5%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-4.5%`** |
| `breakeven_ratchet` | `1` | `0.0%` | **`-2.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-4.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `ADA`

* **Total Candidate Breakouts Filtered (Vetoed):** `225`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `115` (51.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `55`
* **Saved Capital Losses Avoided:** `+1,364.7%`
* **Missed Upside Forgone:** `-1,926.7%`
* **Net Veto Alpha:** `+-562.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `134` | `59.6%` |
| `Core 1: Macro Bear Veto` | `67` | `29.8%` |
| `Core 4: Funding Rate Cap` | `24` | `10.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*