# Kronos V12: Institutional Symbol Tear Sheet — `BNT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`61.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.202`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+41.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.52x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.21%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`42.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.2% / -5.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2023-10-13 10:00` | `2023-10-17 01:00` | 87.0h | `$0.5182` | `$0.6218` | **+7.35%** | **+7.13%** | +20.6% | -4.8% | `target_reclaim` |
| 2 | Book 3 | `2023-10-19 01:00` | `2023-10-22 01:00` | 72.0h | `$0.5380` | `$0.5513` | **+2.48%** | **+2.45%** | +15.8% | -1.4% | `time_expiry` |
| 3 | Book 3 | `2023-11-13 01:00` | `2023-11-13 02:00` | 1.0h | `$1.7059` | `$1.5648` | **-8.27%** | **-8.63%** | +14.3% | -14.6% | `stop_loss` |
| 4 | Book 3 | `2023-12-10 09:00` | `2023-12-11 02:00` | 17.0h | `$0.7820` | `$0.7176` | **-8.23%** | **-8.59%** | +4.1% | -16.2% | `stop_loss` |
| 5 | Book 3 | `2024-02-28 17:00` | `2024-02-29 00:00` | 7.0h | `$0.7974` | `$0.8788` | **+10.20%** | **+9.72%** | +12.7% | -2.1% | `target_reclaim` |
| 6 | Book 3 | `2024-03-14 13:00` | `2024-03-15 08:00` | 19.0h | `$0.9592` | `$0.8802` | **-8.23%** | **-8.59%** | +4.4% | -8.7% | `stop_loss` |
| 7 | Book 3 | `2024-05-28 18:00` | `2024-05-31 18:00` | 72.0h | `$0.8025` | `$0.7995` | **-0.37%** | **-0.37%** | +3.1% | -2.0% | `time_expiry` |
| 8 | Book 3 | `2024-07-21 18:00` | `2024-07-21 20:00` | 2.0h | `$0.6228` | `$0.6487` | **+4.17%** | **+4.08%** | +5.6% | -1.2% | `target_reclaim` |
| 9 | Book 3 | `2024-11-20 19:00` | `2024-11-21 12:00` | 17.0h | `$0.5991` | `$0.6458` | **+7.79%** | **+7.50%** | +10.5% | -1.2% | `target_reclaim` |
| 10 | Book 3 | `2024-12-09 12:00` | `2024-12-09 21:00` | 9.0h | `$0.8735` | `$0.8017` | **-8.23%** | **-8.59%** | +6.3% | -19.0% | `stop_loss` |
| 11 | Book 2 | `2025-04-22 15:00` | `2025-04-29 15:00` | 168.0h | `$0.4061` | `$0.4602` | **+15.20%** | **+14.27%** | +19.5% | -1.1% | `time_cap` |
| 12 | Book 4 | `2025-05-08 15:00` | `2025-05-10 14:00` | 47.0h | `$0.5227` | `$0.6272` | **+30.79%** | **+27.31%** | +20.4% | -0.4% | `target_reclaim` |
| 13 | Book 3 | `2025-07-01 11:00` | `2025-07-02 17:00` | 30.0h | `$0.5791` | `$0.6032` | **+4.17%** | **+4.08%** | +7.5% | -2.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+59.8%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `time_expiry` | `2` | `50.0%` | **`+2.1%`** |
| `time_cap` | `1` | `100.0%` | **`+14.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `BNT`

* **Total Candidate Breakouts Filtered (Vetoed):** `1136`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `498` (43.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `67`
* **Saved Capital Losses Avoided:** `+4,223.3%`
* **Missed Upside Forgone:** `-2,501.8%`
* **Net Veto Alpha:** `+1,721.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `846` | `74.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `181` | `15.9%` |
| `Core 1: Macro Bear Veto` | `54` | `4.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `34` | `3.0%` |
| `Core 4: Defensible Whale Dump` | `20` | `1.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*