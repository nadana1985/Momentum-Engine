# Kronos V12: Institutional Symbol Tear Sheet — `SAND`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`20.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.934`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+7.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.07x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.43%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-5.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`64.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.6% / -4.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-05 01:00` | `2022-10-06 13:00` | 36.0h | `$0.8724` | `$0.8502` | **-2.55%** | **-2.58%** | +0.3% | -4.5% | `stall_bailout` |
| 2 | Book 2 | `2023-07-13 16:00` | `2023-07-15 16:00` | 48.0h | `$0.4568` | `$0.4506` | **-1.37%** | **-1.38%** | +6.4% | -5.6% | `fast_decay_cut` |
| 3 | Book 1 | `2023-11-06 11:00` | `2023-11-07 23:00` | 36.0h | `$0.3921` | `$0.3870` | **-1.10%** | **-1.10%** | +2.8% | -4.8% | `fast_decay_cut` |
| 4 | Book 2 | `2026-09-03 15:00` | `2026-09-05 03:00` | 36.0h | `$0.0402` | `$0.0392` | **-2.58%** | **-2.62%** | +0.9% | -5.5% | `stall_bailout` |
| 5 | Book 2 | `2026-09-18 00:00` | `2026-09-25 00:00` | 168.0h | `$0.0372` | `$0.0432` | **+16.01%** | **+14.85%** | +22.4% | -1.9% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-2.5%`** |
| `stall_bailout` | `2` | `0.0%` | **`-5.2%`** |
| `time_cap` | `1` | `100.0%` | **`+14.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `SAND`

* **Total Candidate Breakouts Filtered (Vetoed):** `231`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `146` (63.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `67`
* **Saved Capital Losses Avoided:** `+1,935.4%`
* **Missed Upside Forgone:** `-4,362.6%`
* **Net Veto Alpha:** `+-2,427.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `88` | `38.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `80` | `34.6%` |
| `Core 1: Macro Bear Veto` | `49` | `21.2%` |
| `Core 4: Funding Rate Cap` | `14` | `6.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*