# Kronos V12: Institutional Symbol Tear Sheet — `GLM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`77.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.768`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+30.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.35x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.37%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`47.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.5% / -3.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-07-23 05:00` | `2024-07-24 10:00` | 29.0h | `$0.3358` | `$0.3650` | **+8.70%** | **+8.34%** | +8.8% | -3.3% | `target_reclaim` |
| 2 | Book 3 | `2024-10-01 15:00` | `2024-10-02 13:00` | 22.0h | `$0.3448` | `$0.3164` | **-8.23%** | **-8.59%** | +0.5% | -8.0% | `stop_loss` |
| 3 | Book 3 | `2024-11-12 10:00` | `2024-11-12 22:00` | 12.0h | `$0.3317` | `$0.3522` | **+6.17%** | **+5.99%** | +6.7% | -1.9% | `target_reclaim` |
| 4 | Book 3 | `2024-11-20 03:00` | `2024-11-23 03:00` | 72.0h | `$0.3453` | `$0.3694` | **+6.96%** | **+6.73%** | +9.7% | -2.9% | `time_expiry` |
| 5 | Book 3 | `2025-04-28 01:00` | `2025-05-01 01:00` | 72.0h | `$0.2664` | `$0.2693` | **+1.08%** | **+1.07%** | +6.3% | -1.9% | `time_expiry` |
| 6 | Book 3 | `2025-05-11 07:00` | `2025-05-13 19:00` | 60.0h | `$0.2869` | `$0.2989` | **+4.17%** | **+4.08%** | +4.7% | -3.8% | `target_reclaim` |
| 7 | Book 3 | `2025-07-28 00:00` | `2025-07-28 22:00` | 22.0h | `$0.3003` | `$0.2756` | **-8.23%** | **-8.59%** | +8.4% | -8.1% | `stop_loss` |
| 8 | Book 4 | `2026-01-02 13:00` | `2026-01-07 23:00` | 130.0h | `$0.2294` | `$0.2753` | **+14.76%** | **+13.92%** | +21.6% | -1.5% | `target_reclaim` |
| 9 | Book 3 | `2026-10-08 15:00` | `2026-10-08 20:00` | 5.0h | `$0.1235` | `$0.1330` | **+7.70%** | **+7.42%** | +9.6% | -0.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+39.7%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `2` | `100.0%` | **`+7.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `GLM`

* **Total Candidate Breakouts Filtered (Vetoed):** `667`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `360` (54.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `57`
* **Saved Capital Losses Avoided:** `+5,292.8%`
* **Missed Upside Forgone:** `-1,575.9%`
* **Net Veto Alpha:** `+3,716.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `444` | `66.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `200` | `30.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `22` | `3.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*