# Kronos V12: Institutional Symbol Tear Sheet — `ENJ`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.683`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+22.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.25x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.78%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-13.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`98.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.8% / -4.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-07-12 00:00` | `2023-07-19 00:00` | 168.0h | `$0.3026` | `$0.3123` | **+3.23%** | **+3.18%** | +9.5% | -4.1% | `time_cap` |
| 2 | Book 2 | `2023-10-01 22:00` | `2023-10-02 18:00` | 20.0h | `$0.2340` | `$0.2191` | **-6.36%** | **-6.57%** | +0.0% | -7.2% | `initial_stop` |
| 3 | Book 2 | `2023-10-09 00:00` | `2023-10-09 16:00` | 16.0h | `$0.2315` | `$0.2181` | **-5.78%** | **-5.95%** | +3.6% | -7.4% | `initial_stop` |
| 4 | Book 2 | `2023-10-16 05:00` | `2023-10-18 05:00` | 48.0h | `$0.2167` | `$0.2147` | **-0.96%** | **-0.96%** | +2.5% | -3.4% | `fast_decay_cut` |
| 5 | Book 2 | `2023-10-23 00:00` | `2023-10-30 00:00` | 168.0h | `$0.2220` | `$0.2757` | **+24.22%** | **+21.69%** | +28.7% | -2.3% | `time_cap` |
| 6 | Book 2 | `2024-02-12 16:00` | `2024-02-19 16:00` | 168.0h | `$0.3068` | `$0.3435` | **+11.99%** | **+11.32%** | +14.3% | -2.2% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `3` | `100.0%` | **`+36.2%`** |
| `initial_stop` | `2` | `0.0%` | **`-12.5%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `ENJ`

* **Total Candidate Breakouts Filtered (Vetoed):** `283`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `178` (62.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `54`
* **Saved Capital Losses Avoided:** `+2,554.8%`
* **Missed Upside Forgone:** `-2,119.9%`
* **Net Veto Alpha:** `+434.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `83` | `29.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `77` | `27.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `58` | `20.5%` |
| `Core 1: Macro Bear Veto` | `43` | `15.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `22` | `7.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*