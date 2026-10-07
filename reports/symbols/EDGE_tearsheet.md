# Kronos V12: Institutional Symbol Tear Sheet — `EDGE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.88%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.7% / -4.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-04 04:00` | `2026-05-11 04:00` | 168.0h | `$1.3074` | `$1.2960` | **-0.87%** | **-0.88%** | +10.7% | -4.3% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `0.0%` | **`-0.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `EDGE`

* **Total Candidate Breakouts Filtered (Vetoed):** `21`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `14` (66.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `7`
* **Saved Capital Losses Avoided:** `+309.8%`
* **Missed Upside Forgone:** `-234.8%`
* **Net Veto Alpha:** `+75.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `17` | `81.0%` |
| `Core 4: Funding Rate Cap` | `4` | `19.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*