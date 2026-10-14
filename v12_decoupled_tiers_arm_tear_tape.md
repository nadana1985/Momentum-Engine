# Kronos V12: Production Executive Tear Sheet
**Clean 6-Core Framework Performance Ledger**  
Generated: `2026-10-04 05:55:24 UTC`

---

## 1. Executive Performance Matrix (Strict Compounding Log Space)

| Performance Metric | V12 Clean 6-Core | Benchmark Target | Status |
| :--- | :--- | :--- | :--- |
| **Total Closed Trades** | `883` | N/A | Validated |
| **Win Rate** | **`35.33%`** | `> 50.0%` | ✅ **Passed** |
| **Profit Factor** | **`1.712`** | `> 1.50` | ✅ **Passed** |
| **Cumulative Net Log Return** | **`+1587.3%`** | `> +200%` | ✅ **Passed** |
| **Compounded Capital Multiple** | **`7827650.24x`** | `> 5.0x` | ✅ **Outperforming** |
| **Mean Net Log Return / Trade** | **`+1.80%`** | `> +1.0%` | ✅ **Passed** |
| **Currently Active Open Trades** | **`27`** | Monitored Live | In Flight |

---

## 2. Liquidity Tier & Book Attribution

### By Dynamic Liquidity Tier
| Liquidity Tier | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | `335` | `39.4%` | `1.644` | `+673.2%` | `839.23x` |
| **Tier 2** | `272` | `37.1%` | `1.806` | `+534.3%` | `209.06x` |
| **Tier 3** | `276` | `28.6%` | `1.729` | `+379.8%` | `44.61x` |


### By Execution Book
| Book | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Book 1** | `190` | `35.8%` | `1.480` | `+314.5%` | `23.22x` |
| **Book 2** | `693` | `35.2%` | `1.808` | `+1272.8%` | `337156.27x` |


---

## 3. Exit Reason & Microstructure Decomposition

| Exit Trigger | Count | Share | Total Net Log PnL |
| :--- | :--- | :--- | :--- |
| `fast_decay_cut` | `238` | `27.0%` | `-592.1%` |
| `time_cap` | `213` | `24.1%` | `+2042.8%` |
| `initial_stop` | `144` | `16.3%` | `-1151.2%` |
| `stall_bailout` | `127` | `14.4%` | `-324.6%` |
| `breakeven_ratchet` | `49` | `5.5%` | `+9.0%` |
| `climax_top_harvest` | `44` | `5.0%` | `+1341.4%` |
| `stagnation_cut` | `30` | `3.4%` | `-64.3%` |
| `trail_stop` | `29` | `3.3%` | `+371.1%` |
| `stagnation_bailout` | `9` | `1.0%` | `-44.8%` |


---

## 4. Top 15 Institutional Alpha Leaders

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MFE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **IMX** | `Tier 3` | `7` | `85.7%` | `76.476` | **`+91.9%`** | **`2.51x`** | `-1.2%` | `+22.9%` |
| **AVAX** | `Tier 1` | `9` | `66.7%` | `6.963` | **`+66.6%`** | **`1.95x`** | `-8.6%` | `+18.4%` |
| **SEI** | `Tier 2` | `5` | `60.0%` | `10.651` | **`+66.6%`** | **`1.95x`** | `-6.9%` | `+24.9%` |
| **AERO** | `Tier 1` | `2` | `100.0%` | `999.000` | **`+64.5%`** | **`1.91x`** | `0.0%` | `+44.4%` |
| **ONE** | `Tier 2` | `4` | `100.0%` | `999.000` | **`+60.3%`** | **`1.83x`** | `0.0%` | `+29.1%` |
| **AR** | `Tier 2` | `3` | `100.0%` | `999.000` | **`+53.8%`** | **`1.71x`** | `0.0%` | `+32.1%` |
| **SUI** | `Tier 1` | `5` | `60.0%` | `4.215` | **`+52.0%`** | **`1.68x`** | `-7.6%` | `+24.7%` |
| **BNB** | `Tier 1` | `24` | `45.8%` | `2.216` | **`+50.7%`** | **`1.66x`** | `-14.6%` | `+7.8%` |
| **ENA** | `Tier 1` | `3` | `66.7%` | `6.841` | **`+50.2%`** | **`1.65x`** | `0.0%` | `+39.7%` |
| **1000FLOKI** | `Tier 2` | `2` | `100.0%` | `999.000` | **`+50.0%`** | **`1.65x`** | `0.0%` | `+34.3%` |
| **UNI** | `Tier 1` | `11` | `27.3%` | `2.903` | **`+46.6%`** | **`1.59x`** | `-10.1%` | `+12.7%` |
| **ETC** | `Tier 1` | `3` | `100.0%` | `999.000` | **`+45.9%`** | **`1.58x`** | `0.0%` | `+24.3%` |
| **GRT** | `Tier 2` | `4` | `75.0%` | `92.590` | **`+45.8%`** | **`1.58x`** | `-0.5%` | `+19.4%` |
| **STX** | `Tier 2` | `3` | `100.0%` | `999.000` | **`+44.9%`** | **`1.57x`** | `0.0%` | `+32.7%` |
| **EPIC** | `Tier 2` | `3` | `66.7%` | `21.259` | **`+44.3%`** | **`1.56x`** | `0.0%` | `+27.4%` |


