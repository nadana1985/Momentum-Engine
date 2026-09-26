"""Tests for the 2026-09-26 production hardening."""
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import pytest

from momentum_v10 import io_utils
from momentum_v10.io_utils import RateLimiter, RunLockedError, atomic_to_parquet, run_lock
import config.ingestion.live_bridger as lb

H = 3_600_000


# ---------------------------------------------------------------- atomic IO
def test_atomic_write_keeps_old_file_on_crash(tmp_path, monkeypatch):
    p = tmp_path / "x.parquet"
    atomic_to_parquet(pd.DataFrame({"timestamp": [1, 2]}), p)

    class Boom(Exception):
        pass

    def bad_to_parquet(self, path, **kw):
        Path(path).write_bytes(b"PAR1 half written")
        raise Boom()

    monkeypatch.setattr(pd.DataFrame, "to_parquet", bad_to_parquet)
    with pytest.raises(Boom):
        atomic_to_parquet(pd.DataFrame({"timestamp": [9]}), p)
    monkeypatch.undo()
    assert pd.read_parquet(p)["timestamp"].tolist() == [1, 2]
    assert [f.name for f in tmp_path.iterdir()] == ["x.parquet"]  # no tmp debris


# ------------------------------------------------------------ rate limiter
def test_rate_limiter_paces_across_threads():
    rl = RateLimiter(20)  # 50 ms spacing
    stamps = []
    lock = threading.Lock()

    def worker():
        for _ in range(5):
            rl.acquire()
            with lock:
                stamps.append(time.monotonic())

    ts = [threading.Thread(target=worker) for _ in range(4)]
    t0 = time.monotonic()
    [t.start() for t in ts]
    [t.join() for t in ts]
    assert len(stamps) == 20
    assert time.monotonic() - t0 >= 19 * 0.05 * 0.95
    s = sorted(stamps)
    assert min(b - a for a, b in zip(s, s[1:])) >= 0.04


# ---------------------------------------------------------------- run lock
def test_run_lock_is_exclusive(tmp_path):
    lock = tmp_path / ".lock"
    with run_lock(lock):
        with pytest.raises(RunLockedError):
            with run_lock(lock):
                pass
    with run_lock(lock):  # released again
        pass


# ------------------------------------------------------- funding schedule
@pytest.fixture
def funding_globals(monkeypatch):
    monkeypatch.setattr(lb, "global_next_funding", {})
    monkeypatch.setattr(lb, "global_funding_interval_h", {})
    return lb


def test_funding_skip_until_new_settlement_closes(funding_globals):
    t16 = 1790352000000 - (1790352000000 % (8 * H))  # an 8h boundary
    lb.global_next_funding["XUSDT"] = t16 + 8 * H     # last settlement = t16
    # shard already holds t16 bucket -> no call
    assert not lb.funding_call_needed("XUSDT", t16, t16 + 3 * H)
    # shard at t16-8h, settlement t16 bucket not closed yet (t16+5min) -> no call
    assert not lb.funding_call_needed("XUSDT", t16 - 8 * H, t16 + 5 * 60_000)
    # bucket closed -> call
    assert lb.funding_call_needed("XUSDT", t16 - 8 * H, t16 + H + 5 * 60_000)


def test_funding_backfills_after_outage_even_if_newest_not_closed(funding_globals):
    t16 = 1790352000000 - (1790352000000 % (8 * H))
    lb.global_next_funding["XUSDT"] = t16 + 8 * H
    # shard 33h stale, newest settlement bucket still forming -> must still call
    assert lb.funding_call_needed("XUSDT", t16 - 33 * H, t16 + 5 * 60_000)


def test_mangled_symbol_names_are_skipped(tmp_path, monkeypatch):
    raw = tmp_path / "raw"; ex = tmp_path / "ex"; raw.mkdir(); ex.mkdir()
    for n in ("BTC_USDT_1h.parquet", "???_USDT_1h.parquet"):
        (raw / n).write_bytes(b"")
    monkeypatch.setattr(lb, "RAW_DIR", str(raw)); monkeypatch.setattr(lb, "EXOTIC_DIR", str(ex))
    assert lb.get_symbols() == ["BTCUSDT"]
    from momentum_v10.universe_generator import discover_assets
    assert discover_assets(raw) == ["BTC"]


