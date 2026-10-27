#!/usr/bin/env bash
# Generates the sample data, creates the S3 bucket via CloudFormation and uploads the files.
#
# Usage:
#   ./scripts/prepare-data.sh                 # uses your AWS CLI default region
#   AWS_REGION=us-east-1 ./scripts/prepare-data.sh
#
# Requirements: AWS CLI v2 authenticated (aws login / aws sso login) and python3.
# IMPORTANT: use the SAME region where you created your Amazon Quick account.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
STACK="${STACK:-aurora-quick-demo}"
REGION="${AWS_REGION:-$(aws configure get region || true)}"
REGION="${REGION:-us-east-1}"

echo ">> Region: $REGION | Stack: $STACK"

echo ">> 1/4 Generating sample data..."
python3 "$ROOT/data/generate_data.py"

echo ">> 2/4 Creating/updating the bucket (CloudFormation)..."
aws cloudformation deploy \
  --region "$REGION" \
  --stack-name "$STACK" \
  --template-file "$ROOT/infra/data-bucket.yaml" \
  --no-fail-on-empty-changeset

BUCKET=$(aws cloudformation describe-stacks --region "$REGION" --stack-name "$STACK" \
  --query "Stacks[0].Outputs[?OutputKey=='BucketName'].OutputValue" --output text)
echo "   Bucket: $BUCKET"

echo ">> 3/4 Uploading CSVs and documents..."
for t in sales targets products; do
  aws s3 cp --region "$REGION" "$ROOT/data/$t.csv" "s3://$BUCKET/$t/$t.csv"
done
aws s3 cp --region "$REGION" --recursive "$ROOT/documents/" "s3://$BUCKET/documents/"

echo ">> 4/4 Generating Quick Sight manifests..."
MANIFEST_DIR="$(mktemp -d)"
for t in sales targets products; do
  cat > "$MANIFEST_DIR/$t-manifest.json" <<EOF
{
  "fileLocations": [ { "URIPrefixes": [ "s3://$BUCKET/$t/" ] } ],
  "globalUploadSettings": { "format": "CSV", "delimiter": ",", "textqualifier": "\"", "containsHeader": "true" }
}
EOF
  aws s3 cp --region "$REGION" "$MANIFEST_DIR/$t-manifest.json" "s3://$BUCKET/manifests/$t-manifest.json"
done
rm -rf "$MANIFEST_DIR"

cat <<EOF

=========================================================
 Done! Next steps (Lab 04):
 1. In Amazon Quick: user menu > Manage Quick >
    Security & permissions > AWS resources > Amazon S3
    > select the bucket: $BUCKET
 2. Data > Create > New dataset > Amazon S3, using the URL:
    s3://$BUCKET/manifests/sales-manifest.json
=========================================================
EOF
