# Kronos V12: Institutional Symbol Tear Sheet — `ZIL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `11` (`11` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`27.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.925`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-3.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.35%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-26.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`189.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.3% / -9.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2022-03-26 20:00` | `2022-03-27 11:00` | 15.0h | `$0.0815` | `$0.0961` | **+4.50%** | **+4.14%** | +20.3% | -7.2% | `climax_whale_euphoria_harvest` |
| 2 | Book 2 | `2022-10-25 17:00` | `2022-10-27 17:00` | 48.0h | `$0.0302` | `$0.0301` | **-0.32%** | **-0.32%** | +3.7% | -2.2% | `fast_decay_cut` |
| 3 | Book 4 | `2023-02-13 05:00` | `2023-03-03 01:00` | 428.0h | `$0.0322` | `$0.0274` | **-16.24%** | **-17.60%** | +14.7% | -16.1% | `structural_stop` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2023-04-19 06:00` | `2023-04-23 06:00` | Live | `$0.0324` | `$0.0297` | **-8.20%** | **-8.56%** | +-2.4% | -26.6% | `shelf_stop_loss` |
| 5 | Book 4 | `2023-11-09 23:00` | `2023-12-08 18:00` | 691.0h | `$0.0208` | `$0.0249` | **+23.62%** | **+21.56%** | +21.3% | -6.3% | `target_reclaim` |
| 6 | Book 1 | `2024-02-25 21:00` | `2024-02-28 17:00` | 68.0h | `$0.0251` | `$0.0246` | **-2.93%** | **-2.96%** | +17.0% | -5.3% | `breakeven_ratchet` |
| 7 | Book 4 | `2024-11-11 18:00` | `2024-11-17 01:00` | 127.0h | `$0.0181` | `$0.0217` | **+25.93%** | **+21.61%** | +21.0% | -12.1% | `target_reclaim` |
| 8 | Book 2 | `2026-05-06 00:00` | `2026-05-08 00:00` | 48.0h | `$0.0044` | `$0.0042` | **-4.65%** | **-4.75%** | +6.6% | -4.3% | `fast_decay_cut` |
| 9 | Book 2 | `2026-08-21 07:00` | `2026-08-22 05:00` | 22.0h | `$0.0026` | `$0.0026` | **-2.08%** | **-2.10%** | +15.2% | -5.5% | `breakeven_ratchet` |
| 10 | Book 2 | `2026-09-06 15:00` | `2026-09-08 03:00` | 36.0h | `$0.0030` | `$0.0029` | **-2.48%** | **-2.51%** | +0.4% | -3.6% | `stall_bailout` |
| 11 | Book 4 | `2026-09-20 00:00` | `2026-10-07 02:00` | 410.0h | `$0.0037` | `$0.0033` | **-11.68%** | **-12.33%** | +17.3% | -12.9% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `2` | `0.0%` | **`-5.1%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-5.1%`** |
| `target_reclaim` | `2` | `100.0%` | **`+43.2%`** |
| `structural_stop` | `2` | `0.0%` | **`-29.9%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+4.1%`** |
| `stall_bailout` | `1` | `0.0%` | **`-2.5%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZIL`

* **Total Candidate Breakouts Filtered (Vetoed):** `730`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `329` (45.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `151`
* **Saved Capital Losses Avoided:** `+4,242.8%`
* **Missed Upside Forgone:** `-4,873.8%`
* **Net Veto Alpha:** `+-631.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `442` | `60.5%` |
| `Core 0: Zero-Tolerance Data Firewall` | `221` | `30.3%` |
| `Core 1: Macro Bear Veto` | `54` | `7.4%` |
| `Core 4: Funding Rate Cap` | `13` | `1.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*