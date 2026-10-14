# Kronos V12: Institutional Symbol Tear Sheet — `SIREN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.292`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+2.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.25%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`5.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+-2.3% / -27.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-03-24 08:00` | `2025-03-28 08:00` | Live | `$0.0672` | `$0.0616` | **-8.20%** | **-8.56%** | +-29.4% | -53.7% | `shelf_stop_loss` |
| 2 | Book 4 | `2025-08-09 11:00` | `2025-08-09 16:00` | 5.0h | `$0.0804` | `$0.0965` | **+11.58%** | **+11.05%** | +24.7% | -1.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+11.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `SIREN`

* **Total Candidate Breakouts Filtered (Vetoed):** `378`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `343` (90.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `63`
* **Saved Capital Losses Avoided:** `+6,320.6%`
* **Missed Upside Forgone:** `-4,549.7%`
* **Net Veto Alpha:** `+1,770.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `196` | `51.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `182` | `48.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*