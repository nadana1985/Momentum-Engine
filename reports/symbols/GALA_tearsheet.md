# Kronos V12: Institutional Symbol Tear Sheet — `GALA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+109.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.98x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+21.82%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`216.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+27.1% / -9.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2023-01-23 12:00` | `2023-01-28 04:00` | 112.0h | `$0.0525` | `$0.0630` | **+11.58%** | **+11.05%** | +20.1% | -12.7% | `target_reclaim` |
| 2 | Book 4 | `2023-11-09 17:00` | `2023-12-04 07:00` | 590.0h | `$0.0235` | `$0.0282` | **+35.96%** | **+31.45%** | +21.2% | -12.8% | `target_reclaim` |
| 3 | Book 1 | `2024-02-21 05:00` | `2024-02-28 17:00` | 180.0h | `$0.0288` | `$0.0353` | **+41.09%** | **+35.36%** | +50.0% | -9.0% | `trail_stop` |
| 4 | Book 2 | `2024-09-18 02:00` | `2024-09-25 02:00` | 168.0h | `$0.0187` | `$0.0222` | **+22.00%** | **+20.20%** | +20.0% | -7.5% | `time_cap` |
| 5 | Book 4 | `2024-11-11 00:00` | `2024-11-12 08:00` | 32.0h | `$0.0256` | `$0.0307` | **+11.58%** | **+11.05%** | +23.9% | -3.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+53.6%`** |
| `time_cap` | `1` | `100.0%` | **`+20.2%`** |
| `trail_stop` | `1` | `100.0%` | **`+35.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `GALA`

* **Total Candidate Breakouts Filtered (Vetoed):** `614`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `342` (55.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `171`
* **Saved Capital Losses Avoided:** `+4,294.9%`
* **Missed Upside Forgone:** `-6,398.0%`
* **Net Veto Alpha:** `+-2,103.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `508` | `82.7%` |
| `Core 1: Macro Bear Veto` | `41` | `6.7%` |
| `Core 4: Funding Rate Cap` | `36` | `5.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `28` | `4.6%` |
| `Core 4: Whale Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*