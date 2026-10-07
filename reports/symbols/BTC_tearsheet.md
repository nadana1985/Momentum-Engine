# Kronos V12: Institutional Symbol Tear Sheet — `BTC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`20.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.603`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-9.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.91x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.91%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-9.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`79.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.2% / -3.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-07-13 18:00` | `2023-07-14 18:00` | 24.0h | `$31325.8193` | `$29949.6881` | **-4.39%** | **-4.49%** | +1.7% | -4.2% | `initial_stop` |
| 2 | Book 2 | `2023-12-08 21:00` | `2023-12-10 09:00` | 36.0h | `$44683.4300` | `$43516.0373` | **-2.61%** | **-2.65%** | +0.2% | -2.5% | `stall_bailout` |
| 3 | Book 2 | `2023-12-20 14:00` | `2023-12-23 14:00` | 72.0h | `$44004.6372` | `$43708.5548` | **-0.67%** | **-0.68%** | +1.1% | -1.7% | `stagnation_cut` |
| 4 | Book 2 | `2024-05-15 15:00` | `2024-05-22 15:00` | 168.0h | `$64847.2137` | `$70309.4858` | **+8.42%** | **+8.09%** | +11.2% | -0.8% | `time_cap` |
| 5 | Book 2 | `2024-10-29 14:00` | `2024-11-01 14:00` | 72.0h | `$72026.3167` | `$71095.2165` | **-1.29%** | **-1.30%** | +2.3% | -4.4% | `stagnation_cut` |
| 6 | Book 2 | `2025-01-06 15:00` | `2025-01-07 19:00` | 28.0h | `$102359.7612` | `$96224.3679` | **-5.99%** | **-6.18%** | +0.4% | -5.9% | `initial_stop` |
| 7 | Book 2 | `2025-04-21 01:00` | `2025-04-28 01:00` | 168.0h | `$87467.0222` | `$92665.9545` | **+5.94%** | **+5.77%** | +9.5% | -1.3% | `time_cap` |
| 8 | Book 2 | `2025-06-16 14:00` | `2025-06-17 16:00` | 26.0h | `$107749.8028` | `$103549.8029` | **-3.90%** | **-3.98%** | +1.1% | -4.0% | `initial_stop` |
| 9 | Book 2 | `2025-10-02 19:00` | `2025-10-09 19:00` | 168.0h | `$121089.8697` | `$120595.3560` | **-0.41%** | **-0.41%** | +4.2% | -1.6% | `time_cap` |
| 10 | Book 2 | `2026-05-06 09:00` | `2026-05-07 21:00` | 36.0h | `$82164.1983` | `$79484.4907` | **-3.26%** | **-3.32%** | +0.8% | -3.3% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `3` | `0.0%` | **`-14.6%`** |
| `time_cap` | `3` | `66.7%` | **`+13.5%`** |
| `stagnation_cut` | `2` | `0.0%` | **`-2.0%`** |
| `stall_bailout` | `2` | `0.0%` | **`-6.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `BTC`

* **Total Candidate Breakouts Filtered (Vetoed):** `258`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `114` (44.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+805.8%`
* **Missed Upside Forgone:** `-113.3%`
* **Net Veto Alpha:** `+692.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: Defensible Whale Dump` | `120` | `46.5%` |
| `Core 1: Macro Bear Veto` | `61` | `23.6%` |
| `Core 4: Funding Rate Cap` | `58` | `22.5%` |
| `Core 0: Zero-Tolerance Data Firewall` | `19` | `7.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*