# Kronos V12: Institutional Symbol Tear Sheet — `RECALL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.784`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+3.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.83%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`60.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.6% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-22 20:00` | `2026-08-25 20:00` | 72.0h | `$0.0505` | `$0.0481` | **-4.57%** | **-4.67%** | +4.3% | -6.7% | `time_expiry` |
| 2 | Book 3 | `2026-09-28 07:00` | `2026-09-30 08:00` | 49.0h | `$0.0459` | `$0.0498` | **+8.70%** | **+8.34%** | +8.9% | -3.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `0.0%` | **`-4.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `RECALL`

* **Total Candidate Breakouts Filtered (Vetoed):** `24`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `22` (91.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `1`
* **Saved Capital Losses Avoided:** `+306.1%`
* **Missed Upside Forgone:** `-20.1%`
* **Net Veto Alpha:** `+285.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `19` | `79.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5` | `20.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*