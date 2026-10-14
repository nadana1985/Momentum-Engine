# Kronos V12: Institutional Symbol Tear Sheet — `ETH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.890`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+29.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.34x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.14%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-5.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`325.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.0% / -3.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2022-03-25 04:00` | `2022-04-11 10:00` | 414.0h | `$3147.8046` | `$3066.1938` | **-1.62%** | **-1.63%** | +13.7% | -3.0% | `structural_stop` |
| 2 | Book 1 | `2022-10-26 08:00` | `2022-10-28 08:00` | 48.0h | `$1539.9302` | `$1498.0256` | **-4.85%** | **-4.95%** | +3.6% | -3.6% | `fast_decay_cut` |
| 3 | Book 3 | `2024-03-05 19:00` | `2024-03-06 04:00` | 9.0h | `$3312.8188` | `$3600.8900` | **+8.70%** | **+8.34%** | +10.4% | -3.3% | `target_reclaim` |
| 4 | Book 1 | `2024-11-09 19:00` | `2024-11-30 19:00` | 504.0h | `$3078.3767` | `$3682.7700` | **+22.11%** | **+20.24%** | +21.2% | -2.0% | `time_cap` |
| 5 | Book 4 | `2025-05-10 13:00` | `2025-06-09 12:00` | 719.0h | `$2440.6555` | `$2540.3837` | **+3.39%** | **+3.35%** | +14.3% | -5.2% | `time_expiry` |
| 6 | Book 1 | `2025-07-14 04:00` | `2025-07-15 16:00` | 36.0h | `$3059.6601` | `$3040.2404` | **-0.87%** | **-0.88%** | +0.8% | -4.2% | `stall_bailout` |
| 7 | Book 4 | `2026-08-19 20:00` | `2026-09-11 14:00` | 546.0h | `$2221.3871` | `$2665.6645` | **+4.76%** | **+4.54%** | +20.0% | -0.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+12.9%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-5.0%`** |
| `stall_bailout` | `1` | `0.0%` | **`-0.9%`** |
| `structural_stop` | `1` | `0.0%` | **`-1.6%`** |
| `time_cap` | `1` | `100.0%` | **`+20.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+3.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `ETH`

* **Total Candidate Breakouts Filtered (Vetoed):** `360`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `183` (50.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `22`
* **Saved Capital Losses Avoided:** `+1,853.7%`
* **Missed Upside Forgone:** `-655.5%`
* **Net Veto Alpha:** `+1,198.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `231` | `64.2%` |
| `Core 1: Macro Bear Veto` | `89` | `24.7%` |
| `Core 4: Funding Rate Cap` | `22` | `6.1%` |
| `Core 4: Defensible Whale Dump` | `12` | `3.3%` |
| `Core 4: Whale Firewall` | `5` | `1.4%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*