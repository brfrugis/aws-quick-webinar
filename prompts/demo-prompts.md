# Demo prompts (copy and paste)

> AI answers vary from run to run. The "What to expect" column shows the correct content according to the demo documents and data.

## Block 4 — Chat + "Aurora Customer Service" Space

| # | Prompt | What to expect |
|---|---|---|
| 1 | `What is the deadline to return a defective product bought 45 days ago?` | Between 31 and 90 days: repair center, repair within 30 days; if not repaired, replacement/refund/price reduction. With a citation of the policy. |
| 2 | `A customer bought the Pulse Bluetooth Headphones 60 days ago and they stopped charging. What should I offer?` | Audio line exception: **immediate replacement** with a new product (within 90 days). |
| 3 | `Write a reply to the customer John, order ORD-104448 (Pulse Bluetooth Headphones that stopped charging), following the customer service manual.` | Greeting, empathy, immediate replacement, next steps, order number and support channels. Does **not** mention the batch or supplier. |
| 4 | `Which bundles can I offer to someone buying a laptop?` | Glide Wireless Mouse + Turbo 65W Charger. |
| 5 | `A customer mentioned Reclame Aqui. What should I do?` | Escalate to Legal within 2 hours. |

## Block 5 — Asking the data (Topic / Space with dashboard)

| # | Prompt | What to expect (data generated with seed 2026) |
|---|---|---|
| 1 | `What was the total revenue from delivered orders?` | ≈ R$ 7.89 million |
| 2 | `Which month had the highest revenue?` | November 2025 (Black Friday), ≈ R$ 1.52 million |
| 3 | `Which product has the highest return rate and what is the main reason?` | Pulse Bluetooth Headphones, ≈ 24%, "Manufacturing defect" |
| 4 | `Did the Northeast hit its target in October 2026?` | Yes (≈ R$ 177K actual vs. R$ 162.7K target). Requires the `targets` dataset. |
| 5 | `In which months was the Northeast below target?` | Nov 2025 to Apr 2026 |
| 6 | `Compare App versus Website revenue over the last 6 months.` | App growing, Website losing share |
| 7 | `Why do the Pulse Bluetooth Headphones have so many returns, and what is being done about it?` | Combines data (high rate) + document (SoundCell battery batch, new supplier, goal < 6%). |

**Analysis assistant (Build visual):**
- `Show the return rate by product in a sorted bar chart`
- `Monthly revenue by channel as a line chart`
- `Map of revenue by state`

## Block 6 — Instructions for the "Aurora Customer Service Assistant" agent

```text
You are the Customer Service Assistant for Aurora Electronics, an online electronics retailer.

Goal: help customer service agents resolve customer tickets quickly, correctly and with empathy.

Rules:
1. Base ALL answers about deadlines, replacements, refunds and compensation on the "Returns and Refunds Policy". Always cite the section used.
2. When drafting messages to customers, follow the "Customer Service Manual" (tone of voice and standard structure).
3. Never share internal information with customers (batch codes, suppliers, targets, quality program).
4. If the situation requires escalation (consumer protection agency, Reclame Aqui, lawsuit, order above R$ 5,000, customer with 2+ returns), state clearly who to escalate to and within what time.
5. If you can't find the information in the documents, say you don't know and suggest checking with the supervisor. Never make up policies.
6. Always answer in English.

Output format when the agent asks for a customer reply:
- **Classification:** category and priority
- **Message to the customer:** ready-to-send text
- **Internal notes:** up to 3 bullets
```

**Sample questions (starters):**
- `A customer wants to return a product because they changed their mind. What are the conditions?`
- `Write a reply for a delivery that is 8 business days late.`
- `I received the Pulse headphones with a defect 2 months ago, I want my money back.`

## Block 7 — "Complaint triage" Flow

**Creation prompt:**
```text
Create a flow called "Aurora Complaint Triage" that takes as input the text of a customer complaint and the order number.
Steps:
1. Classify the complaint according to the Customer Service Manual (category and priority).
2. Check the Returns and Refunds Policy in the "Aurora Customer Service" Space and identify the applicable rule.
3. Generate a ready-to-send reply to the customer, following the manual's standard structure.
4. Generate an internal summary of up to 3 lines for the supervisor, stating whether escalation is needed.
```

**Test input:**
```text
Order: ORD-104448
Complaint: I bought two pairs of Pulse headphones in August. One stopped charging after a few weeks and the other has crackling sound. This is the second time this has happened to me and I'm thinking about posting on Reclame Aqui. I want my money back!
```

**What to expect:** category *Manufacturing defect*, priority *High*; immediate replacement (Audio exception) with the refund option; **escalate to Legal** (Reclame Aqui mention) and possibly to the Supervisor (repeat customer).

## Block 8 — Quick Research

```text
Prepare an executive report on the consumer electronics e-commerce market in Brazil in 2026: market size, growth by region, share of purchases made through mobile apps, and the main reasons for returns in the sector.
Compare these trends with Aurora Electronics' internal data ("Aurora Customer Service" Space and "Aurora Sales" dashboard) and finish with 5 prioritized recommendations.
```
