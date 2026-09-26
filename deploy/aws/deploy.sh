#!/bin/bash
# V10 momentum engine on AWS (EC2 t4g.small, eu-west-2). Run from your Mac.
#
#   ./deploy.sh [-y] deploy        create/update everything, upload code+data, launch
#   ./deploy.sh update             ship new code to the running instance
#   ./deploy.sh verify             wait for bootstrap + first run, then check everything
#   ./deploy.sh status             last hourly status + timer + recent log lines
#   ./deploy.sh logs               bootstrap log + last 80 journal lines
#   ./deploy.sh diag               summarise recent ingest errors
#   ./deploy.sh resubscribe        re-send pending email confirmations
#   ./deploy.sh dashboard          publish the web dashboard (S3 + CloudFront)
#   ./deploy.sh run-now            trigger an hourly run immediately
#   ./deploy.sh destroy            tear down (keeps the S3 bucket + backups)
#
# Uses your normal AWS CLI credentials (AWS_PROFILE works). Settings below
# can be overridden with environment variables. macOS bash 3.2 compatible.
set -euo pipefail

REGION="${REGION:-eu-west-2}"
NAME="${NAME:-v10-momentum}"
INSTANCE_TYPE="${INSTANCE_TYPE:-t4g.small}"
EMAILS="${EMAILS:-nadana1985@protonmail.com abdulkhader86@gmail.com}"
NAMESPACE="${NAMESPACE:-V10}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CODE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
DATA_DIR="${DATA_DIR:-$(cd "$CODE_DIR/.." && pwd)/data}"
ASSUME_YES=0
FORCE_DATA=0

export AWS_DEFAULT_REGION="$REGION" AWS_PAGER=""

say()  { printf '\033[1m==> %s\033[0m\n' "$*"; }
warn() { printf '\033[33m!!  %s\033[0m\n' "$*" >&2; }
die()  { printf '\033[31mxx  %s\033[0m\n' "$*" >&2; exit 1; }
confirm() {
  if [ "$ASSUME_YES" = 1 ]; then return 0; fi
  printf '%s [y/N] ' "$1"; read -r ans
  case "$ans" in y|Y|yes|YES) return 0 ;; *) die "aborted" ;; esac
}

preflight() {
  command -v aws >/dev/null || die "AWS CLI not found (brew install awscli)"
  ACCOUNT=$(aws sts get-caller-identity --query Account --output text) || die "AWS credentials not working (aws sso login / AWS_PROFILE?)"
  CALLER=$(aws sts get-caller-identity --query Arn --output text)
  BUCKET="${BUCKET:-${NAME}-${ACCOUNT}-${REGION}}"
  ROLE="${NAME}-ec2"
  PROFILE_NAME="${NAME}-ec2"
  SG_NAME="${NAME}-sg"
  TOPIC_NAME="${NAME}-alerts"
  ALARM="${NAME}-heartbeat"
}

instance_id() {
  aws ec2 describe-instances \
    --filters "Name=tag:Name,Values=${NAME}" "Name=instance-state-name,Values=pending,running,stopping,stopped" \
    --query 'Reservations[].Instances[].InstanceId' --output text | awk '{print $1}'
}

topic_arn() { aws sns create-topic --name "$TOPIC_NAME" --tags "Key=Project,Value=${NAME}" --query TopicArn --output text; }

build_release() {
  RELEASE="/tmp/${NAME}-$(date -u +%Y%m%dT%H%M%SZ).tar.gz"
  say "Packaging code from $CODE_DIR"
  local noxattr=""
  if tar --help 2>&1 | grep -q -- '--no-mac-metadata'; then noxattr="--no-mac-metadata --no-xattrs"; fi
  # shellcheck disable=SC2086  # $noxattr is intentionally word-split
  COPYFILE_DISABLE=1 tar $noxattr -czf "$RELEASE" -C "$CODE_DIR" \
    --exclude '__pycache__' --exclude '*.pyc' --exclude '.DS_Store' --exclude '.pytest_cache' \
    README.md Dockerfile requirements.txt requirements-dashboard.txt requirements-dev.txt \
    build_v10_tape.py config momentum_v10 deploy
  aws s3 cp --only-show-errors "$RELEASE" "s3://${BUCKET}/releases/$(basename "$RELEASE")"
  aws s3 cp --only-show-errors "$RELEASE" "s3://${BUCKET}/releases/current.tar.gz"
  rm -f "$RELEASE"
}

