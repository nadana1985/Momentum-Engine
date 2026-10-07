# Kronos V12: Institutional Symbol Tear Sheet — `LTC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.913`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+15.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.16x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.54%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-13.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`170.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.3% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 19:00` | `2022-10-28 19:00` | 72.0h | `$56.9119` | `$55.0121` | **-3.34%** | **-3.40%** | +1.2% | -6.1% | `stagnation_cut` |
| 2 | Book 2 | `2023-01-14 00:00` | `2023-01-17 00:00` | 72.0h | `$88.7814` | `$85.5656` | **-3.62%** | **-3.69%** | +3.6% | -6.2% | `stagnation_cut` |
| 3 | Book 2 | `2023-02-15 12:00` | `2023-02-22 12:00` | 168.0h | `$98.3653` | `$94.3436` | **-4.09%** | **-4.17%** | +7.6% | -6.9% | `time_cap` |
| 4 | Book 2 | `2023-09-19 09:00` | `2023-09-20 21:00` | 36.0h | `$68.0697` | `$64.4585` | **-5.31%** | **-5.45%** | +0.5% | -7.2% | `stall_bailout` |
| 5 | Book 1 | `2025-07-18 03:00` | `2025-08-08 03:00` | 504.0h | `$108.0895` | `$121.0965` | **+9.70%** | **+9.26%** | +19.5% | -7.9% | `time_cap` |
| 6 | Book 2 | `2026-09-18 22:00` | `2026-09-25 22:00` | 168.0h | `$57.9245` | `$72.6978` | **+25.50%** | **+22.72%** | +29.0% | -2.5% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `3` | `66.7%` | **`+27.8%`** |
| `stagnation_cut` | `2` | `0.0%` | **`-7.1%`** |
| `stall_bailout` | `1` | `0.0%` | **`-5.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `LTC`

* **Total Candidate Breakouts Filtered (Vetoed):** `246`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `138` (56.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+1,683.4%`
* **Missed Upside Forgone:** `-319.3%`
* **Net Veto Alpha:** `+1,364.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `157` | `63.8%` |
| `Core 1: Macro Bear Veto` | `58` | `23.6%` |
| `Core 4: Funding Rate Cap` | `24` | `9.8%` |
| `Core 4: Defensible Whale Dump` | `4` | `1.6%` |
| `Core 4: Whale Firewall` | `3` | `1.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*