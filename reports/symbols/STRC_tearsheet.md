# Kronos V12: Institutional Symbol Tear Sheet — `STRC`
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
| **Cumulative Net Log Return** | **`-1.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.70%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.4% / -0.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-18 14:00` | `2026-09-20 02:00` | 36.0h | `$98.8264` | `$98.2138` | **-0.62%** | **-0.62%** | +0.3% | -0.6% | `stall_bailout` |
| 2 | Book 2 | `2026-09-28 17:00` | `2026-09-30 05:00` | 36.0h | `$99.6084` | `$98.8323` | **-0.78%** | **-0.78%** | +0.4% | -0.7% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `2` | `0.0%` | **`-1.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `STRC`

* **Total Candidate Breakouts Filtered (Vetoed):** `19`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `6` (31.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+9.5%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+9.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `11` | `57.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `21.1%` |
| `Core 3: Min Turnover Velocity` | `3` | `15.8%` |
| `Core 4: Defensible Whale Dump` | `1` | `5.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*