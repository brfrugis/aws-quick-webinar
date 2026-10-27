# Lab 02 — Aurora Electronics sample data

⏱️ 5–10 min · 🎯 Generate the fictitious data and (optionally) publish it to a private S3 bucket.

## What's in the repository
| File | Content |
|---|---|
| `data/generate_data.py` | Generates the CSVs (fixed seed: everyone gets the same numbers) |
| `data/sales.csv` | ~7,900 order line items, Nov 2025 to Oct 2026 (each row is one item; `order_id` repeats for orders with several items) |
| `data/targets.csv` | Monthly revenue target per region |
| `data/products.csv` | Catalog with price and cost |
| `documents/*.md` | Returns policy, customer service manual and catalog, used in Spaces |
| `infra/data-bucket.yaml` | CloudFormation: encrypted S3 bucket, no public access, TLS only |
| `scripts/prepare-data.sh` | Does it all: generates the data, creates the bucket, uploads the files and creates the manifests |

### Data dictionary — `sales.csv`
| Column | Type | Example |
|---|---|---|
| order_id | text | ORD-104448 |
| order_date | date (YYYY-MM-DD) | 2026-08-01 |
| region / state | text | Northeast / PE |
| channel | text | Website, App, Marketplace |
| product_id / product / category | text | P005 / Pulse Bluetooth Headphones / Audio |
| quantity | integer | 2 |
| unit_price | decimal | 349.00 |
| discount_pct | integer | 5 |
| revenue | decimal | 663.10 (after discount) |
| total_cost | decimal | 280.00 |
| status | text | Delivered, Returned, Canceled |
| return_reason | text | Manufacturing defect |
| rating | integer 1–5 (empty if not delivered) | 4 |

> Amounts are in Brazilian reais (R$); regions and states are Brazilian.

## Option A — Files only (beginner, no AWS CLI)
The CSVs are already in `data/`. To regenerate them:
```bash
python3 data/generate_data.py
```
In Lab 04, use **Upload a file**.

## Option B — S3 bucket with CloudFormation (recommended)
```bash
./scripts/prepare-data.sh
```
At the end, the script prints the **bucket name** and the **manifest URL**. Keep both.

Structure created in the bucket:
```
s3://aurora-quick-demo-<account>-<region>/
├── sales/sales.csv
├── targets/targets.csv
├── products/products.csv
├── documents/*.md
└── manifests/{sales,targets,products}-manifest.json
```

> **Why manifests?** Quick Sight reads S3 files through a JSON file that says where the data is and its format (CSV, delimiter, header).

## ✅ Validation
```bash
aws s3 ls s3://aurora-quick-demo-$(aws sts get-caller-identity --query Account --output text)-$AWS_REGION --recursive
```

➡️ Next: [Lab 03 — Chat and Spaces](03-chat-and-spaces.md)
