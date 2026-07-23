---
type: Operational Practice
title: "Agentic Ideation"
description: "Using an AI agent as a thinking partner during feature exploration, with explicit rules that prevent premature implementation and code generation."
tags: [agentic-workflows, feature-development, ideation]
timestamp: 2026-07-23T00:00:00Z
---

# Agentic Ideation

## Definition
Using an AI agent as a thinking partner during the exploration phase of feature development, with explicit rules that prevent premature implementation.

## The Rule: No Code in Ideation
The most important rule of agentic ideation: if the agent starts writing code, stop it. "We're still in ideation."

## Why This Matters
When an agent starts coding during ideation:
- It commits to implementation details before architecture is settled
- It optimizes for "working code" rather than "right architecture"
- It stops exploring alternatives ("this works, let's ship it")
- It creates sunk-cost bias ("we already wrote this function")

## The Ideation Prompt Pattern
```
I want to build [feature].
Business context: [2-3 sentences].
I want to brainstorm the approach.
Don't write code yet.
Help me think through: architectures, tradeoffs, risks.
```

## What Good Ideation Looks Like
- The agent throws out multiple approaches
- You push back and propose alternatives
- Edge cases surface naturally
- Stack decisions are debated, not assumed
- Constraints emerge from discussion, not from prior knowledge

## When Ideation Is Done
Ideation is done when you can write a plan that the agent agrees is complete. Not when you have working code. When you have a plan.

## Related

- [Session Hygiene](/concepts/session-hygiene.md) — ideation requires a fresh session.
- [Build Mode Protocol](/concepts/build-mode-protocol.md) — execution phase after ideation.
- [Progressive Disclosure](/concepts/progressive-disclosure.md) — ideation is the first stage of progressive disclosure.
- [Agentic Feature Development](/workflows/agentic-feature-development.md) — workflow this practice belongs to.
