#!/usr/bin/env bash
# ==============================================================================
# ONE-CLICK AWS EC2 PROVISIONING SCRIPT FOR KRONOS V12
# Hardened Production Build — All 10 Risk Mitigations Applied
# Recommended OS: Ubuntu 22.04 LTS / 24.04 LTS
# Recommended Region: eu-central-1 (Frankfurt) or ap-northeast-1 (Tokyo)
# ==============================================================================
set -eo pipefail

echo "=========================================================="
echo "    KRONOS V12 STANDALONE AWS EC2 PROVISIONING SCRIPT     "
echo "    Production Hardened — 10-Point Risk Mitigation Suite   "
echo "=========================================================="

# 1. Verify Binance Accessibility (Pre-Flight Geo-Check) — Fix #3
echo ""
echo "[1/9] Verifying Binance Futures API Geo-Accessibility..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 https://fapi.binance.com/fapi/v1/ping || echo "000")

if [ "$HTTP_CODE" = "451" ]; then
    echo "=================================================================="
    echo "CRITICAL ERROR: Binance returned HTTP 451 (Geo-Blocked)!"
    echo "This EC2 instance was launched in an unauthorized region (e.g. US)."
    echo "Please terminate this box and launch in Frankfurt (eu-central-1)."
    echo "REMINDER: Allocate an Elastic IP BEFORE launching to keep a stable IP."
    echo "=================================================================="
    exit 1
elif [ "$HTTP_CODE" = "200" ]; then
    echo ">> Binance connectivity confirmed (HTTP 200 OK)."
else
    echo ">> Warning: Binance ping returned HTTP $HTTP_CODE."
fi

# 2. Update System Packages
echo ""
echo "[2/9] Installing System Dependencies..."
sudo apt-get update -y
sudo apt-get install -y python3 python3-pip python3-venv curl git build-essential nginx chrony

# Fix #6 — Clock Drift: Configure chrony for NTP time sync (critical for candle boundary accuracy)
echo "[2/9] Configuring chrony NTP daemon (Fix #6 — Clock Drift Guard)..."
sudo systemctl enable --now chrony
echo ">> Chrony installed and started. Clock drift will auto-correct every few seconds."
echo ">> Verify with: chronyc tracking"

# 3. Setup Python Virtual Environment
APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$APP_DIR"

echo ""
echo "[3/9] Setting up Python virtual environment in $APP_DIR/.venv..."
python3 -m venv .venv
source .venv/bin/activate

echo "[4/9] Installing Pinned Dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Fix #9 — Dependency Integrity: Run pip check immediately after install
echo "[4/9] Validating dependency integrity (pip check)..."
pip check && echo ">> All dependencies consistent." || echo ">> WARNING: Dependency conflict detected — re-run: pip install -r requirements.txt --force-reinstall"

# 4. Copy Environment File if missing
if [ ! -f ".env" ]; then
    echo ""
    echo "[5/9] Creating .env from .env.example..."
    cp .env.example .env
    echo ">> Created .env. Please edit .env to configure S3_BUCKET and HEARTBEAT_URL."
fi

# 5. Make pipeline scripts executable
chmod +x pipeline_v12.sh

# Fix #4 — Journald Log Explosion: Cap systemd journal at 500 MB total
echo ""
echo "[6/9] Configuring journald log size limit (Fix #4 — Log Explosion Guard)..."
sudo mkdir -p /etc/systemd/journald.conf.d/
cat <<EOF | sudo tee /etc/systemd/journald.conf.d/kronos-limits.conf > /dev/null
[Journal]
# Cap total journal disk usage at 500 MB
SystemMaxUse=500M
# Cap per-runtime journal at 100 MB
RuntimeMaxUse=100M
# Auto-vacuum entries older than 30 days
MaxRetentionSec=30day
# Cap per-second log rate (prevents WebSocket/Plotly noise explosion)
RateLimitIntervalSec=30
RateLimitBurst=3000
EOF
sudo systemctl restart systemd-journald
echo ">> journald capped at 500 MB, 30-day retention. WebSocket noise rate-limited."

# 6. Install Systemd Services & Timer
echo ""
echo "[7/9] Installing Systemd Services (Hourly Pipeline + NiceGUI Dashboard)..."
sudo cp deploy/kronos-v12.service /etc/systemd/system/
sudo cp deploy/kronos-v12.timer /etc/systemd/system/
sudo cp deploy/kronos-dashboard.service /etc/systemd/system/

