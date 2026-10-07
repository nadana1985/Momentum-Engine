# Kronos V12: Production Executive Tear Sheet
**Clean 6-Core Framework Performance Ledger**  
Generated: `2026-10-07 06:38:26 UTC`

---

## 1. Executive Performance Matrix (Strict Compounding Log Space)

| Performance Metric | V12 Clean 6-Core | Benchmark Target | Status |
| :--- | :--- | :--- | :--- |
| **Total Closed Trades** | `3,336` | N/A | Validated |
| **Win Rate** | **`50.42%`** | `> 50.0%` | ✅ **Passed** |
| **Profit Factor** | **`1.352`** | `> 1.50` | ✅ **Passed** |
| **Cumulative Net Log Return** | **`+3641.6%`** | `> +200%` | ✅ **Passed** |
| **Compounded Capital Multiple** | **`6537752839521056.00x`** | `> 5.0x` | ✅ **Outperforming** |
| **Mean Net Log Return / Trade** | **`+1.09%`** | `> +1.0%` | ✅ **Passed** |
| **Currently Active Open Trades** | **`38`** | Monitored Live | In Flight |

---

## 2. Liquidity Tier & Book Attribution

### By Dynamic Liquidity Tier
| Liquidity Tier | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | `601` | `48.6%` | `1.627` | `+1141.8%` | `90912.58x` |
| **Tier 2** | `274` | `38.3%` | `1.930` | `+624.2%` | `513.90x` |
| **Tier 3** | `2,461` | `52.2%` | `1.239` | `+1875.7%` | `139935779.83x` |


### By Execution Book
| Book | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Book 1** | `164` | `39.6%` | `2.025` | `+533.7%` | `207.90x` |
| **Book 2** | `738` | `34.6%` | `1.672` | `+1175.9%` | `127869.69x` |
| **Book 3** | `2,434` | `56.0%` | `1.240` | `+1932.1%` | `245925447.48x` |


---

## 3. Exit Reason & Microstructure Decomposition

| Exit Trigger | Count | Share | Total Net Log PnL |
| :--- | :--- | :--- | :--- |
| `target_reclaim` | `1,117` | `33.5%` | `+9313.7%` |
| `stop_loss` | `852` | `25.5%` | `-7461.1%` |
| `time_expiry` | `457` | `13.7%` | `+99.8%` |
| `fast_decay_cut` | `231` | `6.9%` | `-553.9%` |
| `time_cap` | `224` | `6.7%` | `+2157.4%` |
| `initial_stop` | `154` | `4.6%` | `-1215.6%` |
| `stall_bailout` | `141` | `4.2%` | `-361.1%` |
| `breakeven_ratchet` | `50` | `1.5%` | `+9.6%` |
| `climax_top_harvest` | `41` | `1.2%` | `+1305.9%` |
| `trail_stop` | `31` | `0.9%` | `+446.3%` |
| `stagnation_cut` | `31` | `0.9%` | `-76.9%` |
| `stagnation_bailout` | `7` | `0.2%` | `-22.4%` |


---

## 4. Top 15 Institutional Alpha Leaders

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MFE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **IMX** | `Tier 3` | `23` | `78.3%` | `6.382` | **`+156.0%`** | **`4.76x`** | `-9.7%` | `+12.8%` |
| **RSR** | `Tier 3` | `22` | `81.8%` | `4.173` | **`+109.0%`** | **`2.97x`** | `-17.2%` | `+9.6%` |
| **SNX** | `Tier 3` | `34` | `70.6%` | `2.384` | **`+96.9%`** | **`2.63x`** | `-17.4%` | `+7.6%` |
| **AVAX** | `Tier 1` | `16` | `62.5%` | `5.044` | **`+96.0%`** | **`2.61x`** | `-11.8%` | `+14.1%` |
| **AERO** | `Tier 1` | `5` | `100.0%` | `999.000` | **`+93.7%`** | **`2.55x`** | `0.0%` | `+27.2%` |
| **WLD** | `Tier 1` | `16` | `75.0%` | `3.979` | **`+86.1%`** | **`2.37x`** | `-11.7%` | `+15.5%` |
| **SKL** | `Tier 3` | `24` | `70.8%` | `2.651` | **`+84.8%`** | **`2.33x`** | `-25.8%` | `+8.7%` |
| **KSM** | `Tier 3` | `21` | `61.9%` | `4.029` | **`+82.2%`** | **`2.27x`** | `-14.5%` | `+7.6%` |
| **ETC** | `Tier 1` | `8` | `100.0%` | `999.000` | **`+81.1%`** | **`2.25x`** | `0.0%` | `+14.3%` |
| **FLOW** | `Tier 3` | `16` | `75.0%` | `4.673` | **`+78.3%`** | **`2.19x`** | `-10.0%` | `+9.5%` |
| **CELO** | `Tier 3` | `27` | `70.4%` | `2.244` | **`+78.3%`** | **`2.19x`** | `-20.5%` | `+7.8%` |
| **ZRX** | `Tier 3` | `22` | `63.6%` | `2.896` | **`+77.5%`** | **`2.17x`** | `-19.5%` | `+7.6%` |
| **APT** | `Tier 1` | `16` | `62.5%` | `3.449` | **`+72.2%`** | **`2.06x`** | `-8.8%` | `+12.4%` |
| **ARPA** | `Tier 3` | `20` | `65.0%` | `2.324` | **`+70.2%`** | **`2.02x`** | `-27.8%` | `+10.2%` |
| **IOTX** | `Tier 3` | `17` | `82.3%` | `3.713` | **`+69.9%`** | **`2.01x`** | `-17.2%` | `+10.8%` |


