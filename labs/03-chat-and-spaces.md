# Lab 03 — Chat and Spaces

⏱️ 15 min · 🎯 Give the AI your company's knowledge and ask questions that get cited answers.

## Concepts
- **Chat:** natural-language conversation with the default Quick agent.
- **Space:** a collaborative workspace with **files, dashboards, datasets and knowledge bases** that give context to answers. It can be shared with other people.
- **Knowledge base / Quick Index:** for larger volumes or enterprise sources (S3, SharePoint, Confluence, Google Drive…), connected and indexed continuously. A good next step.

## 1. First conversation (no context)
1. Click the **chat** icon (top bar or home page).
2. Ask: `What is the deadline to return a defective product at Aurora Electronics?`
3. Notice: without documents, the AI **doesn't know** the company policy and gives a generic answer. That's what we'll fix.

## 2. Create the Space
1. Left menu → **Spaces** → **Create space**.
2. **Name:** `Aurora Customer Service` · **Description:** `Customer service team policies and materials`.
3. **Add knowledge / Upload files** → upload the 3 files from the `documents/` folder:
   - `returns-and-refunds-policy.md`
   - `customer-service-manual.md`
   - `product-catalog.md`
4. Wait for indexing to finish (file status).

> If your environment doesn't accept `.md` files, rename them to `.txt` or export them as PDF/DOCX.

## 3. Chat with the Space
Open the chat **from the Space** (or select the Space as a source in the chat) and use the prompts from [Block 4 in demo-prompts.md](../prompts/demo-prompts.md#block-4--chat--aurora-customer-service-space).

Pay attention to:
- **Citations:** each answer shows which document it came from.
- **Combining sources:** prompt 3 uses the policy (what to do) and the manual (how to say it).
- **Exceptions:** prompt 2 only gets it right if it finds section 2 of the policy (Audio line).

## 4. Share
In the Space → **Share** → add a Reader user. They can now see the files and chat with the same context.

## ✅ Validation
- [ ] Prompt 2 answers **immediate replacement** for the Pulse headphones.
- [ ] The customer reply does **not** mention "batch SC-2511" or "SoundCell" (internal information).

## 💡 Going further (intermediate)
- Connect the `s3://<bucket>/documents/` prefix as a **Knowledge base** (integrations/knowledge bases menu → Amazon S3) to keep documents in sync.
- Try the Quick browser extension or desktop app.

➡️ Next: [Lab 04 — Quick Sight](04-quick-sight.md)
