# Architecture

## Guiding principle

A modular, backend-first Python application with user interfaces as replaceable adapters. Streamlit is not allowed to own domain rules or orchestrate model outputs directly.

## Logical pipeline

```text
Company name (UI)
  -> Company resolver
  -> Research connector (public web)
  -> Evidence store and normalizer
  -> BAJA institutional fact store (versioned)
  -> Strategic-fit evaluator
  -> Hybrid-commercial recommender
  -> Structured proposal writer
  -> Factual + business-rule validator
  -> Human review / approval
  -> PPTX extension renderer
  -> Editable PPTX + optional PDF + run history
```

## Domains

- **Company identity**: canonical name, sector, country, official URLs; disambiguation when essential.
- **Evidence**: assertion, source, publication/capture timestamps, verification state.
- **BAJA knowledge**: official, versioned team facts; technical needs; approved capabilities and tiers.
- **Strategy**: ranked fit dimensions, clearly marked inferences, possible collaboration models.
- **Commercial policy**: approved official tier IDs and custom proposal approvals.
- **Proposal**: page/slide section structure, editable text, source-to-claim mapping, approval state.
- **Document rendering**: PPTX source, manifest, slide generator, visual checks.

## Adapter boundaries

- `src/baja_sponsorship/domain`: dataclasses/Pydantic models, invariants.
- `src/baja_sponsorship/services`: workflow, research, scoring, generation, validation.
- `src/baja_sponsorship/adapters`: OpenAI, web, storage, PPTX, future integrations.
- `src/baja_sponsorship/ui`: MVP Streamlit interface only.
- `api/`: future FastAPI routes (not implemented in MVP).
- `web/`: future React/TypeScript frontend (not implemented in MVP).

## Planned storage

SQLite initially; migration to PostgreSQL if multiuser, concurrent, audited usage warrants it. Store metadata and evidence pointers, avoid persisting unneeded sensitive content.

## API/provider abstraction

Create a `ResearchProvider` and `ModelProvider` interface; default implementation may use OpenAI Responses API with hosted web search and structured outputs. Do not hard-code model IDs or prompt text into UI components. External pages are untrusted input. Model output is always validated by domain constraints.

## Reliability

Each stage emits immutable or versioned artifacts with run identifiers. Retries must not duplicate approved proposals. Persist failure reason and last successful stage; source, prompt and token/cost metrics support reproducibility.

## Architectural validation

A headless CLI/test must be able to run research-to-draft with mocks and without importing Streamlit. This is the primary migration readiness check.
