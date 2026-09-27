#!/bin/bash
# Runs ON the EC2 instance as root. Installs/updates the code from S3.
#   bash refresh.sh            wait for any running hourly job, then update
# Reads BUCKET and REGION from /etc/v10/deploy.conf (written by bootstrap).
set -euo pipefail

# shellcheck source=/dev/null
. /etc/v10/deploy.conf
CODE=/opt/v10_standalone
VENV=/opt/v10_venv
NEW="${CODE}.new"
TGZ=/tmp/v10-release.tar.gz

log() { echo "[refresh $(date -u +%H:%M:%S)] $*"; }

# 1. Never swap code under a running job (max ~55 min wait).
for _ in $(seq 1 330); do
  systemctl is-active --quiet v10-hourly.service || break
  sleep 10
done

# 2. Fetch and unpack the release.
aws s3 cp --only-show-errors --region "$REGION" "s3://${BUCKET}/releases/current.tar.gz" "$TGZ"
rm -rf "$NEW"
mkdir -p "$NEW"
tar -xzf "$TGZ" -C "$NEW"
rm -f "$TGZ"

# 3. Python environment: rebuild only when requirements change.
REQ_SHA=$(sha256sum "$NEW/requirements.txt" | cut -d' ' -f1)
if [ ! -x "$VENV/bin/python" ] || [ "$(cat "$VENV/.req.sha256" 2>/dev/null || true)" != "$REQ_SHA" ]; then
  log "building virtualenv"
  rm -rf "$VENV"
  python3.11 -m venv "$VENV"
  "$VENV/bin/pip" install --quiet --upgrade pip
  "$VENV/bin/pip" install --quiet --only-binary=:all: -r "$NEW/requirements.txt"
  echo "$REQ_SHA" > "$VENV/.req.sha256"
fi

# 4. Swap code in; logs live outside the code tree.
rm -rf "$NEW/logs"
ln -s /var/log/v10 "$NEW/logs"
chown -R root:root "$NEW"
# Files packed on a Mac may be 0600; the v10 service user must be able to read them.
chmod -R u=rwX,go=rX "$NEW"
rm -rf "${CODE}.prev"
if [ -d "$CODE" ]; then mv "$CODE" "${CODE}.prev"; fi
mv "$NEW" "$CODE"

# 5. Units.
install -m 0644 "$CODE/deploy/v10-hourly.service" /etc/systemd/system/v10-hourly.service
install -m 0644 "$CODE/deploy/v10-hourly.timer" /etc/systemd/system/v10-hourly.timer
systemctl daemon-reload
systemctl enable --now v10-hourly.timer >/dev/null

# 6. Smoke test: imports resolve with the installed environment.
runuser -u v10 -- env HOME=/var/lib/v10 NUMBA_CACHE_DIR=/var/lib/v10/numba-cache PYTHONDONTWRITEBYTECODE=1 \
  bash -c "cd $CODE && $VENV/bin/python -c 'import momentum_v10.hourly_job, config.ingestion.live_bridger, momentum_v10.ops'"
log "release installed: $(date -u -r "$CODE/momentum_v10/hourly_job.py" '+%F %T') ; next run: $(systemctl list-timers v10-hourly.timer --no-legend | awk '{print $1, $2, $3}')"
