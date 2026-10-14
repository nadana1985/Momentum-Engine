# Kronos V12: Institutional Symbol Tear Sheet — `POPCAT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.860`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+22.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.25x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.46%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`32.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.8% / -9.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-08-23 15:00` | `2024-08-27 15:00` | Live | `$0.6149` | `$0.6672` | **+8.50%** | **+8.16%** | +12.1% | -30.7% | `shelf_target_reclaim` |
| 2 | Book 3 | `2024-09-27 20:00` | `2024-09-29 20:00` | 48.0h | `$0.9271` | `$0.9957` | **+7.40%** | **+7.13%** | +9.9% | -3.6% | `target_reclaim` |
| 3 | Book 3 | `2024-10-25 17:00` | `2024-10-25 23:00` | 6.0h | `$1.4064` | `$1.2907` | **-8.23%** | **-8.59%** | +3.9% | -9.0% | `stop_loss` |
| 4 | Book 3 | `2024-11-15 00:00` | `2024-11-15 20:00` | 20.0h | `$1.6324` | `$1.8299` | **+12.10%** | **+11.42%** | +15.9% | -6.0% | `target_reclaim` |
| 5 | Book 3 | `2025-04-25 17:00` | `2025-04-27 02:00` | 33.0h | `$0.4042` | `$0.3710` | **-8.23%** | **-8.59%** | +4.6% | -8.3% | `stop_loss` |
| 6 | Book 3 | `2025-05-12 18:00` | `2025-05-12 22:00` | 4.0h | `$0.5353` | `$0.5818` | **+8.70%** | **+8.34%** | +9.9% | -5.6% | `target_reclaim` |
| 7 | Book 3 | `2025-07-14 14:00` | `2025-07-16 11:00` | 45.0h | `$0.3774` | `$0.3951` | **+4.68%** | **+4.57%** | +5.3% | -7.2% | `target_reclaim` |
| 8 | Book 3 | `2025-07-18 14:00` | `2025-07-20 16:00` | 50.0h | `$0.3811` | `$0.4141` | **+8.65%** | **+8.29%** | +11.5% | -5.5% | `target_reclaim` |
| 9 | Book 3 | `2026-08-26 14:00` | `2026-08-28 16:00` | 50.0h | `$0.0572` | `$0.0525` | **-8.23%** | **-8.59%** | +5.7% | -8.9% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+39.8%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `POPCAT`

* **Total Candidate Breakouts Filtered (Vetoed):** `255`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `165` (64.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `77`
* **Saved Capital Losses Avoided:** `+2,926.1%`
* **Missed Upside Forgone:** `-1,921.2%`
* **Net Veto Alpha:** `+1,004.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `192` | `75.3%` |
| `Core 1: Macro Bear Veto` | `35` | `13.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `17` | `6.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `10` | `3.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*