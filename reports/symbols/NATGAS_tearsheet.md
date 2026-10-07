# Kronos V12: Institutional Symbol Tear Sheet — `NATGAS`
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
| **Maximum Log Drawdown** | **`-4.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`80.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.7% / -2.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-02 18:00` | `2026-09-04 06:00` | 36.0h | `$2.9955` | `$2.9177` | **-2.60%** | **-2.63%** | +1.0% | -3.5% | `stall_bailout` |
| 2 | Book 2 | `2026-09-15 12:00` | `2026-09-17 00:00` | 36.0h | `$3.0727` | `$3.0095` | **-2.06%** | **-2.08%** | +0.5% | -2.6% | `stall_bailout` |
| 3 | Book 2 | `2026-09-22 14:00` | `2026-09-29 14:00` | 168.0h | `$3.0947` | `$3.0324` | **-2.01%** | **-2.03%** | +9.7% | -2.0% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `2` | `0.0%` | **`-4.7%`** |
| `time_cap` | `1` | `0.0%` | **`-2.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `NATGAS`

* **Total Candidate Breakouts Filtered (Vetoed):** `26`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `14` (53.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+66.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+66.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `20` | `76.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `23.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*