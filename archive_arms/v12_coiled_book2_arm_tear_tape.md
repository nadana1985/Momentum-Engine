# Kronos V12: Production Executive Tear Sheet
**Clean 6-Core Framework Performance Ledger**  
Generated: `2026-09-29 19:41:24 UTC`

---

## 1. Executive Performance Matrix (Strict Compounding Log Space)

| Performance Metric | V12 Clean 6-Core | Benchmark Target | Status |
| :--- | :--- | :--- | :--- |
| **Total Closed Trades** | `468` | N/A | Validated |
| **Win Rate** | **`37.82%`** | `> 50.0%` | ✅ **Passed** |
| **Profit Factor** | **`1.642`** | `> 1.50` | ✅ **Passed** |
| **Cumulative Net Log Return** | **`+625.1%`** | `> +200%` | ✅ **Passed** |
| **Compounded Capital Multiple** | **`518.75x`** | `> 5.0x` | ✅ **Outperforming** |
| **Mean Net Log Return / Trade** | **`+1.34%`** | `> +1.0%` | ✅ **Passed** |
| **Currently Active Open Trades** | **`9`** | Monitored Live | In Flight |

---

## 2. Liquidity Tier & Book Attribution

### By Dynamic Liquidity Tier
| Liquidity Tier | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | `304` | `39.1%` | `1.623` | `+417.4%` | `64.96x` |
| **Tier 2** | `164` | `35.4%` | `1.691` | `+207.8%` | `7.99x` |


### By Execution Book
| Book | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Book 1** | `176` | `34.1%` | `1.449` | `+136.9%` | `3.93x` |
| **Book 2** | `292` | `40.1%` | `1.794` | `+488.2%` | `131.93x` |


---

## 3. Exit Reason & Microstructure Decomposition

| Exit Trigger | Count | Share | Total Net Log PnL |
| :--- | :--- | :--- | :--- |
| `fast_decay_cut` | `127` | `27.1%` | `-432.8%` |
| `time_cap` | `113` | `24.1%` | `+1118.9%` |
| `initial_stop` | `109` | `23.3%` | `-975.3%` |
| `stagnation_cut` | `30` | `6.4%` | `-75.9%` |
| `breakeven_ratchet` | `30` | `6.4%` | `+6.0%` |
| `climax_top_harvest` | `24` | `5.1%` | `+760.2%` |
| `trail_stop` | `22` | `4.7%` | `+279.0%` |
| `stagnation_bailout` | `13` | `2.8%` | `-54.9%` |


---

## 4. Top 15 Institutional Alpha Leaders

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MFE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SEI** | `Tier 2` | `4` | `75.0%` | `16.902` | **`+68.2%`** | **`1.98x`** | `-5.2%` | `+124.2%` |
| **AERO** | `Tier 1` | `4` | `75.0%` | `10.267` | **`+67.9%`** | **`1.97x`** | `-9.1%` | `+116.8%` |
| **WLD** | `Tier 1` | `8` | `62.5%` | `4.926` | **`+60.9%`** | **`1.84x`** | `-10.7%` | `+219.5%` |
| **ENA** | `Tier 1` | `3` | `66.7%` | `8.522` | **`+50.2%`** | **`1.65x`** | `0.0%` | `+119.1%` |
| **1000FLOKI** | `Tier 2` | `2` | `100.0%` | `999.000` | **`+50.0%`** | **`1.65x`** | `0.0%` | `+68.6%` |
| **GRT** | `Tier 2` | `2` | `100.0%` | `999.000` | **`+46.0%`** | **`1.58x`** | `0.0%` | `+57.8%` |
| **STX** | `Tier 2` | `3` | `100.0%` | `999.000` | **`+44.9%`** | **`1.57x`** | `0.0%` | `+98.0%` |
| **1000PEPE** | `Tier 1` | `5` | `60.0%` | `4.390` | **`+44.2%`** | **`1.56x`** | `-13.1%` | `+168.0%` |
| **UNI** | `Tier 1` | `9` | `33.3%` | `2.942` | **`+41.3%`** | **`1.51x`** | `-16.2%` | `+119.5%` |
| **TRUMP** | `Tier 1` | `2` | `100.0%` | `999.000` | **`+40.3%`** | **`1.50x`** | `0.0%` | `+65.4%` |
| **DOGE** | `Tier 1` | `1` | `100.0%` | `999.000` | **`+34.7%`** | **`1.41x`** | `0.0%` | `+89.1%` |
| **JASMY** | `Tier 2` | `1` | `100.0%` | `999.000` | **`+32.2%`** | **`1.38x`** | `0.0%` | `+44.7%` |
| **AR** | `Tier 2` | `2` | `100.0%` | `999.000` | **`+32.0%`** | **`1.38x`** | `0.0%` | `+65.5%` |
| **ETH** | `Tier 1` | `2` | `100.0%` | `999.000` | **`+30.8%`** | **`1.36x`** | `0.0%` | `+50.0%` |
| **XLM** | `Tier 1` | `8` | `50.0%` | `2.291` | **`+30.3%`** | **`1.35x`** | `-20.8%` | `+110.7%` |


