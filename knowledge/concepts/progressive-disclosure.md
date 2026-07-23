---
type: Core Principle
title: "Progressive Disclosure"
description: "The practice of revealing information to an AI agent in stages rather than dumping everything at once, each stage having a clear purpose and stopping condition."
tags: [agentic-workflows, prompt-design, methodology]
timestamp: 2026-07-23T00:00:00Z
---

# Progressive Disclosure

## Definition
Progressive disclosure is the practice of revealing information to an AI agent in stages rather than dumping everything at once. Each stage has a clear purpose and a clear stopping condition.

## In Skill Creation
1. Show the agent a real task (no skill)
2. Let it attempt, fail, get corrected
3. Only then ask it to synthesize a skill

The agent can't write a good skill until it has experienced the failures the skill is meant to prevent.

## In Feature Development
1. Ideation: divergent thinking, no constraints
2. Specification: convergent planning, written down
3. Build mode: execution, plan is law

Each phase discloses only what's needed for that phase.

## Anti-Pattern: The Dump
Dumping a 5000-token prompt with 20 examples and 50 rules is the opposite of progressive disclosure. It's asking the agent to hold everything in working memory at once. It fails because:
- The agent can't prioritize which rules matter most
- Examples without context are noise
- The agent optimizes for following all rules rather than solving the actual problem

## Related

- [Execution Traces](/concepts/execution-traces.md) — raw material that progressive disclosure organizes.
- [Session Hygiene](/concepts/session-hygiene.md) — fresh sessions are a form of progressive disclosure.
- [Agentic Feature Development](/workflows/agentic-feature-development.md) — three-phase workflow using progressive disclosure.
- [Skill Creation: Trace-Driven Development](/workflows/skill-creation-trace-driven.md) — staged revelation in skill creation.
