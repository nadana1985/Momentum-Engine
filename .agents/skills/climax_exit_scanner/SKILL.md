---
name: climax_exit_scanner
description: Instructions and standard procedure for auditing active momentum runners and short squeezes across the 6 Climax Exhaustion Signatures, BTR Air-Pocket Fragility, and Dynamic Trailing Stops to determine whether to Hold, Add on Dip, Ratchet Stop, or Harvest Climax Profits.
---

# 6-Signature Climax Exit & Position Hold Scanner Skill

This skill teaches the AI agent how to evaluate open long positions and active momentum runners (`OGN`, `ERA`, `MAGIC`, `CTSI`, etc.) using the deterministic production tool [`scripts/scan_climax_exits.py`](file:///f:/kronos_v1_alt/scripts/scan_climax_exits.py).

---

## 1. When to Use This Skill
Activate this skill whenever the user asks:
- "Should I hold or exit `<ASSET>`?" or "Exit scanner?" or "Is the pump over on `<ASSET>`?"
- To check whether a pullback on an active runner is a **Mid-Run Shakeout Dip (`HOLD / ADD`)** or a **Climax Top / Distribution Unwind (`EXIT ALL`)**.
- To audit a portfolio/watchlist of active trades and rank them by **Exit Urgency Score (0–100)**.

---

## 2. Deterministic Command-Line Execution

```bash
# 1. Single-asset Exit vs. Hold Tear Sheet (with 6 Signatures + Dynamic VWAP & -1.5% Cushion Stops):
python scripts/scan_climax_exits.py --symbol ERA
python scripts/scan_climax_exits.py --symbol MAGIC

# 2. Audit a multi-token Watchlist / Portfolio side-by-side:
python scripts/scan_climax_exits.py --watchlist "ERA,MAGIC,CTSI,OGN,C98,KAIA,S"

# 3. Scan the entire 725-shard universe for extended runners needing exit/hold decisions:
python scripts/scan_climax_exits.py --scan

# 4. Historical point-in-time verification (e.g. OGN exact peak at 2026-10-08 20:00:00):
python scripts/scan_climax_exits.py --symbol OGN --as-of "2026-10-08 20:00:00"
```

---

## 3. The 6 Climax Exit Signatures (0 to 100 Exit Urgency Score)

1. **`[Sig 1]` Climax Pinbar Upper Wick Rejection (Max 20 pts):**
   - Upper wick $\ge 75\%$ at an extended high (20 pts) \| $\ge 55\%$ (14 pts) \| $\ge 45\%$ on $\ge 4\times$ volume shock (12 pts).
2. **`[Sig 2]` Volume & Trade Count Bearish Divergence + Ticket Contraction (Max 20 pts):**
   - 1h Volume and 1h Trade Count drop $\le -50\%$ to $-60\%$ below the 24h impulse peak (15 pts) + Average Ticket Size (\$/trade) contracts $< 0.75\times$ median (+5 pts).
3. **`[Sig 3]` Token Open Interest Divergence & Unwind (Max 20 pts):**
   - Token OI drops $\le -15\%$ below 24h peak [Active Post-Climax Unwind] (20 pts) \| drops $-4\%$ to $-15\%$ at a new price high [Peak Fuel Depletion] (14 pts).
4. **`[Sig 4]` 10x Funding Rate Collapse or Retail Long Euphoria (Max 15 pts):**
   - Extreme negative carry ($\le -0.30\%$) snaps near zero ($\ge -0.05\%$) (15 pts) \| mild negative carry snaps to zero (10 pts) \| flips to crowded long euphoria ($\ge +0.05\% / 8\text{h}$) (12 pts).
5. **`[Sig 5]` Taker Buy Breakdown & Velocity Stall (Max 15 pts):**
   - Taker Buy $< 46\%$ (15 pts) \| Taker Buy $< 49.5\%$ with Volume Shock dropping $\le 1.25\times$ median (12 pts).
6. **`[Sig 6]` Whale L/S Floor Inflection (Top-Shorts Covering in Profit) (Max 10 pts):**
   - Whale L/S hits a 24h floor ($\le 0.85$) and rebounds $\ge +0.05$ while Token OI bleeds $\le -4\%$ (10 pts).

---

## 4. Tactical Decision Matrix & Multi-Timeframe 200-EMA Tier (`LEADING` vs. `LAGGING`)

| Tactical Decision Output | Exit Urgency Score & Alarms | Meaning & Execution Mandate |
| :--- | :--- | :--- |
| **`HOLD_STRONG / ADD_DIP (SQUEEZE_FUEL_INTACT)`** | Score $< 35$ \| $\le 1/6$ Alarms | Token OI at `0.0%` peak, Whales at 24h low, negative carry active. Hold above **24h Dynamic VWAP** and **$-1.5\%$ Cushion Stop**. |
| **`RATCHET_STOP / PARTIAL_TP (CAUTION)`** | Score $35 - 54$ \| $2/6$ Alarms | Early momentum deceleration; lock stop to breakeven/trail and harvest partial gains at R1/R2. |
| **`CLIMAX_HARVEST_NOW (TAKE_PROFIT_100%)`** | Score $\ge 55$ or $\ge 3/6$ Alarms at Peak | Blow-off top exhaustion (`OGN` @ \$0.0536); execute immediate 100% market harvest. |
| **`POST_CLIMAX_UNWIND (EXIT_ALL / AVOID_LONGS)`** | Token OI $\le -15\%$ + Whale L/S Rebound | Squeeze is over; whales are covering shorts into retail liquidations (`OGN`, `MAGIC`, `CTSI` post-peak). |

### Multi-Timeframe `200 EMA` Convergence (`LEADING` vs. `LAGGING`) & Breakdown Low Magnets
- **`LEADING` (`200EMA_MERGED_ABOVE`):** `price_vs_ema200_1d_pct >= -3.0%` AND `ema_1h_vs_1d_gap_pct >= -15.0%`. True multi-day flyers (`OGN`, `MAGIC`, `GTC`, `CTSI`, `ARPA`, `BAT`, `LUMIA`, `KAIA`) that run all the way to their **Sep 2025 Breakdown Low (`[M2]`)**.
- **`LAGGING` (`SUB_1D_200EMA_LAGGING`):** `price_vs_ema200_1d_pct < -3.0%` OR `ema_1h_vs_1d_gap_pct < -15.0%`. Sub-200-EMA laggards (`ERA`, `WAL`) where rallies are counter-trend bounces into the descending `1D 200 SMA / 1D 200 EMA` wall—harvest profits early at the `1D 200 SMA` or `Nov 2025 Breakdown Low (`[M1]`)`.

