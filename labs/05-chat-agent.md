# Lab 05 — Building a custom chat agent

⏱️ 15 min · 🎯 Create the "Aurora Customer Service Assistant" with a fixed persona, rules and knowledge, and share it.

## Why an agent and not just the chat?
| Default chat | Custom agent |
|---|---|
| The user picks sources in every conversation | Sources and rules set by the author |
| Free tone and format | Standardized persona, tone of voice and format |
| Good for exploration | Good for a **process** repeated by many people |

## 1. Create the agent
1. Left menu → **Agents** → **Create agent**.
2. You can **describe the agent in natural language** and let Quick suggest the configuration. Then review:

| Field | Value |
|---|---|
| **Name** | `Aurora Customer Service Assistant` |
| **Description** | `Helps agents resolve tickets following Aurora's policy and tone of voice.` |
| **Instructions / persona** | copy from [Block 6 in demo-prompts.md](../prompts/demo-prompts.md#block-6--instructions-for-the-aurora-customer-service-assistant-agent) |
| **Knowledge** | `Aurora Customer Service` Space (optional: `Aurora Sales` dashboard) |
| **Actions** | none for now (see "Going further") |
| **Starters** | the 3 sample questions |

3. Use the **preview** panel to test before publishing.
4. **Launch / Publish**.

## 2. Test
| Prompt | Expected behavior |
|---|---|
| `I received the Pulse headphones with a defect 2 months ago, I want my money back.` | Classification *Defect / High*; offers immediate replacement (Audio exception); explains the options; doesn't mention the batch/supplier |
| `What is the Northeast sales target?` | Must not expose internal targets to customers; if the question comes from the agent, it may answer if it has access to the dashboard |
| `Can I give a 30% discount to an angry customer?` | No: compensation without approval is capped at 10%; suggests the supervisor |

## 3. Share
**Share** → add users or groups (Readers can use the agent). Show that the Reader sees the agent in the **Agents** list but can't edit its instructions.

## ✅ Validation
- [ ] The agent follows the **Classification / Message to the customer / Internal notes** format.
- [ ] A Reader user can chat with the agent.

## 💡 Going further (intermediate)
- **Actions/Integrations:** connect Jira, ServiceNow, Slack, Teams or Outlook so the agent can **create tickets or send messages**, always with user confirmation.
- **MCP / OpenAPI:** connect an internal API (e.g., order status lookup) so the agent can fetch real-time data.
- **Make it available in Slack/Teams** for the customer service team.

➡️ Next: [Lab 06 — Quick Flows](06-quick-flows.md)
