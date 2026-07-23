---
type: Core Principle
title: "Execution Traces"
description: "A complete record of an AI agent attempting a task, used as the foundation for deriving skills and specifications from real outcomes rather than imagined requirements."
tags: [agentic-workflows, skill-creation, methodology]
timestamp: 2026-07-23T00:00:00Z
---

# Execution Traces

## Definition
An execution trace is the complete record of an AI agent attempting a task, including:
- The initial prompt or request
- The agent's first attempt
- Every correction, clarification, or redirection from the human
- The final successful output
- Edge cases discovered along the way

## Why Traces Beat Prompts

A prompt is a hypothesis about what will work. A trace is proof of what did work.

| Prompt | Trace |
|--------|-------|
| Imagined requirements | Real requirements |
| Generic examples | Specific corrections |
| Assumed edge cases | Discovered edge cases |
| Theoretical best practices | Proven patterns |

## The Trace as Specification

In trace-driven development, the trace IS the specification. When you ask an agent to "write a skill from what you learned," you're asking it to generalize from real data rather than imagine from first principles.

## Key Insight
> "The spec is the trace, not a wish."

This applies beyond skill creation:
- API design: build the endpoint first, derive the contract from real usage
- Testing: observe real failures, write tests that would have caught them
- Documentation: write docs from what users actually asked, not what you think they need

## Related

- [Trace-Driven Specification](/concepts/trace-driven-specification.md) — methodology that follows from this principle.
- [Progressive Disclosure](/concepts/progressive-disclosure.md) — how traces are best revealed in stages.
- [Skill Creation: Trace-Driven Development](/workflows/skill-creation-trace-driven.md) — practical application of execution traces.