def test_funding_respects_custom_interval(funding_globals):
    t = 1790352000000 - (1790352000000 % (4 * H))
    lb.global_next_funding["YUSDT"] = t + 4 * H
    lb.global_funding_interval_h["YUSDT"] = 4
    assert lb.funding_call_needed("YUSDT", t - 4 * H, t + H + 60_000)
    assert not lb.funding_call_needed("YUSDT", t, t + 2 * H)


def test_funding_unknown_symbol_keeps_hourly_poll(funding_globals):
    assert lb.funding_call_needed("DEADUSDT", 0, 2 * H)
    assert not lb.funding_call_needed("DEADUSDT", H, H + 30 * 60_000)


def test_kline_limit_uses_lowest_weight_bucket():
    assert lb._kline_limit(1) == 99
    assert lb._kline_limit(200) == 499
    assert lb._kline_limit(5000) == 1000


# ------------------------------------------------------- fake Binance HTTP
class Resp:
    def __init__(self, status, payload, headers=None):
        self.status_code = status
        self._p = payload
        self.headers = headers or {}

    def json(self):
        return self._p


class FakeSession:
    """Serves hourly OI/LS rows from `start` to `end`, 500 per page."""

    def __init__(self, end, status=200):
        self.end = end
        self.status = status
        self.calls = []

    def get(self, url, params=None, timeout=None):
        self.calls.append((url, dict(params or {})))
        if self.status != 200:
            return Resp(self.status, {})
        start = params["startTime"]
        first = start + (-start % H)
        n = min(params["limit"], max(0, (self.end - first) // H + 1))
        rows = [first + i * H for i in range(n)]
        if "openInterestHist" in url:
            return Resp(200, [{"timestamp": t, "sumOpenInterest": "10", "sumOpenInterestValue": "20"} for t in rows])
        if "LongShort" in url:
            return Resp(200, [{"timestamp": t, "longShortRatio": "1.1"} for t in rows])
        return Resp(200, [])


@pytest.fixture
def fake_binance(monkeypatch):
    monkeypatch.setattr(lb, "FUTDATA_LIMITER", RateLimiter(0))
    monkeypatch.setattr(lb, "FUNDING_LIMITER", RateLimiter(0))
    monkeypatch.setattr(lb, "KLINE_LIMITER", RateLimiter(0))
    lb.BANNED.clear()

    def install(sess):
        monkeypatch.setattr(lb, "_session", sess)
        return sess
    yield install
    lb.BANNED.clear()


def test_metrics_paginate_across_long_outage(fake_binance):
    now = 1790352000000
    start = now - 900 * H           # 900h behind -> needs 2 pages of 500
    sess = fake_binance(FakeSession(end=now - H))
    df = lb._fetch_metrics_pages("XUSDT", start, now)
    assert len(df) == 899
    assert df["timestamp"].is_monotonic_increasing
    assert len(sess.calls) == 4     # 2 pages x (OI + LS)


def test_418_halts_all_requests(fake_binance):
    fake_binance(FakeSession(end=0, status=418))
    with pytest.raises(lb.IpBannedError):
        lb.api_get("/fapi/v1/klines", {}, lb.KLINE_LIMITER)
    assert lb.BANNED.is_set()
    with pytest.raises(lb.IpBannedError):
        lb.api_get("/fapi/v1/klines", {}, lb.KLINE_LIMITER)


def test_451_region_block_is_flagged(fake_binance):
    fake_binance(FakeSession(end=0, status=451))
    with pytest.raises(lb.IpBannedError):
        lb.api_get("/fapi/v1/time", {}, lb.KLINE_LIMITER)
    assert lb.BANNED.is_set()


# ------------------------------------------------------------ S3 + metrics
@pytest.fixture
def aws(monkeypatch, tmp_path):
    moto = pytest.importorskip("moto")
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "testing")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "testing")
    monkeypatch.setenv("AWS_DEFAULT_REGION", "eu-west-2")
    monkeypatch.setenv("V10_BACKUP_BUCKET", "v10-test")
    monkeypatch.setenv("V10_CW_NAMESPACE", "V10Test")
    from momentum_v10 import ops
    data = tmp_path / "data"
    tape = data / "all_tapes" / "v10_production"
    tape.mkdir(parents=True)
    (data / "raw_shards").mkdir()
    (data / "exotic_shards").mkdir()
    (data / "engine_state.json").write_text("{}")
    (data / "sync_state.json").write_text("{}")
    (tape / "closed_trades.csv").write_text("asset\nBTC\n")
    (tape / ".gitkeep").write_text("")
    atomic_to_parquet(pd.DataFrame({"timestamp": [1]}), data / "raw_shards" / "BTC_USDT_1h.parquet")
    atomic_to_parquet(pd.DataFrame({"timestamp": [1]}), data / "exotic_shards" / "BTCUSDT_metrics.parquet")
    monkeypatch.setattr(ops, "DATA_DIR", data)
    monkeypatch.setattr(ops, "TAPE_DIR", tape)
    with moto.mock_aws():
        import boto3
        boto3.client("s3", region_name="eu-west-2").create_bucket(
            Bucket="v10-test", CreateBucketConfiguration={"LocationConstraint": "eu-west-2"})
        yield ops, data


