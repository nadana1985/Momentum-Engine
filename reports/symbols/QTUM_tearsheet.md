# Kronos V12: Institutional Symbol Tear Sheet — `QTUM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+13.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.15x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+13.85%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+31.1% / -2.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-04 02:00` | `2026-05-11 02:00` | 168.0h | `$0.8902` | `$1.0224` | **+14.85%** | **+13.85%** | +31.1% | -2.3% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+13.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `QTUM`

* **Total Candidate Breakouts Filtered (Vetoed):** `374`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `218` (58.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `79`
* **Saved Capital Losses Avoided:** `+2,996.9%`
* **Missed Upside Forgone:** `-2,746.5%`
* **Net Veto Alpha:** `+250.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `128` | `34.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `94` | `25.1%` |
| `Core 1: Macro Bear Veto` | `69` | `18.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `69` | `18.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `14` | `3.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*