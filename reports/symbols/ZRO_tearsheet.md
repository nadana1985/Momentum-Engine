# Kronos V12: Institutional Symbol Tear Sheet — `ZRO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`42.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.665`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+22.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.25x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.19%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-24.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`120.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.1% / -6.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-12-02 08:00` | `2024-12-03 13:00` | 29.0h | `$6.5148` | `$5.9787` | **-8.23%** | **-8.59%** | +6.0% | -10.5% | `stop_loss` |
| 2 | Book 2 | `2025-05-08 04:00` | `2025-05-15 04:00` | 168.0h | `$2.5791` | `$2.9863` | **+17.93%** | **+16.65%** | +30.5% | -2.6% | `time_cap` |
| 3 | Book 2 | `2025-05-22 15:00` | `2025-05-23 12:00` | 21.0h | `$2.9315` | `$2.6902` | **-8.74%** | **-9.12%** | +3.1% | -8.1% | `initial_stop` |
| 4 | Book 2 | `2025-06-10 11:00` | `2025-06-12 20:00` | 57.0h | `$2.2591` | `$2.0732` | **-9.58%** | **-10.00%** | +6.4% | -9.2% | `initial_stop` |
| 5 | Book 1 | `2025-07-10 23:00` | `2025-07-23 20:00` | 309.0h | `$2.0730` | `$1.9958` | **-5.66%** | **-5.82%** | +18.6% | -5.3% | `fast_decay_cut` |
| 6 | Book 2 | `2025-08-07 11:00` | `2025-08-11 06:00` | 91.0h | `$1.8485` | `$2.4707` | **+39.45%** | **+34.00%** | +40.6% | -3.9% | `climax_top_harvest` |
| 7 | Book 2 | `2026-05-04 22:00` | `2026-05-11 22:00` | 168.0h | `$1.4494` | `$1.5179` | **+5.30%** | **+5.17%** | +7.3% | -4.4% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-19.1%`** |
| `time_cap` | `2` | `100.0%` | **`+21.8%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+34.0%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-5.8%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZRO`

* **Total Candidate Breakouts Filtered (Vetoed):** `308`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `198` (64.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `49`
* **Saved Capital Losses Avoided:** `+3,016.6%`
* **Missed Upside Forgone:** `-1,229.9%`
* **Net Veto Alpha:** `+1,786.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `306` | `99.4%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.3%` |
| `Core 4: Funding Rate Cap` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*