def _keys(prefix=""):
    import boto3
    r = boto3.client("s3", region_name="eu-west-2").list_objects_v2(Bucket="v10-test", Prefix=prefix)
    return sorted(o["Key"] for o in r.get("Contents", []))


def test_backup_schedule(aws):
    ops, _ = aws
    r = ops.backup(now=datetime(2026, 9, 26, 13, tzinfo=timezone.utc))
    assert r == {"enabled": True, "latest": 3, "daily": 0, "shards": 0}
    assert "v10/latest/all_tapes/v10_production/closed_trades.csv" in _keys()
    r = ops.backup(now=datetime(2026, 9, 27, 0, tzinfo=timezone.utc))
    assert r["daily"] == 3 and _keys("v10/daily/2026-09-27/")
    r = ops.backup(now=datetime(2026, 9, 27, 2, tzinfo=timezone.utc))
    assert r["shards"] == 2
    assert "v10/data/raw_shards/BTC_USDT_1h.parquet" in _keys()


def test_restore_seeds_empty_host(aws, tmp_path, monkeypatch):
    ops, data = aws
    ops.backup(now=datetime(2026, 9, 27, 2, tzinfo=timezone.utc))
    fresh = tmp_path / "fresh"
    monkeypatch.setattr(ops, "DATA_DIR", fresh)
    assert ops.restore()["restored"] == 5
    assert (fresh / "raw_shards" / "BTC_USDT_1h.parquet").exists()
    assert (fresh / "all_tapes" / "v10_production" / "closed_trades.csv").read_text() == "asset\nBTC\n"
    assert ops.restore()["restored"] == 0  # idempotent, no overwrite


def test_heartbeat_publishes(aws):
    ops, _ = aws
    assert ops.heartbeat({"ok": True, "open": 5, "run_seconds": 12})
    import boto3
    names = {m["MetricName"] for m in boto3.client("cloudwatch", region_name="eu-west-2")
             .list_metrics(Namespace="V10Test")["Metrics"]}
    assert {"HourlyOK", "OpenTrades", "RunSeconds"} <= names


def test_backup_disabled_without_bucket(monkeypatch):
    from momentum_v10 import ops
    monkeypatch.delenv("V10_BACKUP_BUCKET", raising=False)
    assert ops.backup() == {"enabled": False}


