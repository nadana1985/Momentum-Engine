# Kronos V12: Institutional Symbol Tear Sheet — `BAT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.665`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+5.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.90%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`133.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.9% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.2251` | `$0.2563` | **+13.86%** | **+12.98%** | +17.6% | -3.4% | `time_cap` |
| 2 | Book 2 | `2023-06-21 16:00` | `2023-06-28 16:00` | 168.0h | `$0.1860` | `$0.1884` | **+1.32%** | **+1.32%** | +10.1% | -2.3% | `time_cap` |
| 3 | Book 2 | `2026-09-13 02:00` | `2026-09-15 18:00` | 64.0h | `$0.0776` | `$0.0712` | **-8.23%** | **-8.59%** | +8.2% | -9.4% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `100.0%` | **`+14.3%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `BAT`

* **Total Candidate Breakouts Filtered (Vetoed):** `430`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `215` (50.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `49`
* **Saved Capital Losses Avoided:** `+2,445.1%`
* **Missed Upside Forgone:** `-1,676.2%`
* **Net Veto Alpha:** `+768.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `174` | `40.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `113` | `26.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `84` | `19.5%` |
| `Core 1: Macro Bear Veto` | `56` | `13.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*