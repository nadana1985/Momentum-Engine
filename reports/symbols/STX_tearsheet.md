# Kronos V12: Institutional Symbol Tear Sheet — `STX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`83.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`22.843`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+72.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.07x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+12.13%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-3.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`64.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.6% / -11.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-02-22 14:00` | `2023-02-26 14:00` | Live | `$0.7078` | `$0.7679` | **+8.50%** | **+8.16%** | +34.5% | -32.3% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2023-05-02 16:00` | `2023-05-06 16:00` | Live | `$0.6808` | `$0.7387` | **+8.50%** | **+8.16%** | +4.8% | -18.9% | `shelf_target_reclaim` |
| 3 | Book 4 | `2023-10-20 02:00` | `2023-10-23 22:00` | 92.0h | `$0.5859` | `$0.7031` | **+14.32%** | **+13.44%** | +25.1% | -0.9% | `target_reclaim` |
| 4 | Book 1 | `2023-10-24 05:00` | `2023-10-25 17:00` | 36.0h | `$0.7015` | `$0.6789` | **-3.28%** | **-3.33%** | +3.8% | -6.7% | `fast_decay_cut` |
| 5 | Book 1 | `2025-04-21 00:00` | `2025-04-24 14:00` | 86.0h | `$0.6964` | `$0.8357` | **+32.85%** | **+28.73%** | +23.4% | -9.2% | `target_reclaim` |
| 6 | Book 4 | `2026-08-23 11:00` | `2026-08-25 06:00` | 43.0h | `$0.2294` | `$0.2753` | **+19.01%** | **+17.64%** | +26.1% | -3.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+59.8%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-3.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `STX`

* **Total Candidate Breakouts Filtered (Vetoed):** `137`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `75` (54.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `14`
* **Saved Capital Losses Avoided:** `+838.4%`
* **Missed Upside Forgone:** `-403.1%`
* **Net Veto Alpha:** `+435.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `59` | `43.1%` |
| `Core 1: Macro Bear Veto` | `49` | `35.8%` |
| `Core 4: Defensible Whale Dump` | `15` | `10.9%` |
| `Core 4: Funding Rate Cap` | `7` | `5.1%` |
| `Core 4: Whale Firewall` | `6` | `4.4%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*