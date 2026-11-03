# Decision log

Decision states: `APPROVED` (explicitly selected), `PROPOSED` (working assumption), `OPEN` (awaiting evidence/approval).

| ID | State | Decision / rationale |
|---|---|---|
| D-001 | APPROVED | Repository name `baja-sponsorship-ai` (repository created by user). |
| D-002 | APPROVED | Only required user input is company name; disambiguation is exceptional. |
| D-003 | APPROVED | Hybrid sponsorship: official tiers plus custom financial, in-kind, technical and institutional partnership. |
| D-004 | APPROVED | The generated proposal **extends** the source BAJA UEA PPTX; it must not replace the original slide system. |
| D-005 | APPROVED | Start with Streamlit; document React/TypeScript + FastAPI migration from the beginning. |
| D-006 | APPROVED | Source evidence and institutional facts must be separated; human review before final output. |
| D-007 | PROPOSED | Python package domain/services/adapters with Pydantic and SQLite; framework-independent core. |
| D-008 | PROPOSED | OpenAI Responses API for web research and structured output. |
| D-009 | PROPOSED | `python-pptx` if E0 fidelity spike is acceptable; otherwise evaluate alternate PPTX pipeline. |
| D-010 | PARTIALLY_RESOLVED | Source PPTX inspected: 15 slides, 16:9; example commercial content on slide 13. Candidate 1–2 slides before 13. Exact insertion point/count requires review. |
| D-011 | OPEN | Updated tier amounts/benefits; owner approvals; authorized image/logo usage. |
| D-012 | OPEN | GitHub repository **confirmed public**. No source PPTX/PDF, logo collections, contacts, or example commercial assets will be committed until BAJA authorizes disclosure. License still open. |
| D-013 | PROPOSED | `main` and `develop` branches, feature branches, reviewed squash PRs. |
| D-014 | APPROVED | Focus is currently the implementation plan and documentation, not coding the product. |
| D-015 | PROPOSED | Introduce company-fit and collaboration slide(s) before slide 13; parameterize slide 13; do not reuse any source-specific financial amount. |
| D-016 | PROPOSED | Keep the OLE sponsorship table as read-only temporarily; replace with native editable table only after official price/benefit approval. |
| D-017 | APPROVED | Basic `python-pptx` load/save and append are technically feasible; final rendering pipeline is not yet approved due to missing fonts and OLE export issues. |

## Update protocol

New decisions use an ID, justification, alternatives, impacts, approver and date. Update specifications and tests for material changes. Do not silently promote PROPOSED/OPEN to APPROVED.

## E1 accepted decisions — 2026-11-03

| ID | State | Decision / rationale |
|---|---|---|
| D-018 | APPROVED | Sponsorship cycle is 2026/2027; 2025/2026 metrics remain historically labeled, confirmed for use. |
| D-019 | APPROVED | Institutional data steward, custom proposal approver and final proposal reviewer are the **operational management** role. |
| D-020 | APPROVED | Money, materials and services are the three primary support types. Mixed sponsorship may combine them. |
| D-021 | APPROVED | Official Diamante/Ouro/Prata/Bronze/Apoio tiers remain; AI may propose financial amounts subject to approval. |
| D-022 | APPROVED | Materials/services receive their own classifications; do not auto-convert either to financial tiers. |
| D-023 | APPROVED | Initial technical needs derive only provisionally from uploaded PPTX, until validated current inventory arrives. |
| D-024 | APPROVED | Exclude legacy annual budget from knowledge, reasoning, arithmetic and recommendations. |
| D-025 | APPROVED | Existing tier-plan benefits are the only baseline; additional and tailored benefits require explicit approval. |
| D-026 | APPROVED | Current contact records confirmed by the team, but must remain in private runtime storage, not public GitHub. |
| D-027 | APPROVED | No sensitive data may be publicly accessible through repository, branches, PRs, issues or artifacts. |
| D-028 | OPEN | Resolve numeric range gaps and benefit transcription of the OLE table before auto tier matching. |
| D-029 | OPEN | Technical-needs validation, private data store and publication rights for logos/documents. |

Previous decisions D-011/D-012 are refined by these decisions: owner role and confidentiality are now established, while detailed commercial tables and asset permission remain open. See `docs/E1_DECISIONS.md`.
