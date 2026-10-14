# Kronos V12: Institutional Symbol Tear Sheet — `USTC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.537`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+18.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.20x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.84%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`24.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.5% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-28 17:00` | `2024-02-28 18:00` | 1.0h | `$0.0348` | `$0.0319` | **-8.23%** | **-8.59%** | +7.5% | -13.4% | `stop_loss` |
| 2 | Book 3 | `2024-10-31 12:00` | `2024-11-01 06:00` | 18.0h | `$0.0245` | `$0.0225` | **-8.23%** | **-8.59%** | +3.4% | -8.5% | `stop_loss` |
| 3 | Book 3 | `2025-02-10 20:00` | `2025-02-11 20:00` | 24.0h | `$0.0160` | `$0.0174` | **+8.70%** | **+8.34%** | +10.1% | -2.9% | `target_reclaim` |
| 4 | Book 3 | `2025-02-13 13:00` | `2025-02-14 22:00` | 33.0h | `$0.0186` | `$0.0170` | **-8.23%** | **-8.59%** | +2.5% | -8.4% | `stop_loss` |
| 5 | Book 3 | `2025-05-02 10:00` | `2025-05-03 16:00` | 30.0h | `$0.0132` | `$0.0121` | **-8.23%** | **-8.59%** | +3.6% | -9.5% | `stop_loss` |
| 6 | Book 3 | `2025-05-12 18:00` | `2025-05-13 20:00` | 26.0h | `$0.0134` | `$0.0147` | **+9.74%** | **+9.30%** | +9.9% | -0.3% | `target_reclaim` |
| 7 | Book 4 | `2025-07-18 04:00` | `2025-07-18 15:00` | 11.0h | `$0.0145` | `$0.0174` | **+16.44%** | **+15.40%** | +20.8% | -1.9% | `target_reclaim` |
| 8 | Book 5 (Shelf Absorption Squeeze) | `2025-12-05 11:00` | `2025-12-09 11:00` | Live | `$0.0067` | `$0.0072` | **+8.50%** | **+8.16%** | +68.8% | -11.6% | `shelf_target_reclaim` |
| 9 | Book 4 | `2026-05-02 09:00` | `2026-05-05 15:00` | 78.0h | `$0.0067` | `$0.0080` | **+7.76%** | **+7.52%** | +25.3% | -0.4% | `target_reclaim` |
| 10 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0053` | `$0.0055` | **+4.17%** | **+4.08%** | +13.3% | -4.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+44.6%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `USTC`

* **Total Candidate Breakouts Filtered (Vetoed):** `243`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `181` (74.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `15`
* **Saved Capital Losses Avoided:** `+2,877.4%`
* **Missed Upside Forgone:** `-456.0%`
* **Net Veto Alpha:** `+2,421.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `188` | `77.4%` |
| `Core 1: Macro Bear Veto` | `40` | `16.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `3.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `5` | `2.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.4%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*