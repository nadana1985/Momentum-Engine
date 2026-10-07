# Kronos V12: Institutional Symbol Tear Sheet — `ZRX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`50.731`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+26.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.30x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.54%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-0.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`109.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.5% / -2.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-01-09 00:00` | `2023-01-11 04:00` | 52.0h | `$0.1711` | `$0.1707` | **-0.27%** | **-0.27%** | +2.6% | -3.1% | `fast_decay_cut` |
| 2 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.2133` | `$0.2488` | **+16.61%** | **+15.37%** | +19.0% | -4.0% | `time_cap` |
| 3 | Book 2 | `2024-09-13 16:00` | `2024-09-15 17:00` | 49.0h | `$0.2924` | `$0.2917` | **-0.26%** | **-0.26%** | +3.5% | -1.2% | `fast_decay_cut` |
| 4 | Book 2 | `2026-05-06 03:00` | `2026-05-13 03:00` | 168.0h | `$0.1142` | `$0.1279` | **+11.99%** | **+11.33%** | +12.8% | -2.9% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-0.5%`** |
| `time_cap` | `2` | `100.0%` | **`+26.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZRX`

* **Total Candidate Breakouts Filtered (Vetoed):** `317`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `209` (65.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `67`
* **Saved Capital Losses Avoided:** `+2,717.3%`
* **Missed Upside Forgone:** `-2,865.9%`
* **Net Veto Alpha:** `+-148.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `110` | `34.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `75` | `23.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `63` | `19.9%` |
| `Core 1: Macro Bear Veto` | `51` | `16.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `18` | `5.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*