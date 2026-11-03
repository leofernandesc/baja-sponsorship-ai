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