# ------------------------------------------------------ fail-closed gates
def test_hourly_fails_closed_on_empty_data_root(tmp_path):
    import json, os, subprocess, sys
    root = Path(__file__).resolve().parents[2]
    env = dict(os.environ, V10_DATA_ROOT=str(tmp_path), V10_SES_FROM="", V10_ALERT_TO="",
               V10_BACKUP_BUCKET="", V10_CW_NAMESPACE="", V10_BINANCE_BASE="http://127.0.0.1:9")
    r = subprocess.run([sys.executable, "-m", "momentum_v10.hourly_job"], cwd=root, env=env,
                       capture_output=True, text=True, timeout=120)
    assert r.returncode == 1
    st = json.loads((tmp_path / "all_tapes" / "v10_production" / "hourly_status.json").read_text())
    assert st["ok"] is False and "raw shards" in st["error"] and st["data_root"] == str(tmp_path.resolve())


def test_raw_fresh_pct(tmp_path, monkeypatch):
    import json
    from momentum_v10 import hourly_job
    import config.ingestion.sync_state_manager as ssm
    raw = tmp_path / "raw"; raw.mkdir()
    for a in ("AAA", "BBB", "CCC", "DDD"):
        (raw / f"{a}_USDT_1h.parquet").write_bytes(b"")
    now = datetime(2026, 9, 26, 12, 5, tzinfo=timezone.utc)
    last_closed = int(datetime(2026, 9, 26, 11, tzinfo=timezone.utc).timestamp() * 1000)
    state = tmp_path / "sync_state.json"
    state.write_text(json.dumps({"raw": {"AAA_USDT": last_closed, "BBB_USDT": last_closed,
                                         "CCC_USDT": last_closed - H, "DDD_USDT": last_closed}}))
    monkeypatch.setattr(hourly_job, "SHARD_DIR", raw)
    monkeypatch.setattr(ssm, "SYNC_STATE_PATH", state)
    assert hourly_job.raw_fresh_pct(now) == 75.0


def test_report_goes_to_sns_topic(aws, monkeypatch):
    import boto3
    from momentum_v10 import hourly_job
    sns = boto3.client("sns", region_name="eu-west-2")
    arn = sns.create_topic(Name="v10-alerts")["TopicArn"]
    q = boto3.client("sqs", region_name="eu-west-2")
    qurl = q.create_queue(QueueName="cap")["QueueUrl"]
    qarn = q.get_queue_attributes(QueueUrl=qurl, AttributeNames=["QueueArn"])["Attributes"]["QueueArn"]
    sns.subscribe(TopicArn=arn, Protocol="sqs", Endpoint=qarn)
    monkeypatch.setenv("V10_SNS_TOPIC_ARN", arn)
    assert hourly_job.send_report({"ok": False, "open": 3, "closed": 9, "error": "stale data"})
    import json
    msg = json.loads(q.receive_message(QueueUrl=qurl)["Messages"][0]["Body"])
    assert msg["Subject"].startswith("V10 hourly FAILED: 3 open")
    assert "Error: stale data" in msg["Message"]


def test_delisted_symbols_are_skipped_not_failed(tmp_path, monkeypatch, fake_binance):
    raw = tmp_path / "raw"; ex = tmp_path / "ex"; raw.mkdir(); ex.mkdir()
    for n in ("DEADUSDT_funding.parquet", "DEADUSDT_metrics.parquet"):
        atomic_to_parquet(pd.DataFrame({"timestamp": [1]}), ex / n)
    monkeypatch.setattr(lb, "RAW_DIR", str(raw)); monkeypatch.setattr(lb, "EXOTIC_DIR", str(ex))
    monkeypatch.setattr(lb, "global_next_funding", {"BTCUSDT": 1})
    monkeypatch.setattr(lb, "_sync", None)
    sess = fake_binance(FakeSession(end=0, status=400))
    assert lb.process_symbol("DEADUSDT")[1] == "delisted"
    assert sess.calls == []            # no request made, no funding fabricated
    assert pd.read_parquet(ex / "DEADUSDT_funding.parquet")["timestamp"].tolist() == [1]


