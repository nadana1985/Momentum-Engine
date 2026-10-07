# Kronos V12: Institutional Symbol Tear Sheet — `NFLX`
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
| **Cumulative Net Log Return** | **`-2.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.07%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.3% / -2.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-02 13:00` | `2026-09-04 01:00` | 36.0h | `$83.4381` | `$82.1242` | **-1.57%** | **-1.59%** | +0.3% | -3.6% | `stall_bailout` |
| 2 | Book 2 | `2026-09-11 17:00` | `2026-09-13 05:00` | 36.0h | `$77.4331` | `$77.0070` | **-0.55%** | **-0.55%** | +0.3% | -0.6% | `stall_bailout` |
| 3 | Book 2 | `2026-10-06 14:00` | `_Open Live_` | 14.9h | `$68.3103` | `$69.2900` | **+1.43%** | **+1.42%** | +1.6% | -1.1% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `2` | `0.0%` | **`-2.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `NFLX`

* **Total Candidate Breakouts Filtered (Vetoed):** `13`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `4` (30.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+9.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+9.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `12` | `92.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `7.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*