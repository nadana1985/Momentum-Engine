# Kronos V12: Institutional Symbol Tear Sheet — `LPT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-7.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.93x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.85%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-3.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`63.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.5% / -4.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-09-13 16:00` | `2024-09-15 16:00` | 48.0h | `$12.8641` | `$12.3311` | **-4.14%** | **-4.23%** | +1.2% | -4.5% | `fast_decay_cut` |
| 2 | Book 2 | `2025-04-22 14:00` | `2025-04-22 15:00` | 1.0h | `$4.3408` | `$4.3202` | **-0.48%** | **-0.48%** | +29.9% | -1.7% | `breakeven_ratchet` |
| 3 | Book 2 | `2026-05-02 15:00` | `2026-05-04 03:00` | 36.0h | `$2.1995` | `$2.1586` | **-1.86%** | **-1.88%** | +0.1% | -4.4% | `stall_bailout` |
| 4 | Book 1 | `2026-09-21 09:00` | `2026-09-28 08:00` | 167.0h | `$1.7103` | `$1.6878` | **-0.81%** | **-0.81%** | +10.7% | -7.1% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-5.0%`** |
| `breakeven_ratchet` | `1` | `0.0%` | **`-0.5%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `LPT`

* **Total Candidate Breakouts Filtered (Vetoed):** `102`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `59` (57.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `25`
* **Saved Capital Losses Avoided:** `+878.5%`
* **Missed Upside Forgone:** `-1,028.6%`
* **Net Veto Alpha:** `+-150.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `52` | `51.0%` |
| `Core 1: Macro Bear Veto` | `49` | `48.0%` |
| `Core 4: Whale Firewall` | `1` | `1.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*