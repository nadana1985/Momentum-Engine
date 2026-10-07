# Kronos V12: Institutional Symbol Tear Sheet — `DIS`
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
| **Cumulative Net Log Return** | **`-1.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.87%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.3% / -1.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-20 13:00` | `2026-08-22 01:00` | 36.0h | `$108.1697` | `$107.5205` | **-0.60%** | **-0.60%** | +0.6% | -1.7% | `stall_bailout` |
| 2 | Book 2 | `2026-09-11 14:00` | `2026-09-13 02:00` | 36.0h | `$107.5983` | `$106.3834` | **-1.13%** | **-1.14%** | +-0.1% | -1.5% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `2` | `0.0%` | **`-1.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `DIS`

* **Total Candidate Breakouts Filtered (Vetoed):** `17`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `11` (64.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+31.8%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+31.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `16` | `94.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `5.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*