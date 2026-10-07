# Kronos V12: Institutional Symbol Tear Sheet — `USELESS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.347`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-15.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.85x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.92%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`2.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.5% / -8.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-01 03:00` | `2026-09-01 08:00` | 5.0h | `$0.0955` | `$0.0876` | **-6.62%** | **-6.85%** | +1.9% | -8.8% | `initial_stop` |
| 2 | Book 3 | `2026-09-07 07:00` | `2026-09-07 08:00` | 1.0h | `$0.2029` | `$0.2205` | **+8.70%** | **+8.34%** | +10.2% | -6.3% | `target_reclaim` |
| 3 | Book 3 | `2026-09-09 14:00` | `2026-09-09 15:00` | 1.0h | `$0.2973` | `$0.2729` | **-8.23%** | **-8.59%** | +4.4% | -8.7% | `stop_loss` |
| 4 | Book 3 | `2026-09-23 14:00` | `2026-09-23 15:00` | 1.0h | `$0.3149` | `$0.2890` | **-8.23%** | **-8.59%** | +5.4% | -8.5% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-6.8%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `USELESS`

* **Total Candidate Breakouts Filtered (Vetoed):** `107`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `98` (91.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `62`
* **Saved Capital Losses Avoided:** `+2,006.4%`
* **Missed Upside Forgone:** `-2,424.3%`
* **Net Veto Alpha:** `+-417.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: Defensible Whale Dump` | `65` | `60.7%` |
| `Core 1: Macro Bear Veto` | `41` | `38.3%` |
| `Core 4: Whale Firewall` | `1` | `0.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*