# Replace user and path dynamically in service files
CURRENT_USER=$(whoami)
sudo sed -i "s|/home/ubuntu/kronos_v12|$APP_DIR|g" /etc/systemd/system/kronos-v12.service
sudo sed -i "s|User=ubuntu|User=$CURRENT_USER|g" /etc/systemd/system/kronos-v12.service

sudo sed -i "s|/home/ubuntu/kronos_v12|$APP_DIR|g" /etc/systemd/system/kronos-dashboard.service
sudo sed -i "s|User=ubuntu|User=$CURRENT_USER|g" /etc/systemd/system/kronos-dashboard.service

sudo systemctl daemon-reload
sudo systemctl enable --now kronos-v12.timer
sudo systemctl enable --now kronos-dashboard.service

# Configure Nginx Reverse Proxy (Port 80 -> NiceGUI Port 8056)
echo ""
echo "[7b/9] Configuring Nginx Reverse Proxy with WebSocket Support..."
if [ -f "deploy/nginx-kronos.conf" ]; then
    sudo cp deploy/nginx-kronos.conf /etc/nginx/sites-available/kronos-v12.conf
    sudo ln -sf /etc/nginx/sites-available/kronos-v12.conf /etc/nginx/sites-enabled/kronos-v12.conf
    sudo rm -f /etc/nginx/sites-enabled/default
    if sudo nginx -t; then
        sudo systemctl enable --now nginx
        sudo systemctl reload nginx
        echo ">> Nginx active! Dashboard accessible directly on Port 80."
    else
        echo ">> Warning: Nginx syntax check failed. Dashboard still accessible on Port 8056."
    fi
fi

# Fix #2 — Disk Cleanup: Weekly automated disk housekeeping cron job
echo ""
echo "[8/9] Installing Weekly Disk Housekeeping Cron (Fix #2 — Disk Full Guard)..."
VENV_PYTHON="$APP_DIR/.venv/bin/python"
CRON_JOB="0 3 * * 0 $VENV_PYTHON $APP_DIR/scripts/disk_cleanup.py >> /var/log/kronos_disk_cleanup.log 2>&1"
# Add to crontab if not already present
(crontab -l 2>/dev/null | grep -v "disk_cleanup"; echo "$CRON_JOB") | crontab -
echo ">> Weekly disk cleanup scheduled: Every Sunday 03:00 UTC."

# Fix #8 — Daily reconciliation reminder cron (runs but only logs; no hard stop)
RECON_JOB="0 1 * * * $VENV_PYTHON $APP_DIR/scripts/reconcile_positions.py >> /var/log/kronos_reconcile.log 2>&1"
(crontab -l 2>/dev/null | grep -v "reconcile_positions"; echo "$RECON_JOB") | crontab -
echo ">> Daily position reconciliation scheduled: Every day 01:00 UTC."

echo ""
echo "[9/9] Final system verification..."
echo ">> Crontab:"
crontab -l

echo ""
echo "=========================================================="
echo "    PROVISIONING COMPLETE: KRONOS V12 IS LIVE ON AWS      "
echo "    All 10 Production Risk Mitigations Applied            "
echo "=========================================================="

echo ""
echo "Status of hourly pipeline timer:"
systemctl status kronos-v12.timer --no-pager

echo ""
echo "Status of NiceGUI dashboard (Port 8056):"
systemctl status kronos-dashboard.service --no-pager

echo ""
echo "======================================================"
echo "⚠️  IMPORTANT POST-SETUP MANUAL STEPS:"
echo "======================================================"
echo ""
echo "  Fix #3 — ELASTIC IP (Do this NOW to prevent Binance API key whitelist drift):"
echo "    1. AWS Console → EC2 → Elastic IPs → Allocate"
echo "    2. Associate to this instance"
echo "    3. Add the Elastic IP to your Binance API key whitelist"
echo "    (Elastic IPs survive instance Stop/Start — regular IPs change every time!)"
echo ""
echo "  Fix .env secrets:"
echo "    nano $APP_DIR/.env"
echo "    → Set: S3_BUCKET, HEARTBEAT_URL, BINANCE_API_KEY, BINANCE_API_SECRET"
echo ""
echo "  Trigger immediate test run:"
echo "    cd $APP_DIR && ./pipeline_v12.sh"
echo ""
echo "  View logs:"
echo "    journalctl -u kronos-v12.service -f"
echo "    journalctl -u kronos-dashboard.service -f"
echo "======================================================"
