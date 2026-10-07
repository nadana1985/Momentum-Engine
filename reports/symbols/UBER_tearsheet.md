# Kronos V12: Institutional Symbol Tear Sheet — `UBER`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`2` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-7.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.97%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-2.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`14.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.3% / -4.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 09:00` | `2026-08-27 12:00` | 27.0h | `$81.9243` | `$77.5707` | **-5.31%** | **-5.46%** | +0.6% | -5.2% | `initial_stop` |
| 2 | Book 2 | `2026-09-08 12:00` | `2026-09-08 13:00` | 1.0h | `$76.8216` | `$74.9439` | **-2.44%** | **-2.47%** | +0.1% | -4.6% | `initial_stop` |
| 3 | Book 2 | `2026-10-05 13:00` | `_Open Live_` | 39.9h | `$69.5534` | `$69.1400` | **-0.59%** | **-0.60%** | +1.2% | -2.2% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-7.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `UBER`

* **Total Candidate Breakouts Filtered (Vetoed):** `15`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `13` (86.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+67.4%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+67.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `11` | `73.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `26.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*