# Amazon Quick in practice — from zero to your first agent

Companion material for the **Amazon Quick (beginner/intermediate)** webinar. Follow the labs at your own pace and reproduce everything shown live, from setup in an AWS account all the way to dashboards, AI agents and automations.

> **Amazon Quick** is AWS's AI agent–powered workspace. It brings together chat, Spaces, Quick Sight (BI, formerly QuickSight), Quick Flows, Quick Automate, Quick Index and Quick Research.

## 🏢 The scenario: Aurora Electronics (fictitious)
An online electronics retailer with three pain points:
1. **"I don't know what's happening with sales."** → Quick Sight + natural-language questions
2. **"Customer service takes too long to answer according to our policy."** → Spaces + Chat agent
3. **"The team wastes time on repetitive tasks."** → Quick Flows

The data hides a few "stories" for you to discover 🕵️ (Black Friday, a fast-growing region, a problematic product…).

## 🗺️ Labs
| # | Lab | Time | Level |
|---|---|---|---|
| 00 | [Prerequisites](labs/00-prerequisites.md) | 10 min | Beginner |
| 01 | [Setting up Amazon Quick](labs/01-setup.md) | 15 min | Beginner |
| 02 | [Sample data (S3 + CloudFormation)](labs/02-sample-data.md) | 10 min | Beginner |
| 03 | [Chat and Spaces](labs/03-chat-and-spaces.md) | 15 min | Beginner |
| 04 | [Quick Sight: dataset → dashboard → questions](labs/04-quick-sight.md) | 30 min | Beginner/Intermediate |
| 05 | [Custom chat agent](labs/05-chat-agent.md) | 15 min | Intermediate |
| 06 | [Quick Flows](labs/06-quick-flows.md) | 15 min | Intermediate |
| 07 | [Quick Research](labs/07-quick-research.md) | 10 min | Intermediate |
| 08 | [Costs, governance and cleanup](labs/08-costs-and-cleanup.md) | 10 min | All |

## 🚀 Quick start
```bash
git clone <REPO-URL>
```
```bash
cd aws-quick-webinar && ./scripts/prepare-data.sh
```
Then follow [Lab 01](labs/01-setup.md).

## 📁 Structure
```
aws-quick-webinar/
├── README.md                  ← you are here
├── PRESENTER_SCRIPT.md        ← minute-by-minute webinar script
├── PRE_WEBINAR_CHECKLIST.md   ← presenter preparation
├── assets/demo-flow.png       ← one-page overview of the demo flow
├── labs/                      ← step-by-step guides for participants
├── prompts/demo-prompts.md    ← every prompt to copy and paste + expected answers
├── data/                      ← generator and CSVs (sales, targets, products)
├── documents/                 ← policy, manual and catalog (used in Spaces)
├── infra/data-bucket.yaml     ← CloudFormation for the S3 bucket
└── scripts/                   ← prepare-data.sh and cleanup.sh
```

## ⚠️ Important notes
- **Costs:** the first subscription through the console includes a 30-day trial for up to 25 users; **after that, billing starts automatically**. See [Lab 08](labs/08-costs-and-cleanup.md) and the [pricing page](https://aws.amazon.com/quick/pricing/).
- Use a **sandbox AWS account**, not production.
- Amazon Quick evolves quickly: **menu and button names may change**. When in doubt, use the search bar at the top of Quick and the [official documentation](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html).
- All data and documents are **fictitious**.

## 📚 References
- [What is Amazon Quick](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html)
- [Setting up and signing in](https://docs.aws.amazon.com/quick/latest/userguide/setting-up.html)
- [Signing up through the AWS Console](https://docs.aws.amazon.com/quick/latest/userguide/signing-up.html)
- [Amazon Quick FAQ](https://aws.amazon.com/quick/faqs/)
- [Implementation starter kit (AWS Builder Center)](https://builder.aws.com/content/33FWxLBkVVy9zWYOppQKWcj7UTz/accelerate-your-amazon-quick-suite-implementation-starter-kit-for-rapid-deployment)
