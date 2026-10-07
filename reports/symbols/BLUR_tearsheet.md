# Kronos V12: Institutional Symbol Tear Sheet — `BLUR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `26` (`26` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `26` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`61.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.808`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+56.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.76x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+2.17%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-27.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`33.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.7% / -5.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-10-03 01:00` | `2023-10-06 01:00` | 72.0h | `$0.1784` | `$0.1728` | **-3.15%** | **-3.20%** | +2.2% | -6.5% | `time_expiry` |
| 2 | Book 3 | `2023-10-18 21:00` | `2023-10-18 23:00` | 2.0h | `$0.1874` | `$0.2037` | **+8.70%** | **+8.34%** | +8.7% | -2.4% | `target_reclaim` |
| 3 | Book 3 | `2023-10-24 15:00` | `2023-10-24 18:00` | 3.0h | `$0.2092` | `$0.2274` | **+8.70%** | **+8.34%** | +14.1% | -2.1% | `target_reclaim` |
| 4 | Book 3 | `2023-10-26 14:00` | `2023-10-29 14:00` | 72.0h | `$0.2355` | `$0.2444` | **+3.77%** | **+3.70%** | +6.0% | -7.6% | `time_expiry` |
| 5 | Book 3 | `2023-10-31 05:00` | `2023-11-01 14:00` | 33.0h | `$0.2448` | `$0.2247` | **-8.23%** | **-8.59%** | +2.3% | -8.6% | `stop_loss` |
| 6 | Book 3 | `2023-11-06 21:00` | `2023-11-07 06:00` | 9.0h | `$0.3522` | `$0.3828` | **+8.70%** | **+8.34%** | +13.3% | -1.1% | `target_reclaim` |
| 7 | Book 3 | `2023-11-07 09:00` | `2023-11-09 05:00` | 44.0h | `$0.3623` | `$0.3938` | **+8.70%** | **+8.34%** | +9.1% | -2.5% | `target_reclaim` |
| 8 | Book 3 | `2023-11-11 08:00` | `2023-11-11 14:00` | 6.0h | `$0.4010` | `$0.4359` | **+8.70%** | **+8.34%** | +9.9% | -2.1% | `target_reclaim` |
| 9 | Book 3 | `2023-11-23 11:00` | `2023-11-23 12:00` | 1.0h | `$0.4600` | `$0.5000` | **+8.70%** | **+8.34%** | +9.7% | -1.8% | `target_reclaim` |
| 10 | Book 3 | `2023-11-25 11:00` | `2023-11-26 16:00` | 29.0h | `$0.5788` | `$0.5311` | **-8.23%** | **-8.59%** | +8.6% | -8.1% | `stop_loss` |
| 11 | Book 3 | `2023-12-03 14:00` | `2023-12-04 03:00` | 13.0h | `$0.5176` | `$0.5626` | **+8.70%** | **+8.34%** | +10.9% | -0.4% | `target_reclaim` |
| 12 | Book 3 | `2024-01-03 12:00` | `2024-01-05 01:00` | 37.0h | `$0.5300` | `$0.4864` | **-8.23%** | **-8.59%** | +4.7% | -22.3% | `stop_loss` |
| 13 | Book 3 | `2024-01-12 17:00` | `2024-01-13 08:00` | 15.0h | `$0.5776` | `$0.6278` | **+8.70%** | **+8.34%** | +9.7% | -6.1% | `target_reclaim` |
| 14 | Book 3 | `2024-02-20 15:00` | `2024-02-23 04:00` | 61.0h | `$0.7270` | `$0.6672` | **-8.23%** | **-8.59%** | +7.3% | -8.3% | `stop_loss` |
| 15 | Book 3 | `2024-02-25 07:00` | `2024-02-28 07:00` | 72.0h | `$0.7552` | `$0.7341` | **-2.80%** | **-2.84%** | +6.1% | -5.7% | `time_expiry` |
| 16 | Book 3 | `2024-05-28 01:00` | `2024-05-31 01:00` | 72.0h | `$0.4317` | `$0.4037` | **-6.48%** | **-6.70%** | +2.7% | -6.8% | `time_expiry` |
| 17 | Book 3 | `2024-10-09 12:00` | `2024-10-12 12:00` | 72.0h | `$0.2185` | `$0.2316` | **+6.00%** | **+5.83%** | +7.2% | -7.9% | `time_expiry` |
| 18 | Book 3 | `2024-10-22 09:00` | `2024-10-25 09:00` | 72.0h | `$0.2601` | `$0.2460` | **-5.42%** | **-5.57%** | +1.9% | -7.7% | `time_expiry` |
| 19 | Book 3 | `2024-11-11 21:00` | `2024-11-12 10:00` | 13.0h | `$0.2717` | `$0.2493` | **-8.23%** | **-8.59%** | +3.1% | -10.2% | `stop_loss` |
| 20 | Book 3 | `2024-11-24 11:00` | `2024-11-24 22:00` | 11.0h | `$0.2937` | `$0.3193` | **+8.70%** | **+8.34%** | +10.4% | -5.4% | `target_reclaim` |
| 21 | Book 3 | `2024-11-26 11:00` | `2024-11-27 20:00` | 33.0h | `$0.2964` | `$0.3222` | **+8.70%** | **+8.34%** | +9.6% | -0.7% | `target_reclaim` |
| 22 | Book 3 | `2025-07-01 05:00` | `2025-07-02 19:00` | 38.0h | `$0.0691` | `$0.0751` | **+8.70%** | **+8.34%** | +8.9% | -2.6% | `target_reclaim` |
| 23 | Book 3 | `2025-09-21 17:00` | `2025-09-22 06:00` | 13.0h | `$0.0834` | `$0.0766` | **-8.23%** | **-8.59%** | +1.6% | -12.5% | `stop_loss` |
| 24 | Book 3 | `2026-09-10 02:00` | `2026-09-11 14:00` | 36.0h | `$0.0171` | `$0.0186` | **+8.70%** | **+8.34%** | +12.0% | -7.0% | `target_reclaim` |
| 25 | Book 3 | `2026-09-11 21:00` | `2026-09-13 13:00` | 40.0h | `$0.0176` | `$0.0191` | **+8.70%** | **+8.34%** | +10.9% | -4.7% | `target_reclaim` |
| 26 | Book 3 | `2026-10-02 18:00` | `2026-10-03 04:00` | 10.0h | `$0.0202` | `$0.0220` | **+8.70%** | **+8.34%** | +9.4% | -1.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `14` | `100.0%` | **`+116.7%`** |
| `stop_loss` | `6` | `0.0%` | **`-51.5%`** |
| `time_expiry` | `6` | `33.3%` | **`-8.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `BLUR`

* **Total Candidate Breakouts Filtered (Vetoed):** `143`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `88` (61.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `22`
* **Saved Capital Losses Avoided:** `+1,142.3%`
* **Missed Upside Forgone:** `-637.5%`
* **Net Veto Alpha:** `+504.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `57` | `39.9%` |
| `Core 1: Macro Bear Veto` | `34` | `23.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `28` | `19.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `24` | `16.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*