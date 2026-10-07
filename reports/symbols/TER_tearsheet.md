# Kronos V12: Institutional Symbol Tear Sheet — `TER`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.15%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.1% / -3.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-08 14:00` | `2026-09-10 14:00` | 48.0h | `$378.6442` | `$371.4191` | **-1.91%** | **-1.93%** | +1.7% | -3.3% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-29 11:00` | `2026-10-01 11:00` | 48.0h | `$408.3283` | `$406.8204` | **-0.37%** | **-0.37%** | +2.6% | -3.6% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-2.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `TER`

* **Total Candidate Breakouts Filtered (Vetoed):** `30`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `18` (60.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+166.9%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+166.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `14` | `46.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `13` | `43.3%` |
| `Core 4: Defensible Whale Dump` | `2` | `6.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `3.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*