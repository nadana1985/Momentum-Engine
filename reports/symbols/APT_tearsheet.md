# Kronos V12: Institutional Symbol Tear Sheet — `APT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `17` (`17` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `17` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`64.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.668`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+121.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`3.36x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+7.12%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-10.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`88.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.7% / -5.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-01-09 11:00` | `2023-01-09 16:00` | 5.0h | `$4.1907` | `$5.0288` | **+31.07%** | **+27.17%** | +28.2% | -2.3% | `target_reclaim` |
| 2 | Book 4 | `2023-01-12 19:00` | `2023-01-14 01:00` | 30.0h | `$6.1955` | `$7.4346` | **+18.89%** | **+16.03%** | +27.5% | -0.2% | `target_reclaim` |
| 3 | Book 2 | `2023-07-13 16:00` | `2023-07-20 16:00` | 168.0h | `$7.3553` | `$7.4064` | **+0.77%** | **+0.76%** | +11.4% | -3.7% | `time_cap` |
| 4 | Book 2 | `2023-10-16 05:00` | `2023-10-19 01:00` | 68.0h | `$5.0125` | `$4.7730` | **-5.59%** | **-5.73%** | +4.4% | -4.6% | `initial_stop` |
| 5 | Book 1 | `2023-10-21 17:00` | `2023-10-25 22:00` | 101.0h | `$5.7975` | `$6.9569` | **+34.09%** | **+29.81%** | +21.0% | -6.0% | `target_reclaim` |
| 6 | Book 3 | `2023-12-11 02:00` | `2023-12-12 07:00` | 29.0h | `$7.3921` | `$8.2800` | **+12.01%** | **+11.34%** | +13.6% | -1.5% | `target_reclaim` |
| 7 | Book 3 | `2023-12-23 07:00` | `2023-12-25 13:00` | 54.0h | `$9.2018` | `$10.0020` | **+8.70%** | **+8.34%** | +13.2% | -2.4% | `target_reclaim` |
| 8 | Book 3 | `2023-12-26 17:00` | `2023-12-26 19:00` | 2.0h | `$9.4843` | `$10.3090` | **+8.70%** | **+8.34%** | +10.7% | -4.4% | `target_reclaim` |
| 9 | Book 3 | `2023-12-28 06:00` | `2023-12-31 06:00` | 72.0h | `$9.9489` | `$9.4613` | **-4.90%** | **-5.03%** | +1.9% | -6.5% | `time_expiry` |
| 10 | Book 3 | `2024-02-17 10:00` | `2024-02-19 08:00` | 46.0h | `$9.4909` | `$10.0480` | **+5.87%** | **+5.70%** | +6.0% | -3.1% | `target_reclaim` |
| 11 | Book 1 | `2024-07-19 16:00` | `2024-07-22 16:00` | 72.0h | `$7.4205` | `$7.2698` | **-3.37%** | **-3.42%** | +3.1% | -4.8% | `stagnation_bailout` |
| 12 | Book 4 | `2024-09-21 09:00` | `2024-10-07 18:00` | 393.0h | `$7.7535` | `$9.3042` | **+30.07%** | **+26.83%** | +20.4% | -6.9% | `target_reclaim` |
| 13 | Book 3 | `2024-12-09 20:00` | `2024-12-09 21:00` | 1.0h | `$13.0387` | `$11.9656` | **-8.23%** | **-8.59%** | +1.2% | -21.5% | `stop_loss` |
| 14 | Book 2 | `2025-04-24 00:00` | `2025-04-27 04:00` | 76.0h | `$5.4776` | `$5.4632` | **-0.30%** | **-0.30%** | +3.8% | -5.7% | `stagnation_cut` |
| 15 | Book 2 | `2025-05-08 15:00` | `2025-05-15 15:00` | 168.0h | `$5.1919` | `$6.1265` | **+18.00%** | **+16.55%** | +21.0% | -1.8% | `climax_whale_euphoria_harvest` |
| 16 | Book 2 | `2025-08-08 07:00` | `2025-08-15 07:00` | 168.0h | `$4.6617` | `$4.7995` | **+3.28%** | **+3.23%** | +10.5% | -3.9% | `time_cap` |
| 17 | Book 2 | `2025-10-26 16:00` | `2025-10-28 20:00` | 52.0h | `$3.6086` | `$3.3116` | **-9.54%** | **-9.95%** | +1.1% | -8.0% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+133.6%`** |
| `initial_stop` | `2` | `0.0%` | **`-15.7%`** |
| `time_cap` | `2` | `100.0%` | **`+4.0%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-0.3%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-3.4%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `0.0%` | **`-5.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `APT`

* **Total Candidate Breakouts Filtered (Vetoed):** `73`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `49` (67.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+480.7%`
* **Missed Upside Forgone:** `-261.8%`
* **Net Veto Alpha:** `+219.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `42` | `57.5%` |
| `Core 4: Funding Rate Cap` | `18` | `24.7%` |
| `Core 4: Defensible Whale Dump` | `6` | `8.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `5` | `6.8%` |
| `Core 4: Whale Firewall` | `2` | `2.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*