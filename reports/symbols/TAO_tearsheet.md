# Kronos V12: Institutional Symbol Tear Sheet — `TAO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`16.7%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.102`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-37.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.69x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-6.30%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-42.1%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`131.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.9% / -15.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2025-07-11 04:00` | `2025-07-29 00:00` | 428.0h | `$384.3786` | `$395.8978` | **+4.39%** | **+4.29%** | +20.1% | -2.9% | `trail_stop` |
| 2 | Book 2 | `2025-08-09 05:00` | `2025-08-12 05:00` | 72.0h | `$384.9901` | `$361.6436` | **-6.06%** | **-6.26%** | +3.6% | -7.1% | `stagnation_cut` |
| 3 | Book 1 | `2025-09-18 18:00` | `2025-09-20 06:00` | 36.0h | `$372.6493` | `$344.9654` | **-10.68%** | **-11.29%** | +0.1% | -8.3% | `stall_bailout` |
| 4 | Book 1 | `2025-10-10 08:00` | `2025-10-10 21:00` | 13.0h | `$370.8548` | `$314.4385` | **-16.74%** | **-18.32%** | +7.3% | -64.8% | `initial_stop` |
| 5 | Book 2 | `2026-05-02 19:00` | `2026-05-05 19:00` | 72.0h | `$290.7350` | `$285.3449` | **-1.85%** | **-1.87%** | +1.8% | -5.0% | `stagnation_cut` |
| 6 | Book 2 | `2026-09-06 11:00` | `2026-09-13 11:00` | 168.0h | `$242.4446` | `$232.0584` | **-4.28%** | **-4.38%** | +14.3% | -6.1% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stagnation_cut` | `2` | `0.0%` | **`-8.1%`** |
| `initial_stop` | `1` | `0.0%` | **`-18.3%`** |
| `stall_bailout` | `1` | `0.0%` | **`-11.3%`** |
| `time_cap` | `1` | `0.0%` | **`-4.4%`** |
| `trail_stop` | `1` | `100.0%` | **`+4.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `TAO`

* **Total Candidate Breakouts Filtered (Vetoed):** `80`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `37` (46.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+418.8%`
* **Missed Upside Forgone:** `-467.9%`
* **Net Veto Alpha:** `+-49.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `76` | `95.0%` |
| `Core 4: Defensible Whale Dump` | `3` | `3.8%` |
| `Core 4: Whale Firewall` | `1` | `1.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*