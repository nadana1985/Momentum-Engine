#!/bin/bash
# Run ONCE with an admin IAM user's credentials. Creates the dedicated
# deployment user and stores its access key in your AWS CLI config as the
# profile "v10-deployer" (the secret is never printed).
#
#   AWS_PROFILE=<your-admin-profile> ./create-deployer-user.sh           create
#   AWS_PROFILE=<your-admin-profile> ./create-deployer-user.sh lock      remove IAM rights after first deploy
#   AWS_PROFILE=<your-admin-profile> ./create-deployer-user.sh unlock    re-add them (redeploy / destroy)
set -euo pipefail
USER_NAME="v10-deployer"
DEPLOY_PROFILE="${DEPLOY_PROFILE:-v10-deployer}"
DIR="$(cd "$(dirname "$0")" && pwd)"
export AWS_PAGER=""
ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
OPS_ARN="arn:aws:iam::${ACCOUNT}:policy/v10-deployer-ops"
IAM_ARN="arn:aws:iam::${ACCOUNT}:policy/v10-deployer-iam-setup"
DASH_ARN="arn:aws:iam::${ACCOUNT}:policy/v10-deployer-dashboard"

upsert_policy() {  # name file arn
  local doc; doc=$(sed "s/ACCOUNT_ID/${ACCOUNT}/g" "$2")
  if aws iam get-policy --policy-arn "$3" >/dev/null 2>&1; then
    # keep at most 5 versions: drop the oldest non-default first
    local old
    # shellcheck disable=SC2016  # backticks are JMESPath literals
    old=$(aws iam list-policy-versions --policy-arn "$3" --query 'Versions[?IsDefaultVersion==`false`].VersionId' --output text | awk '{print $NF}')
    if [ "$(aws iam list-policy-versions --policy-arn "$3" --query 'length(Versions)')" -ge 5 ] && [ -n "$old" ]; then
      aws iam delete-policy-version --policy-arn "$3" --version-id "$old"
    fi
    aws iam create-policy-version --policy-arn "$3" --policy-document "$doc" --set-as-default >/dev/null
  else
    aws iam create-policy --policy-name "$1" --policy-document "$doc" \
      --description "V10 momentum engine deployer" --tags Key=Project,Value=v10-momentum >/dev/null
  fi
}

case "${1:-create}" in
  create)
    echo "Account $ACCOUNT: creating IAM user $USER_NAME (CLI only, no console password)"
    aws iam get-user --user-name "$USER_NAME" >/dev/null 2>&1 || \
      aws iam create-user --user-name "$USER_NAME" --tags Key=Project,Value=v10-momentum >/dev/null
    upsert_policy v10-deployer-ops "$DIR/deployer-policy-ops.json" "$OPS_ARN"
    upsert_policy v10-deployer-iam-setup "$DIR/deployer-policy-iam-setup.json" "$IAM_ARN"
    upsert_policy v10-deployer-dashboard "$DIR/deployer-policy-dashboard.json" "$DASH_ARN"
    aws iam attach-user-policy --user-name "$USER_NAME" --policy-arn "$OPS_ARN"
    aws iam attach-user-policy --user-name "$USER_NAME" --policy-arn "$IAM_ARN"
    aws iam attach-user-policy --user-name "$USER_NAME" --policy-arn "$DASH_ARN"
    if [ "$(aws iam list-access-keys --user-name "$USER_NAME" --query 'length(AccessKeyMetadata)')" -ge 1 ]; then
      echo "User already has an access key; not creating another. Profile '$DEPLOY_PROFILE' left as is."
    else
      KEY=$(aws iam create-access-key --user-name "$USER_NAME" --query 'AccessKey.[AccessKeyId,SecretAccessKey]' --output text)
      aws configure set aws_access_key_id "$(echo "$KEY" | cut -f1)" --profile "$DEPLOY_PROFILE"
      aws configure set aws_secret_access_key "$(echo "$KEY" | cut -f2)" --profile "$DEPLOY_PROFILE"
      aws configure set region eu-west-2 --profile "$DEPLOY_PROFILE"
      unset KEY
      echo "Access key stored in ~/.aws/credentials as profile '$DEPLOY_PROFILE'."
    fi
    echo "Next: AWS_PROFILE=$DEPLOY_PROFILE ./deploy.sh   (new keys can take ~10 s to work)"
    ;;
  lock)
    aws iam detach-user-policy --user-name "$USER_NAME" --policy-arn "$IAM_ARN"
    echo "IAM rights removed. update/status/logs/run-now still work; re-run 'unlock' before deploy or destroy." ;;
  unlock)
    aws iam attach-user-policy --user-name "$USER_NAME" --policy-arn "$IAM_ARN"
    echo "IAM rights restored for deploy/destroy." ;;
  *) echo "usage: $0 [create|lock|unlock]" >&2; exit 1 ;;
esac
