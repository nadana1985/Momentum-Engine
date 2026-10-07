# Kronos V12: Institutional Symbol Tear Sheet — `JST`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`1` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+1.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.80%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.7% / -3.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-01 08:00` | `2026-09-08 08:00` | 168.0h | `$0.1020` | `$0.1039` | **+1.82%** | **+1.80%** | +11.7% | -3.3% | `time_cap` |
| 2 | Book 1 | `2026-10-03 02:00` | `_Open Live_` | 98.9h | `$0.1353` | `$0.1408` | **+2.93%** | **+2.88%** | +4.5% | -1.4% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+1.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `JST`

* **Total Candidate Breakouts Filtered (Vetoed):** `158`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `72` (45.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+525.2%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+525.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `143` | `90.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `15` | `9.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*