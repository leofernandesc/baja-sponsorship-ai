# E2 — Company research and evidence management

**State:** E2-A offline schema implemented and tested; E2-B mocked live-provider adapter implemented, real API integration unverified. E1 commercial validation is not a prerequisite for this independent milestone.

## Scope

Given just the company name:
1. Normalize input and reject missing or excessively long inputs.
2. Resolve company identity and relevant regional unit. If ambiguous, return candidates without making company-specific claims.
3. Research the official website, public business activities, technologies, education programs, sponsorship history, Baja SAE/SAE involvement and official sponsorship channels when documented.
4. Collect actual web-search URLs with titles, access timestamps and publication dates when available.
5. Build explicit fact/inference/proposal statements linked to known source IDs.
6. Expose unknowns and limitations for subsequent human review.

This stage does not define sponsor tiers, values, benefits, or specific parts requests. E1 unapproved information stays out of the E2 research pipeline.

## Evidence policy

A URL being present in a tool response is not proof that an assertion is supported. Source-linked candidates must be reviewed for meaning, context and recency before being approved and sent externally. Only operational management can approve facts for use in a final proposal. The generation service must reject facts with unknown evidence IDs and cannot pass ambiguous identities downstream.

Evidence hierarchy: official company sites and filings; SAE or universities for their own announcements; reputable independent reporting; other sources only as discovery leads.

## Implementation boundary

- Pydantic models and ResearchService are independent of Streamlit.
- ResearchProvider is replaceable and can be mocked.
- Optional Responses API provider invokes hosted web_search with tool_choice=required and requests returned sources.
- Citation extraction forms an explicit URL allowlist; structured extraction may reference only these URLs. References outside it are discarded.
- No automatic approval, emailing, or proposal generation in E2.
- Reports are written locally under outputs/research and ignored by Git. They are never committed to this public repository.

## E2 submilestones

**E2-A (offline core):** typed models, unique source IDs, claim-source cross checks, disambiguation guards, mock fixtures. Implemented and tested.

**E2-B (connector):** web-search adapter and structured-extraction mock tests implemented. Remaining: real API integration, citation semantics, source trust classification, retry and cost budgeting, defensive error handling.

**E2-C (quality gate):** inspect primary sources and validate real company research, stale/contradictory evidence, identity ambiguity and report relevance. Pending.

## Acceptance

Company input is a single name. No known company fact lacks a real cited source. No hallucinated source links are accepted. Non-resolved identities do not yield outbound claims. Actual content support must be independently checked. Sensitive BAJA institutional/commercial files are not committed publicly.

## Official API documentation

https://developers.openai.com/api/docs/guides/tools-web-search
https://developers.openai.com/api/docs/guides/structured-outputs
