# Kronos V12: Institutional Symbol Tear Sheet — `BEAMX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `24` (`24` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `24` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`58.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.121`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+9.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.10x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.39%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-25.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`19.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.3% / -5.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-11-26 01:00` | `2023-11-30 01:00` | Live | `$0.0090` | `$0.0098` | **+8.50%** | **+8.16%** | +100.2% | -13.8% | `shelf_target_reclaim` |
| 2 | Book 3 | `2024-02-21 09:00` | `2024-02-21 23:00` | 14.0h | `$0.0307` | `$0.0334` | **+8.70%** | **+8.34%** | +10.6% | -1.3% | `target_reclaim` |
| 3 | Book 3 | `2024-02-28 11:00` | `2024-02-28 17:00` | 6.0h | `$0.0344` | `$0.0316` | **-8.23%** | **-8.59%** | +3.6% | -10.7% | `stop_loss` |
| 4 | Book 3 | `2024-03-03 06:00` | `2024-03-04 22:00` | 40.0h | `$0.0347` | `$0.0377` | **+8.70%** | **+8.34%** | +17.6% | -7.1% | `target_reclaim` |
| 5 | Book 3 | `2024-03-05 05:00` | `2024-03-05 12:00` | 7.0h | `$0.0368` | `$0.0400` | **+8.70%** | **+8.34%** | +9.3% | -0.0% | `target_reclaim` |
| 6 | Book 3 | `2024-03-10 22:00` | `2024-03-13 22:00` | 72.0h | `$0.0400` | `$0.0391` | **-2.41%** | **-2.44%** | +6.6% | -7.0% | `time_expiry` |
| 7 | Book 3 | `2024-05-31 10:00` | `2024-05-31 16:00` | 6.0h | `$0.0308` | `$0.0283` | **-8.23%** | **-8.59%** | +4.9% | -9.5% | `stop_loss` |
| 8 | Book 3 | `2024-07-23 05:00` | `2024-07-23 09:00` | 4.0h | `$0.0187` | `$0.0194` | **+4.17%** | **+4.08%** | +4.4% | -0.3% | `target_reclaim` |
| 9 | Book 2 | `2024-09-15 07:00` | `2024-09-16 17:00` | 34.0h | `$0.0149` | `$0.0136` | **-9.26%** | **-9.67%** | +3.8% | -8.1% | `initial_stop` |
| 10 | Book 3 | `2024-09-18 16:00` | `2024-09-18 18:00` | 2.0h | `$0.0145` | `$0.0151` | **+4.17%** | **+4.08%** | +5.6% | -0.1% | `target_reclaim` |
| 11 | Book 3 | `2024-10-01 17:00` | `2024-10-02 10:00` | 17.0h | `$0.0187` | `$0.0171` | **-8.23%** | **-8.59%** | +6.0% | -9.1% | `stop_loss` |
| 12 | Book 3 | `2024-10-25 07:00` | `2024-10-25 09:00` | 2.0h | `$0.0189` | `$0.0202` | **+6.92%** | **+6.69%** | +6.9% | -0.1% | `target_reclaim` |
| 13 | Book 3 | `2024-11-10 21:00` | `2024-11-10 22:00` | 1.0h | `$0.0197` | `$0.0207` | **+4.94%** | **+4.82%** | +5.0% | -1.9% | `target_reclaim` |
| 14 | Book 3 | `2024-12-09 09:00` | `2024-12-09 21:00` | 12.0h | `$0.0326` | `$0.0299` | **-8.23%** | **-8.59%** | +5.8% | -16.3% | `stop_loss` |
| 15 | Book 3 | `2025-05-04 04:00` | `2025-05-06 00:00` | 44.0h | `$0.0072` | `$0.0078` | **+8.25%** | **+7.92%** | +8.3% | -1.1% | `target_reclaim` |
| 16 | Book 3 | `2025-05-12 18:00` | `2025-05-13 18:00` | 24.0h | `$0.0087` | `$0.0095` | **+8.88%** | **+8.51%** | +9.4% | -5.2% | `target_reclaim` |
| 17 | Book 3 | `2025-05-15 05:00` | `2025-05-16 17:00` | 36.0h | `$0.0087` | `$0.0082` | **-6.12%** | **-6.31%** | +0.6% | -7.5% | `stall_bailout` |
| 18 | Book 3 | `2025-07-17 03:00` | `2025-07-17 08:00` | 5.0h | `$0.0072` | `$0.0075` | **+4.17%** | **+4.08%** | +4.8% | -0.3% | `target_reclaim` |
| 19 | Book 3 | `2025-07-18 19:00` | `2025-07-20 03:00` | 32.0h | `$0.0073` | `$0.0077` | **+4.85%** | **+4.74%** | +4.9% | -2.6% | `target_reclaim` |
| 20 | Book 3 | `2025-09-20 01:00` | `2025-09-22 06:00` | 53.0h | `$0.0080` | `$0.0073` | **-8.23%** | **-8.59%** | +2.8% | -13.2% | `stop_loss` |
| 21 | Book 3 | `2025-10-09 08:00` | `2025-10-10 15:00` | 31.0h | `$0.0087` | `$0.0080` | **-8.23%** | **-8.59%** | +2.0% | -13.0% | `stop_loss` |
| 22 | Book 3 | `2026-08-27 09:00` | `2026-08-27 13:00` | 4.0h | `$0.0020` | `$0.0018` | **-8.23%** | **-8.59%** | +11.1% | -9.7% | `stop_loss` |
| 23 | Book 3 | `2026-09-22 14:00` | `2026-09-22 17:00` | 3.0h | `$0.0018` | `$0.0019` | **+6.00%** | **+5.83%** | +6.5% | -0.2% | `target_reclaim` |
| 24 | Book 3 | `2026-09-23 14:00` | `2026-09-23 20:00` | 6.0h | `$0.0019` | `$0.0020` | **+4.17%** | **+4.08%** | +5.6% | -2.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `13` | `100.0%` | **`+79.9%`** |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-9.7%`** |
| `stall_bailout` | `1` | `0.0%` | **`-6.3%`** |
| `time_expiry` | `1` | `0.0%` | **`-2.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `BEAMX`

* **Total Candidate Breakouts Filtered (Vetoed):** `267`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `162` (60.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+2,435.1%`
* **Missed Upside Forgone:** `-585.1%`
* **Net Veto Alpha:** `+1,850.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `155` | `58.1%` |
| `Core 1: Macro Bear Veto` | `53` | `19.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `30` | `11.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `26` | `9.7%` |
| `Core 3: Min Turnover Velocity` | `2` | `0.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*