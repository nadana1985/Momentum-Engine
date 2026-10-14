# Kronos V12: Institutional Symbol Tear Sheet — `TRADOOR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.980`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.05%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-4.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`57.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.2% / -7.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-03-16 21:00` | `2026-03-18 16:00` | 43.0h | `$1.9389` | `$2.3267` | **+4.62%** | **+4.51%** | +20.4% | -6.3% | `target_reclaim` |
| 2 | Book 3 | `2026-09-07 06:00` | `2026-09-10 06:00` | 72.0h | `$0.6318` | `$0.6034` | **-4.50%** | **-4.60%** | +12.0% | -7.9% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+4.5%`** |
| `time_expiry` | `1` | `0.0%` | **`-4.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `TRADOOR`

* **Total Candidate Breakouts Filtered (Vetoed):** `401`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `186` (46.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `89`
* **Saved Capital Losses Avoided:** `+3,523.8%`
* **Missed Upside Forgone:** `-2,964.6%`
* **Net Veto Alpha:** `+559.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `400` | `99.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*