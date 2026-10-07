# Kronos V12: Institutional Symbol Tear Sheet — `ASML`
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
| **Mean Net Log Return / Trade** | **`-0.50%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`42.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.9% / -2.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-04 13:00` | `2026-09-06 01:00` | 36.0h | `$1726.0644` | `$1716.6277` | **-0.55%** | **-0.55%** | +-0.2% | -3.0% | `stall_bailout` |
| 2 | Book 2 | `2026-09-29 13:00` | `2026-10-01 13:00` | 48.0h | `$1819.0964` | `$1810.7318` | **-0.46%** | **-0.46%** | +2.0% | -1.1% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.5%`** |
| `stall_bailout` | `1` | `0.0%` | **`-0.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `ASML`

* **Total Candidate Breakouts Filtered (Vetoed):** `17`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `11` (64.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+66.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+66.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `10` | `58.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `35.3%` |
| `Core 3: Min Turnover Velocity` | `1` | `5.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*