"""
tests/test_operational_hardening.py — Tests for V12 Operational Hardening & AWS Tooling
Covers:
  - BANNED Event Circuit Breaker (HTTP 418 & 451 halting)
  - RateLimiter thread safety and pacing
  - Atomic Parquet crash resistance
  - AWS SNS Signal Alert formatter and graceful exit
  - Disaster Recovery restore CLI sanity
"""

import os
import sys
import time
import threading
from pathlib import Path
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import config.ingestion.live_bridger as lb
from config.ingestion.live_bridger import RateLimiter, atomic_to_parquet, api_get, IpBannedError
from scripts.notify_signals_sns import format_table, notify_signals_sns
from scripts.restore_from_s3 import restore_from_s3


def test_rate_limiter_pacing():
    """Verify that RateLimiter properly paces requests across threads."""
    limiter = RateLimiter(max_per_second=20.0)  # 50ms intervals
    timestamps = []
    lock = threading.Lock()

    def worker():
        for _ in range(5):
            limiter.wait()
            with lock:
                timestamps.append(time.monotonic())

    threads = [threading.Thread(target=worker) for _ in range(4)]
    t0 = time.monotonic()
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    total_time = time.monotonic() - t0
    assert len(timestamps) == 20
    # 20 requests at 20 req/s should take at least ~0.8s
    assert total_time >= 0.70


def test_atomic_to_parquet_resilience(tmp_path):
    """Verify that atomic_to_parquet writes safely and cleans up temporary files on error."""
    target = tmp_path / "test_shard.parquet"
    df_init = pd.DataFrame({"timestamp": [1000, 2000], "val": [1.0, 2.0]})
    atomic_to_parquet(df_init, str(target))

    assert target.exists()
    assert len(pd.read_parquet(target)) == 2

    # Verify that a write failure does NOT corrupt the existing file
    class FaultInjectionError(Exception):
        pass

    def broken_to_parquet(*args, **kwargs):
        raise FaultInjectionError("Simulated disk error")

    orig_to_parquet = pd.DataFrame.to_parquet
    pd.DataFrame.to_parquet = broken_to_parquet
    try:
        df_corrupt = pd.DataFrame({"timestamp": [3000], "val": [9.9]})
        with pytest.raises(FaultInjectionError):
            atomic_to_parquet(df_corrupt, str(target))
    finally:
        pd.DataFrame.to_parquet = orig_to_parquet

    # Original file must remain 100% intact
    recovered_df = pd.read_parquet(target)
    assert len(recovered_df) == 2
    assert recovered_df["timestamp"].tolist() == [1000, 2000]


def test_banned_circuit_breaker(monkeypatch):
    """Verify that HTTP 418 trips BANNED event and blocks subsequent requests."""
    lb.BANNED.clear()
    assert not lb.BANNED.is_set()

    class MockResponse:
        status_code = 418
        headers = {"Retry-After": "120"}

    class MockSession:
        def get(self, url, **kwargs):
            return MockResponse()

    monkeypatch.setattr(lb, "get_session", lambda: MockSession())

    with pytest.raises(IpBannedError) as exc_info:
        api_get("https://fapi.binance.com/test")

    assert "HTTP 418" in str(exc_info.value)
    assert lb.BANNED.is_set()

    # Subsequent request must fail immediately without calling get_session
    called = []
    def fail_if_called(*args, **kwargs):
        called.append(True)
        return MockResponse()

    MockSession.get = fail_if_called
    with pytest.raises(IpBannedError) as exc_info2:
        api_get("https://fapi.binance.com/test")

    assert "Request skipped" in str(exc_info2.value)
    assert len(called) == 0  # Was never called because circuit breaker tripped

    # Reset BANNED for subsequent tests
    lb.BANNED.clear()


def test_sns_format_table():
    """Verify ASCII table rendering for trade alert emails."""
    sample_rows = [
        {
            "asset": "1INCH",
            "tier": "Tier 3",
            "book": "Book 3",
            "entry_price": 0.09878,
            "stop_price": 0.09088,
            "sizing_weight": 1.0,
        },
        {
            "asset": "BTC",
            "tier": "Tier 1",
            "book": "Book 1",
            "entry_price": 65000.0,
            "stop_price": 63000.0,
            "sizing_weight": 1.5,
        },
    ]
    table = format_table(sample_rows)
    assert "1INCH" in table
    assert "Tier 3" in table
    assert "Book 3" in table
    assert "BTC" in table
    assert "-8.00%" in table or "-8.0" in table


def test_sns_notify_graceful_local():
    """Verify that notify_signals_sns exits cleanly on localhost without error."""
    code = notify_signals_sns(topic_arn=None)
    assert code == 0


def test_restore_s3_graceful_missing_bucket():
    """Verify that restore_from_s3 exits with code 1 if no bucket specified."""
    # Temporarily unset S3_BUCKET
    old = os.environ.pop("S3_BUCKET", None)
    try:
        code = restore_from_s3(bucket_name=None)
        assert code == 1
    finally:
        if old:
            os.environ["S3_BUCKET"] = old
