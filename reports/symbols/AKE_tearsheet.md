# Kronos V12: Institutional Symbol Tear Sheet — `AKE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.975`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.11%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`1.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+76.6% / -28.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-11-18 06:00` | `2025-11-22 06:00` | Live | `$0.0006` | `$0.0005` | **-8.20%** | **-8.56%** | +-19.1% | -50.7% | `shelf_stop_loss` |
| 2 | Book 3 | `2026-09-02 20:00` | `2026-09-02 21:00` | 1.0h | `$0.0165` | `$0.0179` | **+8.70%** | **+8.34%** | +172.3% | -5.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `AKE`

* **Total Candidate Breakouts Filtered (Vetoed):** `61`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `56` (91.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `33`
* **Saved Capital Losses Avoided:** `+1,688.4%`
* **Missed Upside Forgone:** `-2,795.2%`
* **Net Veto Alpha:** `+-1,106.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `59` | `96.7%` |
| `Core 4: Whale Firewall` | `2` | `3.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*