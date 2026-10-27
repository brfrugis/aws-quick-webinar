# Lab 04 — Quick Sight: from CSV to dashboard to natural-language questions

⏱️ 30 min · 🎯 Create datasets and an analysis, publish a dashboard and ask your data questions.

## Concepts
| Term | What it is |
|---|---|
| **Data source** | Connection to the origin (S3, Athena, Redshift, RDS, upload…) |
| **Dataset** | Prepared data (types, calculated fields, joins), usually imported into **SPICE** (in-memory engine) |
| **Analysis** | The author's workspace for building visuals |
| **Dashboard** | Published, read-only version of the analysis, for consumers |
| **Topic** | Semantic layer for natural-language questions (synonyms, friendly names) |

## 1. Allow Quick to read the bucket (Option B only)
1. User menu → **Manage Quick** → **Security & permissions**.
2. Under **AWS resources**, click **Manage** → **Amazon S3** → **Select S3 buckets**.
3. Select `aurora-quick-demo-<account>-<region>` → **Finish** → **Save**.

## 2. Create the `sales` dataset
**Option B (S3):** Left menu → **Data** → **Create** → **New dataset** → **Amazon S3**
- **Data source name:** `sales`
- **Upload a manifest file → URL:** `s3://<bucket>/manifests/sales-manifest.json`
- **Connect** → **Edit/Preview data**

**Option A (upload):** **Data** → **Create** → **New dataset** → **Upload a file** → `data/sales.csv` → **Edit settings and prepare data**.

### Preparation
1. Check the types: `order_date` → **Date** (format `yyyy-MM-dd`); `revenue`, `total_cost`, `unit_price` → **Decimal**; `quantity`, `discount_pct`, `rating` → **Integer**.
2. **Add calculated field:**
   - `profit` = `revenue - total_cost`
   - `returned` = `ifelse(status = 'Returned', 1, 0)`
   - `return_rate` = `sum(returned) / count(order_id)` *(aggregate-level; format as %)*
3. Rename the dataset to `sales` → **Save & publish**.

Repeat for `targets` (manifest `targets-manifest.json`; `month` → Date, `revenue_target` → Decimal).

> **Intermediate challenge:** in the `sales` dataset, **join** `products` on `product_id` to bring in `list_price`.

## 3. Build the analysis
From the `sales` dataset → **Use in analysis**. Create these visuals:

| # | Visual | Fields | Filter | Expected insight |
|---|---|---|---|---|
| 1 | KPI | `revenue` (sum) | `status = Delivered` | ≈ R$ 7.89 million |
| 2 | Line | X: `order_date` (month) · Value: `revenue` | `status = Delivered` | Peak on Black Friday (Nov) and Christmas |
| 3 | Stacked bars | X: `region` · Value: `revenue` · Group: `channel` | — | Southeast leads; App grows |
| 4 | Horizontal bars | Y: `product` · Value: `return_rate` | — | Pulse headphones ≈ 24% |
| 5 | Donut | `return_reason` × count | `product = Pulse Bluetooth Headphones` | "Manufacturing defect" dominates |
| 6 | Map / Bars | `state` × `revenue` | — | Geographic distribution |

**Use AI in the analysis:** look for the option to build a visual with AI (*Build visual* / AI icon) and ask, for example: `Show the return rate by product as sorted bars`. Then fine-tune it manually.

**Interactivity (intermediate):**
- Add a **filter control** for `region` and `channel`.
- Set up a **filter action** on visual 3: clicking a region filters the other visuals.

## 4. Publish the dashboard
**Publish** (top right) → **Publish new dashboard as** `Aurora Sales` → **Publish dashboard** → **Share** with your users.

## 5. Ask your data
### 5.1 Topic
1. Left menu → **Topics** → **Create topic** → name `Aurora Sales` → dataset `sales` (and `targets`).
2. Wait for preparation. Under **Data**, review fields and synonyms (e.g., `revenue` = "sales", "turnover").
3. Ask the questions from [Block 5 in demo-prompts.md](../prompts/demo-prompts.md#block-5--asking-the-data-topic--space-with-dashboard).

### 5.2 In the chat, combining data and documents
1. Open the `Aurora Customer Service` Space → **Add** → add the `Aurora Sales` dashboard (and/or the Topic).
2. Ask: `Why do the Pulse Bluetooth Headphones have so many returns, and what is being done about it?`
3. The answer should combine the **number** (dashboard) with the **explanation** (policy, section 6).

## ✅ Validation
- [ ] `Aurora Sales` dashboard published with at least 4 visuals.
- [ ] The Topic correctly answers "Which month had the highest revenue?" (Nov 2025).

## 🛠️ Common issues
| Symptom | Fix |
|---|---|
| `Access denied` when reading the manifest | Bucket not authorized under *AWS resources* (step 1) or different region |
| Dates read as text | Change the type to Date with format `yyyy-MM-dd` |
| Wrong decimal separators | The CSVs use a dot as decimal separator; confirm the Decimal type |
| Topic doesn't answer | Wait for indexing to finish; review field names |

📚 [Getting started with Amazon Quick Sight](https://docs.aws.amazon.com/quick/latest/userguide/quick-sight-getting-started.html)

➡️ Next: [Lab 05 — Chat agent](05-chat-agent.md)
