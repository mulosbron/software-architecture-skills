# Factory Candidate Traits

Workflow suitability for an AI factory is evaluated across seven traits. `scripts/factory_blueprint.py check` scores these traits. The goal is never to remove humans from the process — it is to elevate them into ownership, judgment, and accountability above the assembly line. Every report should reflect this framing.

## The Seven Traits

1. **Recurring.** The task arrives repeatedly in the same form (weekly status reports, daily support emails, dependency updates).
2. **Verifiable.** Output quality can be checked against clear criteria (headline length, tone, required fields). Without verifiability, you cannot build evals.
3. **Stable over time.** The process and requirements stay relatively consistent. Work whose rules change completely every time is a weak factory candidate.
4. **Standard quality is sufficient.** Reliable, solid execution is the target rather than one-off genius creativity. Where human originality is the core value, automation is the wrong goal.
5. **Fully digital knowledge work.** Robotics and physical-world operations are outside this methodology.
6. **Known information universe.** The sources the agent must consult are bounded and known. If the knowledge universe shifts unpredictably every run, the agent gets lost.
7. **Low cost of mistakes.** Errors are inexpensive or easy to catch before impact. High-cost workflows require strict shadow runs and gradual permission ramps.

## Score Interpretation

- **6–7 points:** Strong candidate. Proceed to the blueprint phase.
- **4–5 points:** Conditional candidate. Check whether missing traits can be mitigated (for example, if verifiability is weak, define a grading checklist first).
- **0–3 points:** Weak candidate. Do not automate; document why keeping it manual is the right call.

## Factory vs. Non-Factory

An agent setup is a factory only when it satisfies all three criteria: **specific** (one defined class of tasks, not everything), **shared** (used by multiple people), and **scrutinized** (named owners track performance and improve it).

Therefore:
- A personal generalist agent asked to do every task is **not** a factory (not specific).
- A private agent relying on one person's memory or local instructions is **not** a factory (not shared).
- A shared agent nobody monitors or evaluates is **not** a factory (not scrutinized).

Skill files are *proto-factories*: they share instructions, but they do not yet share live context, compute, or ongoing scrutiny.

## Human Involvement

A factory does **not** mean an unsupervised "lights-out" factory. Many steps still require human judgment and creativity. Decide explicitly where humans review, approve, or intervene, and record that boundary in the blueprint.
