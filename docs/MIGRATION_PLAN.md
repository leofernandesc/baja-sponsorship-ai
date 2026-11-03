# Evolution plan — Streamlit to React/FastAPI

## Product principle

Start with Streamlit to validate product fit and output quality. The target is a more mature multiuser app when usage justifies it. No throwaway core logic.

## Stage A — Streamlit MVP

- Python domain and service modules as isolated package.
- Streamlit calls service methods only; no direct prompt composition or PPTX manipulation in UI event handlers.
- Typed request/response objects; integration tests using mocked providers.
- Local SQLite and filesystem outputs for internal controlled use.

## Stage B — API extraction

- Introduce FastAPI adapters for company research, run status, strategy, proposal draft, approval and export.
- Reuse domain and service package without moving business logic into endpoints.
- Add API contract tests, job execution and result pagination if necessary.
- Introduce authentication and role-based review only when organization requires it.

## Stage C — React frontend

- React + TypeScript consumes the same API contracts.
- Company search input, source/evidence report, proposal editor, review queue and history.
- Test UI workflows against the same backend fixtures.
- Retire Streamlit after parity and user acceptance, not before.

## Stage D — Operational scale, only if justified

- PostgreSQL for concurrency and audit requirements.
- Background job queue for long research/PowerPoint generation runs; robust retries and cancellation.
- Role/permission model, deployment, backups and observability.

## Migration triggers

Multiple simultaneous users, approval delegation, complex editing, collaboration, organization-level access control or burdensome Streamlit workarounds. No fixed-date migration commitment.

## Non-regression requirement

The E6 reference suite must pass unchanged after migration; output PPTX fidelity is independent of frontend choice.
