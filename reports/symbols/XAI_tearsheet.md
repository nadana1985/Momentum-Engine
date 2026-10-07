# Kronos V12: Institutional Symbol Tear Sheet — `XAI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.971`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-1.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.13%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`23.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.3% / -5.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-23 16:00` | `2024-02-23 18:00` | 2.0h | `$1.3522` | `$1.4698` | **+8.70%** | **+8.34%** | +9.1% | -0.8% | `target_reclaim` |
| 2 | Book 3 | `2024-02-27 20:00` | `2024-02-28 17:00` | 21.0h | `$1.4037` | `$1.2882` | **-8.23%** | **-8.59%** | +3.3% | -20.6% | `stop_loss` |
| 3 | Book 3 | `2024-05-29 16:00` | `2024-05-30 02:00` | 10.0h | `$0.7324` | `$0.7961` | **+8.70%** | **+8.34%** | +9.0% | -0.2% | `target_reclaim` |
| 4 | Book 3 | `2024-09-28 21:00` | `2024-10-01 15:00` | 66.0h | `$0.2296` | `$0.2107` | **-8.23%** | **-8.59%** | +8.0% | -9.4% | `stop_loss` |
| 5 | Book 3 | `2024-11-11 05:00` | `2024-11-11 17:00` | 12.0h | `$0.2259` | `$0.2455` | **+8.70%** | **+8.34%** | +12.9% | -0.1% | `target_reclaim` |
| 6 | Book 3 | `2024-11-12 10:00` | `2024-11-14 23:00` | 61.0h | `$0.2306` | `$0.2117` | **-8.23%** | **-8.59%** | +12.0% | -8.9% | `stop_loss` |
| 7 | Book 3 | `2024-12-02 03:00` | `2024-12-03 14:00` | 35.0h | `$0.3716` | `$0.3410` | **-8.23%** | **-8.59%** | +5.9% | -8.1% | `stop_loss` |
| 8 | Book 3 | `2024-12-05 01:00` | `2024-12-05 07:00` | 6.0h | `$0.3780` | `$0.4109` | **+8.70%** | **+8.34%** | +9.3% | -1.2% | `target_reclaim` |
| 9 | Book 3 | `2024-12-05 22:00` | `2024-12-06 01:00` | 3.0h | `$0.3917` | `$0.4258` | **+8.70%** | **+8.34%** | +8.8% | -0.7% | `target_reclaim` |
| 10 | Book 3 | `2025-04-21 15:00` | `2025-04-22 05:00` | 14.0h | `$0.0608` | `$0.0558` | **-8.23%** | **-8.59%** | +4.8% | -8.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `target_reclaim` | `5` | `100.0%` | **`+41.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `XAI`

* **Total Candidate Breakouts Filtered (Vetoed):** `109`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `63` (57.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+842.0%`
* **Missed Upside Forgone:** `-697.6%`
* **Net Veto Alpha:** `+144.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `51` | `46.8%` |
| `Core 1: Macro Bear Veto` | `26` | `23.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `18` | `16.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `14` | `12.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*