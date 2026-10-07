# Kronos V12: Institutional Symbol Tear Sheet — `LYTE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.444`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+1.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.79%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`102.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.1% / -1.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-16 15:00` | `2026-09-23 15:00` | 168.0h | `$25.2229` | `$25.7455` | **+2.07%** | **+2.05%** | +7.5% | -2.1% | `time_cap` |
| 2 | Book 2 | `2026-10-02 14:00` | `2026-10-04 02:00` | 36.0h | `$25.9647` | `$25.8452` | **-0.46%** | **-0.46%** | +0.6% | -1.6% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `1` | `0.0%` | **`-0.5%`** |
| `time_cap` | `1` | `100.0%` | **`+2.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `LYTE`

* **Total Candidate Breakouts Filtered (Vetoed):** `2`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `2` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+8.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+8.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `2` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*