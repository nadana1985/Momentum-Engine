# Kronos V12: Institutional Symbol Tear Sheet — `KSM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.777`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+4.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.01%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-4.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`76.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.9% / -3.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 15:00` | `2022-10-27 20:00` | 53.0h | `$35.3782` | `$35.0621` | **-0.89%** | **-0.90%** | +5.4% | -2.1% | `fast_decay_cut` |
| 2 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$32.8920` | `$36.0796` | **+9.69%** | **+9.25%** | +15.5% | -5.7% | `time_cap` |
| 3 | Book 2 | `2023-09-21 00:00` | `2023-09-22 12:00` | 36.0h | `$19.9197` | `$19.2617` | **-3.30%** | **-3.36%** | +0.3% | -4.3% | `stall_bailout` |
| 4 | Book 2 | `2026-05-04 00:00` | `2026-05-06 00:00` | 48.0h | `$4.9313` | `$4.8848` | **-0.94%** | **-0.95%** | +2.4% | -3.4% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-1.8%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.4%`** |
| `time_cap` | `1` | `100.0%` | **`+9.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `KSM`

* **Total Candidate Breakouts Filtered (Vetoed):** `395`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `228` (57.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `75`
* **Saved Capital Losses Avoided:** `+2,758.7%`
* **Missed Upside Forgone:** `-3,042.0%`
* **Net Veto Alpha:** `+-283.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `143` | `36.2%` |
| `Core 1: Macro Bear Veto` | `83` | `21.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `81` | `20.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `55` | `13.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `33` | `8.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*