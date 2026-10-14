# Kronos V12: Institutional Symbol Tear Sheet — `CRV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `18` (`18` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `18` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`44.4%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.907`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+63.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.89x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.54%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-26.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`103.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.7% / -6.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2022-03-27 21:00` | `2022-04-01 01:00` | 100.0h | `$2.6265` | `$2.6015` | **-1.46%** | **-1.47%** | +12.0% | -4.2% | `fast_decay_cut` |
| 2 | Book 1 | `2022-10-28 16:00` | `2022-10-30 16:00` | 48.0h | `$0.9634` | `$0.8918` | **-11.27%** | **-11.95%** | +1.6% | -7.7% | `fast_decay_cut` |
| 3 | Book 4 | `2023-01-20 19:00` | `2023-02-08 13:00` | 450.0h | `$0.9795` | `$1.1754` | **+11.57%** | **+11.04%** | +27.2% | -3.5% | `target_reclaim` |
| 4 | Book 2 | `2023-06-20 17:00` | `2023-06-27 17:00` | 168.0h | `$0.6546` | `$0.6963` | **+7.41%** | **+7.19%** | +13.5% | -2.5% | `time_cap` |
| 5 | Book 1 | `2023-07-04 09:00` | `2023-07-06 13:00` | 52.0h | `$0.8070` | `$0.7601` | **-8.45%** | **-8.84%** | +2.2% | -5.9% | `fast_decay_cut` |
| 6 | Book 2 | `2023-07-13 16:00` | `2023-07-18 16:00` | 120.0h | `$0.8411` | `$0.7719` | **-8.41%** | **-8.78%** | +4.5% | -8.1% | `initial_stop` |
| 7 | Book 2 | `2023-10-01 22:00` | `2023-10-02 14:00` | 16.0h | `$0.5434` | `$0.5084` | **-7.24%** | **-7.48%** | +0.5% | -6.9% | `initial_stop` |
| 8 | Book 1 | `2023-11-05 03:00` | `2023-11-07 15:00` | 60.0h | `$0.5674` | `$0.5436` | **-1.60%** | **-1.61%** | +4.5% | -4.8% | `fast_decay_cut` |
| 9 | Book 3 | `2024-02-20 15:00` | `2024-02-23 14:00` | 71.0h | `$0.5462` | `$0.5690` | **+4.17%** | **+4.08%** | +7.5% | -6.3% | `target_reclaim` |
| 10 | Book 3 | `2024-03-03 07:00` | `2024-03-03 11:00` | 4.0h | `$0.6074` | `$0.6700` | **+10.31%** | **+9.81%** | +12.8% | -2.9% | `target_reclaim` |
| 11 | Book 3 | `2024-03-05 19:00` | `2024-03-06 07:00` | 12.0h | `$0.6326` | `$0.7120` | **+12.55%** | **+11.82%** | +17.1% | -10.1% | `target_reclaim` |
| 12 | Book 3 | `2024-03-12 16:00` | `2024-03-13 06:00` | 14.0h | `$0.7884` | `$0.8570` | **+8.70%** | **+8.34%** | +9.1% | -3.7% | `target_reclaim` |
| 13 | Book 3 | `2024-03-14 19:00` | `2024-03-15 09:00` | 14.0h | `$0.7967` | `$0.7311` | **-8.23%** | **-8.59%** | +6.2% | -11.4% | `stop_loss` |
| 14 | Book 4 | `2024-11-16 16:00` | `2024-11-19 10:00` | 66.0h | `$0.3615` | `$0.4266` | **+9.00%** | **+8.28%** | +21.7% | -13.1% | `climax_whale_euphoria_harvest` |
| 15 | Book 3 | `2024-12-09 06:00` | `2024-12-09 20:00` | 14.0h | `$1.1043` | `$1.0134` | **-8.23%** | **-8.59%** | +2.1% | -8.5% | `stop_loss` |
| 16 | Book 1 | `2025-04-30 17:00` | `2025-05-04 18:00` | 97.0h | `$0.6937` | `$0.6813` | **-3.44%** | **-3.48%** | +8.4% | -3.6% | `fast_decay_cut` |
| 17 | Book 1 | `2025-07-10 21:00` | `2025-07-31 21:00` | 504.0h | `$0.6015` | `$0.9576` | **+102.64%** | **+73.46%** | +93.5% | -3.7% | `time_cap` |
| 18 | Book 2 | `2025-10-26 22:00` | `2025-10-28 20:00` | 46.0h | `$0.5804` | `$0.5327` | **-9.09%** | **-9.49%** | +2.7% | -8.5% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `5` | `0.0%` | **`-27.4%`** |
| `target_reclaim` | `5` | `100.0%` | **`+45.1%`** |
| `initial_stop` | `3` | `0.0%` | **`-25.7%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_cap` | `2` | `100.0%` | **`+80.6%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `CRV`

* **Total Candidate Breakouts Filtered (Vetoed):** `383`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `302` (78.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `47`
* **Saved Capital Losses Avoided:** `+4,351.1%`
* **Missed Upside Forgone:** `-1,726.8%`
* **Net Veto Alpha:** `+2,624.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `216` | `56.4%` |
| `Core 1: Macro Bear Veto` | `144` | `37.6%` |
| `Core 4: Funding Rate Cap` | `12` | `3.1%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `5` | `1.3%` |
| `Core 4: Defensible Whale Dump` | `4` | `1.0%` |
| `Core 4: Whale Firewall` | `2` | `0.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*