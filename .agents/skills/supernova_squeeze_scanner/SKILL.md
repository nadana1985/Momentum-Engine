---
name: supernova_squeeze_scanner
description: Instructions and standard procedure for screening the cryptocurrency universe for AGT/Q-type Supernova Squeezes, Stage A pre-ignition coils, Bar 0 whale counter-short traps, and terminal climax exhaustion across the 6 minute microstructure signatures.
---

# Supernova Squeeze & Whale Counter-Short Scanner Skill

This skill teaches the AI agent how to detect, analyze, and screen for **AGT/Q-type Supernova Squeezes** and **Whale Counter-Short Traps** using the deterministic production tool [`scripts/scan_supernova_squeezes.py`](file:///f:/kronos_v1_alt/scripts/scan_supernova_squeezes.py).

---

## 1. When to Use This Skill
Activate this skill whenever the user asks to:
- Find "the next AGT" or "the next Q" across the perpetual universe.
- Screen for **Stage A Pre-Ignition Coils** (iceberg limit absorption, micro-range volatility compression, open interest retention).
- Screen for **Bar 0 Ignition Traps** (volume shock $\ge 5\times$, 4h OI surge, instantaneous whale inversion $\Delta L/S_{4\text{h}} \le -0.20$).
- Monitor **Active Supernova Runners** (Top Trader Whales pinned net short $L/S < 0.60$ with negative funding carry).
- Detect **Terminal Climax Exhaustion Alerts** (upper wick $\ge 0.55$, distance to 200h EMA $> +8\text{ ATR}$, whale capitulation).
- Audit a specific symbol's microstructure against the 6 fine-grained signatures at the current tape or historical timestamp.

---

## 2. Deterministic Command-Line Execution

Agents must **NEVER** write ad-hoc scanning loops. Always use the canonical production tool:

```bash
# 1. Full universe scan across all liquid shards:
python scripts/scan_supernova_squeezes.py --scan

# 2. Screen exclusively for STAGE A PRE-IGNITION COILS (Early setups before ignition):
python scripts/scan_supernova_squeezes.py --scan --stage a

# 3. Screen exclusively for BAR 0 IGNITION SHOCKS (Active velocity triggers):
python scripts/scan_supernova_squeezes.py --scan --stage b

# 4. Screen exclusively for STAGE C ACTIVE SUPERNOVA RUNNERS (Parabolic squeezes):
python scripts/scan_supernova_squeezes.py --scan --stage c

# 5. Screen for CLIMAX EXHAUSTION ALERTS (Harvesting / Exit triggers):
python scripts/scan_supernova_squeezes.py --scan --stage climax

# 6. Detailed single-symbol diagnostic audit (e.g. AGT, Q, A, SLP):
python scripts/scan_supernova_squeezes.py --symbol AGT
python scripts/scan_supernova_squeezes.py --symbol Q

# 7. Historical point-in-time causal verification (Rule 4 Zero-Lookahead):
python scripts/scan_supernova_squeezes.py --symbol AGT --as-of "2026-10-15 16:00:00"
python scripts/scan_supernova_squeezes.py --symbol AGT --as-of "2026-10-14 12:00:00"

# 8. Machine-readable JSON output:
python scripts/scan_supernova_squeezes.py --symbol A --json
```

---

## 3. The 3-State Causal Finite State Machine Architecture

```
[ STATE A: DORMANT COIL ] ──(Bar 0 Ignition Shock)──> [ STATE B: IGNITION TRAP ] ──(Squeeze Confirmation)──> [ STATE C: SUPERNOVA RUNNER ]
      │                                                         │                                                   │
      │ (Iceberg Bids, Vol Comp, OI Retention)                  │ (Vol Shock ≥ 5x, 4h dOI ≥ 10%, dLS/dt ≤ -0.20)     │ (Whale L/S < 0.60, Negative Carry)
      └─────────────────────────────────────────────────────────┴───────────────────────────────────────────────────┴──> [ CLIMAX EXHAUSTION HARVEST ]
                                                                                                                             (Upper Wick ≥ 0.55, Dist > +8 ATR)
```

### State Definitions:
1. **`STAGE_A_DORMANT_COIL` (Pre-Ignition Stealth Absorption):**
   - **Taker Buy Ratio:** $\text{TBR} \le 0.48$ (Retail market selling into resting institutional limit bids).
   - **Trade Size Shock:** $\frac{\text{AvgTradeSize}_{24\text{h}}}{\text{AvgTradeSize}_{30\text{d}}} \ge 1.20\times$ (Large whale fills).
   - **Volatility Compression:** $\frac{\text{ATR}_{24\text{h}}}{\text{ATR}_{30\text{d}}} \le 0.65$ (Bollinger/Donchian bandwidth compression).
   - **Orderflow Retention:** $\Delta \text{OI}_{72\text{h}} \ge 0.0\%$ despite prior $-10\sigma \text{ ATR}$ drawdown.
   - **Whale Posture:** $30\% \le \text{pct}_{LS} \le 55\%$ (Indifferent/neutral, zero retail crowd chasing).

2. **`BAR_0_IGNITION_TRAP` (The Velocity Breakout Shock):**
   - **Volume Shock:** $\ge 5.0\times$ of 30-day hourly average.
   - **Structural Break:** Hourly Close $> \text{EMA}_{200\text{h}}$ (or $> \text{High}_{72\text{h}}$).
   - **Orderflow Surge:** $4\text{h } \Delta \text{OI} \ge +10\%$ to $+50\%$.
   - **Whale Inversion Derivative:** $\Delta LS_{4\text{h}} \le -0.20$ (Whales aggressively counter-short into the breakout).

3. **`STAGE_C_SUPERNOVA_RUNNER` (Parabolic Trapped Squeeze):**
   - **Whale Net Short:** Whale $L/S < 0.80$ (often $< 0.50$ or $z_{LS} \le -2.0\sigma$) pinned while price trends.
   - **Carry Asymmetry:** Funding APR $\le 0.0\%$ (shorts paying fee penalty) or extreme OI expansion.
   - **Exit Protocol:** Ride structural 72h Donchian floor trail (`low_72h`).

4. **`CLIMAX_EXHAUSTION` (Harvest Alert):**
   - **Upper Wick Ratio:** $\ge 0.55$ (55%+ upper rejection wick).
   - **Extension:** Price $\ge \text{EMA}_{200\text{h}} + 8.0\text{ ATR}$.
   - **Whale Trough:** Whale $L/S < 0.65$.

---

## 4. Key Quantitative Invariants (Rule 7 Compliance)
- **Zero Static Constants:** Volatility must always be normalized by rolling asset ATR ($\Delta P / \text{ATR}_{24\text{h}}$), positioning by studentized Z-scores ($z_{LS}$), and open interest by rolling standard deviations.
- **The Flat-OI vs Surge-OI Law:** Organic spot breakouts have flat OI on Bar 0 ($-5\%$ to $+5\%$). Supernova short squeezes show immediate positive OI surges ($+10\%$ to $+50\%$) as shorts enter into the breakout.
