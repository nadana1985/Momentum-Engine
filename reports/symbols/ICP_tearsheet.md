# Kronos V12: Institutional Symbol Tear Sheet — `ICP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`30.756`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+36.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.43x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+11.99%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`107.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+23.7% / -2.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-06-21 16:00` | `2023-06-24 16:00` | 72.0h | `$4.2556` | `$4.2045` | **-1.20%** | **-1.21%** | +3.6% | -3.7% | `stagnation_cut` |
| 2 | Book 2 | `2026-05-05 11:00` | `2026-05-08 20:00` | 81.0h | `$2.4902` | `$3.4464` | **+38.40%** | **+32.50%** | +48.8% | -1.1% | `climax_top_harvest` |
| 3 | Book 2 | `2026-09-05 04:00` | `2026-09-12 04:00` | 168.0h | `$2.6316` | `$2.7581` | **+4.81%** | **+4.70%** | +18.8% | -2.4% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+32.5%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-1.2%`** |
| `time_cap` | `1` | `100.0%` | **`+4.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `ICP`

* **Total Candidate Breakouts Filtered (Vetoed):** `84`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `55` (65.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `14`
* **Saved Capital Losses Avoided:** `+628.9%`
* **Missed Upside Forgone:** `-629.3%`
* **Net Veto Alpha:** `+-0.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `70` | `83.3%` |
| `Core 4: Funding Rate Cap` | `14` | `16.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*