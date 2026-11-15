---
name: modeling-threats-and-privacy
description: Use when threat-modeling trust boundaries with STRIDE or designing schemas, APIs, and logs that handle personal or sensitive user data.
---

# Modeling Threats and Privacy

## Goal
Identify trust-boundary risks and embed data minimization, retention limits, and user-data protections into architecture before shipping.

## Repo defaults
- **STRIDE per trust boundary.** Map assets and data flows (external, internal, data boundaries) and assign concrete controls before launching auth, payments, or external APIs (`protecting-and-sizing-apis`).
- **Privacy by design and default.** Collect only justified fields (`purpose`), turn optional analytics/marketing off by default, encrypt in transit/at rest, and automate `retention_days` purge/anonymization.
- **Redact PII from logs and telemetry.** Never log raw emails, tokens, secrets, or personal identifiers.

## Boundaries
- Do not store personal data "indefinitely" or send user data to third-party SDKs without explicit consent.
- Account deletion must cover primary stores and downstream/backup retention policies.
- Record trust-boundary and compliance architecture decisions via `python tools/arch_tools.py adr-new`.

## Done when
- Assets, trust boundaries, STRIDE threats, and mitigations are documented.
- Schemas specify field purpose, encryption/access controls, and automated retention periods.
- Access, rectification, portability export, and erasure paths are verified.
