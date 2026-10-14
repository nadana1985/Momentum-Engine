# Kronos V12: Institutional Symbol Tear Sheet — `JST`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.32%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-2.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`120.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.3% / -2.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2025-07-16 20:00` | `2025-07-23 20:00` | 168.0h | `$0.0376` | `$0.0368` | **-2.45%** | **-2.48%** | +4.5% | -2.3% | `stagnation_cut` |
| 2 | Book 1 | `2026-09-15 02:00` | `2026-09-18 02:00` | 72.0h | `$0.1154` | `$0.1139` | **-2.13%** | **-2.15%** | +2.0% | -2.2% | `stagnation_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stagnation_bailout` | `1` | `0.0%` | **`-2.2%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-2.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `JST`

* **Total Candidate Breakouts Filtered (Vetoed):** `359`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `196` (54.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+1,078.0%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+1,078.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `194` | `54.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `162` | `45.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.3%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.3%` |
| `Core 4: Whale Firewall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*