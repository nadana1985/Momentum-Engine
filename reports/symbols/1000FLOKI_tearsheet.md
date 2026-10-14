# Kronos V12: Institutional Symbol Tear Sheet — `1000FLOKI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`83.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`8.049`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+108.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.97x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+18.15%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`59.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+22.5% / -6.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-09-30 16:00` | `2023-10-04 00:00` | 80.0h | `$0.0190` | `$0.0175` | **-14.56%** | **-15.44%** | +10.0% | -10.1% | `initial_stop` |
| 2 | Book 2 | `2023-10-21 06:00` | `2023-10-21 16:00` | 10.0h | `$0.0216` | `$0.0259` | **+18.15%** | **+16.86%** | +23.1% | -5.5% | `target_reclaim` |
| 3 | Book 4 | `2023-10-22 07:00` | `2023-10-25 15:00` | 80.0h | `$0.0265` | `$0.0318` | **+18.45%** | **+16.99%** | +23.2% | -8.5% | `target_reclaim` |
| 4 | Book 1 | `2024-02-26 06:00` | `2024-02-27 12:00` | 30.0h | `$0.0374` | `$0.0479` | **+44.06%** | **+36.92%** | +36.2% | -5.4% | `climax_top_harvest` |
| 5 | Book 1 | `2025-04-22 14:00` | `2025-04-25 07:00` | 65.0h | `$0.0622` | `$0.0746` | **+32.75%** | **+28.64%** | +20.6% | -3.5% | `target_reclaim` |
| 6 | Book 4 | `2025-07-13 01:00` | `2025-07-16 19:00` | 90.0h | `$0.0987` | `$0.1184` | **+27.69%** | **+24.91%** | +21.7% | -6.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+87.4%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+36.9%`** |
| `initial_stop` | `1` | `0.0%` | **`-15.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000FLOKI`

* **Total Candidate Breakouts Filtered (Vetoed):** `496`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `284` (57.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `63`
* **Saved Capital Losses Avoided:** `+3,727.0%`
* **Missed Upside Forgone:** `-2,758.9%`
* **Net Veto Alpha:** `+968.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `440` | `88.7%` |
| `Core 1: Macro Bear Veto` | `50` | `10.1%` |
| `Core 4: Funding Rate Cap` | `5` | `1.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*