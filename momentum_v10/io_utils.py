"""Small production helpers: atomic file writes, a thread-safe rate limiter,
and a single-run lock.

Atomic writes: every file is written to a temporary sibling, flushed to disk,
then swapped in with os.replace. A crash mid-write leaves the previous file
intact instead of a truncated shard (which the ingest layer would quarantine,
silently dropping the asset from the universe).
"""
from __future__ import annotations

import errno
import os
import tempfile
import threading
import time
from contextlib import contextmanager
from pathlib import Path

import pandas as pd


def _atomic_write(path, writer) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    os.close(fd)
    try:
        writer(tmp)
        with open(tmp, "rb+") as fh:
            os.fsync(fh.fileno())
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def atomic_to_parquet(df: pd.DataFrame, path, **kwargs) -> None:
    kwargs.setdefault("index", False)
    _atomic_write(path, lambda tmp: df.to_parquet(tmp, **kwargs))


def atomic_to_csv(df: pd.DataFrame, path, **kwargs) -> None:
    kwargs.setdefault("index", False)
    _atomic_write(path, lambda tmp: df.to_csv(tmp, **kwargs))


def atomic_write_text(path, text: str, encoding: str = "utf-8") -> None:
    def _w(tmp):
        with open(tmp, "w", encoding=encoding) as fh:
            fh.write(text)
    _atomic_write(path, _w)


class RateLimiter:
    """Evenly spaced, thread-safe request pacing (calls per second)."""

    def __init__(self, rate_per_sec: float):
        self.interval = 1.0 / float(rate_per_sec) if rate_per_sec > 0 else 0.0
        self._lock = threading.Lock()
        self._next = 0.0

    def acquire(self) -> None:
        if self.interval <= 0:
            return
        with self._lock:
            now = time.monotonic()
            slot = max(now, self._next)
            self._next = slot + self.interval
        delay = slot - time.monotonic()
        if delay > 0:
            time.sleep(delay)


class RunLockedError(RuntimeError):
    pass


@contextmanager
def run_lock(path):
    """Exclusive non-blocking lock so two hourly runs never overlap."""
    import fcntl

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fh = open(path, "w")
    try:
        try:
            fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as e:
            if e.errno in (errno.EAGAIN, errno.EACCES):
                raise RunLockedError(f"another run holds {path}") from e
            raise
        fh.write(str(os.getpid()))
        fh.flush()
        yield
    finally:
        try:
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
        except OSError:
            pass
        fh.close()