def test_unlisted_symbol_with_price_shard_still_gets_klines(tmp_path, monkeypatch, fake_binance):
    raw = tmp_path / "raw"; ex = tmp_path / "ex"; raw.mkdir(); ex.mkdir()
    atomic_to_parquet(pd.DataFrame({"timestamp": [1]}), raw / "NEW_USDT_1h.parquet")
    monkeypatch.setattr(lb, "RAW_DIR", str(raw)); monkeypatch.setattr(lb, "EXOTIC_DIR", str(ex))
    monkeypatch.setattr(lb, "global_next_funding", {"BTCUSDT": 1})
    monkeypatch.setattr(lb, "_sync", None)
    sess = fake_binance(FakeSession(end=0))
    lb.process_symbol("NEWUSDT")
    assert any("klines" in url for url, _ in sess.calls)


def test_empty_premium_index_does_not_mark_everything_delisted(tmp_path, monkeypatch, fake_binance):
    raw = tmp_path / "raw"; ex = tmp_path / "ex"; raw.mkdir(); ex.mkdir()
    monkeypatch.setattr(lb, "RAW_DIR", str(raw)); monkeypatch.setattr(lb, "EXOTIC_DIR", str(ex))
    monkeypatch.setattr(lb, "global_next_funding", {})
    monkeypatch.setattr(lb, "_sync", None)
    fake_binance(FakeSession(end=0))
    assert lb.process_symbol("ANYUSDT")[1] != "delisted"


# ------------------------------------------------------------ static site
def test_patched_html_points_at_static_files():
    from momentum_v10.site_export import HTML_SRC, patched_html
    html = patched_html(HTML_SRC.read_text(encoding="utf-8"))
    assert "/api/" not in html
    assert "data/${currentMode}.json" in html and "data/asset_dna.json" in html
    assert 'name="robots" content="noindex' in html
    assert "setInterval(loadData, 60000)" in html


def test_clean_makes_strict_json():
    import json, numpy as np
    from momentum_v10.site_export import _clean
    out = json.dumps(_clean({"a": float("nan"), "b": np.float64(1.5), "c": [np.int64(2), float("inf")]}), allow_nan=False)
    assert json.loads(out) == {"a": None, "b": 1.5, "c": [2, None]}


def test_publish_site_uploads_with_content_types(aws, monkeypatch, tmp_path):
    import boto3
    ops, data = aws
    import momentum_v10.site_export as se
    site = tmp_path / "site"
    (site / "data").mkdir(parents=True)
    monkeypatch.setattr(se, "SITE_DIR", site)
    def fake_export():
        (site / "index.html").write_text("<html></html>")
        (site / "data" / "open.json").write_text("{}")
        return {"generated_utc": "x"}
    monkeypatch.setattr(se, "export_site", fake_export)
    r = ops.publish_site()
    assert r["files"] == 2
    s3 = boto3.client("s3", region_name="eu-west-2")
    h = s3.head_object(Bucket="v10-test", Key="site/index.html")
    assert h["ContentType"].startswith("text/html") and h["CacheControl"] == "max-age=300"
    assert s3.head_object(Bucket="v10-test", Key="site/data/open.json")["ContentType"] == "application/json"


# ------------------------------------------------------------ new signals
def test_effective_stop_per_engine():
    from momentum_v10.live_runner import effective_stop
    base = {"entry_price": 100.0, "hard_stop": 97.0, "trade_max_high": 100.0}
    assert effective_stop({**base, "engine": "IGNITION"}) == 97.0
    assert effective_stop({**base, "engine": "PHOENIX_CONTINUATION"}) == 97.0
    assert effective_stop({**base, "engine": "CONTINUATION", "donchian_stop": 99.0}) == 99.0
    assert effective_stop({**base, "engine": "SQUEEZE_IGN", "hard_stop": 80.0}) == 80.0
    assert effective_stop({**base, "engine": "RETAIL_SQZ", "trade_max_high": 140.0}) == 105.0  # 25% trail


