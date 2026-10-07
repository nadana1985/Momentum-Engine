# Kronos V12: Institutional Symbol Tear Sheet — `SOPH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.015`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+8.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.09x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.18%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.6% / -6.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-14 01:00` | `2025-07-17 01:00` | 72.0h | `$0.0350` | `$0.0359` | **+2.59%** | **+2.55%** | +6.0% | -3.8% | `time_expiry` |
| 2 | Book 3 | `2025-08-06 04:00` | `2025-08-09 04:00` | 72.0h | `$0.0392` | `$0.0409` | **+4.24%** | **+4.15%** | +6.6% | -0.9% | `time_expiry` |
| 3 | Book 2 | `2026-09-08 01:00` | `2026-09-08 04:00` | 3.0h | `$0.0070` | `$0.0085` | **+11.19%** | **+10.60%** | +47.2% | -10.0% | `trail_stop` |
| 4 | Book 3 | `2026-09-09 15:00` | `2026-09-09 19:00` | 4.0h | `$0.0050` | `$0.0046` | **-8.23%** | **-8.59%** | +6.4% | -11.9% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `2` | `100.0%` | **`+6.7%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `trail_stop` | `1` | `100.0%` | **`+10.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `SOPH`

* **Total Candidate Breakouts Filtered (Vetoed):** `20`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `17` (85.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+257.1%`
* **Missed Upside Forgone:** `-365.5%`
* **Net Veto Alpha:** `+-108.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `13` | `65.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `4` | `20.0%` |
| `Core 4: Funding Rate Cap` | `3` | `15.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*