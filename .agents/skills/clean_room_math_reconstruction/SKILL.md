---
name: clean_room_math_reconstruction
description: Guidelines for isolating legacy mathematical kernels into pure, side-effect-free functions, verifying them with tests, and avoiding duplicate implementation.
---

# Clean-Room Math Reconstruction Skill

This skill guides the agent in safely extracting legacy mathematical models (volatility, conviction, veto gates) and rebuilding them in a pure, testable, and correct manner.

## Core Rules

1. **Pure Functions Only:**
   * All mathematical estimators and signal normalizers must be "pure functions" (outputs depend strictly on inputs, no side effects, no database/config access).
   
2. **Golden Snapshot Testing:**
   * For every math function extracted, the agent must write a unit test inside `kronos_v2/tests/` using pre-calculated mock input/output pairs to verify mathematical equality.
   
3. **No Zero-Series Fallbacks:**
   * If a mathematical estimation node fails (e.g. Numba matrix math throws exception), the fallback must return a domain-specific conservative estimate (like standard deviation for volatility) instead of returning `0.0`.

4. **Estimator Independence — No Shared Mutation (Data-Verified):**
   * The 4 legacy volatility estimators (Points 48, 52, 56, 57) mutate a shared `_raw_std_vol` variable sequentially. In `kronos_v2/estimators.py`, each estimator MUST compute from raw OHLCV independently with its own explicit lookback window. Do not share or mutate intermediate results across estimators.

5. **Golden Snapshot for `slot_39` Unit Bug:**
   * The mandatory golden snapshot test for Point 48 (MAD vol) must assert the output is a percentage return (not a price): `assert 0.0001 < mad_vol < 0.20`. Historical parquet shows `slot_39` mean = 2,200 (ETH price in USD) — this is the confirmed unit bug. Use `df['close'].pct_change().mad()`, not `df['close'].mad()`.