ensure_bucket() {
  if aws s3api head-bucket --bucket "$BUCKET" 2>/dev/null; then
    say "S3 bucket $BUCKET exists"
  else
    say "Creating S3 bucket $BUCKET"
    aws s3api create-bucket --bucket "$BUCKET" --create-bucket-configuration "LocationConstraint=${REGION}" >/dev/null
  fi
  aws s3api put-public-access-block --bucket "$BUCKET" --public-access-block-configuration \
    BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
  aws s3api put-bucket-encryption --bucket "$BUCKET" --server-side-encryption-configuration \
    '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"}}]}'
  aws s3api put-bucket-lifecycle-configuration --bucket "$BUCKET" --lifecycle-configuration '{
    "Rules":[
      {"ID":"daily-ledger-35d","Status":"Enabled","Filter":{"Prefix":"v10/daily/"},"Expiration":{"Days":35}},
      {"ID":"old-releases-90d","Status":"Enabled","Filter":{"Prefix":"releases/v10-"},"Expiration":{"Days":90}},
      {"ID":"abort-mpu-7d","Status":"Enabled","Filter":{"Prefix":""},"AbortIncompleteMultipartUpload":{"DaysAfterInitiation":7}}
    ]}'
  aws s3api put-bucket-tagging --bucket "$BUCKET" --tagging "TagSet=[{Key=Project,Value=${NAME}}]"
}

upload_data() {
  local n
  n=$(find "$DATA_DIR/raw_shards" -name '*_USDT_1h.parquet' 2>/dev/null | wc -l | tr -d ' ')
  [ "$n" -ge 100 ] || die "DATA_DIR=$DATA_DIR has $n raw shards; expected your data folder (set DATA_DIR=...)"
  say "Uploading data from $DATA_DIR ($n raw shards, ~$(du -sh "$DATA_DIR" | cut -f1)) — first time takes a while"
  local d
  for d in raw_shards exotic_shards; do
    if [ -d "$DATA_DIR/$d" ]; then
      aws s3 sync --only-show-errors "$DATA_DIR/$d" "s3://${BUCKET}/v10/data/$d" --exclude '*' --include '*.parquet'
    fi
  done
  local f
  for f in engine_state.json sync_state.json; do
    if [ -f "$DATA_DIR/$f" ]; then aws s3 cp --only-show-errors "$DATA_DIR/$f" "s3://${BUCKET}/v10/latest/$f"; fi
  done
  if [ -d "$DATA_DIR/all_tapes/v10_production" ]; then
    aws s3 sync --only-show-errors "$DATA_DIR/all_tapes/v10_production" \
      "s3://${BUCKET}/v10/latest/all_tapes/v10_production" --exclude '.*'
  fi
}

ensure_topic() {
  TOPIC_ARN=$(topic_arn)
  say "SNS topic $TOPIC_ARN"
  local subs e
  # Confirmed subscriptions only; pending ones get the confirmation email again.
  subs=$(aws sns list-subscriptions-by-topic --topic-arn "$TOPIC_ARN" \
    --query "Subscriptions[?SubscriptionArn!='PendingConfirmation'].Endpoint" --output text)
  for e in $EMAILS; do
    case " $subs " in
      *"$e"*) echo "    confirmed: $e" ;;
      *) aws sns subscribe --topic-arn "$TOPIC_ARN" --protocol email --notification-endpoint "$e" >/dev/null
         echo "    confirmation email sent to $e  <-- click the link in it (check spam)" ;;
    esac
  done
}

