#!/usr/bin/env python3
"""
Kronos Real-Time Momentum & Climax Exhaustion Alert Engine
Monitors active momentum runners across the 6 Climax Signatures,
BTR Air-Pocket Fragility, and Small-Runner Velocity Stalls.

Supported Dispatch Channels:
  1. Console Banner + Audio Beep (Terminal alert)
  2. Discord Webhook (Rich Embed notifications)
  3. Telegram Bot (Instant push notifications)
  4. Persistent JSONL Ledger (reports/alerts/climax_alerts.jsonl)

Usage:
  # 1. Audit active position / watchlist once:
  python scripts/alert_climax_scanner.py --watchlist "MAGIC,OGN,ERA,CTSI,RLC,SUPER"

  # 2. Continuous real-time daemon (checks every 5 minutes):
  python scripts/alert_climax_scanner.py --watchlist "MAGIC,OGN,ERA" --daemon --interval 300

  # 3. Full universe scan for active blow-offs:
  python scripts/alert_climax_scanner.py --scan

  # 4. With Discord/Telegram notifications:
  # Set DISCORD_WEBHOOK_URL or TELEGRAM_BOT_TOKEN & TELEGRAM_CHAT_ID in environment
"""

import os
import sys
import time
import json
import argparse
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime, timezone

# Windows terminal encoding fix
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from scan_climax_exits import evaluate_exit_signature, resolve_symbol_shards

ALERT_DIR = ROOT / "reports" / "alerts"
ALERT_DIR.mkdir(parents=True, exist_ok=True)
CACHE_FILE = ALERT_DIR / ".alert_cache.json"
LOG_FILE = ALERT_DIR / "climax_alerts.jsonl"


def load_alert_cache():
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_alert_cache(cache):
    try:
        with open(CACHE_FILE, "w") as f:
            json.dump(cache, f, indent=2)
    except Exception:
        pass


def append_alert_log(record):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(record) + "\n")
    except Exception:
        pass


