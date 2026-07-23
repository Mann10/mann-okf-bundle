# Mann's OKF Bundle: Agentic AI Workflows

An [Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) bundle of battle-tested patterns for building AI skills and agentic feature workflows. Every claim is tied to a real execution trace, not theory.

## How to use it

Paste this to your AI coding assistant (Claude Code, Cursor, Codex, Gemini CLI, …):

> Here's a knowledge bundle: `https://github.com/Mann10/mann-okf-bundle`
> Read its README and set it up so I can search over it. Then tell me what's inside.

That's it — your agent reads the rest of this README, clones the repo, and you can start asking questions about anything I teach.

---

## 1. Setup

```bash
git clone https://github.com/Mann10/mann-okf-bundle
cd mann-okf-bundle
python okf_cli.py index      # confirm it works — prints the table of contents
```

## 2. Use the CLI

```bash
python okf_cli.py index [subpath]     — print an index (start at root; e.g. python okf_cli.py index concepts)
python okf_cli.py find "<query>"      — ranked keyword search across the bundle
python okf_cli.py read <path>         — print a page, e.g. python okf_cli.py read concepts/execution-traces.md
```

(You can also open the markdown files directly — `okf_cli.py` is only a convenience.)

## 3. How to answer questions

1. Run `python okf_cli.py index` (or read `knowledge/index.md`) to locate the relevant pages.
2. Run `python okf_cli.py read` the specific files — only what's relevant, not the whole bundle (progressive disclosure).
3. Follow the cross-links between concepts and workflows.
4. Answer grounded in those pages. Cite the source by its `type` + `title` + section heading.

This is read-only reference knowledge — don't modify the bundle.

---

## What's inside

- `index.md` — the table of contents (start here)
- `log.md` — change history
- `knowledge/concepts/` — 6 cross-cutting principles that tie the workflows together
- `knowledge/workflows/` — 2 practical step-by-step methodologies (trace-verified)
- `okf_cli.py` — the dependency-free navigation/search CLI

## License

MIT — Use the patterns, share the traces.
