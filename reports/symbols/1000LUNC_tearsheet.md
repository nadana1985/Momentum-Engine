# Kronos V12: Institutional Symbol Tear Sheet — `1000LUNC`
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
| **Cumulative Net Log Return** | **`-2.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.64%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`70.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.6% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-20 16:00` | `2026-09-23 14:00` | 70.0h | `$0.0550` | `$0.0535` | **-2.60%** | **-2.64%** | +5.6% | -6.0% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-2.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000LUNC`

* **Total Candidate Breakouts Filtered (Vetoed):** `124`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `68` (54.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `30`
* **Saved Capital Losses Avoided:** `+886.5%`
* **Missed Upside Forgone:** `-1,602.4%`
* **Net Veto Alpha:** `+-715.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `61` | `49.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `49` | `39.5%` |
| `Core 4: Defensible Whale Dump` | `7` | `5.6%` |
| `Core 4: Whale Firewall` | `4` | `3.2%` |
| `Core 4: Funding Rate Cap` | `3` | `2.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*