def test_active_record_has_current_price_stop_and_age():
    from momentum_v10.live_runner import active_trade_record
    t = {"engine": "IGNITION", "entry_time": "2026-09-26T10:00:00", "entry_price": 100.0,
         "hard_stop": 95.0, "trade_max_high": 110.0, "trade_min_low": 98.0}
    r = active_trade_record("ABC", t, 104.0, now=pd.Timestamp("2026-09-26 16:05"))
    assert r["current_price"] == 104.0 and r["stop"] == 95.0
    assert abs(r["stop_pct"] - (95 - 104) / 104) < 1e-12
    assert abs(r["duration_hours"] - 6.0833) < 1e-3


def test_new_signals_window_and_order():
    from momentum_v10.live_book import new_signals
    df = pd.DataFrame([
        {"asset": "OLD", "engine": "IGNITION", "entry": "2026-09-20T10:00:00", "entry_price": 1, "pnl": 0.1},
        {"asset": "A", "engine": "IGNITION", "entry": "2026-09-26T08:00:00", "entry_price": 1, "pnl": 0.02,
         "current_price": 1.02, "stop": 0.95, "stop_pct": -0.0686},
        {"asset": "B", "engine": "CONTINUATION", "entry": "2026-09-26T15:00:00", "entry_price": 2, "pnl": float("nan")},
        {"asset": "C", "engine": "IGNITION", "entry": "2026-09-26T14:00:00", "entry_price": 1, "pnl": 0.0, "reason": "open_at_end"},
    ])
    out = new_signals(df, now=pd.Timestamp("2026-09-26 16:05"))
    assert [s["asset"] for s in out] == ["B", "A"]
    assert out[1]["stop_pct"] == -6.86 and out[1]["pnl_pct"] == 2.0 and out[0]["pnl_pct"] is None
    assert out[0]["age_hours"] == 1.1


def test_email_lists_new_signals():
    from momentum_v10.hourly_job import render_report
    subject, body = render_report({"ok": True, "open": 5, "closed": 9, "closed_this_hour": 0, "new_signals": [
        {"asset": "SOON", "engine": "IGNITION", "entry": "2026-09-26 17:00", "entry_price": 0.2206,
         "current_price": 0.2266, "stop": 0.2150, "stop_pct": -5.1, "pnl_pct": 2.7, "age_hours": 1.1},
        {"asset": "CC", "engine": "IGNITION", "entry": "2026-09-24 19:00", "entry_price": 0.1145,
         "current_price": 0.1325, "stop": 0.1090, "stop_pct": -17.7, "pnl_pct": 15.7, "age_hours": 23.0}]})
    assert subject.endswith(", 1 new signal")
    assert "New signals (last 24h): 2" in body and "* SOON" in body and "  CC" in body and "-5.1%" in body


def test_dashboard_payload_has_signals_and_real_current_price(tmp_path, monkeypatch):
    from momentum_v10 import dashboard_server as ds
    now = pd.Timestamp.now(tz="UTC").tz_localize(None).floor("h")
    open_csv = tmp_path / "open_trades.csv"; all_csv = tmp_path / "all_trades.csv"
    pd.DataFrame([{"asset": "NEW", "engine": "IGNITION", "entry": (now - pd.Timedelta(hours=2)).isoformat(),
                   "entry_price": 1.0, "pnl": 0.05, "mfe": 0.06, "mae": -0.01, "current_price": 1.05,
                   "stop": 0.97, "stop_pct": -0.0762, "duration_hours": 2.0}]).to_csv(open_csv, index=False)
    monkeypatch.setattr(ds, "OPEN_CSV", open_csv); monkeypatch.setattr(ds, "ALL_CSV", all_csv)
    ds._DATA_CACHE.update({"open_mtime": 0, "open_df": None, "all_mtime": 0, "all_df": None})
    payload = ds.build_api_response("open")
    assert payload["new_signals"][0]["asset"] == "NEW"
    pos = payload["open_positions"][0]
    assert pos["current_px"] == 1.05 and pos["stop"] == 0.97 and pos["duration"] == "2h"
