"""Golden snapshot test verifying momentum_v10 FDOFI JIT kernel against kronos reference oracle."""
import numpy as np
import pytest

from momentum_v10.fd_ofi import compute_fd_ofi_kernel
# Reference oracle for golden snapshot comparison only:
from kronos.quant_spec.overrides.point_24 import _compute_point_24_kernel


def test_fd_ofi_kernel_golden_snapshot():
    np.random.seed(42)
    n = 200
    ofi = np.random.randn(n) * 1000.0
    ofi[10:15] = 0.0
    ofi[50] = 1e5
    ofi[100] = -1e5

    W_t = np.full(n, 100, dtype=np.float64)
    eps = np.full(n, 1e-8, dtype=np.float64)
    d = 0.45

    res_v7 = compute_fd_ofi_kernel(ofi.astype(np.float64), W_t, eps, d)
    res_oracle = _compute_point_24_kernel(ofi.astype(np.float64), W_t, eps, d)

    assert res_v7.shape == res_oracle.shape
    assert np.allclose(res_v7, res_oracle, equal_nan=True)
    assert not np.isnan(res_v7).all()

