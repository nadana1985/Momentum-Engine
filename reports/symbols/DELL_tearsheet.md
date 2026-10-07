# Kronos V12: Institutional Symbol Tear Sheet — `DELL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-3.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.12%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-3.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`53.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.5% / -2.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-25 13:00` | `2026-08-28 18:00` | 77.0h | `$456.1074` | `$454.4610` | **-0.36%** | **-0.36%** | +4.6% | -3.4% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-17 13:00` | `2026-09-19 13:00` | 48.0h | `$583.0941` | `$572.4154` | **-1.83%** | **-1.85%** | +2.8% | -2.9% | `fast_decay_cut` |
| 3 | Book 2 | `2026-10-02 16:00` | `2026-10-04 04:00` | 36.0h | `$567.2346` | `$560.8145` | **-1.13%** | **-1.14%** | +0.1% | -1.5% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-2.2%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `DELL`

* **Total Candidate Breakouts Filtered (Vetoed):** `18`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `13` (72.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+132.5%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+132.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `14` | `77.8%` |
| `Core 4: Defensible Whale Dump` | `3` | `16.7%` |
| `Core 4: Whale Firewall` | `1` | `5.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*