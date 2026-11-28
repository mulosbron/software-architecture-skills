---
name: sales-agent-mcp-deployment
description: Deploy a 24/7 Sales Representative AI Agent for a business or SaaS product via MCP server (Claude Desktop/Code) or REST API, enrich its knowledge base, verify domain ownership, and extract structured leads.
---

> **Nested sub-skill of [`agent-harness`](../SKILL.md).** Paths such as `tools/`, `scripts/`, `presets/`, `configs/`, `prompts/`, `templates/` or `tests/` that do not exist inside this folder resolve from the parent skill root (`../`).
# Sales Representative Agent Deployment (MCP & REST API)

Use this skill to rapidly spin up an inbound sales/support layer (Web Chat + WhatsApp) that eliminates lead leakage when founders or agencies are offline.

## Path A: 1-Minute Setup via MCP Server
1. **Configure MCP**: Add the sales agent MCP server entry from `templates/claude_desktop_config.json` into `claude_desktop_config.json` (Settings → Developers → Edit Config).
2. **Provide 3 Required Inputs**:
   - Company Name
   - Website URL (automatically scraped for product/service info)
   - Owner Email
3. **Test Before Claiming**:
   - Test via the generated Web Chat link or WhatsApp deep link.
   - Note: Unclaimed agents display an unverified warning for security.
4. **Enrich Knowledge Base**:
   - Use the `add_knowledge` MCP tool to inject high-conversion assets (e.g., Calendly booking link, custom pricing tiers, FAQ overrides).
5. **Claim & Verify Ownership**:
   - Click the email invite link ("Claim your agent") using an email matching the website domain, then verify in Sandbox Mode.

## Path B: Developer Setup via REST API
1. Generate an API key in Settings → API Access (set expiration, e.g., 30 days).
2. Run `scripts/create_sales_agent_api.sh` to create and deploy the agent directly into the Agent Hub without manual claiming.
3. Embed the customizable Web Chat widget (brand color + bottom-right placement) or connect WhatsApp.

## Inbound Conversation → Structured Lead Pipeline
- Review conversations in the Inbox or process them in batches (handling hundreds of monthly inquiries).
- Extract structured fields per lead:
  - **Intent**: Product inquiry, demo/call booking, or enterprise customization.
  - **Action / To-Do**: Next follow-up step.
  - **Estimated Deal Value**: Flag high-value enterprise leads (e.g., $15K+) for immediate human follow-up.
