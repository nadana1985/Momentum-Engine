# Kronos V12: Institutional Symbol Tear Sheet — `ELSA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.806`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-1.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.49%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-5.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`38.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.5% / -3.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-04 12:00` | `2026-09-04 16:00` | 4.0h | `$0.0490` | `$0.0511` | **+4.17%** | **+4.08%** | +4.4% | -2.8% | `target_reclaim` |
| 2 | Book 3 | `2026-09-28 07:00` | `2026-10-01 07:00` | 72.0h | `$0.0574` | `$0.0545` | **-4.94%** | **-5.07%** | +4.5% | -4.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+4.1%`** |
| `time_expiry` | `1` | `0.0%` | **`-5.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `ELSA`

* **Total Candidate Breakouts Filtered (Vetoed):** `19`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `15` (78.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+190.2%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+190.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `14` | `73.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5` | `26.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*