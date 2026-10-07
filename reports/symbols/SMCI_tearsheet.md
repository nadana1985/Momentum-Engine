# Kronos V12: Institutional Symbol Tear Sheet — `SMCI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-6.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.93x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.25%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-6.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`70.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.3% / -4.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-25 14:00` | `2026-08-27 14:00` | 48.0h | `$38.3256` | `$38.0945` | **-0.60%** | **-0.60%** | +3.1% | -4.1% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-04 13:00` | `2026-09-09 19:00` | 126.0h | `$39.1276` | `$38.8127` | **-0.80%** | **-0.81%** | +6.2% | -3.0% | `fast_decay_cut` |
| 3 | Book 2 | `2026-09-17 14:00` | `2026-09-19 02:00` | 36.0h | `$40.9922` | `$38.8626` | **-5.20%** | **-5.34%** | +0.7% | -6.3% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-1.4%`** |
| `stall_bailout` | `1` | `0.0%` | **`-5.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `SMCI`

* **Total Candidate Breakouts Filtered (Vetoed):** `18`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `7` (38.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `3`
* **Saved Capital Losses Avoided:** `+40.6%`
* **Missed Upside Forgone:** `-75.5%`
* **Net Veto Alpha:** `+-34.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `15` | `83.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `16.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*