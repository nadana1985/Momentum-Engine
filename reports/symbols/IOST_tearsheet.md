# Kronos V12: Institutional Symbol Tear Sheet — `IOST`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.424`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+21.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.23x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.21%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-14.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`152.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.1% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-01-11 22:00` | `2023-01-25 08:00` | 322.0h | `$0.0081` | `$0.0102` | **+23.37%** | **+21.00%** | +31.5% | -2.5% | `climax_top_harvest` |
| 2 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$0.0100` | `$0.0113` | **+13.04%** | **+12.26%** | +15.3% | -4.4% | `time_cap` |
| 3 | Book 2 | `2023-07-12 00:00` | `2023-07-19 00:00` | 168.0h | `$0.0087` | `$0.0089` | **+2.49%** | **+2.46%** | +10.0% | -1.8% | `time_cap` |
| 4 | Book 1 | `2023-11-08 18:00` | `2023-11-09 16:00` | 22.0h | `$0.0093` | `$0.0081` | **-13.75%** | **-14.79%** | +4.0% | -12.3% | `initial_stop` |
| 5 | Book 1 | `2023-11-10 04:00` | `2023-11-13 14:00` | 82.0h | `$0.0093` | `$0.0093` | **+0.14%** | **+0.14%** | +24.9% | -4.0% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `100.0%` | **`+14.7%`** |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.1%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+21.0%`** |
| `initial_stop` | `1` | `0.0%` | **`-14.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `IOST`

* **Total Candidate Breakouts Filtered (Vetoed):** `262`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `166` (63.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `63`
* **Saved Capital Losses Avoided:** `+2,523.0%`
* **Missed Upside Forgone:** `-2,290.2%`
* **Net Veto Alpha:** `+232.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `106` | `40.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `89` | `34.0%` |
| `Core 1: Macro Bear Veto` | `52` | `19.8%` |
| `Core 4: Funding Rate Cap` | `11` | `4.2%` |
| `Core 4: Whale Firewall` | `4` | `1.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*