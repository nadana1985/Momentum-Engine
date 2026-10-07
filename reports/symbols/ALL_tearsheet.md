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
| **Profit Factor (Log-Space)** | **`3.234`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+4.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.05x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.44%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-2.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`108.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.7% / -2.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-05 20:00` | `2026-05-12 20:00` | 168.0h | `$0.5905` | `$0.6336` | **+7.31%** | **+7.05%** | +10.1% | -1.0% | `time_cap` |
| 2 | Book 2 | `2026-09-13 03:00` | `2026-09-15 03:00` | 48.0h | `$0.5774` | `$0.5650` | **-2.16%** | **-2.18%** | +1.3% | -3.8% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-2.2%`** |
| `time_cap` | `1` | `100.0%` | **`+7.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALL`

* **Total Candidate Breakouts Filtered (Vetoed):** `121`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `57` (47.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `1`
* **Saved Capital Losses Avoided:** `+332.8%`
* **Missed Upside Forgone:** `-21.4%`
* **Net Veto Alpha:** `+311.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `65` | `53.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `54` | `44.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `2` | `1.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*