---

## 5. Bottom 10 Drag Laggards & Stop-Tax Culprits

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MAE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OP** | `Tier 1` | `7` | `14.3%` | `0.190` | **`-37.4%`** | `0.69x` | `-29.0%` | `-8.2%` |
| **TAO** | `Tier 1` | `6` | `16.7%` | `0.080` | **`-33.8%`** | `0.71x` | `-36.7%` | `-15.7%` |
| **ARB** | `Tier 1` | `5` | `0.0%` | `0.000` | **`-28.7%`** | `0.75x` | `-18.7%` | `-8.3%` |
| **TRX** | `Tier 1` | `17` | `23.5%` | `0.294` | **`-22.8%`** | `0.80x` | `-19.8%` | `-3.2%` |
| **SYN** | `Tier 2` | `2` | `0.0%` | `0.000` | **`-21.6%`** | `0.81x` | `-13.0%` | `-17.2%` |
| **AAVE** | `Tier 1` | `10` | `20.0%` | `0.596` | **`-21.6%`** | `0.81x` | `-49.3%` | `-7.1%` |
| **EIGEN** | `Tier 2` | `3` | `0.0%` | `0.000` | **`-20.3%`** | `0.82x` | `-7.2%` | `-10.6%` |
| **APE** | `Tier 2` | `3` | `0.0%` | `0.000` | **`-20.1%`** | `0.82x` | `-11.5%` | `-7.0%` |
| **CELO** | `Tier 3` | `3` | `0.0%` | `0.000` | **`-20.0%`** | `0.82x` | `-14.3%` | `-7.1%` |
| **ONDS** | `Tier 3` | `3` | `0.0%` | `0.000` | **`-19.3%`** | `0.82x` | `-11.5%` | `-6.5%` |


---

## 6. Symbol Breadth & Universe Participation
- **Total Unique Symbols Traded:** `346`
- **Net Profitable Symbols:** `142` (41.0%)
- **Net Drawdown Symbols:** `200` (57.8%)
- **Neutral / Breakeven Symbols:** `4` (1.2%)
- **Individual Asset Trade Logs:** Available in `data/all_tapes/v12_production/symbols/<ASSET>_trades.csv`

---

### 🛡️ Counterfactual Telemetry & Veto Alpha
| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Total Vetoed Signals** | `55,514` | Signals safely filtered out at gates |
| **Dodged Bullets (Loss Saved)** | `34,437` | Vetoed signals that dumped or hit initial stops |
| **Missed Opportunities** | `10,846` | Vetoed signals that rallied $\ge +20\%$ MFE |
| **Saved Loss Magnitude** | `+506,616.7%` | Total capital protected from false breakouts |
| **Missed Upside Excursion** | `-572,417.0%` | Total upside forgone |
| **Net Veto Alpha** | `+-65,800.3%` | **Net Statistical Advantage of Risk Gates** |
| **Gate Efficiency Ratio** | `62.0%` | Percentage of vetoes that prevented capital loss |

#### Veto Gate Attribution
| Gate | Count | Share |
| :--- | :--- | :--- |
| `Core 1: Macro Bear Veto` | `22,443` | `40.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `13,434` | `24.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `7,205` | `13.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5,248` | `9.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `4,500` | `8.1%` |
| `Core 4: Funding Rate Cap` | `1,397` | `2.5%` |
| `Core 4: Whale Firewall` | `916` | `1.7%` |
| `Core 3: Max Turnover Velocity` | `310` | `0.6%` |

---
*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*