ensure_iam() {
  say "IAM role $ROLE"
  if ! aws iam get-role --role-name "$ROLE" >/dev/null 2>&1; then
    aws iam create-role --role-name "$ROLE" --tags "Key=Project,Value=${NAME}" \
      --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"ec2.amazonaws.com"},"Action":"sts:AssumeRole"}]}' >/dev/null
  fi
  aws iam put-role-policy --role-name "$ROLE" --policy-name "${NAME}-runtime" --policy-document "{
    \"Version\":\"2012-10-17\",\"Statement\":[
      {\"Effect\":\"Allow\",\"Action\":\"s3:ListBucket\",\"Resource\":\"arn:aws:s3:::${BUCKET}\"},
      {\"Effect\":\"Allow\",\"Action\":[\"s3:GetObject\",\"s3:PutObject\"],\"Resource\":\"arn:aws:s3:::${BUCKET}/*\"},
      {\"Effect\":\"Allow\",\"Action\":\"sns:Publish\",\"Resource\":\"${TOPIC_ARN}\"},
      {\"Effect\":\"Allow\",\"Action\":\"cloudwatch:PutMetricData\",\"Resource\":\"*\",
       \"Condition\":{\"StringEquals\":{\"cloudwatch:namespace\":\"${NAMESPACE}\"}}}
    ]}"
  aws iam attach-role-policy --role-name "$ROLE" --policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
  if ! aws iam get-instance-profile --instance-profile-name "$PROFILE_NAME" >/dev/null 2>&1; then
    aws iam create-instance-profile --instance-profile-name "$PROFILE_NAME" >/dev/null
    aws iam add-role-to-instance-profile --instance-profile-name "$PROFILE_NAME" --role-name "$ROLE"
    NEW_PROFILE=1
  else
    NEW_PROFILE=0
  fi
}

ensure_network() {
  if [ -n "${SUBNET_ID:-}" ]; then
    SUBNET="$SUBNET_ID"
    VPC=$(aws ec2 describe-subnets --subnet-ids "$SUBNET" --query 'Subnets[0].VpcId' --output text)
  else
    VPC=$(aws ec2 describe-vpcs --filters "Name=tag:Name,Values=${NAME}-vpc" --query 'Vpcs[0].VpcId' --output text)
    if [ "$VPC" != "None" ] && [ -n "$VPC" ]; then
      SUBNET=$(aws ec2 describe-subnets --filters "Name=vpc-id,Values=$VPC" "Name=tag:Name,Values=${NAME}-public" \
        --query 'Subnets[0].SubnetId' --output text)
    else
      VPC=$(aws ec2 describe-vpcs --filters Name=isDefault,Values=true --query 'Vpcs[0].VpcId' --output text)
      if [ "$VPC" != "None" ] && [ -n "$VPC" ]; then
        SUBNET=$(aws ec2 describe-subnets --filters "Name=vpc-id,Values=$VPC" Name=default-for-az,Values=true \
          --query 'sort_by(Subnets,&AvailabilityZone)[0].SubnetId' --output text)
      else
        create_vpc
      fi
    fi
  fi
  SG="${SG_ID:-$(aws ec2 describe-security-groups --filters "Name=vpc-id,Values=$VPC" "Name=group-name,Values=$SG_NAME" \
    --query 'SecurityGroups[0].GroupId' --output text)}"
  if [ "$SG" = "None" ] || [ -z "$SG" ]; then
    SG=$(aws ec2 create-security-group --group-name "$SG_NAME" --vpc-id "$VPC" \
      --description "V10 hourly job: no inbound, outbound only" \
      --tag-specifications "ResourceType=security-group,Tags=[{Key=Project,Value=${NAME}}]" \
      --query GroupId --output text)
  fi
  say "Network: vpc $VPC  subnet $SUBNET  security group $SG (no inbound rules)"
}

create_vpc() {
  # No default VPC: build a small isolated one (free): 1 public subnet + IGW.
  local az igw rt
  say "No default VPC in $REGION: creating ${NAME}-vpc (10.42.0.0/24, one public subnet, no inbound)"
  tags() { echo "ResourceType=$1,Tags=[{Key=Name,Value=$2},{Key=Project,Value=${NAME}}]"; }
  az=$(aws ec2 describe-instance-type-offerings --location-type availability-zone \
    --filters "Name=instance-type,Values=${INSTANCE_TYPE}" --query 'InstanceTypeOfferings[].Location' --output text \
    | tr '\t' '\n' | sort | head -1)
  [ -n "$az" ] || die "$INSTANCE_TYPE is not offered in any $REGION availability zone"
  VPC=$(aws ec2 create-vpc --cidr-block 10.42.0.0/24 --tag-specifications "$(tags vpc "${NAME}-vpc")" \
    --query Vpc.VpcId --output text)
  aws ec2 wait vpc-available --vpc-ids "$VPC"
  aws ec2 modify-vpc-attribute --vpc-id "$VPC" --enable-dns-hostnames '{"Value":true}'
  SUBNET=$(aws ec2 create-subnet --vpc-id "$VPC" --cidr-block 10.42.0.0/26 --availability-zone "$az" \
    --tag-specifications "$(tags subnet "${NAME}-public")" --query Subnet.SubnetId --output text)
  aws ec2 modify-subnet-attribute --subnet-id "$SUBNET" --map-public-ip-on-launch
  igw=$(aws ec2 create-internet-gateway --tag-specifications "$(tags internet-gateway "${NAME}-igw")" \
    --query InternetGateway.InternetGatewayId --output text)
  aws ec2 attach-internet-gateway --internet-gateway-id "$igw" --vpc-id "$VPC"
  rt=$(aws ec2 create-route-table --vpc-id "$VPC" --tag-specifications "$(tags route-table "${NAME}-public-rt")" \
    --query RouteTable.RouteTableId --output text)
  aws ec2 create-route --route-table-id "$rt" --destination-cidr-block 0.0.0.0/0 --gateway-id "$igw" >/dev/null
  aws ec2 associate-route-table --route-table-id "$rt" --subnet-id "$SUBNET" >/dev/null
}

delete_own_vpc() {
  local vpc igw rt assoc sn
  vpc=$(aws ec2 describe-vpcs --filters "Name=tag:Name,Values=${NAME}-vpc" "Name=tag:Project,Values=${NAME}" \
    --query 'Vpcs[0].VpcId' --output text)
  if [ "$vpc" = "None" ] || [ -z "$vpc" ]; then return 0; fi
  say "Deleting ${NAME}-vpc ($vpc)"
  for rt in $(aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$vpc" "Name=tag:Project,Values=${NAME}" \
      --query 'RouteTables[].RouteTableId' --output text); do
    for assoc in $(aws ec2 describe-route-tables --route-table-ids "$rt" \
        --query 'RouteTables[0].Associations[?!Main].RouteTableAssociationId' --output text); do
      aws ec2 disassociate-route-table --association-id "$assoc" || true
    done
    aws ec2 delete-route-table --route-table-id "$rt" || true
  done
  for igw in $(aws ec2 describe-internet-gateways --filters "Name=attachment.vpc-id,Values=$vpc" \
      --query 'InternetGateways[].InternetGatewayId' --output text); do
    aws ec2 detach-internet-gateway --internet-gateway-id "$igw" --vpc-id "$vpc" || true
    aws ec2 delete-internet-gateway --internet-gateway-id "$igw" || true
  done
  for sn in $(aws ec2 describe-subnets --filters "Name=vpc-id,Values=$vpc" --query 'Subnets[].SubnetId' --output text); do
    aws ec2 delete-subnet --subnet-id "$sn" || true
  done
  aws ec2 delete-vpc --vpc-id "$vpc" || true
}

launch_instance() {
  local ami ud try errf
  errf=$(mktemp)
  ami=$(aws ssm get-parameter --name /aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-arm64 \
    --query Parameter.Value --output text)
  ud=$(mktemp)
  sed -e "s|__BUCKET__|${BUCKET}|g" -e "s|__REGION__|${REGION}|g" \
      -e "s|__TOPIC_ARN__|${TOPIC_ARN}|g" -e "s|__NAMESPACE__|${NAMESPACE}|g" \
      "$SCRIPT_DIR/bootstrap.sh" > "$ud"
  say "Launching $INSTANCE_TYPE ($ami)"
  if [ "$NEW_PROFILE" = 1 ]; then sleep 15; fi   # new instance profiles take a moment to propagate
  for try in 1 2 3 4 5 6; do
    if IID=$(aws ec2 run-instances --image-id "$ami" --instance-type "$INSTANCE_TYPE" \
        --subnet-id "$SUBNET" --security-group-ids "$SG" --associate-public-ip-address \
        --iam-instance-profile "Name=${PROFILE_NAME}" \
        --metadata-options HttpTokens=required,HttpEndpoint=enabled,HttpPutResponseHopLimit=1 \
        --credit-specification CpuCredits=standard \
        --block-device-mappings 'DeviceName=/dev/xvda,Ebs={VolumeSize=20,VolumeType=gp3,Encrypted=true,DeleteOnTermination=true}' \
        --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=${NAME}},{Key=Project,Value=${NAME}}]" \
                             "ResourceType=volume,Tags=[{Key=Name,Value=${NAME}},{Key=Project,Value=${NAME}}]" \
        --user-data "file://$ud" --query 'Instances[0].InstanceId' --output text 2>"$errf"); then
      break
    fi
    if ! grep -q 'Invalid IAM Instance Profile' "$errf"; then cat "$errf" >&2; rm -f "$ud" "$errf"; die "run-instances failed"; fi
    warn "instance profile not visible yet; retry $try/6"; sleep 10
  done
  rm -f "$ud" "$errf"
  [ -n "${IID:-}" ] || die "could not launch instance"
  aws ec2 modify-instance-attribute --instance-id "$IID" --disable-api-termination
  say "Instance $IID launched; waiting for it to run"
  aws ec2 wait instance-running --instance-ids "$IID"
}

ensure_alarm() {
  say "CloudWatch alarm $ALARM (no successful run for 2 hours -> email)"
  aws cloudwatch put-metric-alarm --alarm-name "$ALARM" \
    --alarm-description "V10 hourly job: HourlyOK missing or 0 for 2 consecutive hours" \
    --namespace "$NAMESPACE" --metric-name HourlyOK --statistic Maximum --period 3600 \
    --evaluation-periods 2 --datapoints-to-alarm 2 --threshold 1 --comparison-operator LessThanThreshold \
    --treat-missing-data breaching --alarm-actions "$TOPIC_ARN" --ok-actions "$TOPIC_ARN"
}

ssm_run() {  # ssm_run "<shell commands>"  -> prints output
  local iid cid st
  iid=$(instance_id); [ -n "$iid" ] || die "no ${NAME} instance found"
  cid=$(aws ssm send-command --instance-ids "$iid" --document-name AWS-RunShellScript \
    --parameters "commands=[\"$1\"]" --timeout-seconds 3600 --query Command.CommandId --output text) \
    || die "SSM not reachable yet (agent registers ~2-5 min after boot)"
  for _ in $(seq 1 720); do
    sleep 5
    st=$(aws ssm get-command-invocation --command-id "$cid" --instance-id "$iid" --query Status --output text 2>/dev/null || echo Pending)
    case "$st" in Pending|InProgress|Delayed) ;; *) break ;; esac
  done
  aws ssm get-command-invocation --command-id "$cid" --instance-id "$iid" --query StandardOutputContent --output text
  local err; err=$(aws ssm get-command-invocation --command-id "$cid" --instance-id "$iid" --query StandardErrorContent --output text)
  if [ -n "$err" ] && [ "$err" != "None" ]; then printf '%s\n' "$err" >&2; fi
  [ "$st" = Success ] || die "remote command ended: $st"
}

