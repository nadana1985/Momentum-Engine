# Kronos V12: Institutional Symbol Tear Sheet — `ETHW`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `14` (`14` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `14` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`71.4%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.023`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+54.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.72x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.87%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-10.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`24.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.8% / -3.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-13 15:00` | `2024-02-14 03:00` | 12.0h | `$2.7571` | `$2.8720` | **+4.17%** | **+4.08%** | +4.7% | -0.3% | `target_reclaim` |
| 2 | Book 3 | `2024-02-17 14:00` | `2024-02-18 18:00` | 28.0h | `$2.7588` | `$2.9320` | **+6.28%** | **+6.09%** | +6.5% | -0.3% | `target_reclaim` |
| 3 | Book 3 | `2024-02-21 09:00` | `2024-02-24 09:00` | 72.0h | `$2.9299` | `$2.9007` | **-1.00%** | **-1.00%** | +3.6% | -4.0% | `time_expiry` |
| 4 | Book 3 | `2024-02-28 17:00` | `2024-02-29 02:00` | 9.0h | `$2.9395` | `$3.2870` | **+11.82%** | **+11.17%** | +14.6% | -3.4% | `target_reclaim` |
| 5 | Book 3 | `2024-03-05 16:00` | `2024-03-05 19:00` | 3.0h | `$3.8429` | `$3.5267` | **-8.23%** | **-8.59%** | +9.2% | -12.2% | `stop_loss` |
| 6 | Book 3 | `2024-03-29 18:00` | `2024-03-30 00:00` | 6.0h | `$4.8015` | `$5.2190` | **+8.70%** | **+8.34%** | +9.2% | -0.3% | `target_reclaim` |
| 7 | Book 3 | `2024-07-25 08:00` | `2024-07-28 08:00` | 72.0h | `$2.4351` | `$2.4845` | **+2.03%** | **+2.01%** | +7.2% | -3.2% | `time_expiry` |
| 8 | Book 4 | `2024-09-28 13:00` | `2024-09-29 02:00` | 13.0h | `$2.6082` | `$3.1298` | **+32.30%** | **+28.60%** | +24.4% | -0.3% | `target_reclaim` |
| 9 | Book 3 | `2024-11-10 20:00` | `2024-11-11 01:00` | 5.0h | `$3.4640` | `$3.6083` | **+4.17%** | **+4.08%** | +4.5% | -4.4% | `target_reclaim` |
| 10 | Book 3 | `2024-11-12 10:00` | `2024-11-14 15:00` | 53.0h | `$3.5028` | `$3.2145` | **-8.23%** | **-8.59%** | +5.3% | -8.4% | `stop_loss` |
| 11 | Book 3 | `2024-11-24 12:00` | `2024-11-25 09:00` | 21.0h | `$3.5779` | `$3.8221` | **+6.82%** | **+6.60%** | +6.8% | -3.1% | `target_reclaim` |
| 12 | Book 3 | `2024-12-09 08:00` | `2024-12-09 20:00` | 12.0h | `$4.8134` | `$4.4173` | **-8.23%** | **-8.59%** | +2.7% | -10.0% | `stop_loss` |
| 13 | Book 3 | `2025-04-24 07:00` | `2025-04-24 15:00` | 8.0h | `$1.3519` | `$1.4082` | **+4.17%** | **+4.08%** | +4.8% | -1.5% | `target_reclaim` |
| 14 | Book 3 | `2026-09-23 16:00` | `2026-09-24 14:00` | 22.0h | `$0.2795` | `$0.2964` | **+6.03%** | **+5.86%** | +6.4% | -2.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `9` | `100.0%` | **`+78.9%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_expiry` | `2` | `50.0%` | **`+1.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `ETHW`

* **Total Candidate Breakouts Filtered (Vetoed):** `503`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `247` (49.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `64`
* **Saved Capital Losses Avoided:** `+3,135.5%`
* **Missed Upside Forgone:** `-2,384.2%`
* **Net Veto Alpha:** `+751.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `295` | `58.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `171` | `34.0%` |
| `Core 1: Macro Bear Veto` | `20` | `4.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `15` | `3.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `2` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*