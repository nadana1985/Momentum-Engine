# Kronos V12: Institutional Symbol Tear Sheet — `RENDER`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`28.303`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+34.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.41x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+17.21%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.1% / -1.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2024-11-11 01:00` | `2024-11-11 23:00` | 22.0h | `$5.8287` | `$6.9945` | **+41.56%** | **+35.69%** | +22.0% | -1.2% | `target_reclaim` |
| 2 | Book 1 | `2026-09-21 08:00` | `2026-09-23 12:00` | 52.0h | `$1.7955` | `$1.7795` | **-1.25%** | **-1.26%** | +6.3% | -2.4% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.3%`** |
| `target_reclaim` | `1` | `100.0%` | **`+35.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `RENDER`

* **Total Candidate Breakouts Filtered (Vetoed):** `668`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `366` (54.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `58`
* **Saved Capital Losses Avoided:** `+4,059.2%`
* **Missed Upside Forgone:** `-1,557.1%`
* **Net Veto Alpha:** `+2,502.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `591` | `88.5%` |
| `Core 1: Macro Bear Veto` | `70` | `10.5%` |
| `Core 4: Defensible Whale Dump` | `6` | `0.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*