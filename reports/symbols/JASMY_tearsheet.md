# Kronos V12: Institutional Symbol Tear Sheet — `JASMY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`1` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+35.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.42x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+35.05%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`124.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+44.7% / -8.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-11-05 07:00` | `2023-11-10 11:00` | 124.0h | `$0.0041` | `$0.0057` | **+41.98%** | **+35.05%** | +44.7% | -8.7% | `climax_top_harvest` |
| 2 | Book 1 | `2026-09-27 08:00` | `_Open Live_` | 236.9h | `$0.0049` | `$0.0050` | **+2.10%** | **+2.08%** | +26.1% | -2.5% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+35.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `JASMY`

* **Total Candidate Breakouts Filtered (Vetoed):** `137`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `78` (56.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+1,005.0%`
* **Missed Upside Forgone:** `-1,590.4%`
* **Net Veto Alpha:** `+-585.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `65` | `47.4%` |
| `Core 1: Macro Bear Veto` | `56` | `40.9%` |
| `Core 4: Funding Rate Cap` | `11` | `8.0%` |
| `Core 4: Defensible Whale Dump` | `4` | `2.9%` |
| `Core 4: Whale Firewall` | `1` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*