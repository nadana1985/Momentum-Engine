# Kronos V12: Institutional Symbol Tear Sheet — `WLD`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.377`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+27.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.32x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.99%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-11.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`112.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+22.6% / -7.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-10-06 17:00` | `2023-10-09 09:00` | 64.0h | `$1.6563` | `$1.5200` | **-8.23%** | **-8.59%** | +1.9% | -10.8% | `initial_stop` |
| 2 | Book 2 | `2024-10-11 14:00` | `2024-10-16 07:00` | 113.0h | `$1.9456` | `$2.2469` | **+15.49%** | **+14.40%** | +36.2% | -3.6% | `trail_stop` |
| 3 | Book 1 | `2025-04-22 21:00` | `2025-05-04 00:00` | 267.0h | `$0.8267` | `$0.9418` | **+20.31%** | **+18.49%** | +52.3% | -3.2% | `trail_stop` |
| 4 | Book 2 | `2025-05-08 15:00` | `2025-05-15 15:00` | 168.0h | `$1.0265` | `$1.1933` | **+16.25%** | **+15.06%** | +32.6% | -2.7% | `time_cap` |
| 5 | Book 2 | `2025-06-10 11:00` | `2025-06-12 08:00` | 45.0h | `$1.1828` | `$1.0855` | **-8.23%** | **-8.59%** | +3.1% | -8.0% | `initial_stop` |
| 6 | Book 1 | `2025-07-10 21:00` | `2025-07-14 20:00` | 95.0h | `$1.0550` | `$1.0332` | **-3.07%** | **-3.12%** | +8.1% | -6.0% | `fast_decay_cut` |
| 7 | Book 1 | `2026-08-20 17:00` | `2026-08-22 05:00` | 36.0h | `$0.3749` | `$0.3759` | **+0.29%** | **+0.29%** | +23.7% | -17.1% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-17.2%`** |
| `trail_stop` | `2` | `100.0%` | **`+32.9%`** |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-3.1%`** |
| `time_cap` | `1` | `100.0%` | **`+15.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `WLD`

* **Total Candidate Breakouts Filtered (Vetoed):** `96`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `64` (66.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `31`
* **Saved Capital Losses Avoided:** `+1,084.6%`
* **Missed Upside Forgone:** `-1,809.7%`
* **Net Veto Alpha:** `+-725.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `67` | `69.8%` |
| `Core 4: Funding Rate Cap` | `15` | `15.6%` |
| `Core 4: Defensible Whale Dump` | `8` | `8.3%` |
| `Core 4: Whale Firewall` | `6` | `6.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*