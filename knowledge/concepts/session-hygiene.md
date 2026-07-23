---
type: Operational Practice
title: "Session Hygiene"
description: "The practice of intentionally ending AI conversations and starting fresh ones to prevent context drift, accumulated assumptions, and hallucinated continuity."
tags: [agentic-workflows, operational-practice]
timestamp: 2026-07-23T00:00:00Z
---

# Session Hygiene

## Definition
Session hygiene is the practice of intentionally ending AI conversations and starting fresh ones to prevent context drift, accumulated assumptions, and hallucinated continuity.

## The Drift Problem
In long sessions:
- The agent starts completing your sentences based on pattern matching, not understanding
- Assumptions from hour 1 become "facts" by hour 3
- The agent "remembers" things you never actually said
- Corrections get buried under new context

## Mann's Rule
> "Always start my feature with a fresh session."

This isn't about token limits. It's about cognitive reset. Both you and the agent need to restate what matters.

## When to Start Fresh
- New phase of work (ideation -> spec -> build)
- After a major correction (the correction should be in a plan, not in context)
- When the agent starts "helpfully" doing things you didn't ask for
- When you can't remember what the original request was

## The Plan as Context Carrier
Instead of carrying context in session memory, carry it in a written plan. The plan is:
- Immutable (unless explicitly updated)
- Reviewable (you can read it, the agent can't hallucinate it)
- Portable (works across any session, any model)

## Related

- [Agentic Ideation](/concepts/agentic-ideation.md) — requires a fresh session.
- [Build Mode Protocol](/concepts/build-mode-protocol.md) — requires a fresh session.
- [Agentic Feature Development](/workflows/agentic-feature-development.md) — workflow that enforces session hygiene.
