# Kronos V12: Institutional Symbol Tear Sheet — `STEEM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `11` (`11` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`72.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.171`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+40.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.49x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.64%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`32.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.0% / -6.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$0.2587` | `$0.2555` | **-1.25%** | **-1.26%** | +4.5% | -12.6% | `time_expiry` |
| 2 | Book 3 | `2024-01-03 12:00` | `2024-01-05 17:00` | 53.0h | `$0.2499` | `$0.2293` | **-8.23%** | **-8.59%** | +3.1% | -21.0% | `stop_loss` |
| 3 | Book 3 | `2024-02-28 17:00` | `2024-02-29 00:00` | 7.0h | `$0.2386` | `$0.2594` | **+8.70%** | **+8.34%** | +12.6% | -1.0% | `target_reclaim` |
| 4 | Book 3 | `2024-03-05 19:00` | `2024-03-06 02:00` | 7.0h | `$0.2770` | `$0.3011` | **+8.70%** | **+8.34%** | +11.8% | -9.8% | `target_reclaim` |
| 5 | Book 3 | `2024-03-10 14:00` | `2024-03-11 21:00` | 31.0h | `$0.3272` | `$0.3556` | **+8.70%** | **+8.34%** | +9.4% | -3.9% | `target_reclaim` |
| 6 | Book 3 | `2024-03-15 03:00` | `2024-03-16 18:00` | 39.0h | `$0.3297` | `$0.3026` | **-8.23%** | **-8.59%** | +3.6% | -9.8% | `stop_loss` |
| 7 | Book 3 | `2024-11-24 12:00` | `2024-11-24 23:00` | 11.0h | `$0.2211` | `$0.2403` | **+8.70%** | **+8.34%** | +10.1% | -1.4% | `target_reclaim` |
| 8 | Book 3 | `2024-12-03 13:00` | `2024-12-03 21:00` | 8.0h | `$0.2695` | `$0.2929` | **+8.70%** | **+8.34%** | +8.9% | -3.5% | `target_reclaim` |
| 9 | Book 3 | `2025-04-28 01:00` | `2025-05-01 01:00` | 72.0h | `$0.1502` | `$0.1504` | **+0.10%** | **+0.10%** | +3.4% | -3.9% | `time_expiry` |
| 10 | Book 3 | `2026-09-11 11:00` | `2026-09-12 04:00` | 17.0h | `$0.0434` | `$0.0472` | **+8.70%** | **+8.34%** | +9.4% | -0.2% | `target_reclaim` |
| 11 | Book 3 | `2026-09-24 09:00` | `2026-09-26 00:00` | 39.0h | `$0.0617` | `$0.0671` | **+8.70%** | **+8.34%** | +10.9% | -1.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `7` | `100.0%` | **`+58.4%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `2` | `50.0%` | **`-1.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `STEEM`

* **Total Candidate Breakouts Filtered (Vetoed):** `119`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `67` (56.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+825.2%`
* **Missed Upside Forgone:** `-316.3%`
* **Net Veto Alpha:** `+509.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `88` | `73.9%` |
| `Core 1: Macro Bear Veto` | `17` | `14.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `12` | `10.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `1.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*