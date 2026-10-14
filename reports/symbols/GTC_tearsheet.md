# Kronos V12: Institutional Symbol Tear Sheet — `GTC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `34` (`34` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `34` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`58.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.882`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+89.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.44x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+2.62%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-26.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.1% / -8.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2022-03-28 23:00` | `2022-03-30 09:00` | 34.0h | `$7.1764` | `$8.1200` | **+13.15%** | **+12.35%** | +13.8% | -1.2% | `target_reclaim` |
| 2 | Book 3 | `2022-04-04 16:00` | `2022-04-06 00:00` | 32.0h | `$7.4600` | `$6.8460` | **-8.23%** | **-8.59%** | +10.2% | -8.1% | `stop_loss` |
| 3 | Book 3 | `2023-01-23 13:00` | `2023-01-24 07:00` | 18.0h | `$1.7002` | `$1.7850` | **+4.99%** | **+4.87%** | +5.2% | -1.4% | `target_reclaim` |
| 4 | Book 3 | `2023-01-24 21:00` | `2023-01-26 05:00` | 32.0h | `$1.7002` | `$1.8330` | **+7.81%** | **+7.52%** | +9.0% | -4.7% | `target_reclaim` |
| 5 | Book 3 | `2023-01-30 19:00` | `2023-01-31 00:00` | 5.0h | `$1.7613` | `$1.8620` | **+5.72%** | **+5.56%** | +7.3% | -1.8% | `target_reclaim` |
| 6 | Book 3 | `2023-02-01 16:00` | `2023-02-04 11:00` | 67.0h | `$1.8223` | `$2.1060` | **+15.57%** | **+14.47%** | +16.3% | -0.6% | `target_reclaim` |
| 7 | Book 3 | `2023-02-08 16:00` | `2023-02-09 19:00` | 27.0h | `$2.0282` | `$1.8613` | **-8.23%** | **-8.59%** | +2.9% | -12.3% | `stop_loss` |
| 8 | Book 3 | `2023-02-27 18:00` | `2023-03-01 16:00` | 46.0h | `$2.3503` | `$2.1569` | **-8.23%** | **-8.59%** | +5.3% | -8.1% | `stop_loss` |
| 9 | Book 5 (Shelf Absorption Squeeze) | `2023-03-21 13:00` | `2023-03-25 13:00` | Live | `$1.9164` | `$2.0793` | **+8.50%** | **+8.16%** | +19.3% | -19.3% | `shelf_target_reclaim` |
| 10 | Book 3 | `2023-03-27 04:00` | `2023-03-27 06:00` | 2.0h | `$2.3521` | `$2.1585` | **-8.23%** | **-8.59%** | +5.7% | -8.8% | `stop_loss` |
| 11 | Book 3 | `2023-07-05 10:00` | `2023-07-06 14:00` | 28.0h | `$1.1406` | `$1.0468` | **-8.23%** | **-8.59%** | +2.9% | -8.6% | `stop_loss` |
| 12 | Book 5 (Shelf Absorption Squeeze) | `2023-08-06 06:00` | `2023-08-10 06:00` | Live | `$0.9945` | `$1.0791` | **+8.50%** | **+8.16%** | +14.2% | -29.1% | `shelf_target_reclaim` |
| 13 | Book 3 | `2023-10-04 00:00` | `2023-10-05 12:00` | 36.0h | `$0.9201` | `$0.8987` | **-2.32%** | **-2.34%** | +0.9% | -4.9% | `stall_bailout` |
| 14 | Book 3 | `2023-11-09 16:00` | `2023-11-10 00:00` | 8.0h | `$1.0454` | `$1.1190` | **+7.04%** | **+6.80%** | +10.2% | -15.8% | `target_reclaim` |
| 15 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$1.1193` | `$1.1511` | **+2.84%** | **+2.80%** | +5.6% | -9.8% | `time_expiry` |
| 16 | Book 3 | `2024-02-13 13:00` | `2024-02-14 04:00` | 15.0h | `$1.2537` | `$1.3100` | **+4.49%** | **+4.39%** | +4.5% | -0.7% | `target_reclaim` |
| 17 | Book 3 | `2024-03-05 15:00` | `2024-03-05 19:00` | 4.0h | `$2.0571` | `$1.8878` | **-8.23%** | **-8.59%** | +15.2% | -18.2% | `stop_loss` |
| 18 | Book 3 | `2024-03-07 13:00` | `2024-03-09 17:00` | 52.0h | `$2.2604` | `$2.4570` | **+8.70%** | **+8.34%** | +9.5% | -7.5% | `target_reclaim` |
| 19 | Book 4 | `2024-05-31 06:00` | `2024-06-01 20:00` | 38.0h | `$1.4041` | `$1.6849` | **+21.96%** | **+20.17%** | +24.7% | -4.2% | `target_reclaim` |
| 20 | Book 3 | `2024-07-24 15:00` | `2024-07-25 16:00` | 25.0h | `$0.9084` | `$0.9530` | **+4.91%** | **+4.79%** | +5.0% | -1.5% | `target_reclaim` |
| 21 | Book 3 | `2024-07-27 18:00` | `2024-07-27 22:00` | 4.0h | `$0.9312` | `$0.9700` | **+4.17%** | **+4.08%** | +4.5% | -2.6% | `target_reclaim` |
| 22 | Book 4 | `2024-11-23 17:00` | `2024-11-29 20:00` | 147.0h | `$0.8383` | `$1.0059` | **+40.79%** | **+35.11%** | +20.1% | -4.6% | `target_reclaim` |
| 23 | Book 3 | `2024-12-04 16:00` | `2024-12-05 12:00` | 20.0h | `$1.2864` | `$1.3400` | **+4.17%** | **+4.08%** | +4.2% | -6.2% | `target_reclaim` |
| 24 | Book 3 | `2024-12-08 04:00` | `2024-12-09 09:00` | 29.0h | `$1.2849` | `$1.1792` | **-8.23%** | **-8.59%** | +4.0% | -8.7% | `stop_loss` |
| 25 | Book 3 | `2025-05-15 07:00` | `2025-05-17 00:00` | 41.0h | `$0.3234` | `$0.2968` | **-8.23%** | **-8.59%** | +2.7% | -8.2% | `stop_loss` |
| 26 | Book 3 | `2025-07-15 00:00` | `2025-07-15 21:00` | 21.0h | `$0.2795` | `$0.2980` | **+6.62%** | **+6.41%** | +8.1% | -2.0% | `target_reclaim` |
| 27 | Book 5 (Shelf Absorption Squeeze) | `2026-05-11 17:00` | `2026-05-15 17:00` | Live | `$0.1473` | `$0.1352` | **-8.20%** | **-8.56%** | +-3.8% | -41.5% | `shelf_stop_loss` |
| 28 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0796` | `$0.0855` | **+7.45%** | **+7.19%** | +17.8% | -0.4% | `time_expiry` |
| 29 | Book 3 | `2026-08-28 18:00` | `2026-08-31 18:00` | 72.0h | `$0.0827` | `$0.0804` | **-2.81%** | **-2.85%** | +3.2% | -5.4% | `time_expiry` |
| 30 | Book 2 | `2026-09-19 07:00` | `2026-09-23 15:00` | 104.0h | `$0.0847` | `$0.0836` | **-1.39%** | **-1.40%** | +5.4% | -3.4% | `fast_decay_cut` |
| 31 | Book 3 | `2026-09-28 09:00` | `2026-09-30 07:00` | 46.0h | `$0.0853` | `$0.1006` | **+18.00%** | **+16.55%** | +45.2% | -2.5% | `climax_whale_euphoria_harvest` |
| 32 | Book 3 | `2026-09-30 11:00` | `2026-09-30 13:00` | 2.0h | `$0.1068` | `$0.0980` | **-8.23%** | **-8.59%** | +6.9% | -9.1% | `stop_loss` |
| 33 | Book 3 | `2026-10-03 16:00` | `2026-10-04 10:00` | 18.0h | `$0.1155` | `$0.1255` | **+8.69%** | **+8.34%** | +11.1% | -5.5% | `target_reclaim` |
| 34 | Book 3 | `2026-10-05 02:00` | `2026-10-05 03:00` | 1.0h | `$0.1936` | `$0.1777` | **-8.23%** | **-8.59%** | +26.9% | -9.6% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `15` | `100.0%` | **`+147.3%`** |
| `stop_loss` | `10` | `0.0%` | **`-85.9%`** |
| `time_expiry` | `3` | `66.7%` | **`+7.1%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.4%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |
| `stall_bailout` | `1` | `0.0%` | **`-2.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `GTC`

* **Total Candidate Breakouts Filtered (Vetoed):** `981`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `574` (58.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `142`
* **Saved Capital Losses Avoided:** `+10,489.4%`
* **Missed Upside Forgone:** `-4,421.9%`
* **Net Veto Alpha:** `+6,067.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `529` | `53.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `333` | `33.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `53` | `5.4%` |
| `Core 1: Macro Bear Veto` | `46` | `4.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `20` | `2.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*