cmd_deploy() {
  preflight
  say "Account $ACCOUNT  ($CALLER)"
  say "Region $REGION  instance $INSTANCE_TYPE  bucket $BUCKET"
  say "Alerts to: $EMAILS"
  confirm "Create/update these resources (~\$19/month while running)?"
  ensure_bucket
  ensure_topic
  ensure_iam
  ensure_network
  build_release
  IID=$(instance_id)
  if [ -n "$IID" ]; then
    warn "Instance $IID already exists: not relaunching, not overwriting its data. Use './deploy.sh update' for code."
    if [ "$FORCE_DATA" = 1 ]; then upload_data; fi
  else
    upload_data
    launch_instance
  fi
  ensure_alarm
  cat <<MSG

Done. What happens next:
  1. Confirm the SNS subscription email(s) if you haven't (check spam).
  2. The instance installs itself (~5 min) and emails "V10 bootstrap: ready",
     including whether Binance is reachable from it (HTTP 200).
  3. The first hourly report arrives ~15 min later, then every hour (:05 UTC run).
  You may get one heartbeat ALARM email before the first run lands, then OK.

  ./deploy.sh status     check it any time
  ./deploy.sh logs       bootstrap + service logs
MSG
}

cmd_update()  { preflight; build_release; say "Installing on instance"; ssm_run "bash /opt/v10_standalone/deploy/aws/refresh.sh"; }
cmd_resubscribe() { preflight; ensure_topic; }
cmd_status()  { preflight; ssm_run "cat /var/lib/v10/data/all_tapes/v10_production/hourly_status.json 2>/dev/null || echo 'no run yet'; echo; systemctl list-timers v10-hourly.timer --no-pager; systemctl status v10-hourly.service --no-pager -n 0 | head -5; free -m | head -2; df -h / | tail -1"; }
cmd_logs()    { preflight; ssm_run "tail -n 40 /var/log/v10-bootstrap.log; echo ----; journalctl -u v10-hourly.service -n 80 --no-pager"; }
ssm_try() {  # like ssm_run but never exits; prints output or nothing
  local iid cid st
  iid=$(instance_id); [ -n "$iid" ] || return 1
  cid=$(aws ssm send-command --instance-ids "$iid" --document-name AWS-RunShellScript \
    --parameters "commands=[\"$1\"]" --timeout-seconds 120 --query Command.CommandId --output text 2>/dev/null) || return 1
  for _ in $(seq 1 30); do
    sleep 4
    st=$(aws ssm get-command-invocation --command-id "$cid" --instance-id "$iid" --query Status --output text 2>/dev/null || echo Pending)
    case "$st" in Pending|InProgress|Delayed) ;; *) break ;; esac
  done
  aws ssm get-command-invocation --command-id "$cid" --instance-id "$iid" --query StandardOutputContent --output text 2>/dev/null
}

