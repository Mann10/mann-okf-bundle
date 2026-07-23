---
type: Personal Experience
title: "Agentic Feature Development: My Daily Workflow"
description: "A three-phase daily workflow for building features with AI agents: Ideation, Specification, and Build Mode, each in a fresh session."
author: "Mann Limbachiya"
timestamp: 2026-07-23T00:00:00Z
tags: [agentic-workflows, feature-development, workflow]
duration: "~8 min read"
verified_transcript: true
---

# Agentic Feature Development: My Daily Workflow

## Opening: Why This Workflow Exists

[00:00] I've tried every approach to building software with AI agents. The one that consistently delivers is not about better prompts or bigger context windows. It's about how you structure the conversation itself.

[00:20] This is my daily workflow. It has three phases: Ideation, Specification, and Build Mode. Each phase has a different session. Each session has a different purpose. The key is never mixing them.

---

## Phase 1: Ideation (Fresh Session, Brainstorm Mode)

[01:00] I always start my feature with a fresh session. Not a continuation of yesterday's work. Not a long-running conversation that has accumulated 50K tokens of drift. A clean slate.

[01:15] **Why fresh sessions matter:**
- Long sessions accumulate assumptions that were never stated
- The agent starts filling in gaps from prior context, not from your actual requirements
- By hour 3 of a session, the agent is "helpfully" completing your sentences - and getting them wrong
- A fresh session forces both of you to restate what matters

[01:45] **The Ideation Prompt:**
I start with something like:
> "I want to build [feature]. Here's the business context: [2-3 sentences]. I want to brainstorm the approach. Don't write code yet. Just help me think through: what are the possible architectures? What are the tradeoffs? What could go wrong?"

[02:30] **What happens in ideation:**
- The agent throws out 3-4 possible approaches
- I push back: "What if we do this instead?"
- We explore edge cases: "What if the user does X?"
- We debate stacks: "Why not use Y instead of Z?"
- We surface constraints I hadn't articulated: "Oh right, we can't do that because of our auth setup"

[03:15] **The rule of ideation:** No code. No implementation. Just thinking. If the agent starts writing a function, I stop it. "We're still in ideation."

---

## Phase 2: Specification (From Brainstorm to Plan)

[04:00] Once we've explored enough, I ask the agent to write a detailed plan.

[04:10] **The specification prompt:**
> "Based on our discussion, write a detailed implementation plan. Include: architecture decisions with rationale, file structure, key functions and their responsibilities, data models, API contracts, error handling strategy, testing approach. Write it as a markdown file I can save and refer to later."

[04:45] **Why I store the plan locally:**
- It becomes the contract for the build phase
- If the agent drifts during build, I can point to the plan: "You agreed to use approach A, not B"
- It lets me switch sessions between ideation and build without losing context
- It forces the agent to commit to decisions rather than improvising

[05:15] **The plan file lives in the repo:**
I save it as `docs/plans/feature-name.md` or `.ai/plans/feature-name.md` depending on the project. This isn't documentation for others - it's a contract between me and the agent.

---

## Phase 3: Build Mode (Execution with Guardrails)

[05:45] Now I switch to build mode. This is a new session. I paste the plan at the top. I tell the agent: "We're executing this plan. Don't deviate without asking."

[06:00] **Build mode rules:**
1. **The plan is law.** If the agent suggests a different approach, I ask: "Why is this better than what we planned?" Sometimes it is. Most times it's drift.
2. **Small increments.** I don't ask for 500 lines at once. I ask for one function, one test, one file. Review. Merge. Next.
3. **Refer back constantly.** "According to our plan, the auth middleware should..." This keeps the agent grounded.
4. **When I go off track, I read the plan.** I literally open the markdown file and re-read it. It resets my own thinking too.

[07:00] **What happens when things go wrong:**
- The agent implements something not in the plan -> I paste the relevant section and say "Stick to the plan"
- I get excited about a shiny new library -> I check the plan: "Did we agree to use this? No."
- The agent forgets an edge case we discussed in ideation -> I open the plan: "We discussed this in section 3.2"

[07:45] **The plan is not a straitjacket.** If we discover a better approach during build, we update the plan first, then implement. The plan is the source of truth, but it's mutable - just not silently.

---

## Why This Workflow Works

[08:00] **Separation of concerns.** Ideation is divergent thinking. Build is convergent execution. Mixing them means the agent is always half-thinking, half-coding. Neither gets done well.

[08:20] **Fresh sessions prevent drift.** A 3-hour session has more hallucination than three 1-hour sessions with a plan. The plan carries context better than token memory.

[08:40] **The plan is the spec, not a wish.** Because it was written after real discussion and debate, it captures real requirements, not imagined ones. It's the trace of the ideation phase.

---

## Key Claims

- [CLAIM 1] Fresh sessions for each phase (ideation, spec, build) produce more reliable output than long continuous sessions.
- [CLAIM 2] A written plan stored locally is a more reliable context carrier than accumulated conversation tokens.
- [CLAIM 3] Separating ideation from build prevents the agent from improvising architecture during implementation.
- [CLAIM 4] Referring back to the written plan during build mode is the primary anti-drift mechanism.
- [CLAIM 5] The plan should be updated explicitly, not silently overridden during build.

## Trap Facts (Hallucination Canaries)

- WRONG: "Long context sessions are better for complex tasks because the agent remembers everything." - The bundle says fresh sessions with stored plans are more reliable because accumulated context drifts.
- WRONG: "You should start coding immediately and iterate as you go." - The bundle says ideation must be separate from build, and coding during ideation pollutes both phases.
- WRONG: "The agent's memory is sufficient to carry requirements across sessions." - The bundle explicitly stores plans locally because agent memory is unreliable.
- WRONG: "Plans are overhead - just tell the agent what to do." - The bundle says the plan is the primary anti-drift mechanism and is essential for reliable delivery.

## Related

- [Agentic Ideation](/concepts/agentic-ideation.md) — the ideation phase of this workflow.
- [Build Mode Protocol](/concepts/build-mode-protocol.md) — the build phase of this workflow.
- [Session Hygiene](/concepts/session-hygiene.md) — fresh-session discipline used throughout.
- [Trace-Driven Specification](/concepts/trace-driven-specification.md) — the plan is a trace of the ideation phase.
- [Progressive Disclosure](/concepts/progressive-disclosure.md) — three-phase structure is a form of progressive disclosure.
- [Skill Creation: Trace-Driven Development](/workflows/skill-creation-trace-driven.md) — companion methodology for skill creation.

# Citations

[1] Personal workflow documentation + execution logs, Mann Limbachiya, 2026.
