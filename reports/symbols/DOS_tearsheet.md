# Kronos V12: Institutional Symbol Tear Sheet — `DOS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.328`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-15.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.85x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-5.25%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-23.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`3.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+40.4% / -34.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-10-08 19:00` | `2026-10-09 04:00` | 9.0h | `$0.2255` | `$0.2349` | **+4.17%** | **+4.08%** | +4.2% | -4.2% | `target_reclaim` |
| 2 | Book 4 | `2026-10-12 20:00` | `2026-10-12 21:00` | 1.0h | `$0.3794` | `$0.4076` | **+3.66%** | **+3.60%** | +125.1% | -61.6% | `breakeven_ratchet` |
| 3 | Book 3 | `2026-10-12 22:00` | `2026-10-12 23:00` | 1.0h | `$0.2831` | `$0.2239` | **-20.89%** | **-23.44%** | +-8.2% | -36.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+3.6%`** |
| `stop_loss` | `1` | `0.0%` | **`-23.4%`** |
| `target_reclaim` | `1` | `100.0%` | **`+4.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `DOS`

* **Total Candidate Breakouts Filtered (Vetoed):** `8`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `1` (12.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+10.1%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+10.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `87.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `12.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*