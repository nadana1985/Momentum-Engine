# Kronos V12: Institutional Symbol Tear Sheet — `1MBABYDOGE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`71.4%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.715`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+29.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.34x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.21%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`30.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.9% / -9.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-09-25 12:00` | `2024-09-29 12:00` | Live | `$0.0022` | `$0.0024` | **+8.50%** | **+8.16%** | +38.5% | -26.3% | `shelf_target_reclaim` |
| 2 | Book 3 | `2025-04-24 08:00` | `2025-04-25 07:00` | 23.0h | `$0.0013` | `$0.0014` | **+9.05%** | **+8.66%** | +9.5% | -11.9% | `target_reclaim` |
| 3 | Book 3 | `2025-04-26 09:00` | `2025-04-27 13:00` | 28.0h | `$0.0015` | `$0.0013` | **-8.23%** | **-8.59%** | +2.4% | -8.1% | `stop_loss` |
| 4 | Book 3 | `2025-05-10 03:00` | `2025-05-10 06:00` | 3.0h | `$0.0017` | `$0.0018` | **+5.12%** | **+4.99%** | +17.2% | -1.8% | `target_reclaim` |
| 5 | Book 3 | `2025-05-10 15:00` | `2025-05-13 11:00` | 68.0h | `$0.0017` | `$0.0020` | **+15.97%** | **+14.82%** | +17.1% | -3.6% | `target_reclaim` |
| 6 | Book 3 | `2025-05-14 08:00` | `2025-05-15 07:00` | 23.0h | `$0.0019` | `$0.0018` | **-8.23%** | **-8.59%** | +1.9% | -10.7% | `stop_loss` |
| 7 | Book 3 | `2025-07-15 03:00` | `2025-07-16 14:00` | 35.0h | `$0.0013` | `$0.0014` | **+10.52%** | **+10.00%** | +10.6% | -1.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+38.5%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `1MBABYDOGE`

* **Total Candidate Breakouts Filtered (Vetoed):** `163`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `132` (81.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+2,002.8%`
* **Missed Upside Forgone:** `-286.4%`
* **Net Veto Alpha:** `+1,716.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `112` | `68.7%` |
| `Core 1: Macro Bear Veto` | `44` | `27.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `3.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*