# Kronos V12: Institutional Symbol Tear Sheet — `SEI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.686`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+53.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.71x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+8.92%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-6.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`82.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+21.4% / -6.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-11-08 12:00` | `2023-11-09 16:00` | 28.0h | `$0.1266` | `$0.1111` | **-12.22%** | **-13.03%** | +3.9% | -18.7% | `initial_stop` |
| 2 | Book 1 | `2023-11-10 20:00` | `2023-11-17 10:00` | 158.0h | `$0.1324` | `$0.1435` | **+8.34%** | **+8.01%** | +32.4% | -6.0% | `trail_stop` |
| 3 | Book 2 | `2024-09-18 23:00` | `2024-09-25 01:00` | 146.0h | `$0.3114` | `$0.4606` | **+47.94%** | **+39.16%** | +52.4% | -4.2% | `climax_top_harvest` |
| 4 | Book 2 | `2026-05-04 02:00` | `2026-05-05 14:00` | 36.0h | `$0.0603` | `$0.0593` | **-1.64%** | **-1.65%** | +0.1% | -3.8% | `stall_bailout` |
| 5 | Book 2 | `2026-09-02 19:00` | `2026-09-04 19:00` | 48.0h | `$0.0496` | `$0.0470` | **-5.11%** | **-5.24%** | +1.1% | -7.4% | `fast_decay_cut` |
| 6 | Book 2 | `2026-09-18 04:00` | `2026-09-21 13:00` | 81.0h | `$0.0467` | `$0.0607` | **+30.07%** | **+26.29%** | +38.5% | -1.4% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `2` | `100.0%` | **`+65.5%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-5.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-13.0%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.7%`** |
| `trail_stop` | `1` | `100.0%` | **`+8.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `SEI`

* **Total Candidate Breakouts Filtered (Vetoed):** `138`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `94` (68.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+1,067.8%`
* **Missed Upside Forgone:** `-585.7%`
* **Net Veto Alpha:** `+482.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `63` | `45.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `55` | `39.9%` |
| `Core 4: Funding Rate Cap` | `13` | `9.4%` |
| `Core 4: Whale Firewall` | `4` | `2.9%` |
| `Core 4: Defensible Whale Dump` | `3` | `2.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*