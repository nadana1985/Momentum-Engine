# Kronos V12: Institutional Symbol Tear Sheet — `METIS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.875`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-3.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.78%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-14.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`50.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.5% / -7.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-07-23 16:00` | `2024-07-25 01:00` | 33.0h | `$49.3086` | `$45.2505` | **-8.23%** | **-8.59%** | +3.2% | -8.6% | `stop_loss` |
| 2 | Book 3 | `2024-11-26 10:00` | `2024-11-27 15:00` | 29.0h | `$51.4614` | `$57.3900` | **+11.52%** | **+10.90%** | +13.2% | -4.2% | `target_reclaim` |
| 3 | Book 3 | `2025-09-19 14:00` | `2025-09-22 00:00` | 58.0h | `$15.8080` | `$14.5070` | **-8.23%** | **-8.59%** | +1.4% | -8.6% | `stop_loss` |
| 4 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$2.5082` | `$2.9597` | **+18.00%** | **+16.55%** | +22.0% | -0.4% | `climax_whale_euphoria_harvest` |
| 5 | Book 4 | `2026-09-27 07:00` | `2026-10-02 18:00` | 131.0h | `$3.6895` | `$3.1361` | **-13.08%** | **-14.18%** | +2.7% | -15.8% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |
| `structural_stop` | `1` | `0.0%` | **`-14.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+10.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `METIS`

* **Total Candidate Breakouts Filtered (Vetoed):** `120`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `77` (64.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+1,063.5%`
* **Missed Upside Forgone:** `-568.7%`
* **Net Veto Alpha:** `+494.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `85` | `70.8%` |
| `Core 1: Macro Bear Veto` | `18` | `15.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `16` | `13.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*