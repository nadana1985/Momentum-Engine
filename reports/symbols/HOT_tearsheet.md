# Kronos V12: Institutional Symbol Tear Sheet — `HOT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `16` (`16` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `16` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`56.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.918`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-5.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.34%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-43.3%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`68.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.3% / -6.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-01-30 09:00` | `2023-02-02 09:00` | 72.0h | `$0.0021` | `$0.0022` | **+7.38%** | **+7.12%** | +8.2% | -6.1% | `time_expiry` |
| 2 | Book 3 | `2023-02-21 15:00` | `2023-02-24 15:00` | 72.0h | `$0.0022` | `$0.0021` | **-5.81%** | **-5.99%** | +2.6% | -6.7% | `time_expiry` |
| 3 | Book 4 | `2023-03-31 12:00` | `2023-04-21 19:00` | 511.0h | `$0.0021` | `$0.0018` | **-16.17%** | **-17.37%** | +11.5% | -15.2% | `structural_stop` |
| 4 | Book 3 | `2023-10-31 02:00` | `2023-10-31 10:00` | 8.0h | `$0.0014` | `$0.0015` | **+4.17%** | **+4.08%** | +5.6% | -1.2% | `target_reclaim` |
| 5 | Book 3 | `2023-12-04 11:00` | `2023-12-04 18:00` | 7.0h | `$0.0016` | `$0.0017` | **+8.80%** | **+8.43%** | +8.9% | -0.9% | `target_reclaim` |
| 6 | Book 3 | `2024-03-14 18:00` | `2024-03-15 03:00` | 9.0h | `$0.0041` | `$0.0038` | **-8.23%** | **-8.59%** | +4.0% | -9.1% | `stop_loss` |
| 7 | Book 3 | `2024-05-30 07:00` | `2024-06-02 07:00` | 72.0h | `$0.0025` | `$0.0025` | **+1.93%** | **+1.91%** | +4.3% | -3.6% | `time_expiry` |
| 8 | Book 3 | `2024-06-07 18:00` | `2024-06-08 11:00` | 17.0h | `$0.0025` | `$0.0023` | **-8.23%** | **-8.59%** | +2.4% | -11.8% | `stop_loss` |
| 9 | Book 3 | `2024-08-26 12:00` | `2024-08-28 16:00` | 52.0h | `$0.0018` | `$0.0017` | **-8.23%** | **-8.59%** | +4.1% | -9.9% | `stop_loss` |
| 10 | Book 3 | `2024-10-21 16:00` | `2024-10-23 12:00` | 44.0h | `$0.0018` | `$0.0016` | **-8.23%** | **-8.59%** | +4.1% | -8.3% | `stop_loss` |
| 11 | Book 3 | `2024-11-13 03:00` | `2024-11-16 03:00` | 72.0h | `$0.0020` | `$0.0021` | **+4.66%** | **+4.55%** | +11.0% | -6.5% | `time_expiry` |
| 12 | Book 3 | `2024-12-02 08:00` | `2024-12-02 16:00` | 8.0h | `$0.0030` | `$0.0033` | **+8.51%** | **+8.17%** | +8.6% | -0.5% | `target_reclaim` |
| 13 | Book 3 | `2025-01-19 08:00` | `2025-01-20 00:00` | 16.0h | `$0.0024` | `$0.0022` | **-8.23%** | **-8.59%** | +5.4% | -11.1% | `stop_loss` |
| 14 | Book 3 | `2025-07-14 18:00` | `2025-07-15 17:00` | 23.0h | `$0.0010` | `$0.0010` | **+4.17%** | **+4.08%** | +4.3% | -3.2% | `target_reclaim` |
| 15 | Book 4 | `2026-09-20 16:00` | `2026-09-22 11:00` | 43.0h | `$0.0004` | `$0.0005` | **+16.85%** | **+15.77%** | +23.5% | -1.8% | `target_reclaim` |
| 16 | Book 3 | `2026-09-23 14:00` | `2026-09-26 14:00` | 72.0h | `$0.0004` | `$0.0005` | **+6.96%** | **+6.73%** | +7.6% | -4.9% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `target_reclaim` | `5` | `100.0%` | **`+40.5%`** |
| `time_expiry` | `5` | `80.0%` | **`+14.3%`** |
| `structural_stop` | `1` | `0.0%` | **`-17.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `HOT`

* **Total Candidate Breakouts Filtered (Vetoed):** `429`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `299` (69.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `35`
* **Saved Capital Losses Avoided:** `+4,068.7%`
* **Missed Upside Forgone:** `-1,017.8%`
* **Net Veto Alpha:** `+3,051.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `183` | `42.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `93` | `21.7%` |
| `Core 1: Macro Bear Veto` | `63` | `14.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `50` | `11.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `40` | `9.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*