# Kronos V12: Institutional Symbol Tear Sheet — `SIGN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.724`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.81%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-9.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`23.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.2% / -4.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-30 16:00` | `2025-05-31 10:00` | 18.0h | `$0.0779` | `$0.0715` | **-8.23%** | **-8.59%** | +3.2% | -8.5% | `stop_loss` |
| 2 | Book 3 | `2025-07-19 14:00` | `2025-07-20 11:00` | 21.0h | `$0.0743` | `$0.0774` | **+4.17%** | **+4.08%** | +4.4% | -0.4% | `target_reclaim` |
| 3 | Book 3 | `2025-07-22 01:00` | `2025-07-23 12:00` | 35.0h | `$0.0781` | `$0.0817` | **+4.71%** | **+4.60%** | +5.9% | -1.7% | `target_reclaim` |
| 4 | Book 3 | `2025-07-24 12:00` | `2025-07-25 14:00` | 26.0h | `$0.0841` | `$0.0772` | **-8.23%** | **-8.59%** | +6.3% | -11.4% | `stop_loss` |
| 5 | Book 2 | `2026-05-04 14:00` | `2026-05-06 02:00` | 36.0h | `$0.0160` | `$0.0160` | **-0.46%** | **-0.46%** | +0.8% | -3.9% | `stall_bailout` |
| 6 | Book 3 | `2026-09-02 23:00` | `2026-09-03 02:00` | 3.0h | `$0.0087` | `$0.0091` | **+4.17%** | **+4.08%** | +4.3% | -0.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+12.8%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `stall_bailout` | `1` | `0.0%` | **`-0.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `SIGN`

* **Total Candidate Breakouts Filtered (Vetoed):** `255`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `102` (40.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `32`
* **Saved Capital Losses Avoided:** `+1,122.7%`
* **Missed Upside Forgone:** `-696.8%`
* **Net Veto Alpha:** `+426.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `199` | `78.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `23` | `9.0%` |
| `Core 1: Macro Bear Veto` | `19` | `7.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `13` | `5.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*