cmd_verify() {
  preflight
  local out ok=1 t0
  t0=$(date +%s)
  say "Verifying $(instance_id) — waits for bootstrap (~5-10 min) and the first hourly run (~12 min)"
  for _ in $(seq 1 60); do
    out=$(ssm_try "cat /var/lib/v10/.bootstrap-done /var/log/v10-bootstrap.failed 2>/dev/null; tail -n 1 /var/log/v10-bootstrap.log 2>/dev/null" || true)
    case "$out" in *BOOTSTRAP_DONE*) break ;; esac
    case "$out" in *BOOTSTRAP_FAILED*) warn "bootstrap failed:"; ssm_try "tail -n 60 /var/log/v10-bootstrap.log"; exit 1 ;; esac
    echo "    [$(( ($(date +%s)-t0)/60 )) min] waiting for bootstrap... ${out:+last log: $(printf '%s' "$out" | tail -c 120 | tr '\n' ' ')}"
    sleep 30
  done
  case "$out" in *BOOTSTRAP_DONE*) ;; *) die "bootstrap did not finish in 30 min; run ./deploy.sh logs" ;; esac
  printf '%s\n' "$out" | grep -E 'BOOTSTRAP_DONE|BINANCE_HTTP|SHARDS' || true
  for _ in $(seq 1 50); do
    out=$(ssm_try "systemctl is-active v10-hourly.service; cat /var/lib/v10/data/all_tapes/v10_production/hourly_status.json 2>/dev/null" || true)
    case "$out" in activating*|active*|"") echo "    [$(( ($(date +%s)-t0)/60 )) min] first hourly run in progress..." ; sleep 60 ;; *) break ;; esac
  done
  say "Hourly status"
  printf '%s\n' "$out"
  case "$out" in *'"ok": true'*) ok=0 ;; esac
  say "Service, timer, resources"
  ssm_try "systemctl list-timers v10-hourly.timer --no-pager --no-legend; systemctl show v10-hourly.service -p Result -p ExecMainStatus; free -m | sed -n 2p; df -h / | tail -1; journalctl -u v10-hourly.service --no-pager -n 400 | grep -E 'Phase|Bridging Complete|backup\\]|SNS report|CRITICAL|ERROR' | tail -12" || true
  say "S3 backup (latest/)"
  aws s3 ls "s3://${BUCKET}/v10/latest/all_tapes/v10_production/" || true
  say "Heartbeat alarm"
  aws cloudwatch describe-alarms --alarm-names "$ALARM" --query 'MetricAlarms[0].[StateValue,StateReason]' --output text || true
  say "SNS subscriptions"
  aws sns list-subscriptions-by-topic --topic-arn "$(topic_arn)" --query 'Subscriptions[].[Endpoint,SubscriptionArn]' --output text \
    | sed 's/PendingConfirmation/PENDING CONFIRMATION - click the email link/' || true
  if [ "$ok" = 0 ]; then say "VERIFY PASSED"; else warn "VERIFY: first run not ok - see status above"; exit 1; fi
}

