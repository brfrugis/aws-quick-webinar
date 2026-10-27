# Lab 00 — Prerequisites

⏱️ 10 min · 🎯 Get your environment ready for the following labs.

## You will need
- [ ] An **AWS account** where you have administrator permissions. We recommend a **sandbox account** separate from production.
- [ ] IAM permissions to subscribe to Amazon Quick. See the [IAM policy examples](https://docs.aws.amazon.com/quicksight/latest/user/iam-policy-examples.html). With AWS Organizations, check that no SCP blocks `quicksight:*`.
- [ ] **AWS CLI v2** installed and authenticated (`aws login` or `aws sso login`), only needed for Lab 02 (S3 option).
- [ ] **Python 3.8+**, to generate the sample data.
- [ ] An up-to-date browser (Chrome, Edge or Firefox).

> **No AWS account?** You can follow Labs 03, 05, 06 and 07 with an individual account at [aws.com/quick](https://aws.com/quick) (Free/Plus plans, sign in with email/Google/Apple/GitHub). Full BI features (Lab 04) and some automations require the enterprise plans.

## Quick check
```bash
aws --version
```
```bash
aws sts get-caller-identity
```
```bash
python3 --version
```

## Choosing a region
Pick **one region** and use it for everything (Quick + S3). Check the available regions in the [Amazon Quick documentation](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html). The examples use `us-east-1`.
```bash
export AWS_REGION=us-east-1
```

## Clone the repository
```bash
git clone <REPO-URL>
```
```bash
cd aws-quick-webinar
```

➡️ Next: [Lab 01 — Setup](01-setup.md)
