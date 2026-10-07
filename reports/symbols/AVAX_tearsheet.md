# Kronos V12: Institutional Symbol Tear Sheet — `AVAX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `10` (`9` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`8.683`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+83.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.31x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+9.28%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`189.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.9% / -5.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 17:00` | `2022-11-01 17:00` | 168.0h | `$16.9834` | `$18.6163` | **+9.62%** | **+9.18%** | +16.6% | -3.5% | `time_cap` |
| 2 | Book 1 | `2023-01-11 18:00` | `2023-01-28 00:00` | 390.0h | `$13.9448` | `$21.2777` | **+70.61%** | **+53.42%** | +56.5% | -10.8% | `climax_top_harvest` |
| 3 | Book 2 | `2023-04-26 10:00` | `2023-04-26 19:00` | 9.0h | `$17.9578` | `$16.4799` | **-8.23%** | **-8.59%** | +1.5% | -8.1% | `initial_stop` |
| 4 | Book 2 | `2023-06-20 18:00` | `2023-06-27 18:00` | 168.0h | `$11.8435` | `$13.2668` | **+12.02%** | **+11.35%** | +15.6% | -1.7% | `time_cap` |
| 5 | Book 2 | `2023-07-13 17:00` | `2023-07-20 17:00` | 168.0h | `$14.0460` | `$13.7914` | **-1.81%** | **-1.83%** | +13.9% | -3.7% | `time_cap` |
| 6 | Book 2 | `2023-10-21 07:00` | `2023-10-28 07:00` | 168.0h | `$9.4646` | `$10.8428` | **+14.56%** | **+13.59%** | +21.2% | -1.1% | `time_cap` |
| 7 | Book 1 | `2023-11-05 09:00` | `2023-11-09 20:00` | 107.0h | `$12.5924` | `$12.4977` | **-0.45%** | **-0.46%** | +11.1% | -7.7% | `fast_decay_cut` |
| 8 | Book 2 | `2025-04-21 08:00` | `2025-04-28 08:00` | 168.0h | `$20.7628` | `$22.1824` | **+6.84%** | **+6.61%** | +11.1% | -6.5% | `time_cap` |
| 9 | Book 1 | `2025-07-15 22:00` | `2025-07-30 19:00` | 357.0h | `$22.3136` | `$22.3692` | **+0.25%** | **+0.25%** | +22.9% | -3.1% | `breakeven_ratchet` |
| 10 | Book 1 | `2026-09-19 01:00` | `_Open Live_` | 435.9h | `$8.7187` | `$11.3290` | **+25.58%** | **+22.78%** | +37.7% | -5.1% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `5` | `80.0%` | **`+38.9%`** |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.3%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+53.4%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.5%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `AVAX`

* **Total Candidate Breakouts Filtered (Vetoed):** `255`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `136` (53.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `71`
* **Saved Capital Losses Avoided:** `+1,842.0%`
* **Missed Upside Forgone:** `-4,121.2%`
* **Net Veto Alpha:** `+-2,279.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `160` | `62.7%` |
| `Core 1: Macro Bear Veto` | `66` | `25.9%` |
| `Core 4: Funding Rate Cap` | `29` | `11.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*