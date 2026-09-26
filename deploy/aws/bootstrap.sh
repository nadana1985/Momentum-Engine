#!/bin/bash
# EC2 user-data (first boot, runs as root). deploy.sh fills in the
# __PLACEHOLDERS__ before launching the instance.
set -euxo pipefail
exec > >(tee -a /var/log/v10-bootstrap.log) 2>&1

BUCKET="__BUCKET__"
REGION="__REGION__"
TOPIC_ARN="__TOPIC_ARN__"
NAMESPACE="__NAMESPACE__"

notify() {
  aws sns publish --region "$REGION" --topic-arn "$TOPIC_ARN" \
    --subject "V10 bootstrap: $1" --message "$2" >/dev/null || true
}
trap 'echo "BOOTSTRAP_FAILED line $LINENO" > /var/log/v10-bootstrap.failed; notify "FAILED on $(hostname)" "Bootstrap failed at line $LINENO. See /var/log/v10-bootstrap.log (./deploy.sh logs)."' ERR

# Packages and a 1 GB swap file as headroom.
dnf install -y -q python3.11 python3.11-pip tar
if [ ! -f /swapfile ]; then
  dd if=/dev/zero of=/swapfile bs=1M count=1024 status=none
  chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile
  echo '/swapfile none swap sw 0 0' >> /etc/fstab
fi

# Service account and directories.
id v10 >/dev/null 2>&1 || useradd --system --home-dir /var/lib/v10 --shell /sbin/nologin v10
install -d -o v10 -g v10 -m 0700 /var/lib/v10 /var/lib/v10/data /var/lib/v10/numba-cache
install -d -o v10 -g v10 -m 0750 /var/log/v10
install -d -o root -g v10 -m 0750 /etc/v10

cat > /etc/v10/deploy.conf <<CONF
BUCKET=${BUCKET}
REGION=${REGION}
CONF
cat > /etc/v10/v10.env <<ENV
AWS_DEFAULT_REGION=${REGION}
V10_DATA_ROOT=/var/lib/v10/data
V10_SNS_TOPIC_ARN=${TOPIC_ARN}
V10_BACKUP_BUCKET=${BUCKET}
V10_BACKUP_PREFIX=v10
V10_DATA_BACKUP_HOUR=2
V10_CW_NAMESPACE=${NAMESPACE}
ENV
chmod 0640 /etc/v10/deploy.conf /etc/v10/v10.env
chown root:v10 /etc/v10/deploy.conf /etc/v10/v10.env

# Code + virtualenv via the same path updates use.
aws s3 cp --only-show-errors --region "$REGION" "s3://${BUCKET}/releases/current.tar.gz" /tmp/boot.tgz
mkdir -p /tmp/boot && tar -xzf /tmp/boot.tgz -C /tmp/boot deploy/aws/refresh.sh
bash /tmp/boot/deploy/aws/refresh.sh
rm -rf /tmp/boot /tmp/boot.tgz

# Data: shard mirror + latest ledger/state from S3.
runuser -u v10 -- bash -c 'set -a; . /etc/v10/v10.env; set +a; cd /opt/v10_standalone && /opt/v10_venv/bin/python -m momentum_v10.ops restore'

# Can this host reach Binance futures? (451 = region blocked)
CODE_HTTP=$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 https://fapi.binance.com/fapi/v1/time || echo 000)
SHARDS=$(find /var/lib/v10/data/raw_shards -name '*_USDT_1h.parquet' | wc -l)

# First run now (async); afterwards the timer fires at :05 every hour.
systemctl start --no-block v10-hourly.service
printf 'BOOTSTRAP_DONE %s\nBINANCE_HTTP %s\nSHARDS %s\n' "$(date -u +%FT%TZ)" "$CODE_HTTP" "$SHARDS" > /var/lib/v10/.bootstrap-done
trap - ERR
notify "ready on $(hostname)" "Bootstrap complete.
Binance futures API HTTP status: ${CODE_HTTP} (200 = reachable)
Raw shards restored: ${SHARDS}
First hourly run started now (expect its report in ~15 minutes); then every hour at :05 UTC."
