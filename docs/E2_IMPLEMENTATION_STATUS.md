# E2 — Implementation and test evidence

**Status (2026-11-03):** research and independent semantic-verification foundation committed. **43 offline tests + GitHub Actions pass.** Authenticated Responses API research has **NOT** been run (no API key/model configured here); E2 remains open.

## Implemented

- Pydantic 2 models for identity, sources, claims, review states and reports.
- Cross-reference checks; unresolved/ambiguous company identities cannot carry company facts.
- ResearchProvider protocol and standalone ResearchService (no Streamlit).
- Synthetic JSON fixture and offline fixture provider.
- OpenAI Responses web-search adapter with tool URL allowlist, structured extraction and a review-required claim state.
- Local CLI that stores results privately under outputs/research.
- 20 original deterministic pytest cases with synthetic/mocked API data plus four recorded-public-source Bosch/SAE replay tests.

## Local test evidence

On 2026-11-03, Python 3.13 / Pydantic 2.13.5:

    python -m pytest -q /mnt/data/e2_research_work/tests -c /mnt/data/e2_research_work/pyproject.toml
    24 passed in 0.06s

The suite uses mocked Responses calls and HTML/public-source snippet fixtures; it makes no authenticated API calls or external network requests. The GitHub Actions PR workflow completed successfully at the current implementation commit. Literal-source quote checks and mocked semantic verdicts are exercised, but live judge accuracy is **not established**. See `docs/E2_SEMANTIC_VALIDATION.md`.

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

1. Run authenticated Responses API smoke test using a private API key and supported model; no credentials are available in the execution environment.
2. Implemented conservative independent content fetch, LLM judge and quote-anchor validation; **still needs authenticated live verification and evaluation of semantic correctness**.
3. Add bounded retries, rate limits, call/token/cost budgets and safe error handling.
4. Extend real public-company examples beyond Bosch into electronics/logistics/materials/retail; ambiguity/negative tests currently use mocks.
5. Define private retention/access policy for research histories.
6. Review source age, contradictory claims and regional business-unit correctness.

See also docs/E2_RESEARCH_DESIGN.md.

## E2 semantic verification upgrade (2026-11-03)

Run: `python -m pytest -q` → **43 passed**. Run without configured private credentials: `python -m baja_sponsorship.research.live_validation Bosch` → blocked with exit code 2 **before contacting API**. See `docs/E2_SEMANTIC_VALIDATION.md` for a controlled real test command. No confidential data committed. Production egress/SSRF network controls and spending controls remain pending.
