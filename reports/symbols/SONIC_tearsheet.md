# Kronos V12: Institutional Symbol Tear Sheet — `SONIC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`41.041`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+17.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.19x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.40%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-0.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`27.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.9% / -2.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-23 01:00` | `2025-04-23 05:00` | 4.0h | `$0.2486` | `$0.2590` | **+4.17%** | **+4.08%** | +7.1% | -1.6% | `target_reclaim` |
| 2 | Book 3 | `2025-06-17 15:00` | `2025-06-20 15:00` | 72.0h | `$0.2015` | `$0.2006` | **-0.44%** | **-0.44%** | +4.8% | -2.0% | `time_expiry` |
| 3 | Book 3 | `2025-07-24 05:00` | `2025-07-25 12:00` | 31.0h | `$0.2348` | `$0.2591` | **+10.36%** | **+9.86%** | +10.7% | -4.9% | `target_reclaim` |
| 4 | Book 3 | `2025-10-29 18:00` | `2025-10-29 19:00` | 1.0h | `$0.1288` | `$0.1342` | **+4.17%** | **+4.08%** | +5.1% | -1.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+18.0%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `SONIC`

* **Total Candidate Breakouts Filtered (Vetoed):** `52`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `36` (69.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+355.6%`
* **Missed Upside Forgone:** `-47.6%`
* **Net Veto Alpha:** `+308.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `19` | `36.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `18` | `34.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `15` | `28.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*