# Kronos V12: Institutional Symbol Tear Sheet — `GME`
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
| **Cumulative Net Log Return** | **`-3.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.86%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.6% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-04 07:00` | `2026-09-06 07:00` | 48.0h | `$19.6390` | `$19.1819` | **-2.33%** | **-2.35%** | +2.2% | -3.2% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-30 13:00` | `2026-10-02 13:00` | 48.0h | `$24.6414` | `$24.3091` | **-1.35%** | **-1.36%** | +1.0% | -2.5% | `fast_decay_cut` |
| 3 | Book 2 | `2026-10-05 14:00` | `_Open Live_` | 38.9h | `$25.6439` | `$24.7100` | **-3.64%** | **-3.71%** | +0.6% | -4.6% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-3.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `GME`

* **Total Candidate Breakouts Filtered (Vetoed):** `24`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `15` (62.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+44.9%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+44.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `17` | `70.8%` |
| `Core 1: Macro Bear Veto` | `4` | `16.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `12.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*