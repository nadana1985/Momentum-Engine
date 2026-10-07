# Kronos V12: Institutional Symbol Tear Sheet — `POPCAT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `11` (`11` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`54.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.165`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+7.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.07x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.64%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-25.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.8% / -5.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-09-27 20:00` | `2024-09-29 20:00` | 48.0h | `$0.9160` | `$0.9957` | **+8.70%** | **+8.34%** | +11.3% | -2.4% | `target_reclaim` |
| 2 | Book 3 | `2024-10-13 19:00` | `2024-10-14 14:00` | 19.0h | `$1.3691` | `$1.4882` | **+8.70%** | **+8.34%** | +9.2% | -3.7% | `target_reclaim` |
| 3 | Book 3 | `2024-10-25 06:00` | `2024-10-25 17:00` | 11.0h | `$1.4791` | `$1.3574` | **-8.23%** | **-8.59%** | +2.5% | -8.3% | `stop_loss` |
| 4 | Book 3 | `2024-11-14 14:00` | `2024-11-15 04:00` | 14.0h | `$1.6835` | `$1.5450` | **-8.23%** | **-8.59%** | +9.2% | -8.9% | `stop_loss` |
| 5 | Book 3 | `2025-04-25 17:00` | `2025-04-27 02:00` | 33.0h | `$0.4042` | `$0.3710` | **-8.23%** | **-8.59%** | +4.6% | -8.3% | `stop_loss` |
| 6 | Book 3 | `2025-05-12 18:00` | `2025-05-12 22:00` | 4.0h | `$0.5353` | `$0.5818` | **+8.70%** | **+8.34%** | +9.9% | -5.6% | `target_reclaim` |
| 7 | Book 3 | `2025-07-14 20:00` | `2025-07-16 11:00` | 39.0h | `$0.3635` | `$0.3951` | **+8.70%** | **+8.34%** | +9.3% | -3.6% | `target_reclaim` |
| 8 | Book 3 | `2025-07-18 14:00` | `2025-07-20 16:00` | 50.0h | `$0.3810` | `$0.4141` | **+8.70%** | **+8.34%** | +11.6% | -5.5% | `target_reclaim` |
| 9 | Book 3 | `2025-07-22 08:00` | `2025-07-22 18:00` | 10.0h | `$0.4037` | `$0.4388` | **+8.70%** | **+8.34%** | +10.1% | -0.3% | `target_reclaim` |
| 10 | Book 3 | `2025-07-23 07:00` | `2025-07-23 17:00` | 10.0h | `$0.4401` | `$0.4039` | **-8.23%** | **-8.59%** | +3.1% | -9.0% | `stop_loss` |
| 11 | Book 3 | `2026-08-26 14:00` | `2026-08-28 16:00` | 50.0h | `$0.0572` | `$0.0525` | **-8.23%** | **-8.59%** | +5.7% | -8.9% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+50.0%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `POPCAT`

* **Total Candidate Breakouts Filtered (Vetoed):** `102`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `70` (68.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+1,002.5%`
* **Missed Upside Forgone:** `-553.5%`
* **Net Veto Alpha:** `+449.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `40` | `39.2%` |
| `Core 1: Macro Bear Veto` | `35` | `34.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `17` | `16.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `10` | `9.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*