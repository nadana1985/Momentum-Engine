# Kronos V12: Institutional Symbol Tear Sheet — `Q`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.039`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-8.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.13%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`3.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.6% / -28.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-20 15:00` | `2026-09-20 17:00` | 2.0h | `$0.0265` | `$0.0243` | **-8.23%** | **-8.59%** | +6.4% | -11.1% | `initial_stop` |
| 2 | Book 1 | `2026-09-26 11:00` | `2026-09-26 16:00` | 5.0h | `$0.0359` | `$0.0360` | **+0.34%** | **+0.34%** | +16.8% | -45.7% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.3%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `Q`

* **Total Candidate Breakouts Filtered (Vetoed):** `62`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `54` (87.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+1,531.0%`
* **Missed Upside Forgone:** `-1,710.4%`
* **Net Veto Alpha:** `+-179.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `43` | `69.4%` |
| `Core 4: Funding Rate Cap` | `9` | `14.5%` |
| `Core 3: Min Turnover Velocity` | `6` | `9.7%` |
| `Core 4: Whale Firewall` | `3` | `4.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `1` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*