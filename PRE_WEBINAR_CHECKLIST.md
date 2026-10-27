# Pre-webinar checklist (presenters)

## 1 week before
- [ ] **Dedicated sandbox AWS account** for the demo, with nothing in production.
- [ ] Confirm the Quick region is available and use it for everything (e.g., `us-east-1`).
- [ ] **Full dry run** in another account to check the current menu names (the service changes often) and adjust the script.
- [ ] Record **backup videos** (2–3 min each): subscription (Block 2), Topic creation (Block 5.4) and Flow (Block 7).
- [ ] Public repository with a short URL and a QR code on the slide.
- [ ] Create an **AWS Budget** with an alert in the demo account.

## 1 day before
- [ ] Decide: **live** subscription (new account) or an **already-subscribed account** + video. The subscription can only be done once per account.
- [ ] Run `./scripts/prepare-data.sh` and authorize the bucket under *AWS resources*.
- [ ] Have ready (as "plan B"): the `targets` dataset, the `Aurora Sales` Topic already indexed, and a **Research** report already generated.
- [ ] Create a test **Reader** user (another browser/profile) to demonstrate sharing.
- [ ] Test every prompt in `prompts/demo-prompts.md` and note the answers.

## Day of — 30 min before
- [ ] Clean browser: only the demo tabs, zoom at 125–150%, notifications off.
- [ ] Terminal with a large font, in the `aws-quick-webinar` directory.
- [ ] Open tabs: AWS Console · Amazon Quick · S3 · GitHub repository · `demo-prompts.md`.
- [ ] Valid AWS session (`aws sts get-caller-identity`).
- [ ] Remove any sensitive data visible in the console (other account names, emails).

## After
- [ ] Share the recording + repository link.
- [ ] Run [Lab 08](labs/08-costs-and-cleanup.md) **before the trial ends** if the account won't be kept.
