# Kronos V12: Institutional Symbol Tear Sheet — `MANA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.595`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+9.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.10x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.89%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-11.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`91.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.1% / -4.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-03-29 08:00` | `2023-03-30 20:00` | 36.0h | `$0.6045` | `$0.5760` | **-4.72%** | **-4.84%** | +0.4% | -6.1% | `stall_bailout` |
| 2 | Book 2 | `2023-06-20 18:00` | `2023-06-27 18:00` | 168.0h | `$0.3464` | `$0.3881` | **+12.06%** | **+11.38%** | +24.9% | -1.2% | `time_cap` |
| 3 | Book 1 | `2023-07-13 23:00` | `2023-07-15 11:00` | 36.0h | `$0.4435` | `$0.4181` | **-6.10%** | **-6.30%** | +1.1% | -10.1% | `fast_decay_cut` |
| 4 | Book 2 | `2026-09-13 03:00` | `2026-09-15 03:00` | 48.0h | `$0.0773` | `$0.0737` | **-4.65%** | **-4.76%** | +2.1% | -5.1% | `fast_decay_cut` |
| 5 | Book 2 | `2026-09-19 00:00` | `2026-09-26 00:00` | 168.0h | `$0.0795` | `$0.0915` | **+15.00%** | **+13.98%** | +17.4% | -1.0% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-11.1%`** |
| `time_cap` | `2` | `100.0%` | **`+25.4%`** |
| `stall_bailout` | `1` | `0.0%` | **`-4.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `MANA`

* **Total Candidate Breakouts Filtered (Vetoed):** `205`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `134` (65.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `31`
* **Saved Capital Losses Avoided:** `+1,594.4%`
* **Missed Upside Forgone:** `-5,720.4%`
* **Net Veto Alpha:** `+-4,126.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `78` | `38.0%` |
| `Core 1: Macro Bear Veto` | `66` | `32.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `45` | `22.0%` |
| `Core 4: Funding Rate Cap` | `16` | `7.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*