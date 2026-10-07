# Kronos V12: Institutional Symbol Tear Sheet — `NXPC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`9.904`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+7.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.75%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-0.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.9% / -3.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-23 21:00` | `2025-07-23 23:00` | 2.0h | `$1.0295` | `$1.1190` | **+8.70%** | **+8.34%** | +9.2% | -2.3% | `target_reclaim` |
| 2 | Book 3 | `2025-07-25 07:00` | `2025-07-28 07:00` | 72.0h | `$1.0719` | `$1.0629` | **-0.84%** | **-0.84%** | +2.6% | -5.3% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `NXPC`

* **Total Candidate Breakouts Filtered (Vetoed):** `53`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (45.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+242.3%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+242.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `39` | `73.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `7` | `13.2%` |
| `Core 3: Min Turnover Velocity` | `5` | `9.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `3.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*