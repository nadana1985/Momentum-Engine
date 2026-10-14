# Kronos V12: Institutional Symbol Tear Sheet — `JELLYJELLY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`22.2%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.353`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-30.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.74x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.37%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-25.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`39.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.4% / -12.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-01 13:00` | `2025-05-02 20:00` | 31.0h | `$0.0366` | `$0.0336` | **-8.23%** | **-8.59%** | +4.8% | -8.8% | `stop_loss` |
| 2 | Book 3 | `2025-05-09 09:00` | `2025-05-09 10:00` | 1.0h | `$0.0385` | `$0.0353` | **-8.23%** | **-8.59%** | +12.9% | -32.3% | `stop_loss` |
| 3 | Book 3 | `2025-05-14 13:00` | `2025-05-14 14:00` | 1.0h | `$0.0481` | `$0.0441` | **-8.23%** | **-8.59%** | +16.9% | -26.3% | `stop_loss` |
| 4 | Book 3 | `2025-06-12 02:00` | `2025-06-12 19:00` | 17.0h | `$0.0248` | `$0.0228` | **-8.23%** | **-8.59%** | +2.2% | -9.4% | `stop_loss` |
| 5 | Book 4 | `2026-05-04 21:00` | `2026-05-11 05:00` | 152.0h | `$0.0557` | `$0.0657` | **+10.80%** | **+9.93%** | +21.2% | -9.1% | `climax_whale_euphoria_harvest` |
| 6 | Book 3 | `2026-05-11 06:00` | `2026-05-11 13:00` | 7.0h | `$0.0572` | `$0.0611` | **+6.82%** | **+6.60%** | +17.6% | -0.7% | `target_reclaim` |
| 7 | Book 3 | `2026-08-22 05:00` | `2026-08-22 10:00` | 5.0h | `$0.0590` | `$0.0542` | **-8.23%** | **-8.59%** | +5.0% | -11.7% | `stop_loss` |
| 8 | Book 3 | `2026-09-18 04:00` | `2026-09-21 04:00` | 72.0h | `$0.0570` | `$0.0556` | **-2.43%** | **-2.46%** | +10.4% | -6.0% | `time_expiry` |
| 9 | Book 3 | `2026-09-27 22:00` | `2026-09-30 22:00` | 72.0h | `$0.0569` | `$0.0561` | **-1.47%** | **-1.48%** | +3.0% | -3.3% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `time_expiry` | `2` | `0.0%` | **`-3.9%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+9.9%`** |
| `target_reclaim` | `1` | `100.0%` | **`+6.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `JELLYJELLY`

* **Total Candidate Breakouts Filtered (Vetoed):** `102`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `86` (84.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `57`
* **Saved Capital Losses Avoided:** `+2,434.3%`
* **Missed Upside Forgone:** `-3,082.3%`
* **Net Veto Alpha:** `+-648.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `76` | `74.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `18` | `17.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5` | `4.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `2.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*