# Kronos V12: Institutional Symbol Tear Sheet — `ALL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`6.928`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+6.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.10%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.9% / -3.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-05 20:00` | `2026-05-12 20:00` | 168.0h | `$0.5905` | `$0.6336` | **+7.50%** | **+7.24%** | +10.1% | -1.0% | `time_cap` |
| 2 | Book 4 | `2026-08-22 05:00` | `2026-08-29 05:00` | 168.0h | `$0.5562` | `$0.5474` | **-1.03%** | **-1.05%** | +1.7% | -6.7% | `stagnation_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stagnation_cut` | `1` | `0.0%` | **`-1.0%`** |
| `time_cap` | `1` | `100.0%` | **`+7.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALL`

* **Total Candidate Breakouts Filtered (Vetoed):** `115`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `49` (42.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `1`
* **Saved Capital Losses Avoided:** `+248.7%`
* **Missed Upside Forgone:** `-21.4%`
* **Net Veto Alpha:** `+227.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `65` | `56.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `46` | `40.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `2` | `1.7%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `1.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*