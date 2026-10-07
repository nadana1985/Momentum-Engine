# Kronos V12: Institutional Symbol Tear Sheet — `PENDLE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.959`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+17.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.19x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.85%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`119.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.5% / -5.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-04-21 00:00` | `2025-04-27 13:00` | 157.0h | `$3.2389` | `$3.2469` | **+0.25%** | **+0.25%** | +16.3% | -4.0% | `breakeven_ratchet` |
| 2 | Book 2 | `2025-06-16 19:00` | `2025-06-17 15:00` | 20.0h | `$4.1260` | `$3.7864` | **-8.23%** | **-8.59%** | +0.6% | -9.5% | `initial_stop` |
| 3 | Book 2 | `2025-07-09 13:00` | `2025-07-16 13:00` | 168.0h | `$3.5849` | `$4.1610` | **+16.07%** | **+14.90%** | +17.9% | -1.3% | `time_cap` |
| 4 | Book 2 | `2025-08-07 10:00` | `2025-08-14 10:00` | 168.0h | `$4.3762` | `$5.3147` | **+21.44%** | **+19.43%** | +37.1% | -3.3% | `time_cap` |
| 5 | Book 1 | `2025-09-19 00:00` | `2025-09-20 12:00` | 36.0h | `$5.3997` | `$5.0592` | **-8.82%** | **-9.23%** | +0.4% | -9.0% | `stall_bailout` |
| 6 | Book 2 | `2026-09-03 22:00` | `2026-09-10 22:00` | 168.0h | `$1.9776` | `$1.9843` | **+0.34%** | **+0.34%** | +15.0% | -6.4% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `3` | `100.0%` | **`+34.7%`** |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `stall_bailout` | `1` | `0.0%` | **`-9.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `PENDLE`

* **Total Candidate Breakouts Filtered (Vetoed):** `113`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `64` (56.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+741.5%`
* **Missed Upside Forgone:** `-282.0%`
* **Net Veto Alpha:** `+459.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `63` | `55.8%` |
| `Core 4: Funding Rate Cap` | `24` | `21.2%` |
| `Core 4: Whale Firewall` | `18` | `15.9%` |
| `Core 4: Defensible Whale Dump` | `8` | `7.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*