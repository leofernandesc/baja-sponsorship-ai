# E2 — Implementation and test evidence

**Status:** foundation committed on a feature branch; authenticated web research has NOT been run and E2 is NOT fully complete.

## Implemented

- Pydantic 2 models for identity, sources, claims, review states and reports.
- Cross-reference checks; unresolved/ambiguous company identities cannot carry company facts.
- ResearchProvider protocol and standalone ResearchService (no Streamlit).
- Synthetic JSON fixture and offline fixture provider.
- OpenAI Responses web-search adapter with tool URL allowlist, structured extraction and a review-required claim state.
- Local CLI that stores results privately under outputs/research.
- 20 deterministic local pytest cases with synthetic content and mocked API responses.

## Local test evidence

On 2026-11-03, Python 3.13 / Pydantic 2.13.5:

    python -m pytest -q /mnt/data/e2_research_work/tests -c /mnt/data/e2_research_work/pyproject.toml
    20 passed in 0.06s

This was a local test of equivalent files before upload. This is NOT a GitHub Actions result, and does NOT validate real Responses API source objects or factual truth.

## Setup

From a checkout of this branch:

    python -m pip install -e '.[test]'
    python -m pytest -q

Optional real private integration smoke test, subject to authorization and billing limits:

    python -m pip install -e '.[research-openai,test]'
    export OPENAI_MODEL='supported-model-id'
    export OPENAI_API_KEY='set-privately'
    python -m baja_sponsorship.research.cli 'Company Name'

Keep API keys outside Git, and do not place real prospect dossiers in a public repo. The CLI stores JSON outputs in outputs/research (ignored). No email or PowerPoint is generated.

## Remaining before E2 release

1. Validate behavior and source objects against current authenticated Responses API.
2. Verify content of cited pages independently; URL traceability is not content verification.
3. Add bounded retries, rate limits, call/token/cost budgets and safe error handling.
4. Add tests with real public company examples and negative/ambiguous cases.
5. Define private retention/access policy for research histories.
6. Review source age, contradictory claims and regional business-unit correctness.

See also docs/E2_RESEARCH_DESIGN.md.
