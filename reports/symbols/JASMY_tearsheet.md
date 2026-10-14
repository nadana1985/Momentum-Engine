# Kronos V12: Institutional Symbol Tear Sheet — `JASMY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.109`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+57.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.77x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+9.55%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-19.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`176.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+24.9% / -14.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-02-05 11:00` | `2023-02-09 11:00` | Live | `$0.0060` | `$0.0065` | **+8.50%** | **+8.16%** | +28.6% | -10.4% | `shelf_target_reclaim` |
| 2 | Book 4 | `2023-02-05 14:00` | `2023-02-13 09:00` | 187.0h | `$0.0071` | `$0.0060` | **-7.55%** | **-8.18%** | +18.5% | -17.4% | `structural_stop` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2023-05-03 04:00` | `2023-05-07 04:00` | Live | `$0.0061` | `$0.0066` | **+8.50%** | **+8.16%** | +18.0% | -33.0% | `shelf_target_reclaim` |
| 4 | Book 1 | `2023-11-05 07:00` | `2023-11-10 11:00` | 124.0h | `$0.0041` | `$0.0057` | **+53.03%** | **+42.66%** | +44.7% | -8.7% | `climax_top_harvest` |
| 5 | Book 4 | `2025-07-18 00:00` | `2025-07-30 11:00` | 299.0h | `$0.0178` | `$0.0152` | **-17.56%** | **-18.99%** | +15.9% | -15.0% | `structural_stop` |
| 6 | Book 1 | `2026-09-27 08:00` | `2026-10-01 08:00` | 96.0h | `$0.0049` | `$0.0059` | **+28.92%** | **+25.51%** | +23.4% | -2.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `structural_stop` | `2` | `0.0%` | **`-27.2%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+42.7%`** |
| `target_reclaim` | `1` | `100.0%` | **`+25.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `JASMY`

* **Total Candidate Breakouts Filtered (Vetoed):** `402`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `290` (72.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `30`
* **Saved Capital Losses Avoided:** `+4,173.9%`
* **Missed Upside Forgone:** `-1,610.6%`
* **Net Veto Alpha:** `+2,563.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `324` | `80.6%` |
| `Core 1: Macro Bear Veto` | `61` | `15.2%` |
| `Core 4: Funding Rate Cap` | `11` | `2.7%` |
| `Core 4: Defensible Whale Dump` | `4` | `1.0%` |
| `Core 4: Whale Firewall` | `1` | `0.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*