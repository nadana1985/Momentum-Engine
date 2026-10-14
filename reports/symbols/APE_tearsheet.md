# Kronos V12: Institutional Symbol Tear Sheet — `APE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.629`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-10.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.90x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.45%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-19.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`140.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.7% / -10.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-04-26 12:00` | `2023-04-26 19:00` | 7.0h | `$4.1133` | `$3.8129` | **-7.93%** | **-8.23%** | +0.6% | -7.2% | `initial_stop` |
| 2 | Book 4 | `2024-02-18 08:00` | `2024-02-26 07:00` | 191.0h | `$1.7381` | `$2.0510` | **+19.06%** | **+17.53%** | +20.1% | -7.2% | `climax_whale_euphoria_harvest` |
| 3 | Book 4 | `2025-06-04 06:00` | `2025-06-13 13:00` | 223.0h | `$0.7458` | `$0.6339` | **-18.12%** | **-19.64%** | +5.3% | -15.9% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+17.5%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-19.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `APE`

* **Total Candidate Breakouts Filtered (Vetoed):** `553`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `437` (79.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+6,216.8%`
* **Missed Upside Forgone:** `-1,125.2%`
* **Net Veto Alpha:** `+5,091.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `473` | `85.5%` |
| `Core 1: Macro Bear Veto` | `59` | `10.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `11` | `2.0%` |
| `Core 4: Funding Rate Cap` | `7` | `1.3%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.2%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.2%` |
| `Core 4: CSMI Anti-Chop Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*