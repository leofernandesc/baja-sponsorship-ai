# BAJA Sponsorship AI

AI-assisted sponsorship prospecting and personalized PowerPoint proposal generation for the BAJA UEA engineering team.

**Status:** Planning / E0 feasibility audit (2026-11-03). The editable PPTX files have been inspected; the generation engine is not implemented.

## Product goal

Given only a company name, identify the relevant organization, research reliable public sources, cross-reference approved BAJA UEA information, recommend a hybrid sponsorship approach, and prepare an **editable, reviewable extension of the existing BAJA UEA sponsorship PowerPoint**.

The editable 2026 sponsorship deck (15 slides) is authoritative for presentation structure and visual identity. The company-specific example on original slide 13 must be parameterized and its proposal terms never reused by default. Each generation creates an independent file and adds a small, approved company-specific section. See `docs/E0_PPTX_AUDIT.md` and the candidate manifest.

## Core workflow

1. Identify company (resolve ambiguous names only when needed).
2. Research primary/official sources and collect traceable evidence.
3. Assess strategic fit and possible financial, in-kind, technical and institutional support.
4. Draft company-specific arguments within approved sponsorship rules.
5. Validate factual claims, commercial constraints and presentation compatibility.
6. Review and approve before creating a final editable PPTX; PDF export is optional.
7. Record a reproducible generation history. **No automatic emailing or outreach in the MVP.**

## Confirmed product decisions

- **Single required input:** company name.
- **Commercial policy:** hybrid — official BAJA UEA sponsorship tiers plus tailored partnerships, subject to human approval.
- **Document strategy:** extend the **user-supplied source PPTX** instead of designing a replacement deck.
- **MVP UI:** Streamlit; all domain logic remains framework-independent Python.
- **Target application architecture:** React + TypeScript frontend and FastAPI backend; migrate based on product needs, not simply aesthetics.
- **Research:** public, traceable sources; facts distinguished from proposals and inferences.
- **Output:** internal prospecting report and editable PPTX, with optional PDF export; human review required.

## Planned stack (subject to validation)

Python · Streamlit · OpenAI Responses API (`web_search` and structured outputs) · Pydantic · SQLite · `python-pptx` (conditional on fidelity spike) · pytest. Future: React/TypeScript · FastAPI · PostgreSQL when multiuser complexity justifies it.

`python-pptx` can edit an existing deck and append slides, but cloning arbitrary visually complex slides is limited. A technical fidelity spike is mandatory before committing to a renderer. See `docs/POWERPOINT_EXTENSION.md`.

## Repository map

- `specs/technical_specification.md`: **normative source of truth**.
- `specs/data_contracts.md`: research, commercial and generation contracts.
- `specs/sponsorship_policy.md`: hybrid commercial rules and approvals.
- `docs/DEVELOPMENT_PLAN.md`: milestones, checkpoints and evidence.
- `docs/ARCHITECTURE.md`: logical layers and boundaries.
- `docs/POWERPOINT_EXTENSION.md`: template-extension strategy and fidelity criteria.
- `docs/E0_PPTX_AUDIT.md`: measured PPTX inventory and first compatibility tests.
- `specs/template_manifest.candidate.json`: *non-approved* draft source map.
- `docs/AI_RESEARCH_POLICY.md`: sourcing, uncertainty and content safety.
- `docs/QUALITY_AND_EVALUATION.md`: test and evaluation plan.
- `docs/MIGRATION_PLAN.md`: framework migration path.
- `docs/DECISION_LOG.md`: accepted, proposed and pending decisions.
- `docs/GITFLOW.md`: branching and review rules.
- `docs/CODEX_HANDOFF.md`: instructions for Codex implementation handoff.

## Before development

1. **Source supplied and structurally inspected.** Complete E0 approvals on fonts/rendering, embedded OLE table and extension layout; the local original must remain out of public GitHub.
2. Approve or correct the current BAJA UEA institutional data, technical needs, sponsorship tiers, benefits and contacts.
3. The basic E0 round-trip/append feasibility spike passed, but font/embedded-object correctness is unresolved. Approve a frozen `template_manifest.json` after visual review; `specs/template_manifest.candidate.json` is not normative.
4. Implement in the milestone order documented in `docs/DEVELOPMENT_PLAN.md`.

## Security and assets

Do not commit API keys, real contact lists, private partner conversations, generated proposals, or restricted presentation assets. Use `.env` locally. Validate trademark/logo usage and distribution rights before publishing any official deck. Repository visibility and license require an explicit team decision.

## Reference documentation

- https://platform.openai.com/docs/guides/tools-web-search
- https://platform.openai.com/docs/guides/structured-outputs
- https://python-pptx.readthedocs.io/en/latest/user/presentations.html
- https://python-pptx.readthedocs.io/en/latest/user/slides.html

Current supplied references: editable sponsorship request 2026 (15-slide company-specific example), editable 2026 portfolio (16 portrait slides) and historic 2025 sponsorship PDF (20 pages). **Source files are restricted and must not be published merely because the repository is public.**
