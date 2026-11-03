# Codex handoff guide

## Initial work session

1. Inspect the repository, branch and existing files.
2. Read `AGENTS.md`, `README.md`, `specs/technical_specification.md`, `docs/DECISION_LOG.md`, `docs/DEVELOPMENT_PLAN.md`, and `docs/POWERPOINT_EXTENSION.md`.
3. Summarize current milestone and identify blocked external dependencies.
4. Enter plan/review mode before changing code.
5. Do not implement product features until the relevant milestone is approved.
6. Do not commit/push or alter GitHub settings without explicit instruction.

## Suggested first task after source PPTX is provided

**E0 PPTX audit only**. Inventory slides, masters/layouts, objects, fonts and editability; preserve source; test unchanged load/save fidelity; produce `docs/PPTX_AUDIT.md` with evidence and a draft `specs/template_manifest.json` after validation. **Do not generate a new commercial deck yet.**

## Implementation handoff report template

- Scope and accepted requirements.
- Files inspected; files changed.
- Architecture choices and trade-offs.
- Actual commands/tests run and observed outcomes.
- Screenshots/visual evidence where applicable.
- Known risks and unresolved constraints.
- Next milestone recommendation.

## Nonnegotiable rules

Preserve source decks; no fabricated external research or sponsor offers; facts cite sources; requirements belong in spec; stop when review is blocked rather than bypassing acceptance gates.

## Current E0 evidence (03 Nov 2026)

Before modifying presentation behavior, read `docs/E0_PPTX_AUDIT.md`, `docs/POWERPOINT_EXTENSION.md` and `specs/template_manifest.candidate.json`. **Do not auto-fill or ship the source company-specific financial terms on slide 13.** The current source has an embedded OLE/Excel object on slide 12. The test renderer lacks the original fonts. No commercial or visual acceptance has been granted. Keep all original decks in ignored local asset folders, not public GitHub.
