# Kronos V12: Institutional Symbol Tear Sheet — `TLM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `15` (`15` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.803`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+29.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.34x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.98%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`33.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.9% / -4.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-07-14 18:00` | `2023-07-17 18:00` | 72.0h | `$0.0115` | `$0.0114` | **-0.79%** | **-0.79%** | +5.9% | -2.5% | `time_expiry` |
| 2 | Book 3 | `2023-10-04 00:00` | `2023-10-07 00:00` | 72.0h | `$0.0097` | `$0.0100` | **+3.06%** | **+3.01%** | +4.0% | -1.4% | `time_expiry` |
| 3 | Book 3 | `2023-11-13 21:00` | `2023-11-16 21:00` | 72.0h | `$0.0132` | `$0.0130` | **-1.76%** | **-1.78%** | +5.8% | -6.2% | `time_expiry` |
| 4 | Book 3 | `2023-12-26 17:00` | `2023-12-27 13:00` | 20.0h | `$0.0183` | `$0.0199` | **+8.70%** | **+8.34%** | +9.6% | -4.3% | `target_reclaim` |
| 5 | Book 3 | `2023-12-29 01:00` | `2023-12-29 05:00` | 4.0h | `$0.0191` | `$0.0208` | **+8.70%** | **+8.34%** | +9.0% | -0.7% | `target_reclaim` |
| 6 | Book 3 | `2024-02-17 14:00` | `2024-02-18 09:00` | 19.0h | `$0.0150` | `$0.0163` | **+8.70%** | **+8.34%** | +10.3% | -0.5% | `target_reclaim` |
| 7 | Book 3 | `2024-03-14 11:00` | `2024-03-15 03:00` | 16.0h | `$0.0295` | `$0.0271` | **-8.23%** | **-8.59%** | +1.1% | -12.3% | `stop_loss` |
| 8 | Book 3 | `2024-09-22 22:00` | `2024-09-24 07:00` | 33.0h | `$0.0105` | `$0.0114` | **+8.70%** | **+8.34%** | +8.8% | -0.5% | `target_reclaim` |
| 9 | Book 3 | `2024-11-10 21:00` | `2024-11-11 02:00` | 5.0h | `$0.0108` | `$0.0118` | **+8.70%** | **+8.34%** | +9.1% | -1.8% | `target_reclaim` |
| 10 | Book 3 | `2024-11-12 10:00` | `2024-11-14 15:00` | 53.0h | `$0.0111` | `$0.0102` | **-8.23%** | **-8.59%** | +5.6% | -8.0% | `stop_loss` |
| 11 | Book 3 | `2024-11-24 12:00` | `2024-11-24 22:00` | 10.0h | `$0.0135` | `$0.0146` | **+8.70%** | **+8.34%** | +12.1% | -2.4% | `target_reclaim` |
| 12 | Book 3 | `2024-12-09 09:00` | `2024-12-09 20:00` | 11.0h | `$0.0187` | `$0.0172` | **-8.23%** | **-8.59%** | +4.5% | -8.7% | `stop_loss` |
| 13 | Book 3 | `2025-05-14 23:00` | `2025-05-15 14:00` | 15.0h | `$0.0065` | `$0.0060` | **-8.23%** | **-8.59%** | +1.8% | -10.1% | `stop_loss` |
| 14 | Book 3 | `2025-07-15 02:00` | `2025-07-16 00:00` | 22.0h | `$0.0050` | `$0.0054` | **+8.70%** | **+8.34%** | +9.2% | -1.8% | `target_reclaim` |
| 15 | Book 3 | `2026-09-28 14:00` | `2026-10-01 14:00` | 72.0h | `$0.0015` | `$0.0016` | **+5.31%** | **+5.17%** | +6.4% | -1.5% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `7` | `100.0%` | **`+58.4%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `time_expiry` | `4` | `50.0%` | **`+5.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `TLM`

* **Total Candidate Breakouts Filtered (Vetoed):** `123`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `69` (56.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `15`
* **Saved Capital Losses Avoided:** `+950.7%`
* **Missed Upside Forgone:** `-597.6%`
* **Net Veto Alpha:** `+353.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `52` | `42.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `36` | `29.3%` |
| `Core 1: Macro Bear Veto` | `21` | `17.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `14` | `11.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*