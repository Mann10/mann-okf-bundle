---
type: Operational Practice
title: "Build Mode Protocol"
description: "A structured execution phase where an AI agent implements a pre-agreed plan with explicit guardrails against drift and improvisation."
tags: [agentic-workflows, feature-development, execution]
timestamp: 2026-07-23T00:00:00Z
---

# Build Mode Protocol

## Definition
A structured execution phase where an AI agent implements a pre-agreed plan with explicit guardrails against drift and improvisation.

## The Five Rules

### 1. The Plan Is Law
The written plan is the single source of truth. If the agent suggests a different approach, the response is: "Why is this better than what we planned?"

### 2. Small Increments
Don't ask for 500 lines at once. Ask for one function, one test, one file. Review. Merge. Next. Small increments make drift visible before it compounds.

### 3. Refer Back Constantly
"According to our plan, the auth middleware should..." This isn't pedantic. It's the primary anti-drift mechanism.

### 4. When You Go Off Track, Read the Plan
Literally open the markdown file and re-read it. It resets your own thinking too. The plan is as much for you as for the agent.

### 5. Update the Plan Explicitly
If a better approach emerges during build, update the plan first, then implement. The plan is mutable, but not silently.

## Anti-Pattern: Silent Override
The agent implements something not in the plan. You don't notice until code review. Now you have a codebase that diverges from the agreed architecture. This is how technical debt accumulates in agentic workflows.

## The Plan as Contract
The plan isn't documentation. It's a contract between you and the agent. Both parties can refer to it. Both can challenge deviations from it. It exists outside the session, so it survives context loss.

## Related

- [Agentic Ideation](/concepts/agentic-ideation.md) — phase that produces the plan executed here.
- [Session Hygiene](/concepts/session-hygiene.md) — build mode requires a fresh session.
- [Trace-Driven Specification](/concepts/trace-driven-specification.md) — the plan is a trace-driven spec.
- [Agentic Feature Development](/workflows/agentic-feature-development.md) — workflow this practice belongs to.
