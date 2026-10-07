# Kronos V12: Institutional Symbol Tear Sheet — `SQQQ`
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
| **Cumulative Net Log Return** | **`-6.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.18%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-2.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.1% / -4.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-10 12:00` | `2026-09-12 00:00` | 36.0h | `$40.3105` | `$38.6731` | **-4.06%** | **-4.15%** | +-0.1% | -4.6% | `stall_bailout` |
| 2 | Book 2 | `2026-09-28 14:00` | `2026-09-30 02:00` | 36.0h | `$35.4384` | `$34.6631` | **-2.19%** | **-2.21%** | +0.2% | -3.3% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `2` | `0.0%` | **`-6.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `SQQQ`

* **Total Candidate Breakouts Filtered (Vetoed):** `21`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `13` (61.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+110.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+110.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `20` | `95.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `4.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*