# Technical specification — v0.1 (planning)

**Status:** Partially approved. This is the normative document; unresolved items are marked `OPEN`.

## 1. Purpose

Generate a company-specific, sourced, commercially valid BAJA UEA sponsorship PowerPoint **as an extension of the team's original editable PPTX**, from a single company-name input.

## 2. Confirmed functional requirements

- **FR-001:** Require only `company_name` for an ordinary generation.
- **FR-002:** Identify correct company; if materially ambiguous, ask for disambiguation.
- **FR-003:** Search publicly available information, capturing sources and dates.
- **FR-004:** Use a versioned and reviewed BAJA UEA knowledge base.
- **FR-005:** Distinguish verified facts, analytic inferences, custom offers and unknowns.
- **FR-006:** Recommend sponsorship via an approved **hybrid** approach (official tiers and tailored financial/in-kind/technical/institutional cooperation).
- **FR-007:** Block unapproved prices, tiers, brand promises, legal claims and special benefits.
- **FR-008:** Produce an internal prospecting report with evidence citations and strategic assessment.
- **FR-009:** Draft a company-specific proposal using the existing BAJA UEA PowerPoint as the immutable base; add editable company-specific slides.
- **FR-010:** Validate factual content, business policy, and PPTX visual/content integrity.
- **FR-011:** Require explicit human approval before final-status delivery.
- **FR-012:** Maintain generation/version/approval history and permit optional PDF export.
- **FR-013:** Do not automatically send emails, submit contact forms or approach companies in the MVP.

## 3. Confirmed architecture requirements

- **AR-001:** MVP presentation layer uses Streamlit.
- **AR-002:** Domain and service layers are framework-independent Python.
- **AR-003:** React/TypeScript and FastAPI are the documented future architecture, not a blocking MVP requirement.
- **AR-004:** Model and research providers are replaceable adapters.
- **AR-005:** Structured model output is validated against schemas and domain/business rules.
- **AR-006:** Source PPTX stays unchanged; all outputs are derived copies.

## 4. Proposed nonfunctional targets (review before implementation)

- **NFR-001:** Reliable evidence traceability for every company-specific factual claim.
- **NFR-002:** Reproducible test runs using cached/mocked research fixtures.
- **NFR-003:** No secrets in repository or logs; minimal sensitive-data retention.
- **NFR-004:** Robust failure states and bounded retries; no invented content on failures.
- **NFR-005:** Editable PowerPoint output; source slides visually preserved.
- **NFR-006:** Multi-provider/testable architecture that does not import Streamlit in core modules.

## 5. Commercial policy

See `specs/sponsorship_policy.md`. Official tiers must be verified and gap-free before use. Customized proposals may suggest forms of cooperation but never bind the team without approval.

## 6. PPTX extension

See `docs/POWERPOINT_EXTENSION.md`. The source PPTX is pending. Slide count, insertion locations, template manifest and compatibility matrix are OPEN until inspection.

## 7. Milestones

See `docs/DEVELOPMENT_PLAN.md` (E0–E7). MVP accepted at E6; React/FastAPI migration tracked as E7.

## 8. OPEN decisions

- Original editable PPTX source + technical inventory.
- Exact number/sequence of appended slides and variable fields.
- Final current sponsorship tiers, values, cumulative benefits and approval owners.
- Current technical priorities and legitimate in-kind needs.
- Publication rights for original deck and third-party logos.
- Repository visibility and license.
- MVP deployment target and number of internal users (not needed for E0).

## 9. Change control

Treat approved requirements as frozen. Any incompatible change requires explicit decision log entry, changed spec version, affected test update and review.
