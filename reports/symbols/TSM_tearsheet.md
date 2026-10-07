# Kronos V12: Institutional Symbol Tear Sheet — `TSM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.864`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.12%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`96.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.7% / -1.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-27 16:00` | `2026-08-29 04:00` | 36.0h | `$429.6615` | `$418.6907` | **-2.55%** | **-2.59%** | +0.0% | -2.7% | `stall_bailout` |
| 2 | Book 2 | `2026-09-04 13:00` | `2026-09-10 13:00` | 144.0h | `$427.1552` | `$423.8677` | **-0.77%** | **-0.77%** | +4.1% | -1.7% | `fast_decay_cut` |
| 3 | Book 2 | `2026-09-17 13:00` | `2026-09-24 13:00` | 168.0h | `$427.2956` | `$441.0746` | **+3.22%** | **+3.17%** | +6.0% | -0.7% | `time_cap` |
| 4 | Book 2 | `2026-09-29 14:00` | `2026-10-01 02:00` | 36.0h | `$458.8743` | `$457.4336` | **-0.31%** | **-0.31%** | +0.8% | -1.9% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `2` | `0.0%` | **`-2.9%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.8%`** |
| `time_cap` | `1` | `100.0%` | **`+3.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `TSM`

* **Total Candidate Breakouts Filtered (Vetoed):** `37`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `21` (56.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+115.2%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+115.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `32` | `86.5%` |
| `Core 3: Min Turnover Velocity` | `5` | `13.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*