cmd_diag() {
  preflight
  say "Ingest errors from the most recent runs (grouped)"
  ssm_run "f=/var/log/v10/v10_errors.log; grep -E ' ERROR ' \$f | tail -n 400 | sed -E 's/^[^]]*[]] //; s/[A-Z0-9]{2,}USDT/<SYM>/g; s/[0-9]{12,}/<TS>/g' | cut -c1-200 | sort | uniq -c | sort -rn | head -15; echo; echo 'failing symbols (last run):'; grep -E ' ERROR ' \$f | tail -n 200 | grep -oE '(funding|metrics|kline) [A-Z0-9]+USDT' | sort | uniq -c | awk '{print \$2}' | sort | uniq -c; grep -E ' ERROR ' \$f | tail -n 200 | grep -oE '(funding|metrics|kline) [A-Z0-9]+USDT' | awk '{print \$2}' | sort -u | head -40 | tr '\n' ' '"
}

# ---------------------------------------------------------------- dashboard
CF_COMMENT_SUFFIX="dashboard"
CACHING_OPTIMIZED=658327ea-f89d-4fab-a63d-7e88639e58f6      # AWS managed cache policy
SECURITY_HEADERS=67f7725c-6f97-4210-82d7-5512b31e9d03       # AWS managed response-headers policy

dist_id() {
  aws cloudfront list-distributions \
    --query "DistributionList.Items[?Comment=='${NAME}-${CF_COMMENT_SUFFIX}'].Id | [0]" --output text 2>/dev/null
}

oac_id() {
  aws cloudfront list-origin-access-controls \
    --query "OriginAccessControlList.Items[?Name=='${NAME}-oac'].Id | [0]" --output text 2>/dev/null
}