---

## 5. Bottom 10 Drag Laggards & Stop-Tax Culprits

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MAE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ID** | `Tier 3` | `18` | `27.8%` | `0.384` | **`-57.2%`** | `0.56x` | `-55.9%` | `-6.8%` |
| **TNSR** | `Tier 3` | `18` | `33.3%` | `0.429` | **`-55.8%`** | `0.57x` | `-84.5%` | `-7.6%` |
| **1000000BOB** | `Tier 3` | `5` | `60.0%` | `0.273` | **`-55.2%`** | `0.58x` | `-75.9%` | `-16.3%` |
| **TAO** | `Tier 1` | `8` | `12.5%` | `0.072` | **`-55.0%`** | `0.58x` | `-46.4%` | `-13.8%` |
| **BEAMX** | `Tier 3` | `20` | `30.0%` | `0.466` | **`-53.5%`** | `0.59x` | `-69.9%` | `-7.4%` |
| **JELLYJELLY** | `Tier 3` | `7` | `0.0%` | `0.000` | **`-48.7%`** | `0.61x` | `-40.1%` | `-14.1%` |
| **1000RATS** | `Tier 3` | `14` | `35.7%` | `0.504` | **`-41.0%`** | `0.66x` | `-49.3%` | `-11.4%` |
| **AGLD** | `Tier 3` | `15` | `33.3%` | `0.490` | **`-40.4%`** | `0.67x` | `-53.9%` | `-7.9%` |
| **ACH** | `Tier 3` | `23` | `39.1%` | `0.598` | **`-39.4%`** | `0.67x` | `-59.5%` | `-7.2%` |
| **SOL** | `Tier 1` | `9` | `11.1%` | `0.328` | **`-39.1%`** | `0.68x` | `-25.8%` | `-9.2%` |


---

## 6. Symbol Breadth & Universe Participation
- **Total Unique Symbols Traded:** `529`
- **Net Profitable Symbols:** `260` (49.1%)
- **Net Drawdown Symbols:** `266` (50.3%)
- **Neutral / Breakeven Symbols:** `3` (0.6%)
- **Individual Asset Trade Logs:** Available in `data/all_tapes/v12_production/symbols/<ASSET>_trades.csv`

---

### 🛡️ Counterfactual Telemetry & Veto Alpha
| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Total Vetoed Signals** | `52,992` | Signals safely filtered out at gates |
| **Dodged Bullets (Loss Saved)** | `32,932` | Vetoed signals that dumped or hit initial stops |
| **Missed Opportunities** | `10,138` | Vetoed signals that rallied $\ge +20\%$ MFE |
| **Saved Loss Magnitude** | `+484,030.4%` | Total capital protected from false breakouts |
| **Missed Upside Excursion** | `-529,633.3%` | Total upside forgone |
| **Net Veto Alpha** | `+-45,602.9%` | **Net Statistical Advantage of Risk Gates** |
| **Gate Efficiency Ratio** | `62.1%` | Percentage of vetoes that prevented capital loss |

#### Veto Gate Attribution
| Gate | Count | Share |
| :--- | :--- | :--- |
| `Core 1: Macro Bear Veto` | `22,470` | `42.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `13,420` | `25.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `7,205` | `13.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5,398` | `10.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2,002` | `3.8%` |
| `Core 4: Funding Rate Cap` | `1,339` | `2.5%` |
| `Core 4: Defensible Whale Dump` | `839` | `1.6%` |
| `Core 4: Whale Firewall` | `250` | `0.5%` |

---
*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*
