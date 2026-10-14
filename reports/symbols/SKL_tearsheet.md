# Kronos V12: Institutional Symbol Tear Sheet — `SKL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `29` (`29` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `29` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`69.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.336`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+96.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.62x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.32%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-21.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`29.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.6% / -6.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-11 06:00` | `2021-08-12 16:00` | 34.0h | `$0.3322` | `$0.2824` | **-13.97%** | **-15.15%** | +1.3% | -15.3% | `structural_stop` |
| 2 | Book 3 | `2022-03-25 15:00` | `2022-03-26 13:00` | 22.0h | `$0.1445` | `$0.1505` | **+4.17%** | **+4.08%** | +7.7% | -5.1% | `target_reclaim` |
| 3 | Book 3 | `2023-01-14 09:00` | `2023-01-16 06:00` | 45.0h | `$0.0275` | `$0.0298` | **+8.28%** | **+7.96%** | +8.5% | -2.4% | `target_reclaim` |
| 4 | Book 3 | `2023-01-18 15:00` | `2023-01-20 20:00` | 53.0h | `$0.0275` | `$0.0302` | **+9.96%** | **+9.49%** | +16.0% | -4.1% | `target_reclaim` |
| 5 | Book 4 | `2023-02-10 13:00` | `2023-02-10 19:00` | 6.0h | `$0.0488` | `$0.0586` | **+8.96%** | **+8.52%** | +23.7% | -4.7% | `target_reclaim` |
| 6 | Book 3 | `2023-02-13 16:00` | `2023-02-15 16:00` | 48.0h | `$0.0497` | `$0.0571` | **+15.04%** | **+14.01%** | +17.3% | -4.0% | `target_reclaim` |
| 7 | Book 3 | `2023-07-05 10:00` | `2023-07-06 09:00` | 23.0h | `$0.0281` | `$0.0294` | **+4.67%** | **+4.56%** | +5.3% | -1.6% | `target_reclaim` |
| 8 | Book 2 | `2023-07-13 16:00` | `2023-07-15 16:00` | 48.0h | `$0.0293` | `$0.0292` | **-0.33%** | **-0.33%** | +3.2% | -6.1% | `fast_decay_cut` |
| 9 | Book 2 | `2023-10-16 05:00` | `2023-10-17 13:00` | 32.0h | `$0.0223` | `$0.0206` | **-8.83%** | **-9.20%** | +1.2% | -8.2% | `initial_stop` |
| 10 | Book 3 | `2023-11-09 16:00` | `2023-11-10 00:00` | 8.0h | `$0.0269` | `$0.0293` | **+8.70%** | **+8.34%** | +13.9% | -6.5% | `target_reclaim` |
| 11 | Book 3 | `2023-11-14 00:00` | `2023-11-15 20:00` | 44.0h | `$0.0287` | `$0.0312` | **+8.70%** | **+8.34%** | +10.4% | -7.3% | `target_reclaim` |
| 12 | Book 3 | `2023-11-18 13:00` | `2023-11-18 23:00` | 10.0h | `$0.0298` | `$0.0324` | **+8.70%** | **+8.34%** | +8.7% | -0.2% | `target_reclaim` |
| 13 | Book 3 | `2024-01-02 20:00` | `2024-01-03 08:00` | 12.0h | `$0.0870` | `$0.0946` | **+8.70%** | **+8.34%** | +12.6% | -5.3% | `target_reclaim` |
| 14 | Book 3 | `2024-01-03 12:00` | `2024-01-03 17:00` | 5.0h | `$0.0925` | `$0.1006` | **+8.70%** | **+8.34%** | +10.5% | -16.5% | `target_reclaim` |
| 15 | Book 3 | `2024-02-10 10:00` | `2024-02-13 10:00` | 72.0h | `$0.0769` | `$0.0790` | **+2.78%** | **+2.74%** | +6.0% | -1.7% | `time_expiry` |
| 16 | Book 3 | `2024-02-14 00:00` | `2024-02-14 08:00` | 8.0h | `$0.0803` | `$0.0846` | **+5.44%** | **+5.30%** | +6.8% | -0.3% | `target_reclaim` |
| 17 | Book 3 | `2024-03-29 01:00` | `2024-03-29 10:00` | 9.0h | `$0.1140` | `$0.1239` | **+8.70%** | **+8.34%** | +8.9% | -2.6% | `target_reclaim` |
| 18 | Book 3 | `2024-03-30 16:00` | `2024-04-02 02:00` | 58.0h | `$0.1203` | `$0.1104` | **-8.23%** | **-8.59%** | +1.5% | -9.1% | `stop_loss` |
| 19 | Book 3 | `2024-08-02 03:00` | `2024-08-03 00:00` | 21.0h | `$0.0528` | `$0.0484` | **-8.23%** | **-8.59%** | +2.3% | -9.2% | `stop_loss` |
| 20 | Book 3 | `2024-11-12 16:00` | `2024-11-15 16:00` | 72.0h | `$0.0387` | `$0.0370` | **-4.45%** | **-4.55%** | +10.4% | -6.3% | `time_expiry` |
| 21 | Book 3 | `2024-11-17 18:00` | `2024-11-18 15:00` | 21.0h | `$0.0415` | `$0.0472` | **+13.66%** | **+12.80%** | +14.9% | -2.7% | `target_reclaim` |
| 22 | Book 3 | `2025-04-21 17:00` | `2025-04-22 23:00` | 30.0h | `$0.0232` | `$0.0253` | **+8.70%** | **+8.34%** | +11.0% | -6.7% | `target_reclaim` |
| 23 | Book 3 | `2025-06-30 14:00` | `2025-07-03 06:00` | 64.0h | `$0.0183` | `$0.0191` | **+4.17%** | **+4.08%** | +4.2% | -6.2% | `target_reclaim` |
| 24 | Book 3 | `2025-07-15 02:00` | `2025-07-15 05:00` | 3.0h | `$0.0231` | `$0.0241` | **+4.17%** | **+4.08%** | +7.1% | -3.3% | `target_reclaim` |
| 25 | Book 3 | `2025-07-21 16:00` | `2025-07-23 13:00` | 45.0h | `$0.0241` | `$0.0221` | **-8.23%** | **-8.59%** | +3.1% | -8.5% | `stop_loss` |
| 26 | Book 4 | `2025-08-13 05:00` | `2025-08-14 00:00` | 19.0h | `$0.0273` | `$0.0328` | **+26.78%** | **+24.17%** | +21.6% | -3.6% | `target_reclaim` |
| 27 | Book 3 | `2025-09-22 02:00` | `2025-09-22 06:00` | 4.0h | `$0.0259` | `$0.0238` | **-8.23%** | **-8.59%** | +1.5% | -11.1% | `stop_loss` |
| 28 | Book 5 (Shelf Absorption Squeeze) | `2026-07-10 05:00` | `2026-07-14 05:00` | Live | `$0.0049` | `$0.0045` | **-8.20%** | **-8.56%** | +-1.0% | -29.3% | `shelf_stop_loss` |
| 29 | Book 3 | `2026-08-23 04:00` | `2026-08-23 13:00` | 9.0h | `$0.0037` | `$0.0040` | **+8.70%** | **+8.34%** | +10.0% | -0.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `19` | `100.0%` | **`+165.8%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `time_expiry` | `2` | `50.0%` | **`-1.8%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `initial_stop` | `1` | `0.0%` | **`-9.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.3%`** |
| `structural_stop` | `1` | `0.0%` | **`-15.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `SKL`

* **Total Candidate Breakouts Filtered (Vetoed):** `1630`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `989` (60.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `468`
* **Saved Capital Losses Avoided:** `+14,354.6%`
* **Missed Upside Forgone:** `-16,882.4%`
* **Net Veto Alpha:** `+-2,527.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `486` | `29.8%` |
| `Core 1: Macro Bear Veto` | `417` | `25.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `393` | `24.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `274` | `16.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `60` | `3.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*