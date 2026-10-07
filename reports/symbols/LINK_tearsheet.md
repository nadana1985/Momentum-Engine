# Kronos V12: Institutional Symbol Tear Sheet — `LINK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`2.103`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+19.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.22x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.27%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-16.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`118.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.1% / -3.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$6.5684` | `$7.0633` | **+7.53%** | **+7.26%** | +11.1% | -3.0% | `time_cap` |
| 2 | Book 1 | `2023-07-03 02:00` | `2023-07-04 14:00` | 36.0h | `$6.6426` | `$6.4937` | **-1.33%** | **-1.33%** | +0.7% | -3.2% | `stall_bailout` |
| 3 | Book 2 | `2023-10-21 07:00` | `2023-10-23 05:00` | 46.0h | `$7.8536` | `$10.6184` | **+35.20%** | **+30.16%** | +41.1% | -1.5% | `climax_top_harvest` |
| 4 | Book 1 | `2024-11-09 22:00` | `2024-11-13 02:00` | 76.0h | `$13.7994` | `$13.7206` | **-0.43%** | **-0.43%** | +11.4% | -2.4% | `fast_decay_cut` |
| 5 | Book 1 | `2025-04-23 04:00` | `2025-05-06 11:00` | 319.0h | `$14.7347` | `$13.2658` | **-13.08%** | **-14.02%** | +4.2% | -10.3% | `initial_stop` |
| 6 | Book 1 | `2025-05-10 12:00` | `2025-05-13 03:00` | 63.0h | `$16.3588` | `$16.0218` | **-1.99%** | **-2.01%** | +9.9% | -2.2% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-2.4%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+30.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-14.0%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.3%`** |
| `time_cap` | `1` | `100.0%` | **`+7.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `LINK`

* **Total Candidate Breakouts Filtered (Vetoed):** `263`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `152` (57.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `27`
* **Saved Capital Losses Avoided:** `+1,961.2%`
* **Missed Upside Forgone:** `-783.3%`
* **Net Veto Alpha:** `+1,178.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `128` | `48.7%` |
| `Core 1: Macro Bear Veto` | `111` | `42.2%` |
| `Core 4: Funding Rate Cap` | `20` | `7.6%` |
| `Core 4: Whale Firewall` | `4` | `1.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*