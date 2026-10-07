# Kronos V12: Institutional Symbol Tear Sheet — `ONG`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`9.707`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+11.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.12x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.84%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`108.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.6% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-09-13 15:00` | `2024-09-15 15:00` | 48.0h | `$0.2803` | `$0.2766` | **-1.33%** | **-1.34%** | +1.6% | -2.1% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-20 01:00` | `2026-09-27 01:00` | 168.0h | `$0.0840` | `$0.0957` | **+13.90%** | **+13.01%** | +17.7% | -3.8% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.3%`** |
| `time_cap` | `1` | `100.0%` | **`+13.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `ONG`

* **Total Candidate Breakouts Filtered (Vetoed):** `108`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `57` (52.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `16`
* **Saved Capital Losses Avoided:** `+809.7%`
* **Missed Upside Forgone:** `-594.8%`
* **Net Veto Alpha:** `+214.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `80` | `74.1%` |
| `Core 1: Macro Bear Veto` | `27` | `25.0%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*