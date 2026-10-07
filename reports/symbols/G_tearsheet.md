# Kronos V12: Institutional Symbol Tear Sheet — `G`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.078`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-16.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.85x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.04%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`23.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.8% / -11.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-11-13 04:00` | `2024-11-16 04:00` | 72.0h | `$0.0295` | `$0.0299` | **+1.37%** | **+1.36%** | +8.3% | -5.8% | `time_expiry` |
| 2 | Book 3 | `2025-01-07 21:00` | `2025-01-08 13:00` | 16.0h | `$0.0338` | `$0.0310` | **-8.23%** | **-8.59%** | +7.5% | -8.0% | `stop_loss` |
| 3 | Book 2 | `2026-09-18 07:00` | `2026-09-18 08:00` | 1.0h | `$0.0073` | `$0.0072` | **-0.32%** | **-0.32%** | +18.1% | -19.6% | `breakeven_ratchet` |
| 4 | Book 3 | `2026-09-18 15:00` | `2026-09-18 18:00` | 3.0h | `$0.0086` | `$0.0079` | **-8.23%** | **-8.59%** | +17.4% | -11.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `breakeven_ratchet` | `1` | `0.0%` | **`-0.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `G`

* **Total Candidate Breakouts Filtered (Vetoed):** `81`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `56` (69.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+620.5%`
* **Missed Upside Forgone:** `-190.3%`
* **Net Veto Alpha:** `+430.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `52` | `64.2%` |
| `Core 1: Macro Bear Veto` | `28` | `34.6%` |
| `Core 4: Whale Firewall` | `1` | `1.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*