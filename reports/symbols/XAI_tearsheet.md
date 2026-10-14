# Kronos V12: Institutional Symbol Tear Sheet — `XAI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`77.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.636`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+28.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.32x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.12%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`13.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.0% / -3.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-23 16:00` | `2024-02-23 18:00` | 2.0h | `$1.3522` | `$1.4698` | **+8.70%** | **+8.34%** | +9.1% | -0.8% | `target_reclaim` |
| 2 | Book 3 | `2024-02-27 20:00` | `2024-02-28 17:00` | 21.0h | `$1.4037` | `$1.2882` | **-8.23%** | **-8.59%** | +3.3% | -20.6% | `stop_loss` |
| 3 | Book 3 | `2024-05-29 16:00` | `2024-05-30 02:00` | 10.0h | `$0.7348` | `$0.7961` | **+8.34%** | **+8.01%** | +8.6% | -0.5% | `target_reclaim` |
| 4 | Book 3 | `2024-09-20 13:00` | `2024-09-21 23:00` | 34.0h | `$0.2011` | `$0.2095` | **+4.17%** | **+4.08%** | +4.5% | -1.0% | `target_reclaim` |
| 5 | Book 3 | `2024-09-26 00:00` | `2024-09-26 05:00` | 5.0h | `$0.2164` | `$0.2254` | **+4.17%** | **+4.08%** | +5.3% | -0.5% | `target_reclaim` |
| 6 | Book 3 | `2024-12-02 03:00` | `2024-12-03 14:00` | 35.0h | `$0.3716` | `$0.3410` | **-8.23%** | **-8.59%** | +5.9% | -8.1% | `stop_loss` |
| 7 | Book 3 | `2024-12-05 01:00` | `2024-12-05 07:00` | 6.0h | `$0.3780` | `$0.4109` | **+8.70%** | **+8.34%** | +9.3% | -1.2% | `target_reclaim` |
| 8 | Book 3 | `2024-12-05 22:00` | `2024-12-06 01:00` | 3.0h | `$0.3917` | `$0.4258` | **+8.70%** | **+8.34%** | +8.8% | -0.7% | `target_reclaim` |
| 9 | Book 3 | `2025-04-21 13:00` | `2025-04-21 14:00` | 1.0h | `$0.0635` | `$0.0661` | **+4.17%** | **+4.08%** | +7.8% | -1.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `7` | `100.0%` | **`+45.3%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `XAI`

* **Total Candidate Breakouts Filtered (Vetoed):** `420`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `285` (67.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+5,375.8%`
* **Missed Upside Forgone:** `-697.6%`
* **Net Veto Alpha:** `+4,678.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `362` | `86.2%` |
| `Core 1: Macro Bear Veto` | `26` | `6.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `18` | `4.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `14` | `3.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*