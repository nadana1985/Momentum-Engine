# Kronos V12: Institutional Symbol Tear Sheet — `ZETA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`71.4%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.262`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+21.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.24x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.10%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`53.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.2% / -6.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-10-24 08:00` | `2024-10-25 23:00` | 39.0h | `$0.6731` | `$0.6177` | **-8.23%** | **-8.59%** | +7.6% | -10.9% | `stop_loss` |
| 2 | Book 3 | `2024-12-02 03:00` | `2024-12-04 00:00` | 45.0h | `$0.8450` | `$0.9185` | **+8.70%** | **+8.34%** | +11.9% | -7.9% | `target_reclaim` |
| 3 | Book 3 | `2024-12-04 16:00` | `2024-12-07 16:00` | 72.0h | `$0.8758` | `$0.9254` | **+5.66%** | **+5.50%** | +7.7% | -4.8% | `time_expiry` |
| 4 | Book 3 | `2025-04-26 13:00` | `2025-04-29 12:00` | 71.0h | `$0.2597` | `$0.2823` | **+8.70%** | **+8.34%** | +10.4% | -6.6% | `target_reclaim` |
| 5 | Book 3 | `2025-07-15 01:00` | `2025-07-17 13:00` | 60.0h | `$0.2112` | `$0.2296` | **+8.70%** | **+8.34%** | +8.7% | -2.3% | `target_reclaim` |
| 6 | Book 3 | `2025-07-23 13:00` | `2025-07-24 06:00` | 17.0h | `$0.2260` | `$0.2074` | **-8.23%** | **-8.59%** | +2.1% | -9.5% | `stop_loss` |
| 7 | Book 3 | `2026-09-15 18:00` | `2026-09-18 13:00` | 67.0h | `$0.0338` | `$0.0367` | **+8.70%** | **+8.34%** | +9.0% | -4.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+5.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZETA`

* **Total Candidate Breakouts Filtered (Vetoed):** `85`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `60` (70.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `10`
* **Saved Capital Losses Avoided:** `+826.2%`
* **Missed Upside Forgone:** `-372.9%`
* **Net Veto Alpha:** `+453.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `30` | `35.3%` |
| `Core 1: Macro Bear Veto` | `24` | `28.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `24` | `28.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `8.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*