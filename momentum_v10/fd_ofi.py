# Version 10
"""Fractionally Differenced Order Flow Imbalance (FDOFI) kernel.

Clean-room port of the causal binomial expansion kernel (formerly Point 24).
Pure function only: zero kronos dependencies, zero config/YAML access.
"""
from __future__ import annotations

import numpy as np
from numba import njit


@njit(cache=True)
def compute_fd_ofi_kernel(
    OFI: np.ndarray,
    W_t: np.ndarray,
    epsilon_t: np.ndarray,
    d: float,
) -> np.ndarray:
    """
    JIT Kernel: Fractionally Differenced OFI (FDOFI) per bar.

    Pre-compute FD binomial weights w[k] using the standard recurrence:
      w[0] = 1.0
      w[k] = w[k-1] * (k - 1 - d) / k  for k >= 1

    For each bar t:
      FDOFI[t] = sum(OFI[t-k] * w[k] for k = 0 .. min(W-1, t))
               = causal dot-product of window with FD weights

    Equivalent to original: pad(OFI, W-1) -> sliding_window_view -> dot(window, w_reversed).
    Only difference: warmup bars 0..W-2 use shorter actual history (no padding artefact).
    This is causally purer — no future-value padding injected at the start.
    """
    n = len(OFI)
    out = np.zeros(n, dtype=np.float64)

    # Pre-compute FD weights for max W across the series
    max_w = 0
    for i in range(n):
        wi = int(W_t[i])
        if wi > max_w:
            max_w = wi
    if max_w < 1:
        max_w = 1

    w = np.zeros(max_w, dtype=np.float64)
    w[0] = 1.0
    for k in range(1, max_w):
        w[k] = w[k - 1] * (k - 1.0 - d) / k

    for t in range(n):
        W = int(W_t[t])
        if W < 1:
            W = 1
        # Causal window: OFI[t], OFI[t-1], ..., OFI[max(0, t-W+1)]
        limit = min(W, t + 1)  # how many bars available
        val = 0.0
        for k in range(limit):
            val += OFI[t - k] * w[k]
        if val != val or val > 1e18 or val < -1e18:
            val = 0.0
        out[t] = val

    return out



