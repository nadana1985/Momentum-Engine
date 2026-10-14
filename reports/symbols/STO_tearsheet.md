# Kronos V12: Institutional Symbol Tear Sheet — `STO`
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
| **Cumulative Net Log Return** | **`-11.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.89x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-5.86%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-3.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`21.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.6% / -22.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-10-10 21:00` | `2025-10-11 03:00` | 6.0h | `$0.1813` | `$0.1663` | **-8.23%** | **-8.59%** | +26.9% | -40.4% | `stop_loss` |
| 2 | Book 2 | `2026-09-19 16:00` | `2026-09-21 04:00` | 36.0h | `$0.0413` | `$0.0402` | **-3.09%** | **-3.13%** | +0.4% | -5.1% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `1` | `0.0%` | **`-3.1%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `STO`

* **Total Candidate Breakouts Filtered (Vetoed):** `121`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `112` (92.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `32`
* **Saved Capital Losses Avoided:** `+3,129.0%`
* **Missed Upside Forgone:** `-7,573.6%`
* **Net Veto Alpha:** `+-4,444.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `111` | `91.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `9` | `7.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*