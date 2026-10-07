# Kronos V12: Institutional Symbol Tear Sheet — `T`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+14.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.16x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+7.32%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.5% / -3.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-10-23 22:00` | `2023-10-30 22:00` | 168.0h | `$0.0211` | `$0.0234` | **+10.55%** | **+10.03%** | +11.5% | -3.8% | `time_cap` |
| 2 | Book 2 | `2026-05-04 02:00` | `2026-05-11 02:00` | 168.0h | `$0.0060` | `$0.0063` | **+4.73%** | **+4.62%** | +7.5% | -2.7% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `100.0%` | **`+14.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `T`

* **Total Candidate Breakouts Filtered (Vetoed):** `89`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `63` (70.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+886.9%`
* **Missed Upside Forgone:** `-378.9%`
* **Net Veto Alpha:** `+507.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `50` | `56.2%` |
| `Core 1: Macro Bear Veto` | `35` | `39.3%` |
| `Core 4: Whale Firewall` | `3` | `3.4%` |
| `Core 4: Defensible Whale Dump` | `1` | `1.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*