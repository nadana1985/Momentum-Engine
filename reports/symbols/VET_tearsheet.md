# Kronos V12: Institutional Symbol Tear Sheet — `VET`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`85.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`12.424`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+153.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`4.64x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+21.93%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-13.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`183.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.8% / -3.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2020-11-21 07:00` | `2020-11-23 04:00` | 45.0h | `$0.0125` | `$0.0150` | **+10.65%** | **+10.17%** | +20.2% | -0.4% | `target_reclaim` |
| 2 | Book 4 | `2021-08-05 17:00` | `2021-08-08 00:00` | 55.0h | `$0.0910` | `$0.1092` | **+29.11%** | **+26.06%** | +21.7% | -1.7% | `target_reclaim` |
| 3 | Book 1 | `2023-01-12 01:00` | `2023-01-21 10:00` | 225.0h | `$0.0188` | `$0.0226` | **+31.29%** | **+27.37%** | +20.1% | -4.2% | `target_reclaim` |
| 4 | Book 4 | `2023-02-01 21:00` | `2023-02-13 17:00` | 284.0h | `$0.0252` | `$0.0221` | **-12.60%** | **-13.44%** | +6.2% | -12.3% | `structural_stop` |
| 5 | Book 4 | `2023-10-24 22:00` | `2023-11-08 17:00` | 355.0h | `$0.0187` | `$0.0224` | **+16.83%** | **+15.75%** | +20.7% | -2.9% | `target_reclaim` |
| 6 | Book 4 | `2024-11-15 20:00` | `2024-11-16 18:00` | 22.0h | `$0.0262` | `$0.0314` | **+78.60%** | **+60.46%** | +21.0% | -0.8% | `target_reclaim` |
| 7 | Book 1 | `2026-08-26 22:00` | `2026-09-08 09:00` | 299.0h | `$0.0064` | `$0.0076` | **+30.75%** | **+27.17%** | +21.6% | -3.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+167.0%`** |
| `structural_stop` | `1` | `0.0%` | **`-13.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `VET`

* **Total Candidate Breakouts Filtered (Vetoed):** `1346`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `653` (48.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `278`
* **Saved Capital Losses Avoided:** `+8,829.1%`
* **Missed Upside Forgone:** `-9,166.0%`
* **Net Veto Alpha:** `+-336.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `689` | `51.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `549` | `40.8%` |
| `Core 1: Macro Bear Veto` | `96` | `7.1%` |
| `Core 4: Funding Rate Cap` | `12` | `0.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*