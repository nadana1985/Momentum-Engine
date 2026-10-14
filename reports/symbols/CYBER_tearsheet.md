# Kronos V12: Institutional Symbol Tear Sheet — `CYBER`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `17` (`17` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `17` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`47.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.014`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+0.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.01x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.06%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-37.0%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`30.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.1% / -7.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-10-31 12:00` | `2023-10-31 13:00` | 1.0h | `$7.1914` | `$7.4910` | **+4.17%** | **+4.08%** | +6.6% | -1.0% | `target_reclaim` |
| 2 | Book 3 | `2023-11-13 17:00` | `2023-11-14 18:00` | 25.0h | `$7.2150` | `$6.6212` | **-8.23%** | **-8.59%** | +6.5% | -8.5% | `stop_loss` |
| 3 | Book 3 | `2023-12-26 17:00` | `2023-12-27 07:00` | 14.0h | `$6.4890` | `$7.5120` | **+15.77%** | **+14.64%** | +17.9% | -2.5% | `target_reclaim` |
| 4 | Book 3 | `2024-01-03 12:00` | `2024-01-03 13:00` | 1.0h | `$7.2330` | `$8.3190` | **+15.01%** | **+13.99%** | +28.3% | -9.7% | `target_reclaim` |
| 5 | Book 3 | `2024-03-03 07:00` | `2024-03-05 19:00` | 60.0h | `$8.8907` | `$8.1590` | **-8.23%** | **-8.59%** | +17.1% | -9.8% | `stop_loss` |
| 6 | Book 3 | `2024-03-10 00:00` | `2024-03-10 05:00` | 5.0h | `$11.7346` | `$10.7688` | **-8.23%** | **-8.59%** | +1.2% | -8.7% | `stop_loss` |
| 7 | Book 3 | `2024-03-27 04:00` | `2024-03-27 14:00` | 10.0h | `$13.8340` | `$12.6955` | **-8.23%** | **-8.59%** | +9.9% | -8.7% | `stop_loss` |
| 8 | Book 3 | `2024-05-23 04:00` | `2024-05-26 04:00` | 72.0h | `$8.8722` | `$8.8369` | **-0.40%** | **-0.40%** | +6.3% | -5.5% | `time_expiry` |
| 9 | Book 2 | `2024-08-11 05:00` | `2024-08-11 19:00` | 14.0h | `$3.1709` | `$2.9099` | **-10.13%** | **-10.57%** | +1.8% | -8.9% | `initial_stop` |
| 10 | Book 3 | `2024-09-25 17:00` | `2024-09-26 06:00` | 13.0h | `$3.6374` | `$3.7890` | **+4.17%** | **+4.08%** | +4.6% | -2.1% | `target_reclaim` |
| 11 | Book 3 | `2024-09-28 09:00` | `2024-10-01 09:00` | 72.0h | `$3.7227` | `$3.5661` | **-4.21%** | **-4.30%** | +2.5% | -8.0% | `time_expiry` |
| 12 | Book 3 | `2024-11-13 06:00` | `2024-11-13 14:00` | 8.0h | `$3.3485` | `$3.6030` | **+7.60%** | **+7.33%** | +9.8% | -0.2% | `target_reclaim` |
| 13 | Book 3 | `2024-12-02 08:00` | `2024-12-03 00:00` | 16.0h | `$4.4381` | `$4.8240` | **+8.70%** | **+8.34%** | +9.1% | -2.9% | `target_reclaim` |
| 14 | Book 3 | `2024-12-03 13:00` | `2024-12-03 19:00` | 6.0h | `$4.6561` | `$5.0610` | **+8.70%** | **+8.34%** | +8.8% | -2.5% | `target_reclaim` |
| 15 | Book 3 | `2024-12-08 22:00` | `2024-12-09 20:00` | 22.0h | `$5.1787` | `$4.7525` | **-8.23%** | **-8.59%** | +4.5% | -16.1% | `stop_loss` |
| 16 | Book 2 | `2025-04-21 04:00` | `2025-04-28 04:00` | 168.0h | `$1.2351` | `$1.3067` | **+7.14%** | **+6.94%** | +16.0% | -5.0% | `time_cap` |
| 17 | Book 3 | `2025-09-22 00:00` | `2025-09-22 06:00` | 6.0h | `$1.8106` | `$1.6616` | **-8.23%** | **-8.59%** | +3.4% | -18.5% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `7` | `100.0%` | **`+60.8%`** |
| `stop_loss` | `6` | `0.0%` | **`-51.5%`** |
| `time_expiry` | `2` | `0.0%` | **`-4.7%`** |
| `initial_stop` | `1` | `0.0%` | **`-10.6%`** |
| `time_cap` | `1` | `100.0%` | **`+6.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `CYBER`

* **Total Candidate Breakouts Filtered (Vetoed):** `387`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `240` (62.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `17`
* **Saved Capital Losses Avoided:** `+4,244.9%`
* **Missed Upside Forgone:** `-842.2%`
* **Net Veto Alpha:** `+3,402.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `337` | `87.1%` |
| `Core 1: Macro Bear Veto` | `25` | `6.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `20` | `5.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `5` | `1.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*