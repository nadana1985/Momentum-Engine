# Kronos V12: Institutional Symbol Tear Sheet — `ZEN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.052`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.26%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`99.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.1% / -5.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-12-26 09:00` | `2022-12-28 09:00` | 48.0h | `$9.3704` | `$8.9336` | **-4.66%** | **-4.77%** | +2.2% | -6.3% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-17 08:00` | `2026-09-23 14:00` | 150.0h | `$7.1568` | `$7.1747` | **+0.25%** | **+0.25%** | +20.1% | -5.0% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-4.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZEN`

* **Total Candidate Breakouts Filtered (Vetoed):** `233`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `154` (66.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `56`
* **Saved Capital Losses Avoided:** `+2,472.6%`
* **Missed Upside Forgone:** `-1,969.5%`
* **Net Veto Alpha:** `+503.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `84` | `36.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `70` | `30.0%` |
| `Core 1: Macro Bear Veto` | `69` | `29.6%` |
| `Core 4: Funding Rate Cap` | `9` | `3.9%` |
| `Core 4: Whale Firewall` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*