# Example Factories

Reference patterns of proven AI factories. Notice how each satisfies all three criteria (**specific, shared, scrutinized**).

## Five Common Factory Archetypes

1. **Customer Experience Factory.** Customers email or open chat tickets. The agent resolves standard inquiries autonomously and escalates edge cases to human specialists.
2. **Presentation Deck Factory.** Shared pipeline for teams that repeatedly produce standardized decks (weekly status, sales briefs, QBRs) from live context.
3. **Bug-Fix Factory.** Production crashes trigger an agent that investigates stack traces, writes a fix, and opens a pull request; adversarial review agents and CI validate before merge.
4. **Data Question Factory.** Team members ask questions (*"How many orders landed last week?"*). The agent clarifies ambiguities, queries the warehouse, and builds an interactive visual summary while analysts audit samples and refine behavior.
5. **Customer Onboarding Factory.** Triggered when a new customer signs; orchestrates multiple repeatable setup steps that need light judgment while keeping execution consistent every time.

## Additional Proven Candidates

- Answering routine customer support emails
- Quality-checking newsletters before send
- Keeping software dependencies up to date
- Fixing small, well-scoped bugs
- Answering recurring analytics/data questions
- Generating simple product announcement clips
- Drafting weekly project updates
- Sales follow-up drafting
- Triaging and prioritizing product feedback
- Employee onboarding checklists
- Invoice and expense processing

## Example Eval Suite: Presentation Deck Factory

An eval suite records representative tasks and explicit grading criteria. Testing only the last observed bug is insufficient because prompt edits often introduce regressions elsewhere.

| Task | Grading Criteria | Judge |
|---|---|---|
| 20-slide sales deck | Slide titles <= 6 words, matches brand tone, includes required pricing table | Code (length/presence) + Human (tone) |
| 3-slide executive summary | Single clear takeaway, metrics pulled from current warehouse data | Code + Human |
| Out-of-template request (negative test) | Factory rejects the request or routes it to human approval | Code |

Always include negative tests and run the full suite on every prompt revision.

## Example Shadow Run: Support Email Factory

- **Stage 1:** Factory touches zero live emails; writes proposed replies into a review table for every incoming ticket.
- **Stage 2:** Humans review 20% of drafted replies and tag failure categories.
- **Stage 3:** Once error rate drops below threshold, ramp live volume from 5% -> 25% -> 100%.
- **Anti-pattern:** Unleashing live sends on 100% of volume on day one.
