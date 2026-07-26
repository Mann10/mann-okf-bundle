# Mann's OKF Bundle: Agentic AI Workflows

An [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) bundle of battle-tested patterns for building AI skills and agentic feature workflows. Every claim is tied to a real execution trace, not theory.

## How to use it

Paste this to your AI coding assistant (Claude Code, Cursor, Codex, Gemini CLI, …):

> Here's a knowledge bundle: `https://github.com/Mann10/mann-okf-bundle`
> Clone it and set it up. Read the README first for instructions, then read the root `index.md` only for the gist and mention whats in the gist to user, and stop. Wait for questions. When user ask something, navigate using the `index.md` chain: read a subdirectory's `index.md` first, then read only the pages you need.

That's it — your agent reads the rest of this README, clones the repo, and you can start asking questions about anything I teach.

---

## 1. Setup

```bash
git clone https://github.com/Mann10/mann-okf-bundle
cd mann-okf-bundle
```

## 2. Navigate the bundle

This bundle uses progressive disclosure through its index.md chain:

1. Read `index.md` for the section list
2. Read `knowledge/index.md` to pick between concepts and workflows
3. Read that section's `index.md` to see available pages
4. Read only the pages you need, follow cross-links to dive deeper

## 3. How to answer questions

1. Read `index.md` (or `knowledge/index.md`) to locate the relevant pages.
2. Read the specific files — only what's relevant, not the whole bundle (progressive disclosure).
3. Follow the cross-links between concepts and workflows.
4. Answer grounded in those pages. Cite the source by its `type` + `title` + section heading.

This is read-only reference knowledge — don't modify the bundle.

---

## What's inside

- `index.md` — the table of contents (start here)
- `log.md` — change history
- `knowledge/concepts/` — 6 cross-cutting principles that tie the workflows together
- `knowledge/workflows/` — 2 practical step-by-step methodologies (trace-verified)

## License

MIT — Use the patterns, share the traces.
