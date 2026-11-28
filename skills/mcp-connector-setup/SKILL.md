---
name: mcp-connector-setup
description: Step-by-step guide and troubleshooting workflow for connecting external apps (Gmail, Google Drive, Calendar, Zapier MCP, PayPal, QuickBooks) to Claude via native connectors or Custom Remote MCP servers.
---

# MCP & External App Connector Setup Skill

## Purpose
Connect Claude to external SaaS tools (e.g., QuickBooks, Gmail, Google Drive, Calendar, PayPal, CRM) using either native connectors, Zapier MCP, or a direct Remote MCP server.

## Decision Tree
1. **Check Native Connectors First**:
   - Go to **Settings -> Connectors** (or click the `+` menu in chat).
   - Enable built-in integrations directly: **Google Drive**, **Gmail**, **Google Calendar**, **GitHub**, **PayPal**, **Zapier**.
2. **Need an App Without a Native Connector (e.g., QuickBooks)?**
   - **Option A — Zapier MCP Bridge (Fastest)**:
     1. Connect the target app (e.g., QuickBooks) to your Zapier account.
     2. Add **Zapier** as an MCP connector inside Claude.
     3. Expose only the specific Zapier actions you need.
   - **Option B — Direct Remote MCP Server**:
     1. Check if the vendor publishes an official Remote MCP server URL.
     2. In Claude, click **Add Custom Connector** and enter the Remote MCP server URL + OAuth/API credentials.
3. **Self-Guided Setup Hack**:
   - Copy the vendor's MCP documentation page text, paste it into Claude, and ask: *"Walk me through connecting this MCP step by step and flag any required permissions or security settings."*
