# Kronos V12: Institutional Symbol Tear Sheet — `TURTLE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+23.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.26x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.80%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`54.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.9% / -3.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0440` | `$0.0445` | **+1.27%** | **+1.26%** | +9.8% | -4.5% | `time_expiry` |
| 2 | Book 3 | `2026-09-24 10:00` | `2026-09-24 15:00` | 5.0h | `$0.0413` | `$0.0434` | **+5.14%** | **+5.01%** | +5.7% | -0.3% | `target_reclaim` |
| 3 | Book 3 | `2026-09-28 07:00` | `2026-10-01 07:00` | 72.0h | `$0.0428` | `$0.0429` | **+0.37%** | **+0.37%** | +2.4% | -2.8% | `time_expiry` |
| 4 | Book 3 | `2026-10-05 19:00` | `2026-10-08 16:00` | 69.0h | `$0.0428` | `$0.0505` | **+18.00%** | **+16.55%** | +21.8% | -8.1% | `climax_whale_euphoria_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `2` | `100.0%` | **`+1.6%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+5.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `TURTLE`

* **Total Candidate Breakouts Filtered (Vetoed):** `29`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `28` (96.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+318.0%`
* **Missed Upside Forgone:** `-48.7%`
* **Net Veto Alpha:** `+269.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `20` | `69.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `9` | `31.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*