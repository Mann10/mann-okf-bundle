# Mann's OKF Bundle: Agentic AI Workflows

Conforms to [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md).

A grounded knowledge base documenting real, battle-tested patterns for building AI skills and agentic workflows. Every claim is tied to a real execution trace, not theory.

## How to Use It

Paste this to your AI coding assistant (Claude Code, Cursor, Codex, Gemini CLI, …):

> Here's a knowledge bundle: `My github`
> Read its README and set it up so I can search over it. Then tell me what's inside.

That's it — your agent reads the rest of this README, clones the bundle, and you can start asking questions about anything I teach.

### Setup

```bash
pip install -r requirements.txt   # MCP server dependency
python serve/mcp_server.py        # Start the MCP server
```

### Tools (call in this order)

| Order | Tool | What It Does |
|-------|------|-------------|
| **1** | `okf_index` | List everything available, grouped by type. |
| **2** | `okf_find` | Search across all content by keyword. |
| **3** | `okf_read` | Read a specific file by path. |
| **4** | `okf_concepts` | Explore the concept relationship graph. |

**You must call `okf_index` first** — the bundle is designed around progressive disclosure.

## Philosophy

> "I don't write skills. I let the agent write them from what it learned doing the work."

This bundle captures two core bodies of knowledge:
1. **Skill Creation** — How to build AI skills that actually work by deriving them from execution traces, not abstract prompts.
2. **Agentic Feature Development** — A day-to-day workflow for building software features with AI agents, from ideation to delivery.

## Bundle Structure
```
knowledge/                         # OKF v0.1 bundle root
  index.md                         # Directory listing (progressive disclosure)
  log.md                           # Update history
  concepts/
    index.md                       # Concepts directory listing
    execution-traces.md            # Core principle: traces as spec
    progressive-disclosure.md      # Core principle: stage revelation
    session-hygiene.md             # Operational practice: fresh starts
    trace-driven-specification.md  # Methodology: spec from reality
    agentic-ideation.md            # Operational practice: brainstorm first
    build-mode-protocol.md         # Operational practice: structured execution
  workflows/
    index.md                       # Workflows directory listing
    agentic-feature-development.md # Personal experience: daily workflow
    skill-creation-trace-driven.md # Personal experience: skill method
serve/
  mcp_server.py                    # MCP server — boot this first
  CLAUDE.md                        # Agent consumption protocol
```

## Verification Status

| Workflow | Source | Verified |
|-------|------------------|----------|
| Skill Creation: Trace-Driven | LinkedIn post + execution logs | Manual |
| Agentic Feature Development | Personal workflow documentation | Manual |

## License
MIT — Use the patterns, share the traces.
