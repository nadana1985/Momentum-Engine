# Kronos V12: Institutional Symbol Tear Sheet — `HOME`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.439`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+18.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.21x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.30%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-7.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`184.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.6% / -5.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-01-09 18:00` | `2026-01-23 17:00` | 335.0h | `$0.0261` | `$0.0313` | **+9.43%** | **+9.06%** | +22.1% | -3.0% | `target_reclaim` |
| 2 | Book 4 | `2026-05-21 13:00` | `2026-05-28 16:00` | 171.0h | `$0.0228` | `$0.0274` | **+18.95%** | **+17.59%** | +23.3% | -6.7% | `target_reclaim` |
| 3 | Book 2 | `2026-08-29 02:00` | `2026-08-31 02:00` | 48.0h | `$0.0064` | `$0.0060` | **-7.51%** | **-7.75%** | +1.5% | -6.8% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+26.7%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-7.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `HOME`

* **Total Candidate Breakouts Filtered (Vetoed):** `760`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `192` (25.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `208`
* **Saved Capital Losses Avoided:** `+3,155.6%`
* **Missed Upside Forgone:** `-10,075.6%`
* **Net Veto Alpha:** `+-6,920.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `749` | `98.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `11` | `1.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*