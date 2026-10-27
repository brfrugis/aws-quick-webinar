# Lab 06 — Quick Flows: natural-language automation

⏱️ 15 min · 🎯 Create a flow that triages complaints and generates the customer reply.

## Concepts
- **Flow:** a sequence of steps (inputs → AI/reasoning → source lookups → actions → outputs) created **by describing it in natural language** or built step by step.
- Anyone with access can **run** a shared flow, no code required.
- **Flows vs Automate:** Flows are for day-to-day tasks of people and teams. **Quick Automate** is for end-to-end enterprise processes (multiple steps, systems, approvals, high volume).

## 1. Create the flow
1. Left menu → **Flows** → **Create flow**.
2. Paste the creation prompt from [Block 7 in demo-prompts.md](../prompts/demo-prompts.md#block-7--complaint-triage-flow).
3. Review the steps Quick generated. You should see something like:

```
[Input] Complaint text + Order number
      │
[AI] Classify (category + priority) ──── source: Customer Service Manual
      │
[AI] Identify applicable rule ────────── source: "Aurora Customer Service" Space
      │
[AI] Draft customer reply
      │
[AI] Internal summary for supervisor (+ escalation?)
      │
[Outputs] Customer reply · Internal summary
```

4. Adjust as needed: rename steps, make sure the Space is set as a source and keep the outputs readable.
5. **Save / Publish**.

## 2. Run it
**Run** → paste the *Test input* from the prompts file.

Expected result:
- **Category:** Manufacturing defect · **Priority:** High
- **Rule:** Audio line exception, immediate replacement (a refund is also possible; explain the options)
- **Escalation:** Legal within 2 hours (Reclame Aqui mention) and Supervisor (repeat customer)

## 3. Share
**Share** → customer service team. Each agent runs the flow with their own complaint.

## ✅ Validation
- [ ] The flow runs end to end and produces both outputs.
- [ ] The internal summary flags escalation to Legal.

## 💡 Going further (intermediate)
- Add an **action** at the end: create a ticket (Jira/ServiceNow) or post the summary to a Slack/Teams channel.
- Create a **weekly report** flow: "Summarize last week's revenue and return rate from the Aurora Sales dashboard and draft an email to the leadership team".
- Schedule runs, if your plan allows it.

➡️ Next: [Lab 07 — Quick Research](07-quick-research.md)
