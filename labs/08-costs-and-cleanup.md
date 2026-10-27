# Lab 08 — Costs, governance and cleanup

⏱️ 10 min · 🎯 Understand the cost model and remove everything you created.

## Cost model (overview)
> ⚠️ Amazon Quick prices and plans have changed since launch. **Always check the [official pricing page](https://aws.amazon.com/quick/pricing/)** before budgeting.

Items that usually show up on the bill:
- **Per-user monthly subscription**, depending on the plan (individual: Free/Plus; enterprise through the console: Professional/Enterprise).
- **Monthly account infrastructure fee**, on enterprise plans.
- **Usage** beyond what's included: SPICE capacity, agent hours (Research/Automate), index storage, etc.
- **Trial:** 30 days for up to 25 users on the first subscription through the console. **When it ends, billing starts automatically.**

Tips:
- Set up an **AWS Budget** with an alert before you start.
- Remove users who don't use the service (**Manage Quick → Manage users**).

## Governance — production checklist
- [ ] Authentication through **IAM Identity Center** with groups (Admin / Author / Reader).
- [ ] **AWS resources** granted only to the buckets and databases you need.
- [ ] Encryption with your own **KMS key**, if compliance requires it.
- [ ] **Row-level security (RLS)** on sensitive datasets (e.g., each manager sees only their region).
- [ ] Integrations/Actions with least-privilege scope and user confirmation.
- [ ] **CloudTrail** logging and periodic access reviews.

## Cleanup

### 1. Demo AWS resources (S3 + CloudFormation)
```bash
./scripts/cleanup.sh
```

### 2. Content in Amazon Quick (optional, if you keep the account)
Delete in this order: Flow → Agent → Topic → Dashboard → Analysis → Datasets → Data sources → Space.

### 3. Cancel the Amazon Quick account
1. User menu → **Manage Quick** → **Account settings**.
2. **Manage / Delete account** → confirm.

> ⚠️ Deleting the account removes **all** Quick users and assets in that AWS account. Don't do this in an account that already uses QuickSight/Quick in production.

### 4. Double-check
- **Billing and Cost Management** → make sure there are no recurring Quick charges the following month.
