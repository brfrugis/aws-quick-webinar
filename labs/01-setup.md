# Lab 01 — Setting up Amazon Quick

⏱️ 15 min · 🎯 Enable Amazon Quick in your AWS account, understand the authentication options and invite users.

> ⚠️ **Costs:** the first subscription includes a **30-day trial for up to 25 users**. When the trial ends, billing starts automatically. If you're only learning, write down the date and follow [Lab 08](08-costs-and-cleanup.md) to cancel.

## 1. Open Amazon Quick in the console
1. Sign in to the [AWS Console](https://console.aws.amazon.com/).
2. In the search bar, type **Quick** (the service also appears under *Analytics*).
3. Click **Sign up**. Your AWS account number is displayed for verification.

## 2. Fill in the subscription
| Field | What to enter | Why |
|---|---|---|
| **Quick account name** | `aurora-demo-<your-name>` | Must be unique; used to sign in |
| **Notification email** | your email or a group's | Receives service and usage notifications |
| **Region** | e.g., `us-east-1` | Where your data lives (SPICE). Use the same region as S3 |
| **Authentication method** | see the table below | Not trivial to change later |

### Which authentication method should I choose?
| Option | When to use |
|---|---|
| **Password-based or Single Sign-On** (recommended on screen) | POCs and small teams: users with email/password plus an SSO option |
| **IAM Identity Center** | Companies that already centralize identities (Entra ID/Azure AD, Okta, Google) in Identity Center. Assignment by **groups** |
| **Single Sign-On only** | Federation via SAML/IdP, no local passwords |
| **Active Directory** | AD integration (legacy scenarios) |

> For the webinar and for learning, use **Password-based or Single Sign-On**. For production, prefer **IAM Identity Center** with groups (e.g., `quick-admins`, `quick-authors`, `quick-readers`).

4. Review and click **Create account**.
5. When it finishes, click **Go to Quick**.

## 3. Get to know the home page
- **Top bar:** search, chat with the Quick agent, region, user menu.
- **Left menu:** Agents, Spaces, Flows, Automations, Research, Dashboards, Analyses, Topics, Data, Actions, among others.
- **User menu → Manage Quick:** administration (users, subscription, security, SPICE).

> Menu names may change with service updates. If something looks different, search for it by name in the top bar.

## 4. Invite users
1. User menu → **Manage Quick** → **Manage users** → **Invite users**.
2. Add an email address and choose the role:

| Role | Can |
|---|---|
| **Admin** | Everything, including users, subscription and security |
| **Author** | Create datasets, analyses, dashboards, agents, flows |
| **Reader** | Use shared dashboards, agents and flows |

3. The invitee receives an email to activate access.

## 5. (Optional) Security settings
Under **Manage Quick → Security & permissions**:
- **AWS resources:** which services (S3, Athena, Redshift…) Quick can access. We'll use this in Lab 04.
- **Encryption:** AWS-managed keys by default; you can use KMS keys instead.

## ✅ Validation
- [ ] You can open Amazon Quick and see the left menu.
- [ ] Under **Manage users**, your user is listed as **Admin**.

## 🛠️ Common issues
| Symptom | Likely cause | Fix |
|---|---|---|
| "You are not authorized…" when subscribing | Missing IAM permission or an SCP blocking it | Use an admin user/role or adjust the SCP |
| Account name unavailable | Name already taken globally | Add a suffix |
| IAM Identity Center option missing | Identity Center not enabled in the account/region | Enable Identity Center or use the password option |

📚 [Signing up through the AWS Console](https://docs.aws.amazon.com/quick/latest/userguide/signing-up.html)

➡️ Next: [Lab 02 — Sample data](02-sample-data.md)
