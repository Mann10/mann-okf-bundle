---
type: Methodology
title: "Trace-Driven Specification"
description: "A specification derived from execution traces rather than written upfront — the trace of doing the work becomes the blueprint for doing it again."
tags: [agentic-workflows, methodology, specification]
timestamp: 2026-07-23T00:00:00Z
---

# Trace-Driven Specification

## Definition
A specification derived from execution traces rather than written upfront. The trace of doing the work becomes the blueprint for doing it again.

## Two Applications

### 1. Skill Creation
- Execute the task manually with the agent
- Capture every correction
- Ask the agent to write the skill from the trace
- Result: a skill grounded in real failure modes

### 2. Feature Development
- Ideate with the agent (divergent)
- Capture the agreed plan in writing
- Execute against the plan (convergent)
- Result: a feature built from a real discussion, not an imagined requirement

## The Common Thread
In both cases, the specification emerges from interaction, not imagination. You can't know what you need until you've tried to get it.

## Why This Feels Wrong
Most engineering training says "spec first, build second." Trace-driven specification says "build a little, learn, then spec." This is uncomfortable because:
- It feels like wasted work (the first attempt is "throwaway")
- It lacks the certainty of a written spec
- It requires admitting you don't know the answer yet

But the alternative - a spec written from imagination - is guaranteed to be wrong in ways you can't predict.

## Related

- [Execution Traces](/concepts/execution-traces.md) — foundation of this methodology.
- [Progressive Disclosure](/concepts/progressive-disclosure.md) — how traces are structured for skill creation.
- [Agentic Feature Development](/workflows/agentic-feature-development.md) — trace-driven spec applied to features.
- [Skill Creation: Trace-Driven Development](/workflows/skill-creation-trace-driven.md) — trace-driven spec applied to skills.
