# E2 — Independent source-content verification and authenticated API smoke test

**Status (2026-11-03):** E2 verifier implemented and **43 tests passed offline**. A live OpenAI Responses API call was **NOT executed**: neither `OPENAI_API_KEY` nor `OPENAI_MODEL` is configured in the evaluation environment. Do not report the mocked requests as a live API integration. The user's Plus/ChatGPT subscription does not automatically provide this project's API key or billing.

## Execution chain

`Company name -> OpenAIWebResearchProvider.search -> structured claims (drafts) -> independent HTTPS fetch of cited URL -> HTML/PDF text extraction -> OpenAISourceJudge (second structured Responses call over fetched page) -> literal excerpt-presence guard -> per-claim result -> human review`

The verifier returns five terminal **assessment outcomes**: `supported`, `contradicted`, `insufficient`, `source_unavailable`, `conflicting`. All include `requires_human_approval=true`. It **does not mutate** an original research claim into `APPROVED`. No amount, benefit or pre-existing team sponsorship is inferred automatically.

## Verifier safety design

- The source **must** be one of the URLs recorded by the web-search adapter. The original research report has source-ID referential checks.
- Fetches only `https://` links without credentials, alternate ports, redirects, numeric IPs, or DNS resolution to private/non-public IPs; caps response size, page count and time. HTML and text/PDF only.
- **Infrastructure requirement:** a production service must additionally enforce outbound-network egress restrictions against DNS rebinding; an application-level DNS check is not a complete SSRF defense. Host-based allowlisting is also recommended.
- The source is untrusted, including text such as embedded instructions. The independent judge receives no search tool and returns a Pydantic `SourceReview` verdict.
- To count a verdict as `supported` or `contradicted`, its evidence quote must be an exact, contiguous substring of the fetched document with at least 25 characters (whitespace differences allowed). Otherwise, the verdict is downgraded to `insufficient`.
- If supporting and contradicting sources both supply anchored evidence, return `conflicting`.
- A valid literal quote is necessary **but not sufficient**: model interpretation can still be wrong. Management review remains mandatory before publication.
- Sources that are blocked or inaccessible produce `source_unavailable`, not an invented summary.
- A per-run cap of three claims and one URL per claim is the smoke-test default; one required web-search Response + one extraction Response + up to three judgment Responses. Actual tool usage/charges depend on the provider; billing limits must be set at API-account level.

## Reproduction of offline tests

```bash
python -m pip install -e '.[test]'
python -m pytest -q
# 43 passed (Python 3.13, local fixture + mocked OpenAI responses)
```

## Running the REAL integration privately

1. Configure an OpenAI API account with billing/spend limits. Keep the API key out of all commits, shells recorded to shared logs, GitHub issues, PRs and this chat.
2. Install the optional live dependencies from your private checkout.
3. Configure environment variables in the local terminal (do **not** substitute a ChatGPT app session token).

```bash
python -m pip install -e '.[research-openai,test]'
export OPENAI_MODEL='MODEL_WITH_RESPONSES_WEB_SEARCH_AND_STRUCTURED_OUTPUT'
read -rs OPENAI_API_KEY && export OPENAI_API_KEY  # paste the key privately and press Enter
python -m baja_sponsorship.research.live_validation 'Bosch'
unset OPENAI_API_KEY
```

Output is a confidential JSON file under `outputs/research/` with mode `0600`, and terminal summary of identity, source count and verdicts. **No automatic publishing or contacting companies.** The smoke command returns `2` without calling the API when the credential or model is missing.

**How to declare success:** complete authentic search output and URLs recorded; independent pages fetched; structured judge returns at least one properly anchored supported/insufficient assessment; actual tool usage and cost observed in the API account; zero automatically approved claims. A 403/anti-bot/redirect may make sources unavailable and does **not** justify bypassing gates.

## Remaining E2 gates

1. Execute and inspect an authenticated Responses API smoke test with configured billing and a supported model.
2. Evaluate semantic accuracy using a diverse, annotated corpus; quoting a passage alone cannot prove correct entailment.
3. Apply controlled retries, explicit spending limits and production network-egress protections.
4. Test more sectors and date/country conflicts; verify real consent/retention access policy.

## Implementation references

- `src/baja_sponsorship/research/evidence_verifier.py`
- `src/baja_sponsorship/research/http_fetcher.py`
- `src/baja_sponsorship/research/openai_judge.py`
- `src/baja_sponsorship/research/live_validation.py`
- `tests/test_evidence_verifier.py`, `tests/test_http_fetcher.py`, `tests/test_live_validation.py`, `tests/fixtures/bosch_official_short_excerpt.txt`
- API docs: https://developers.openai.com/api/docs/guides/tools-web-search and https://developers.openai.com/api/docs/guides/structured-outputs
