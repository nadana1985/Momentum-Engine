# Kronos V12: Institutional Symbol Tear Sheet — `BRKB`
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
| **Cumulative Net Log Return** | **`-1.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.49%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.3% / -1.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-02 14:00` | `2026-09-04 02:00` | 36.0h | `$509.6810` | `$507.0492` | **-0.52%** | **-0.52%** | +0.6% | -0.9% | `stall_bailout` |
| 2 | Book 2 | `2026-09-14 13:00` | `2026-09-16 01:00` | 36.0h | `$518.1321` | `$515.7374` | **-0.46%** | **-0.46%** | +0.0% | -1.1% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `2` | `0.0%` | **`-1.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `BRKB`

* **Total Candidate Breakouts Filtered (Vetoed):** `18`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `10` (55.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+21.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+21.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `14` | `77.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `16.7%` |
| `Core 3: Min Turnover Velocity` | `1` | `5.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*