def send_discord_alert(webhook_url, alert_data):
    """Dispatches a rich embed to Discord webhook."""
    if not webhook_url:
        return False
    try:
        severity = alert_data['severity']
        color = 0xFF0000 if severity == "CRITICAL_EXIT" else (0xFFA500 if severity == "RATCHET_STOP" else 0xFFFF00)
        
        embed = {
            "title": f"🚨 {alert_data['severity']}: {alert_data['symbol']}/USDT",
            "description": f"**Decision:** `{alert_data['action']}`\n**Urgency Score:** `{alert_data['exit_score']}/100` | **Alarms:** `{alert_data['alarm_count']}/6`",
            "color": color,
            "fields": [
                {"name": "Current Price", "value": f"${alert_data['current_price']:.5f} ({alert_data['ret_24h_pct']:+.1f}% 24h)", "inline": True},
                {"name": "72h Extension", "value": f"+{alert_data['gain_from_72h_low_pct']:.1f}%", "inline": True},
                {"name": "Upper Wick", "value": f"{alert_data['upper_wick_pct']:.1f}%", "inline": True},
                {"name": "Token OI Div", "value": f"{alert_data['oi_div_pct']:+.1f}%", "inline": True},
                {"name": "Funding Rate", "value": f"{alert_data['funding_rate']*100:+.4f}%", "inline": True},
                {"name": "Trailing Stop", "value": f"${alert_data['bar1_cushion_stop']:.5f}", "inline": True},
            ],
            "footer": {"text": f"Kronos Climax Scanner • {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}"}
        }
        payload = json.dumps({"embeds": [embed]}).encode('utf-8')
        req = urllib.request.Request(webhook_url, data=payload, headers={'Content-Type': 'application/json', 'User-Agent': 'KronosAlertEngine/1.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status in (200, 204)
    except Exception as e:
        print(f"  [DISCORD ERROR] Failed to send webhook: {e}")
        return False


def send_telegram_alert(bot_token, chat_id, alert_data):
    """Dispatches formatted message to Telegram Bot."""
    if not bot_token or not chat_id:
        return False
    try:
        emoji = "🔴" if alert_data['severity'] == "CRITICAL_EXIT" else ("🟡" if alert_data['severity'] == "RATCHET_STOP" else "⚡")
        msg = (
            f"{emoji} *KRONOS CLIMAX ALERT: {alert_data['symbol']}*\n\n"
            f"*Action:* `{alert_data['action']}`\n"
            f"*Urgency Score:* `{alert_data['exit_score']}/100` | *Alarms:* `{alert_data['alarm_count']}/6`\n"
            f"*Price:* `${alert_data['current_price']:.5f}` ({alert_data['ret_24h_pct']:+.1f}% 24h)\n"
            f"*72h Run:* `+{alert_data['gain_from_72h_low_pct']:.1f}%`\n"
            f"*Upper Wick:* `{alert_data['upper_wick_pct']:.1f}%`\n"
            f"*Token OI Bleed:* `{alert_data['oi_div_pct']:+.1f}%`\n"
            f"*Funding APR:* `{alert_data['funding_rate']*1095*100:+.1f}%`\n"
            f"*Dynamic Stop:* `${alert_data['bar1_cushion_stop']:.5f}`\n\n"
            f"⏱ `{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}`"
        )
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = json.dumps({"chat_id": chat_id, "text": msg, "parse_mode": "Markdown"}).encode('utf-8')
        req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status == 200
    except Exception as e:
        print(f"  [TELEGRAM ERROR] Failed to send alert: {e}")
        return False


def classify_alert_severity(res):
    """Classifies runner state into severity levels."""
    score = res['exit_score']
    alarms = res['alarm_count']
    oi_div = res['oi_div_pct']
    wick = res['upper_wick_pct']
    gain = res['gain_from_72h_low_pct']

    # 1. Critical Exit (100% Climax Take Profit / Terminal Unwind)
    if score >= 55 or alarms >= 3 or (gain >= 25.0 and oi_div <= -15.0):
        return "CRITICAL_EXIT"

    # 2. Ratchet Stop / Defense Alert (Approaching climax or multi-alarm breakdown)
    if score >= 35 or alarms >= 2:
        return "RATCHET_STOP"

    # 3. Small Runner Velocity Stall (Air-Pocket Rejection)
    # Gains +3% to +25% AND prints severe >=60% upper wick rejection or stall
    if (3.0 <= gain <= 25.0) and wick >= 60.0 and (res['vol_div_pct'] <= -35.0 or oi_div <= -5.0):
        return "MICRO_STALL"

    # 4. Squeeze Fuel Intact (Holding Dip)
    if gain >= 15.0:
        return "HOLD_RUNNER"

    return "NEUTRAL"


def trigger_alert(res, discord_url=None, tg_token=None, tg_chat=None, cache=None, sound=True):
    sym = res['symbol']
    severity = classify_alert_severity(res)
    
    # Check deduplication
    now_ts = time.time()
    if cache is not None:
        last_entry = cache.get(sym)
        if last_entry:
            last_sev = last_entry.get('severity')
            last_time = last_entry.get('time', 0)
            # Re-alert only if severity escalated or at least 3 hours passed
            if last_sev == severity and (now_ts - last_time) < 10800:
                return False

    res['severity'] = severity
    res['alert_time'] = datetime.now(timezone.utc).isoformat()

    # Audio alert on Windows
    if sound and severity in ("CRITICAL_EXIT", "MICRO_STALL", "RATCHET_STOP"):
        try:
            if sys.platform == 'win32':
                import winsound
                freq = 1000 if severity == "CRITICAL_EXIT" else 750
                winsound.Beep(freq, 350)
            else:
                sys.stdout.write('\a')
                sys.stdout.flush()
        except Exception:
            pass

    # Print Visual Banner
    tag = "🔴 [CRITICAL HARVEST 100%]" if severity == "CRITICAL_EXIT" else ("⚡ [MICRO RUNNER STALL]" if severity == "MICRO_STALL" else "🟡 [RATCHET STOP DEFENSE]")
    print("\n" + "#" * 96)
    print(f"  {tag} {sym}/USDT — {res['action']}")
    print(f"  Exit Score: {res['exit_score']}/100 | Alarms: {res['alarm_count']}/6 | Upper Wick: {res['upper_wick_pct']:.1f}%")
    print(f"  Price: ${res['current_price']:.5f} | 72h Run: +{res['gain_from_72h_low_pct']:.1f}% | Token OI Bleed: {res['oi_div_pct']:+.1f}%")
    print(f"  Dynamic Stop Floor: ${res['bar1_cushion_stop']:.5f} | 24h VWAP: ${res['vwap_24h']:.5f}")
    print("#" * 96 + "\n")

    # Dispatch webhooks
    if discord_url:
        send_discord_alert(discord_url, res)
    if tg_token and tg_chat:
        send_telegram_alert(tg_token, tg_chat, res)

    # Log to persistent ledger
    append_alert_log({
        'timestamp': res['alert_time'],
        'symbol': sym,
        'severity': severity,
        'action': res['action'],
        'score': res['exit_score'],
        'alarms': res['alarm_count'],
        'price': res['current_price'],
        'gain_72h': res['gain_from_72h_low_pct'],
        'upper_wick': res['upper_wick_pct'],
        'oi_div': res['oi_div_pct'],
        'stop_floor': res['bar1_cushion_stop']
    })

    # Update cache
    if cache is not None:
        cache[sym] = {'severity': severity, 'time': now_ts, 'score': res['exit_score']}
        save_alert_cache(cache)

    return True


def audit_symbols(symbols, discord_url, tg_token, tg_chat, cache, sound):
    alerts_fired = 0
    for s in symbols:
        res, err = evaluate_exit_signature(s)
        if res:
            sev = classify_alert_severity(res)
            if sev in ("CRITICAL_EXIT", "MICRO_STALL", "RATCHET_STOP"):
                fired = trigger_alert(res, discord_url, tg_token, tg_chat, cache, sound)
                if fired:
                    alerts_fired += 1
            else:
                print(f"  [{s}] Score {res['exit_score']:>2}/100 | Alarms {res['alarm_count']}/6 | {res['action']:<35} (OK)")
    return alerts_fired


def main():
    parser = argparse.ArgumentParser(description="Kronos Real-Time Momentum & Climax Alert Engine")
    parser.add_argument("--watchlist", type=str, help="Comma-separated active tickers to monitor (e.g. 'MAGIC,OGN,ERA,CTSI,RLC')")
    parser.add_argument("--scan", action="store_true", help="Scan entire liquid universe for active runners")
    parser.add_argument("--daemon", action="store_true", help="Run continuously on a recurring timer")
    parser.add_argument("--interval", type=int, default=300, help="Poll interval in seconds for daemon (default: 300s = 5m)")
    parser.add_argument("--discord", type=str, default=os.environ.get("DISCORD_WEBHOOK_URL"), help="Discord Webhook URL")
    parser.add_argument("--tg-token", type=str, default=os.environ.get("TELEGRAM_BOT_TOKEN"), help="Telegram Bot Token")
    parser.add_argument("--tg-chat", type=str, default=os.environ.get("TELEGRAM_CHAT_ID"), help="Telegram Chat ID")
    parser.add_argument("--no-sound", action="store_true", help="Disable audio beeps on alert")
    args = parser.parse_args()

    cache = load_alert_cache()
    sound = not args.no_sound

    if args.watchlist:
        symbols = [s.strip() for s in args.watchlist.split(",") if s.strip()]
    elif args.scan:
        import glob
        raw_files = glob.glob("data/raw_shards/*_USDT_1h.parquet")
        if not raw_files:
            raw_files = glob.glob("data/raw_shards/*_1h.parquet")
        symbols = [os.path.basename(f).split('_')[0] for f in raw_files]
    else:
        # Default active watchlist if none specified
        symbols = ["MAGIC", "OGN", "ERA", "CTSI", "RLC", "SUPER", "C", "A", "PHAROS"]
        print(f"[INFO] No watchlist specified. Monitoring default active cohort: {symbols}")

    print(f"\n==========================================================================")
    print(f"  KRONOS MOMENTUM & CLIMAX ALERT ENGINE")
    print(f"  Monitoring {len(symbols)} assets | Audio: {'ON' if sound else 'OFF'}")
    print(f"  Discord: {'CONNECTED' if args.discord else 'NONE'} | Telegram: {'CONNECTED' if (args.tg_token and args.tg_chat) else 'NONE'}")
    print(f"==========================================================================\n")

    if args.daemon:
        print(f"[DAEMON] Running continuously every {args.interval} seconds (Press Ctrl+C to stop)...")
        iteration = 1
        while True:
            t_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            print(f"\n[{t_now}] Cycle #{iteration}: Checking {len(symbols)} tickers...")
            n_fired = audit_symbols(symbols, args.discord, args.tg_token, args.tg_chat, cache, sound)
            print(f"[{t_now}] Cycle #{iteration} complete: {n_fired} new alerts fired.")
            iteration += 1
            time.sleep(args.interval)
    else:
        n_fired = audit_symbols(symbols, args.discord, args.tg_token, args.tg_chat, cache, sound)
        print(f"\n[DONE] Scan complete: {n_fired} alerts dispatched. Ledger: {LOG_FILE}\n")


if __name__ == "__main__":
    main()
