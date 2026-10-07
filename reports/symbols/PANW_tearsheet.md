# Kronos V12: Institutional Symbol Tear Sheet — `PANW`
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
| **Cumulative Net Log Return** | **`-1.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.94%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`51.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.5% / -3.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-14 14:00` | `2026-09-17 09:00` | 67.0h | `$372.9601` | `$369.7832` | **-0.85%** | **-0.86%** | +2.4% | -4.8% | `fast_decay_cut` |
| 2 | Book 2 | `2026-10-02 13:00` | `2026-10-04 01:00` | 36.0h | `$407.1253` | `$402.9701` | **-1.02%** | **-1.03%** | +0.6% | -2.1% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.9%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `PANW`

* **Total Candidate Breakouts Filtered (Vetoed):** `17`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `9` (52.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+44.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+44.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `10` | `58.8%` |
| `Core 1: Macro Bear Veto` | `7` | `41.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*