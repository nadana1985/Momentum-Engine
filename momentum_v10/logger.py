"""
momentum_v10/logger.py — Centralized Production Logging Architecture for Kronos V10.

Provides hierarchical sub-loggers under the root 'kronos' namespace:
  - kronos.ingest        : Binance REST API, rate limits, gap detection, sync state
  - kronos.data_quality   : Parquet file integrity, corruption detection, quarantining
  - kronos.engine        : Multi-process execution, batch progress, compute performance
  - kronos.trades        : Immutable trade audit ledger (signals, entries, exits, PnL)
  - kronos.system        : Host telemetry, disk space, timers, AWS SES notifications

Handlers:
  1. Console (sys.stdout) - Clean timestamped logs for systemd/journalctl
  2. logs/v10_engine.log  - Rotating file log (10 MB, 5 backups)
  3. logs/v10_errors.log  - Filtered file log (WARNING & ERROR only, 5 MB, 3 backups)
  4. logs/v10_trades.log  - Append-only trade audit log
"""
from __future__ import annotations

import logging
import os
import shutil
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LOG_DIR = ROOT / "logs"

_INITIALIZED = False


class TradeLogFilter(logging.Filter):
    """Filter that only permits records with attribute is_trade=True or from kronos.trades."""
    def filter(self, record: logging.LogRecord) -> bool:
        return getattr(record, "is_trade", False) or record.name.startswith("kronos.trades")


class SafeStreamHandler(logging.StreamHandler):
    """StreamHandler that ensures Unicode characters don't crash Windows charmap consoles."""
    def emit(self, record: logging.LogRecord) -> None:
        try:
            super().emit(record)
        except UnicodeEncodeError:
            try:
                msg = self.format(record)
                encoding = getattr(self.stream, "encoding", "utf-8") or "utf-8"
                safe_msg = msg.encode(encoding, errors="replace").decode(encoding)
                self.stream.write(safe_msg + self.terminator)
                self.flush()
            except Exception:
                self.handleError(record)


def init_logging(log_dir: Path | str | None = None) -> None:
    """Initialize root 'kronos' logger with rotating files, trade audit, and console handlers."""
    global _INITIALIZED
    if _INITIALIZED:
        return

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(errors="replace")
        except Exception:
            pass

    log_path = Path(log_dir) if log_dir is not None else DEFAULT_LOG_DIR
    log_path.mkdir(parents=True, exist_ok=True)

    root_logger = logging.getLogger("kronos")
    root_logger.setLevel(logging.DEBUG)
    root_logger.propagate = False

    # Standard log format
    standard_formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-7s | [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Clean audit format for trades
    trade_formatter = logging.Formatter(
        fmt="%(asctime)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # 1. Console Handler (INFO+)
    console_handler = SafeStreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(standard_formatter)
    root_logger.addHandler(console_handler)

    # 2. General Rotating File Handler (DEBUG+)
    engine_file = log_path / "v10_engine.log"
    engine_handler = RotatingFileHandler(
        engine_file, maxBytes=10 * 1024 * 1024, backupCount=5, encoding="utf-8"
    )
    engine_handler.setLevel(logging.DEBUG)
    engine_handler.setFormatter(standard_formatter)
    root_logger.addHandler(engine_handler)

    # 3. Errors-Only Rotating File Handler (WARNING+)
    error_file = log_path / "v10_errors.log"
    error_handler = RotatingFileHandler(
        error_file, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
    )
    error_handler.setLevel(logging.WARNING)
    error_handler.setFormatter(standard_formatter)
    root_logger.addHandler(error_handler)

    # 4. Dedicated Trade Audit File Handler
    trades_file = log_path / "v10_trades.log"
    trades_handler = RotatingFileHandler(
        trades_file, maxBytes=20 * 1024 * 1024, backupCount=10, encoding="utf-8"
    )
    trades_handler.setLevel(logging.INFO)
    trades_handler.setFormatter(trade_formatter)
    trades_handler.addFilter(TradeLogFilter())
    root_logger.addHandler(trades_handler)

    _INITIALIZED = True


def get_logger(subsystem: str = "engine") -> logging.Logger:
    """Return a logger configured under the kronos namespace."""
    if not _INITIALIZED:
        init_logging()
    name = f"kronos.{subsystem}" if not subsystem.startswith("kronos") else subsystem
    return logging.getLogger(name)


# ---------------------------------------------------------------------------
# Utility Diagnostics & Self-Healing
# ---------------------------------------------------------------------------

def check_disk_space(path: Path | str | None = None, min_free_gb: float = 5.0, min_free_pct: float = 15.0) -> dict:
    """
    Check available disk space on the volume hosting the specified path.
    Logs warnings or errors if space falls below safety thresholds.
    """
    check_dir = Path(path) if path is not None else ROOT
    logger = get_logger("system")
    try:
        total, used, free = shutil.disk_usage(check_dir)
        total_gb = total / (1024 ** 3)
        free_gb = free / (1024 ** 3)
        free_pct = (free / total) * 100.0

        stats = {
            "path": str(check_dir),
            "total_gb": round(total_gb, 2),
            "free_gb": round(free_gb, 2),
            "free_pct": round(free_pct, 1),
            "healthy": True,
        }

        if free_gb < (min_free_gb / 2.0) or free_pct < (min_free_pct / 2.0):
            stats["healthy"] = False
            logger.critical(
                f"[DISK CRITICAL] Free disk space dangerously low on {check_dir}: "
                f"{free_gb:.2f} GB ({free_pct:.1f}% free). Immediate action required!"
            )
        elif free_gb < min_free_gb or free_pct < min_free_pct:
            stats["healthy"] = False
            logger.warning(
                f"[DISK WARNING] Low disk space on {check_dir}: "
                f"{free_gb:.2f} GB ({free_pct:.1f}% free). Minimum threshold: {min_free_gb} GB ({min_free_pct}%)."
            )
        else:
            logger.debug(f"[DISK OK] {check_dir}: {free_gb:.2f} GB free ({free_pct:.1f}%).")

        return stats
    except Exception as e:
        logger.warning(f"Could not determine disk usage for {check_dir}: {e}")
        return {"path": str(check_dir), "healthy": True, "error": str(e)}


def quarantine_corrupted_shard(shard_path: Path | str, quarantine_dir: Path | str | None = None, reason: str = "") -> Path | None:
    """
    Safely move a corrupted Parquet shard to the quarantine directory so it does
    not crash subsequent batch runs, and can be cleanly backfilled.
    """
    src = Path(shard_path)
    if not src.exists():
        return None

    q_dir = Path(quarantine_dir) if quarantine_dir is not None else ROOT / "data" / "quarantine"
    q_dir.mkdir(parents=True, exist_ok=True)

    dest = q_dir / f"{src.stem}_{int(os.path.getmtime(src))}{src.suffix}.corrupt"
    logger = get_logger("data_quality")
    try:
        shutil.move(str(src), str(dest))
        logger.error(
            f"[QUARANTINE] Corrupted shard isolated: {src.name} -> {dest.name} | Reason: {reason or 'Unreadable'}"
        )
        return dest
    except Exception as e:
        logger.critical(f"[QUARANTINE FAILED] Could not move corrupted shard {src}: {e}")
        return None
