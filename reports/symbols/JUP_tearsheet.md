# Kronos V12: Institutional Symbol Tear Sheet — `JUP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.905`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-1.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.39%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-16.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`184.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.0% / -6.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2024-07-16 18:00` | `2024-07-21 21:00` | 123.0h | `$0.9035` | `$1.0841` | **+15.94%** | **+14.97%** | +20.3% | -2.2% | `target_reclaim` |
| 2 | Book 2 | `2024-10-11 16:00` | `2024-10-13 17:00` | 49.0h | `$0.7823` | `$0.7769` | **-0.73%** | **-0.73%** | +3.6% | -3.1% | `fast_decay_cut` |
| 3 | Book 4 | `2026-06-24 23:00` | `2026-07-17 00:00` | 529.0h | `$0.2188` | `$0.1937` | **-6.95%** | **-7.16%** | +15.8% | -12.0% | `structural_stop` |
| 4 | Book 1 | `2026-08-27 18:00` | `2026-08-29 06:00` | 36.0h | `$0.2357` | `$0.2175` | **-8.34%** | **-8.66%** | +4.1% | -9.2% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-9.4%`** |
| `structural_stop` | `1` | `0.0%` | **`-7.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+15.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `JUP`

* **Total Candidate Breakouts Filtered (Vetoed):** `907`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `627` (69.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `43`
* **Saved Capital Losses Avoided:** `+6,912.2%`
* **Missed Upside Forgone:** `-1,372.9%`
* **Net Veto Alpha:** `+5,539.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `475` | `52.4%` |
| `Core 1: Macro Bear Veto` | `430` | `47.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.1%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*