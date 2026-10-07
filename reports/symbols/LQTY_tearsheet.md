# Kronos V12: Institutional Symbol Tear Sheet — `LQTY`
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
| **Cumulative Net Log Return** | **`-1.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.63%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`50.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.8% / -4.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-09-20 03:00` | `2023-09-22 16:00` | 61.0h | `$0.8388` | `$0.8287` | **-1.20%** | **-1.21%** | +5.5% | -2.1% | `fast_decay_cut` |
| 2 | Book 2 | `2023-10-23 23:00` | `2023-10-25 15:00` | 40.0h | `$1.5999` | `$1.5991` | **-0.05%** | **-0.05%** | +26.0% | -6.0% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `0.0%` | **`-0.0%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `LQTY`

* **Total Candidate Breakouts Filtered (Vetoed):** `168`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `101` (60.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `27`
* **Saved Capital Losses Avoided:** `+1,345.5%`
* **Missed Upside Forgone:** `-922.1%`
* **Net Veto Alpha:** `+423.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `73` | `43.5%` |
| `Core 1: Macro Bear Veto` | `58` | `34.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `25` | `14.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `11` | `6.5%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*