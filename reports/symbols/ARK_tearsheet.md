# Kronos V12: Institutional Symbol Tear Sheet — `ARK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.21%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.5% / -4.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2026-09-04 07:00` | `2026-09-05 20:00` | 37.0h | `$0.1200` | `$0.1172` | **-2.19%** | **-2.21%** | +2.5% | -4.7% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-2.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ARK`

* **Total Candidate Breakouts Filtered (Vetoed):** `86`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `64` (74.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+774.1%`
* **Missed Upside Forgone:** `-927.4%`
* **Net Veto Alpha:** `+-153.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `38` | `44.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `35` | `40.7%` |
| `Core 4: Defensible Whale Dump` | `8` | `9.3%` |
| `Core 4: Whale Firewall` | `5` | `5.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*