# Kronos V12: Institutional Symbol Tear Sheet — `ZRO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.117`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+25.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.29x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.25%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-22.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`135.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.8% / -5.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-05-08 04:00` | `2025-05-15 04:00` | 168.0h | `$2.5791` | `$2.9863` | **+15.79%** | **+14.66%** | +30.5% | -2.6% | `time_cap` |
| 2 | Book 2 | `2025-05-22 15:00` | `2025-05-23 12:00` | 21.0h | `$2.9315` | `$2.6902` | **-8.23%** | **-8.59%** | +3.1% | -8.1% | `initial_stop` |
| 3 | Book 2 | `2025-06-10 11:00` | `2025-06-12 20:00` | 57.0h | `$2.2591` | `$2.0732` | **-8.23%** | **-8.59%** | +6.4% | -9.2% | `initial_stop` |
| 4 | Book 1 | `2025-07-10 23:00` | `2025-07-23 20:00` | 309.0h | `$2.0730` | `$1.9958` | **-5.47%** | **-5.63%** | +18.6% | -5.3% | `fast_decay_cut` |
| 5 | Book 2 | `2025-08-07 11:00` | `2025-08-11 06:00` | 91.0h | `$1.8485` | `$2.4707` | **+33.66%** | **+29.01%** | +40.6% | -3.9% | `climax_top_harvest` |
| 6 | Book 2 | `2026-05-04 22:00` | `2026-05-11 22:00` | 168.0h | `$1.4494` | `$1.5179` | **+4.72%** | **+4.62%** | +7.3% | -4.4% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `100.0%` | **`+19.3%`** |
| `initial_stop` | `2` | `0.0%` | **`-17.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-5.6%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+29.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZRO`

* **Total Candidate Breakouts Filtered (Vetoed):** `67`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `46` (68.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `7`
* **Saved Capital Losses Avoided:** `+632.5%`
* **Missed Upside Forgone:** `-186.4%`
* **Net Veto Alpha:** `+446.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `65` | `97.0%` |
| `Core 4: Defensible Whale Dump` | `1` | `1.5%` |
| `Core 4: Funding Rate Cap` | `1` | `1.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*