# Kronos V12: Institutional Symbol Tear Sheet — `LUNA2`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `18` (`18` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `18` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`61.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.291`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+63.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.89x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.55%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-24.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`43.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.6% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-07-17 13:00` | `2023-07-20 13:00` | 72.0h | `$0.6640` | `$0.6523` | **-1.77%** | **-1.78%** | +4.2% | -8.0% | `time_expiry` |
| 2 | Book 3 | `2023-10-26 14:00` | `2023-10-28 02:00` | 36.0h | `$0.4402` | `$0.4611` | **+4.74%** | **+4.64%** | +8.3% | -3.3% | `target_reclaim` |
| 3 | Book 3 | `2023-11-09 16:00` | `2023-11-10 01:00` | 9.0h | `$0.4413` | `$0.5093` | **+15.40%** | **+14.32%** | +17.3% | -6.6% | `target_reclaim` |
| 4 | Book 3 | `2023-12-04 11:00` | `2023-12-04 12:00` | 1.0h | `$0.9387` | `$1.0203` | **+8.70%** | **+8.34%** | +20.9% | -4.1% | `target_reclaim` |
| 5 | Book 3 | `2023-12-05 07:00` | `2023-12-05 10:00` | 3.0h | `$1.1211` | `$1.2186` | **+8.70%** | **+8.34%** | +10.5% | -4.9% | `target_reclaim` |
| 6 | Book 3 | `2024-02-29 22:00` | `2024-03-02 00:00` | 26.0h | `$0.6784` | `$0.7774` | **+14.60%** | **+13.62%** | +17.2% | -0.0% | `target_reclaim` |
| 7 | Book 3 | `2024-03-03 07:00` | `2024-03-03 08:00` | 1.0h | `$0.7219` | `$0.8038` | **+11.35%** | **+10.75%** | +16.8% | -1.9% | `target_reclaim` |
| 8 | Book 3 | `2024-03-05 19:00` | `2024-03-05 20:00` | 1.0h | `$0.8832` | `$1.0422` | **+18.00%** | **+16.55%** | +41.5% | -2.1% | `climax_whale_euphoria_harvest` |
| 9 | Book 3 | `2024-05-30 22:00` | `2024-06-02 22:00` | 72.0h | `$0.6740` | `$0.6427` | **-4.64%** | **-4.75%** | +3.2% | -6.4% | `time_expiry` |
| 10 | Book 3 | `2024-09-30 18:00` | `2024-10-01 17:00` | 23.0h | `$0.4115` | `$0.3776` | **-8.23%** | **-8.59%** | +7.9% | -12.7% | `stop_loss` |
| 11 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$0.3880` | `$0.3561` | **-8.23%** | **-8.59%** | +4.8% | -10.0% | `stop_loss` |
| 12 | Book 4 | `2024-11-22 04:00` | `2024-11-30 16:00` | 204.0h | `$0.4718` | `$0.5662` | **+26.54%** | **+22.84%** | +21.4% | -6.4% | `target_reclaim` |
| 13 | Book 3 | `2025-05-12 18:00` | `2025-05-13 16:00` | 22.0h | `$0.2076` | `$0.2162` | **+4.17%** | **+4.08%** | +5.1% | -4.7% | `target_reclaim` |
| 14 | Book 3 | `2025-07-22 01:00` | `2025-07-23 17:00` | 40.0h | `$0.1863` | `$0.1710` | **-8.23%** | **-8.59%** | +2.7% | -9.4% | `stop_loss` |
| 15 | Book 3 | `2025-09-19 23:00` | `2025-09-22 06:00` | 55.0h | `$0.1531` | `$0.1405` | **-8.23%** | **-8.59%** | +3.9% | -14.2% | `stop_loss` |
| 16 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0487` | `$0.0491` | **+0.90%** | **+0.89%** | +10.5% | -6.3% | `time_expiry` |
| 17 | Book 3 | `2026-09-07 18:00` | `2026-09-09 22:00` | 52.0h | `$0.0488` | `$0.0448` | **-8.23%** | **-8.59%** | +1.8% | -8.6% | `stop_loss` |
| 18 | Book 3 | `2026-09-23 14:00` | `2026-09-26 14:00` | 72.0h | `$0.0496` | `$0.0542` | **+9.39%** | **+8.97%** | +11.3% | -0.3% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+86.9%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `time_expiry` | `4` | `50.0%` | **`+3.3%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `LUNA2`

* **Total Candidate Breakouts Filtered (Vetoed):** `454`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `249` (54.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `114`
* **Saved Capital Losses Avoided:** `+3,663.3%`
* **Missed Upside Forgone:** `-3,584.8%`
* **Net Veto Alpha:** `+78.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `310` | `68.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `98` | `21.6%` |
| `Core 1: Macro Bear Veto` | `35` | `7.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `10` | `2.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*