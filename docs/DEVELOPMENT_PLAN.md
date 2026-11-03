# Development plan and checkpoints

**Status:** E0 structurally feasible and accepted as a planning basis; residual PowerPoint fidelity/embedded-object checks remain gated in E4. E1 business policy confirmed on 2026-11-03; E1 data approval remains in progress. No dates assigned; phase gates depend on evidence.

## E0 — Repository and PowerPoint feasibility

**Deliverables:** specs, Git workflow, decision register, slide inventory and save/append experiment. E0 audit in `docs/E0_PPTX_AUDIT.md`.

**Tasks:**
- [ ] Bootstrap repository docs and branching conventions.
- [x] Receive and structurally inventory editable source PPTX; identify slide size, masters, layouts, objects, fonts, media and embedded resources.
- [x] Identify preserve-vs-extend requirements and capture source checksum; **final insertion order still pending**.
- [x] Try opening/saving and appending a native slide via `python-pptx`; no difference in original-slide raster under one renderer.
- [ ] Verify typography/editability in PowerPoint with appropriate fonts; address embedded OLE table.
- [ ] Select final rendering/export approach, fallbacks and **approved** template manifest (candidate exists).
- [x] Record initial E0 experiment and constraints; before/after evidence is recorded in audit.
- [ ] Obtain acceptance of final commercial slide treatment and visual output.

**Gate E0:** Baseline accepted; original PPTX unchanged; feasible, documented generation approach. No invented slide count/placements.

## E1 — Institutional knowledge and sponsorship rules

**Deliverables:** 2026/2027 sponsorship policy, source-versioned approved facts, validated tier/benefit catalog, provisional/current technical-needs catalog and private data-handling policy. See `docs/E1_DECISIONS.md`.

**Tasks:**
- [x] Confirm 2026/2027 cycle, while labeling 2025/2026 achievements as historical.
- [x] Approve operational management as institutional, commercial, and final-output authority.
- [x] Confirm official tier names and the hybrid arrangement model; AI may propose financial amounts for approval.
- [x] Confirm three primary support types: money, materials, services; preserve their distinctions in any mixed deal.
- [x] Set existing plan benefits as baseline, with manually approved custom additions.
- [x] Exclude legacy annual budget from recommendations and public project datasets.
- [x] Establish public-repository prohibition for sensitive information; publish schema/docs only.
- [ ] Transcribe and validate current tier boundaries/benefits from embedded 2026 table; resolve gaps.
- [ ] Seed provisional needs from the PPTX and obtain technical confirmation before actual requests.
- [ ] Create controlled private store, protected contact dataset, and update/review workflow.
- [ ] Complete authorization checks for logos and third-party artwork.

**Gate E1:** Commercial taxonomy approved (done); source and private data are not yet fully approved. No live tier classification from ambiguous amount bands, no real requests based on provisional needs, and no public sensitive data.

## E2 — Research and evidence

**Deliverables:** company identification, public web research, auditable evidence records, research report with uncertainty states.

**Tasks:**
- [ ] Resolve company identity from name; request clarification only on real ambiguity.
- [ ] Prioritize primary sources; label secondary sources and opinion separately.
- [ ] Record URLs, access dates, dates of claims and supporting snippets/notes.
- [ ] Detect company-sponsored Baja/SAE and university programs where supported.
- [ ] Add negative, stale and contradictory source tests.

**Gate E2:** No asserted company fact is emitted without linked evidence; invalid/ambiguous names fail safely and clearly.

## E3 — Strategy and hybrid commercial proposal

**Deliverables:** explainable fit assessment and recommended partnership modality.

**Tasks:**
- [ ] Score fit dimensions without representing scores as probability of acceptance.
- [ ] Generate up to three ranked, supported collaboration opportunities.
- [ ] Choose official tier or custom/mixed proposal according to approved rules.
- [ ] Require manual confirmation for unapproved non-standard benefits, prices and brand placement.
- [ ] Separate documented company facts from suggested activities.

**Gate E3:** Recommendation traceable to evidence and current BAJA needs; unsupported benefits blocked.

## E4 — Editable PPTX extension

**Deliverables:** native company extension in copied source PowerPoint with full editable output, optional PDF export.

**Tasks:**
- [ ] Define company-specific layout(s) using original deck theme/master where feasible.
- [ ] Map section fields and text limits to slide shapes.
- [ ] Add visuals only when sourced and authorized.
- [ ] Preserve original institutional slides without unexpected changes.
- [ ] Implement post-export validation: missing fields, text overflow, object loss, layout and image comparison.

**Gate E4:** Original source immutable; every original slide retained; company section native/editable; manual visual inspection passes on test fixtures.

## E5 — MVP Streamlit

**Deliverables:** single-input UI, research report, proposal preview/review, approve and export.

**Tasks:**
- [ ] Implement UI as adapter over a framework-independent service layer.
- [ ] Provide run status and recoverable errors.
- [ ] Save draft and approval history; prevent silent finalization.
- [ ] Display links for the sources of externally-derived claims.

**Gate E5:** End-to-end flow functions from company name, with review and output; non-UI tests work headlessly.

## E6 — Pilot, benchmark and hardening

**Deliverables:** five cross-sector company test cases, defects, scorecards, reproducible test/evaluation report.

**Tasks:**
- [ ] Test automotive, electronics, logistics, materials/manufacturing and retail profiles.
- [ ] Measure factual accuracy, relevance, distinctiveness, layout fidelity, review effort and execution cost.
- [ ] Verify no external factual claim lacks source, nor any unapproved promise.
- [ ] Run regression suite on saved and mock research fixtures.

**Gate E6 — MVP completed:** All critical checks pass, artifacts remain editable, output is visibly customized for each sector, stakeholder accepts quality.

## E7 — React/FastAPI evolution (document now, implement later)

**Preconditions:** actual need for simultaneous users, authentication, approvals or complex dashboards.

**Deliverables:** API contracts, FastAPI backend, React/TypeScript frontend, auth and audit capabilities if needed.

**Gate E7:** Service and domain logic reused; no reimplementation of core generation; E6 acceptance tests still pass.

## Work ordering

E0 -> E1 -> E2 -> E3 -> E4 -> E5 -> E6. E4 rendering feasibility is probed during E0. Independent mock-driven investigations may proceed in parallel, but milestone gates must not be bypassed.

## Definition of Done per milestone

Updated specifications + reviewed implementation + passing relevant tests + reproducible evidence + documented known limitations + review approval. Never claim completion based only on files existing.