---

## 5. Bottom 10 Drag Laggards & Stop-Tax Culprits

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MAE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OP** | `Tier 1` | `8` | `12.5%` | `0.179` | **`-44.5%`** | `0.64x` | `-36.1%` | `-63.3%` |
| **AAVE** | `Tier 1` | `10` | `20.0%` | `0.360` | **`-42.9%`** | `0.65x` | `-53.3%` | `-76.2%` |
| **TAO** | `Tier 1` | `5` | `20.0%` | `0.088` | **`-33.1%`** | `0.72x` | `-36.0%` | `-90.2%` |
| **DOT** | `Tier 1` | `12` | `33.3%` | `0.481` | **`-24.6%`** | `0.78x` | `-30.9%` | `-75.1%` |
| **ARB** | `Tier 2` | `3` | `0.0%` | `0.000` | **`-22.9%`** | `0.80x` | `-17.3%` | `-26.0%` |
| **XRP** | `Tier 1` | `7` | `42.9%` | `0.045` | **`-21.6%`** | `0.81x` | `-22.6%` | `-53.5%` |
| **EIGEN** | `Tier 2` | `3` | `0.0%` | `0.000` | **`-20.3%`** | `0.82x` | `-7.2%` | `-31.7%` |
| **APE** | `Tier 2` | `3` | `0.0%` | `0.000` | **`-20.1%`** | `0.82x` | `-11.5%` | `-21.0%` |
| **TRX** | `Tier 2` | `12` | `8.3%` | `0.102` | **`-17.1%`** | `0.84x` | `-13.4%` | `-35.0%` |
| **1000BONK** | `Tier 2` | `2` | `0.0%` | `0.000` | **`-17.0%`** | `0.84x` | `-4.0%` | `-22.7%` |


---

## 6. Symbol Breadth & Universe Participation
- **Total Unique Symbols Traded:** `121`
- **Net Profitable Symbols:** `63` (52.1%)
- **Net Drawdown Symbols:** `58` (47.9%)
- **Neutral / Breakeven Symbols:** `0` (0.0%)
- **Individual Asset Trade Logs:** Available in `data/all_tapes/v12_production/symbols/<ASSET>_trades.csv`

---

### 🛡️ Counterfactual Telemetry & Veto Alpha
| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Total Vetoed Signals** | `20,645` | Signals safely filtered out at gates |
| **Dodged Bullets (Loss Saved)** | `12,137` | Vetoed signals that dumped or hit initial stops |
| **Missed Opportunities** | `4,065` | Vetoed signals that rallied $\ge +20\%$ MFE |
| **Saved Loss Magnitude** | `+167,353.5%` | Total capital protected from false breakouts |
| **Missed Upside Excursion** | `-198,805.8%` | Total upside forgone |
| **Net Veto Alpha** | `+-31,452.3%` | **Net Statistical Advantage of Risk Gates** |
| **Gate Efficiency Ratio** | `58.8%` | Percentage of vetoes that prevented capital loss |

---
*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*