cmd_dashboard() {
  preflight
  local oac did dom cfg acct http
  say "Publishing the dashboard data to s3://${BUCKET}/site/ from the server"
  build_release
  ssm_run "bash /opt/v10_standalone/deploy/aws/refresh.sh"
  ssm_run "runuser -u v10 -- bash -c 'set -a; . /etc/v10/v10.env; set +a; export HOME=/var/lib/v10 NUMBA_CACHE_DIR=/var/lib/v10/numba-cache; cd /opt/v10_standalone && /opt/v10_venv/bin/python -m momentum_v10.ops publish-site'"

  oac=$(oac_id)
  if [ -z "$oac" ] || [ "$oac" = "None" ]; then
    oac=$(aws cloudfront create-origin-access-control --origin-access-control-config \
      "Name=${NAME}-oac,Description=V10 dashboard bucket access,SigningProtocol=sigv4,SigningBehavior=always,OriginAccessControlOriginType=s3" \
      --query OriginAccessControl.Id --output text)
  fi
  say "Origin access control $oac (bucket stays private; only CloudFront can read site/)"

  did=$(dist_id)
  if [ -z "$did" ] || [ "$did" = "None" ]; then
    cfg=$(mktemp)
    cat > "$cfg" <<JSON
{
  "CallerReference": "${NAME}-dashboard-$(date +%s)",
  "Comment": "${NAME}-${CF_COMMENT_SUFFIX}",
  "Enabled": true,
  "DefaultRootObject": "index.html",
  "PriceClass": "PriceClass_100",
  "HttpVersion": "http2and3",
  "IsIPV6Enabled": true,
  "Origins": {"Quantity": 1, "Items": [{
    "Id": "s3-site",
    "DomainName": "${BUCKET}.s3.${REGION}.amazonaws.com",
    "OriginPath": "/site",
    "S3OriginConfig": {"OriginAccessIdentity": ""},
    "OriginAccessControlId": "${oac}"
  }]},
  "DefaultCacheBehavior": {
    "TargetOriginId": "s3-site",
    "ViewerProtocolPolicy": "redirect-to-https",
    "CachePolicyId": "${CACHING_OPTIMIZED}",
    "ResponseHeadersPolicyId": "${SECURITY_HEADERS}",
    "Compress": true,
    "AllowedMethods": {"Quantity": 2, "Items": ["GET", "HEAD"],
                       "CachedMethods": {"Quantity": 2, "Items": ["GET", "HEAD"]}}
  }
}
JSON
    did=$(aws cloudfront create-distribution --distribution-config "file://$cfg" --query Distribution.Id --output text)
    rm -f "$cfg"
    acct=$(aws sts get-caller-identity --query Account --output text)
    aws cloudfront tag-resource --resource "arn:aws:cloudfront::${acct}:distribution/${did}" \
      --tags "Items=[{Key=Project,Value=${NAME}}]" || true
    say "Created CloudFront distribution $did"
  else
    say "CloudFront distribution $did exists"
  fi

  acct=$(aws sts get-caller-identity --query Account --output text)
  aws s3api put-bucket-policy --bucket "$BUCKET" --policy "{
    \"Version\":\"2012-10-17\",\"Statement\":[{
      \"Sid\":\"V10DashboardReadViaCloudFront\",\"Effect\":\"Allow\",
      \"Principal\":{\"Service\":\"cloudfront.amazonaws.com\"},
      \"Action\":\"s3:GetObject\",\"Resource\":\"arn:aws:s3:::${BUCKET}/site/*\",
      \"Condition\":{\"StringEquals\":{\"AWS:SourceArn\":\"arn:aws:cloudfront::${acct}:distribution/${did}\"}}}]}"

  dom=$(aws cloudfront get-distribution --id "$did" --query Distribution.DomainName --output text)
  say "Waiting for CloudFront to finish deploying (usually 3-10 min)..."
  aws cloudfront wait distribution-deployed --id "$did" || warn "still deploying; try the URL in a few minutes"
  http=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 "https://${dom}/data/meta.json" || true)
  say "Check: https://${dom}/data/meta.json -> HTTP $http"
  if [ "$http" = 200 ]; then curl -s "https://${dom}/data/meta.json"; echo; fi
  cat <<MSG

Dashboard: https://${dom}/
  - Updates after every hourly run (data cached up to 60 s, page up to 5 min).
  - No login yet: anyone with this URL can view it. Search engines are told not to index it.
MSG
}

