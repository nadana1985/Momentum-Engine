# Kronos V12: Institutional Symbol Tear Sheet — `ICNT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+16.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.34%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`30.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.2% / -3.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-08-07 21:00` | `2025-08-10 01:00` | 52.0h | `$0.2596` | `$0.2822` | **+8.70%** | **+8.34%** | +10.2% | -6.1% | `target_reclaim` |
| 2 | Book 3 | `2025-08-10 15:00` | `2025-08-10 23:00` | 8.0h | `$0.2860` | `$0.3109` | **+8.70%** | **+8.34%** | +10.2% | -1.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `ICNT`

* **Total Candidate Breakouts Filtered (Vetoed):** `26`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `18` (69.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `6`
* **Saved Capital Losses Avoided:** `+304.6%`
* **Missed Upside Forgone:** `-185.7%`
* **Net Veto Alpha:** `+118.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `18` | `69.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `8` | `30.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*