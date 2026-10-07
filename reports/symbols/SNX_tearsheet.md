# Kronos V12: Institutional Symbol Tear Sheet — `SNX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`2.432`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+1.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.60%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`97.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.8% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 17:00` | `2022-10-28 07:00` | 62.0h | `$2.3388` | `$2.3212` | **-0.75%** | **-0.76%** | +7.7% | -2.5% | `fast_decay_cut` |
| 2 | Book 2 | `2023-10-16 05:00` | `2023-10-18 20:00` | 63.0h | `$1.9238` | `$1.9142` | **-0.50%** | **-0.50%** | +2.5% | -2.9% | `fast_decay_cut` |
| 3 | Book 2 | `2023-10-23 22:00` | `2023-10-30 22:00` | 168.0h | `$2.2416` | `$2.3112` | **+3.11%** | **+3.06%** | +10.2% | -3.5% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-1.3%`** |
| `time_cap` | `1` | `100.0%` | **`+3.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `SNX`

* **Total Candidate Breakouts Filtered (Vetoed):** `373`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `253` (67.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `41`
* **Saved Capital Losses Avoided:** `+3,711.5%`
* **Missed Upside Forgone:** `-1,496.1%`
* **Net Veto Alpha:** `+2,215.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `99` | `26.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `95` | `25.5%` |
| `Core 1: Macro Bear Veto` | `79` | `21.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `72` | `19.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `28` | `7.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*