delete_dashboard() {
  local did etag cfg acct oac
  did=$(dist_id)
  if [ -n "$did" ] && [ "$did" != "None" ]; then
    say "Disabling CloudFront distribution $did (takes a few minutes)"
    cfg=$(mktemp)
    aws cloudfront get-distribution-config --id "$did" --output json > "$cfg"
    etag=$(perl -MJSON::PP -e 'local $/; my $j=decode_json(<STDIN>); print $j->{ETag}' < "$cfg")
    if [ "$(perl -MJSON::PP -e 'local $/; my $j=decode_json(<STDIN>); print($j->{DistributionConfig}{Enabled} ? 1 : 0)' < "$cfg")" = 1 ]; then
      perl -MJSON::PP -e 'local $/; my $j=decode_json(<STDIN>); my $c=$j->{DistributionConfig}; $c->{Enabled}=JSON::PP::false; print encode_json($c)' < "$cfg" > "$cfg.new"
      etag=$(aws cloudfront update-distribution --id "$did" --if-match "$etag" \
        --distribution-config "file://$cfg.new" --query ETag --output text)
    fi
    aws cloudfront wait distribution-deployed --id "$did" || true
    aws cloudfront delete-distribution --id "$did" --if-match "$etag" || warn "delete distribution $did later in the console"
    rm -f "$cfg" "$cfg.new"
  fi
  oac=$(oac_id)
  if [ -n "$oac" ] && [ "$oac" != "None" ]; then
    etag=$(aws cloudfront get-origin-access-control --id "$oac" --query ETag --output text)
    aws cloudfront delete-origin-access-control --id "$oac" --if-match "$etag" || true
  fi
  aws s3api delete-bucket-policy --bucket "$BUCKET" 2>/dev/null || true
}

cmd_run_now() { preflight; ssm_run "systemctl start --no-block v10-hourly.service && echo started"; }

cmd_destroy() {
  preflight
  warn "This terminates the instance and removes the dashboard, role, security group, alarm and SNS topic."
  warn "The S3 bucket $BUCKET (your data + backups) is kept; delete it yourself if you want."
  if [ "$ASSUME_YES" != 1 ]; then
    printf 'Type the name %s to confirm: ' "$NAME"; read -r ans; [ "$ans" = "$NAME" ] || die "aborted"
  fi
  local iid; iid=$(instance_id)
  if [ -n "$iid" ]; then
    aws ec2 modify-instance-attribute --instance-id "$iid" --no-disable-api-termination
    aws ec2 terminate-instances --instance-ids "$iid" >/dev/null
    say "Terminating $iid"; aws ec2 wait instance-terminated --instance-ids "$iid"
  fi
  delete_dashboard
  aws cloudwatch delete-alarms --alarm-names "$ALARM" || true
  aws iam remove-role-from-instance-profile --instance-profile-name "$PROFILE_NAME" --role-name "$ROLE" 2>/dev/null || true
  aws iam delete-instance-profile --instance-profile-name "$PROFILE_NAME" 2>/dev/null || true
  aws iam detach-role-policy --role-name "$ROLE" --policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore 2>/dev/null || true
  aws iam delete-role-policy --role-name "$ROLE" --policy-name "${NAME}-runtime" 2>/dev/null || true
  aws iam delete-role --role-name "$ROLE" 2>/dev/null || true
  local sg
  for sg in $(aws ec2 describe-security-groups --filters "Name=group-name,Values=${SG_NAME}" "Name=tag:Project,Values=${NAME}" \
      --query 'SecurityGroups[].GroupId' --output text); do
    aws ec2 delete-security-group --group-id "$sg" || true
  done
  delete_own_vpc
  local t; t=$(aws sns list-topics --query "Topics[?ends_with(TopicArn, ':${TOPIC_NAME}')].TopicArn" --output text)
  if [ -n "$t" ]; then aws sns delete-topic --topic-arn "$t" || true; fi
  say "Destroyed. Bucket $BUCKET kept."
}

while [ $# -gt 0 ]; do
  case "$1" in
    -y|--yes) ASSUME_YES=1; shift ;;
    --force-data) FORCE_DATA=1; shift ;;
    deploy|update|status|logs|run-now|destroy|verify|diag|resubscribe|dashboard) CMD="$1"; shift ;;
    -h|--help) sed -n '2,17p' "$0"; exit 0 ;;
    *) die "unknown argument: $1" ;;
  esac
done
case "${CMD:-deploy}" in
  deploy) cmd_deploy ;; update) cmd_update ;; status) cmd_status ;;
  logs) cmd_logs ;; run-now) cmd_run_now ;; destroy) cmd_destroy ;; verify) cmd_verify ;; diag) cmd_diag ;; resubscribe) cmd_resubscribe ;; dashboard) cmd_dashboard ;;
esac
