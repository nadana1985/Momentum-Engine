# Kronos V12: Institutional Symbol Tear Sheet — `MEME`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `16` (`16` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `16` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`62.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.528`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+24.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.27x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.50%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`20.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.7% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-12-06 11:00` | `2023-12-06 18:00` | 7.0h | `$0.0363` | `$0.0423` | **+16.36%** | **+15.15%** | +21.8% | -3.7% | `target_reclaim` |
| 2 | Book 3 | `2024-02-13 13:00` | `2024-02-14 05:00` | 16.0h | `$0.0238` | `$0.0248` | **+4.17%** | **+4.08%** | +4.4% | -2.2% | `target_reclaim` |
| 3 | Book 3 | `2024-02-19 10:00` | `2024-02-20 15:00` | 29.0h | `$0.0271` | `$0.0249` | **-8.23%** | **-8.59%** | +4.1% | -9.3% | `stop_loss` |
| 4 | Book 3 | `2024-03-01 21:00` | `2024-03-01 22:00` | 1.0h | `$0.0391` | `$0.0407` | **+4.17%** | **+4.08%** | +4.4% | -1.1% | `target_reclaim` |
| 5 | Book 3 | `2024-03-03 07:00` | `2024-03-03 11:00` | 4.0h | `$0.0404` | `$0.0432` | **+7.01%** | **+6.77%** | +12.7% | -15.8% | `target_reclaim` |
| 6 | Book 3 | `2024-03-05 16:00` | `2024-03-05 19:00` | 3.0h | `$0.0424` | `$0.0389` | **-8.23%** | **-8.59%** | +6.1% | -29.9% | `stop_loss` |
| 7 | Book 3 | `2024-05-23 13:00` | `2024-05-25 09:00` | 44.0h | `$0.0261` | `$0.0279` | **+6.94%** | **+6.71%** | +7.9% | -6.0% | `target_reclaim` |
| 8 | Book 3 | `2024-09-25 13:00` | `2024-09-26 06:00` | 17.0h | `$0.0109` | `$0.0114` | **+4.53%** | **+4.43%** | +4.8% | -2.4% | `target_reclaim` |
| 9 | Book 3 | `2024-10-16 16:00` | `2024-10-19 16:00` | 72.0h | `$0.0127` | `$0.0130` | **+2.55%** | **+2.52%** | +8.3% | -4.2% | `time_expiry` |
| 10 | Book 3 | `2024-11-12 10:00` | `2024-11-12 13:00` | 3.0h | `$0.0135` | `$0.0124` | **-8.23%** | **-8.59%** | +2.7% | -9.1% | `stop_loss` |
| 11 | Book 3 | `2024-11-13 19:00` | `2024-11-14 02:00` | 7.0h | `$0.0135` | `$0.0148` | **+9.77%** | **+9.32%** | +13.2% | -3.4% | `target_reclaim` |
| 12 | Book 3 | `2024-12-02 08:00` | `2024-12-03 00:00` | 16.0h | `$0.0147` | `$0.0163` | **+11.27%** | **+10.68%** | +11.5% | -1.7% | `target_reclaim` |
| 13 | Book 3 | `2024-12-09 09:00` | `2024-12-09 20:00` | 11.0h | `$0.0166` | `$0.0153` | **-8.23%** | **-8.59%** | +4.7% | -12.1% | `stop_loss` |
| 14 | Book 3 | `2025-06-17 00:00` | `2025-06-18 13:00` | 37.0h | `$0.0016` | `$0.0015` | **-8.23%** | **-8.59%** | +5.7% | -10.4% | `stop_loss` |
| 15 | Book 3 | `2025-07-17 16:00` | `2025-07-17 22:00` | 6.0h | `$0.0019` | `$0.0021` | **+5.98%** | **+5.80%** | +6.2% | -0.2% | `target_reclaim` |
| 16 | Book 2 | `2026-05-05 01:00` | `2026-05-07 01:00` | 48.0h | `$0.0006` | `$0.0006` | **-2.54%** | **-2.57%** | +4.2% | -3.3% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `9` | `100.0%` | **`+67.0%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-2.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+2.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `MEME`

* **Total Candidate Breakouts Filtered (Vetoed):** `524`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `395` (75.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `39`
* **Saved Capital Losses Avoided:** `+6,678.6%`
* **Missed Upside Forgone:** `-1,169.7%`
* **Net Veto Alpha:** `+5,508.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `409` | `78.1%` |
| `Core 1: Macro Bear Veto` | `89` | `17.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `20` | `3.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `1.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*