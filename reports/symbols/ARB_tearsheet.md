# Kronos V12: Institutional Symbol Tear Sheet — `ARB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `11` (`11` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`54.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.193`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+51.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.68x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.71%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-14.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`45.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.7% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-10-01 09:00` | `2023-10-04 00:00` | 63.0h | `$0.9594` | `$0.8685` | **-16.05%** | **-17.31%** | +3.0% | -11.2% | `fast_decay_cut` |
| 2 | Book 2 | `2023-10-16 05:00` | `2023-10-17 13:00` | 32.0h | `$0.8263` | `$0.7918` | **-4.73%** | **-4.83%** | +2.6% | -6.1% | `initial_stop` |
| 3 | Book 3 | `2023-12-11 02:00` | `2023-12-12 22:00` | 44.0h | `$1.0872` | `$1.2069` | **+11.01%** | **+10.45%** | +12.2% | -9.0% | `target_reclaim` |
| 4 | Book 3 | `2024-01-03 12:00` | `2024-01-03 13:00` | 1.0h | `$1.5820` | `$1.8668` | **+18.00%** | **+16.55%** | +23.1% | -10.1% | `climax_whale_euphoria_harvest` |
| 5 | Book 3 | `2024-03-11 00:00` | `2024-03-13 09:00` | 57.0h | `$1.9616` | `$2.2346` | **+13.91%** | **+13.03%** | +15.2% | -3.1% | `target_reclaim` |
| 6 | Book 1 | `2024-09-26 16:00` | `2024-09-30 18:00` | 98.0h | `$0.6396` | `$0.6134` | **-6.65%** | **-6.87%** | +6.4% | -4.8% | `fast_decay_cut` |
| 7 | Book 3 | `2024-11-13 06:00` | `2024-11-16 06:00` | 72.0h | `$0.5731` | `$0.6144` | **+7.20%** | **+6.95%** | +12.5% | -1.2% | `time_expiry` |
| 8 | Book 3 | `2024-11-24 12:00` | `2024-11-24 21:00` | 9.0h | `$0.7985` | `$0.8430` | **+5.58%** | **+5.43%** | +6.3% | -0.4% | `target_reclaim` |
| 9 | Book 3 | `2024-12-09 03:00` | `2024-12-09 20:00` | 17.0h | `$1.1150` | `$1.0233` | **-8.23%** | **-8.59%** | +2.2% | -12.4% | `stop_loss` |
| 10 | Book 2 | `2025-02-12 22:00` | `2025-02-15 22:00` | 72.0h | `$0.4978` | `$0.4742` | **-5.69%** | **-5.82%** | +2.8% | -5.5% | `stagnation_cut` |
| 11 | Book 4 | `2026-09-02 16:00` | `2026-09-04 01:00` | 33.0h | `$0.1221` | `$0.1465` | **+51.49%** | **+42.84%** | +20.2% | -1.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+71.7%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-24.2%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |
| `initial_stop` | `1` | `0.0%` | **`-4.8%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-5.8%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+7.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `ARB`

* **Total Candidate Breakouts Filtered (Vetoed):** `76`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `53` (69.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `7`
* **Saved Capital Losses Avoided:** `+573.1%`
* **Missed Upside Forgone:** `-162.1%`
* **Net Veto Alpha:** `+411.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `46` | `60.5%` |
| `Core 4: Funding Rate Cap` | `28` | `36.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `2.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*