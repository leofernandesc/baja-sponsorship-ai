# E2 — Real-world Bosch research validation (03 Nov 2026)

**Status: PARTIAL VALIDATION.** Independent public web research and evidence-to-claim checks were performed; an authenticated call through the implemented OpenAI Responses adapter **was not performed** (no `OPENAI_API_KEY` or `OPENAI_MODEL` configured in the test environment). E2 issue remains open. No company contacted.

## Scope and method

- Input: `Bosch`; resolved scope: **Bosch group, Brazilian operations**.
- Sources examined on 2026-11-03: Bosch Brazil corporate/company pages, official contact/sponsorship guidance, SAE BRASIL's legacy official announcement of the 31st Baja SAE Brazil competition, and 2026 SAE official almanac.
- Checked whether each *specific assertion* was supported by the cited source, whether the source concerned Bosch in Brazil vs the global group, and whether event sponsorship was confused with team sponsorship.
- This is a **human-driven live web source audit**. It is not evidence that the app's `OpenAIWebResearchProvider` executed against a live OpenAI API.
- An offline replay with those real public URLs and synthetic Responses object envelopes is covered in `tests/test_bosch_real_source_replay.py`.

## Verified findings and sources

| ID | Statement | Evidence | Verdict | Caveat |
|---|---|---|---|---|
| B-01 | Bosch is active in Brazil and operates in mobility, industrial technology, consumer goods, and energy/building technology. | https://www.bosch.com.br/nossa-empresa/bosch-no-brasil/ | SUPPORTED | Official self-description; do not infer availability of any specific Bosch division for sponsorship. |
| B-02 | Bosch's global mobility activities include sensors, control units, semiconductors, powertrain and off-road vehicles. | https://www.bosch.com.br/nossa-empresa/grupo-bosch-no-mundo/ | SUPPORTED | Product/global business description; does not mean products can be donated to BAJA UEA. |
| B-03 | Bosch Brazil accepts corporate sponsorship requests **without tax incentive** through its official form and states an analysis/response window of three months. | https://www.bosch.com.br/contato/ | SUPPORTED | The form is linked from this page. It is not a promise of sponsorship or response acceptance. |
| B-04 | Bosch Brazil states that non-incentivized corporate sponsorship proposals must relate to business areas such as mobility, technology and innovation, sustainability or agribusiness. | https://www.bosch.com.br/contato/ | SUPPORTED | Location restriction explicitly described for *incentivized* projects must **not** be generalized to every non-incentivized request. Eligibility beyond the page remains unknown. |
| B-05 | Bosch sponsored the **31st Baja SAE BRASIL national event in March 2026**. | https://legado.saebrasil.org.br/competicao-baja-sae-brasil-etapa-nacional-2026-tem-62-equipes-inscritas/ and https://arquivos.saebrasil.org.br/2026/BajaNacional/AlmanaqueBajaSAE2026.pdf | SUPPORTED | The event sponsorship is not proof of direct sponsorship of BAJA UEA. |
| B-06 | In the SAE official 2026 event almanac Bosch appears under **event-level "Patrocínio Prata"**. | https://arquivos.saebrasil.org.br/2026/BajaNacional/AlmanaqueBajaSAE2026.pdf (PDF page 2) | SUPPORTED | SAE event tier is NOT the BAJA UEA team's sponsorship tier and must never be mapped into the team's offer. |
| B-07 | BAJA UEA is listed as a team from Amazonas among event entries. | https://legado.saebrasil.org.br/competicao-baja-sae-brasil-etapa-nacional-2026-tem-62-equipes-inscritas/ | SUPPORTED | Team entered the event; does not prove a direct partnership with any event sponsor. |

## Explicitly unsupported or prohibited assertions

| Candidate claim | Verdict | Action |
|---|---|---|
| “Bosch already sponsors BAJA UEA directly.” | NOT SUPPORTED by the checked sources | Reject; SAE event sponsorship ≠ direct team sponsorship. |
| “Bosch will donate sensors/tools or approve a particular amount.” | NOT SUPPORTED | Reject; source product catalog or sponsorship form ≠ commitment. |
| “The three-month analysis period guarantees acceptance.” | FALSE INFERENCE | Reject; the page describes review/response, not approval. |
| “Project location in Amazonas prohibits non-incentivized corporate sponsorship.” | NOT SUPPORTED by the stated rules | Do not infer a categorical geographical exclusion from rules specific to incentivized projects. |
| “SAE Prata sponsorship is equivalent to BAJA UEA Prata tier.” | FALSE CONFLATION | Reject; different institutions' categories. |

## Source-quality anomalies and limitations

- The newer SAE news page responded **HTTP 403** when opened directly in the search environment. The **official SAE legacy page** was accessible and carried the same claim; the official almanac PDF independently confirms Bosch's event sponsorship.
- The SAE 2026 almanac displays a likely **2029 date typo on its second PDF page** despite a 2026 title/event branding and a separate SAE March 2026 announcement. Prefer the dated SAE news article for event date and flag the almanac discrepancy instead of copying the 2029 figure.
- Some company site pages use globally scoped group descriptions; a Brazil-specific claim requires a Brazil source or explicit scope label.
- OpenAI Research Provider currently checks **source URL provenance**, not semantic support. A fabricated claim attached to a genuine URL can pass as `source_linked` but must **not** become `approved` without a separate verification gate.
- In the current adapter, all source types are output as `other`; official/SAE classification is a remaining enhancement.
- Search cost/token ceilings, live provider shape compatibility, source age/conflict handling, and protected report retention remain unverified.

## Local reproducible tests

Command (existing tests plus the new recorded-source replay):

```bash
python -m pytest -q
# 24 passed in 0.06s (Python 3.13, Pydantic 2.13.5, pytest 9.0.2)
```

Replay confirms: observed source links are recorded; three supported public-source claims can be represented as `source_linked` drafts; a model-generated unobserved URL is dropped; a semantically unsupported claim citing a real SAE page is not automatically blocked at the draft level; and no unapproved draft can flow downstream as an approved fact.

**No authenticated Responses API integration smoke test was run. No real network was used by the Python replay.** The real external research was performed through an independent web browsing tool and manually audited. E2 release gate remains open.

## Next E2 gate

1. Run live `OpenAIWebResearchProvider` with privately configured API credentials, confirm actual Responses output shapes/tool costs, and do not store credentials or real prospect reports in public GitHub.
2. Introduce a separate content-support verifier and explicit claim status `source_linked -> checked -> approved/rejected`.
3. Implement a hard budget/timeout/retry policy, detect misleading sources and conflicting dates, and improve source-type/domain classification.
4. Expand evaluation to non-automotive companies and ambiguous company identities.

**Security:** this file records only public companies, URLs and generic research claims; no internal sponsor requests, contacts, price offers, personal information or protected slide assets were uploaded.
