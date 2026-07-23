---
type: Personal Experience
title: "Skill Creation: Trace-Driven Development"
description: "A method for creating AI agent skills by deriving them from real execution traces rather than pre-written prompts or community templates."
author: "Mann Limbachiya"
timestamp: 2026-07-23T00:00:00Z
tags: [agentic-workflows, skill-creation, methodology]
duration: "~5 min read"
verified_transcript: true
---

# Skill Creation: Trace-Driven Development

## Opening: The Problem with Template Skills

[00:00] I downloaded a popular "code review" skill from the community. Sounded great. Automated PR reviews. Set it up and... it worked but not how I needed.

[00:15] It flagged syntax nits. Wrote overly polite feedback. Missed every structural issue my team actually cares about.

[00:30] This is the trap most people fall into: they think the skill is the prompt. They spend hours rewriting prompts, adding more rules, more examples, more constraints. But the skill isn't the prompt. The skill is the accumulated wisdom of what actually worked in real execution.

## The Trace-Driven Method

[01:00] I deleted the skill. Opened a fresh conversation. Ran real PRs through the agent manually.

[01:15] **Step 1: Raw Execution**
- Took a real PR from our repo
- Asked the agent to review it with no pre-written skill
- Watched where it stumbled
- Guided it when it went off track
- Iterated until the output matched what I'd want from a human reviewer

[02:00] **Step 2: Capture the Trace**
Every correction became data:
- "Wait, we also need to check for X" - edge case discovered
- "That's not what I meant, look at line 47" - clarification pattern
- "Actually, we care more about structural coupling than naming" - priority shift
- "Skip the polite fluff, just tell me if it's wrong" - tone calibration

[03:00] **Step 3: Derive the Skill**
Then I asked the agent: "Write a skill from what you learned doing this work."

The whole execution trace became source material. Every correction. Every edge case. Every "wait, we also need to check for X" moment. The agent had lived through all of it.

[03:45] The skill it drafted was grounded in real failures, not imagined ones.

## Why This Works

[04:00] **Skills created this way almost never fail on first run.** Because the spec is the trace, not a wish.

[04:15] The key insight: execution teaches the model what matters in a way that abstract prompting never can.

When you write a prompt, you're describing what you think you want. When you execute and correct, you're showing what you actually need. The difference is the gap between "I think I want polite feedback" and "I actually want direct structural analysis." You only discover that gap through execution.

## The Full Protocol

[05:00] Here's the repeatable protocol:

1. **Delete the template.** Start from zero. No preconceptions.
2. **Run real work through a fresh session.** Use actual PRs, actual tickets, actual code.
3. **Guide, don't prompt.** When the agent goes wrong, correct it. Explain why. Let it learn.
4. **Capture the corrections.** Every "no, that's wrong" is a requirement.
5. **Ask for the skill.** Once the output is good, ask the agent to synthesize what it learned into a reusable skill.
6. **Test the skill on new work.** If it fails, the trace wasn't complete enough. Go back to step 2.

## Key Claims

- [CLAIM 1] Skills derived from execution traces outperform templated skills on first-run accuracy.
- [CLAIM 2] The gap between "what users think they want" and "what they actually need" is only discoverable through execution.
- [CLAIM 3] Corrections during execution are more valuable than pre-written examples because they carry context about why something is wrong.
- [CLAIM 4] The agent that writes the skill from its own trace has better grounding than a human writing a prompt from imagination.

## Trap Facts (Hallucination Canaries)

- WRONG: "Write detailed prompts first, then test them." - The bundle says the opposite: execute first, derive from trace.
- WRONG: "Skills should be built from community templates." - The bundle says templates fail because they carry imagined requirements, not real ones.
- WRONG: "More examples in the prompt equals better performance." - The bundle says examples without execution context are noise.

## Related

- [Execution Traces](/concepts/execution-traces.md) — raw material this method captures and uses.
- [Trace-Driven Specification](/concepts/trace-driven-specification.md) — the methodology formalized from this practice.
- [Progressive Disclosure](/concepts/progressive-disclosure.md) — reveals the skill in stages through execution.
- [Agentic Feature Development](/workflows/agentic-feature-development.md) — companion workflow for feature building.

# Citations

[1] LinkedIn post + personal execution logs, Mann Limbachiya, 2026.
