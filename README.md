# Mann's OKF Bundle: Agentic AI Workflows

Conforms to [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md).

A grounded knowledge base documenting real, battle-tested patterns for building AI skills and agentic workflows. Every claim is tied to a real execution trace, not theory.

## How to use it

Paste this to your AI coding assistant (Claude Code, Cursor, Codex, Gemini CLI, …):

> Here's a knowledge bundle: `https://github.com/Mann10/mann-okf-bundle`
> Read its README and set it up so I can search over it. Then tell me what's inside.

That's it — your agent reads the rest of this README, clones the bundle, and you can start asking questions about anything I teach.

---

## 1. Setup

```bash
git clone https://github.com/Mann10/mann-okf-bundle
cd mann-okf-bundle
pip install -r requirements.txt
python serve/mcp_server.py        # starts MCP server over stdio
```

## 2. Use the MCP server

The server exposes 4 tools. Call them in strict order — the bundle is designed around **progressive disclosure**:

| Order | Tool | What it does |
|-------|------|-------------|
| **1** | `okf_index` | Print the full table of contents, grouped by type. Start here. |
| **2** | `okf_find "<query>"` | Ranked keyword search across all content. |
| **3** | `okf_read <path>` | Read a specific page, e.g. `concepts/execution-traces.md` |
| **4** | `okf_concepts` | Explore how concepts relate (supports / contradicts). |

**You must call `okf_index` first.** Don't `okf_read` without knowing what exists.

(You can also open the markdown files directly — the MCP server is only a convenience.)

## 3. How to answer questions

1. Call `okf_index` (or browse `knowledge/index.md`) to locate relevant pages.
2. Call `okf_read` on only what's relevant — don't read the whole bundle. Progressive disclosure.
3. Follow the cross-links between concepts and workflows.
4. Answer grounded in those pages. Cite the source by its `type` + `title` + section heading.

This is read-only reference knowledge — don't modify the bundle.

---

## What's inside

- `knowledge/index.md` — the table of contents (start here)
- `knowledge/concepts/` — 6 cross-cutting principles that tie everything together
- `knowledge/workflows/` — 2 practical workflows you can follow
- `serve/mcp_server.py` — the MCP server for AI agents to query the bundle
- `serve/CLAUDE.md` — agent consumption protocol (citation rules, trap facts)
- `knowledge/log.md` — change history

## Philosophy

> "I don't write skills. I let the agent write them from what it learned doing the work."

This bundle captures two core bodies of knowledge:
1. **Skill Creation** — How to build AI skills that actually work by deriving them from execution traces, not abstract prompts.
2. **Agentic Feature Development** — A day-to-day workflow for building software features with AI agents, from ideation to delivery.

## License

MIT — Use the patterns, share the traces.
