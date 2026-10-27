#!/usr/bin/env bash
# Removes the AWS resources created by the demo (S3 bucket + CloudFormation stack).
# It does NOT remove the Amazon Quick account — do that in the console (see labs/08-costs-and-cleanup.md).
set -euo pipefail

STACK="${STACK:-aurora-quick-demo}"
REGION="${AWS_REGION:-$(aws configure get region || true)}"
REGION="${REGION:-us-east-1}"

BUCKET=$(aws cloudformation describe-stacks --region "$REGION" --stack-name "$STACK" \
  --query "Stacks[0].Outputs[?OutputKey=='BucketName'].OutputValue" --output text 2>/dev/null || true)

if [[ -z "$BUCKET" || "$BUCKET" == "None" ]]; then
  echo "Stack $STACK not found in region $REGION. Nothing to do."
  exit 0
fi

read -r -p "Delete ALL content of s3://$BUCKET and the stack $STACK? (type 'yes'): " OK
[[ "$OK" == "yes" ]] || { echo "Canceled."; exit 1; }

aws s3 rm --region "$REGION" "s3://$BUCKET" --recursive
aws cloudformation delete-stack --region "$REGION" --stack-name "$STACK"
aws cloudformation wait stack-delete-complete --region "$REGION" --stack-name "$STACK"
echo "Demo resources removed."
