# Bundle Log

## 2026-07-23
- **Restructure**: Migrated bundle to conform to Google's Open Knowledge Format (OKF) v0.1 spec.
- **Restructure**: Renamed `videos/` to `workflows/` — files describe actionable workflows, not video content.
- **Update**: Added `type`, `description`, `tags`, `timestamp` to all concept and workflow frontmatter blocks.
- **Creation**: Added `index.md` files for progressive disclosure at bundle root, concepts/, and workflows/.
- **Creation**: Added `log.md` for update history.
- **Update**: Converted YAML-based `related_concepts`/`related_workflows` to standard markdown cross-links in body text.
