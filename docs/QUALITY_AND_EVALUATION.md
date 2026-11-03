# Quality assurance and evaluation

## Test pyramid

- **Unit**: Pydantic contracts, canonical company names, tier boundaries, required approvals, stale evidence and explicit state transitions.
- **Integration**: OpenAI/research adapters with mocks, SQLite persistence, PPTX renderer on controlled fixtures.
- **End-to-end**: name -> researched report -> strategy -> editable draft -> approval -> output.
- **Visual**: compare original slides and produced institutional slides as rendered images; inspect fonts, logos, clipping, numbering and overlays.

## Mandatory gates

- Every external claim in the outbound deck links to an acceptable `evidence_id`.
- A model inference is not presented as a verified company fact.
- No unapproved tier, value, branding deliverable, special benefit, tax claim or promise.
- The source PPTX remains unchanged; original slide set is maintained.
- Company-specific elements remain editable in PPTX.
- No leftover `{{PLACEHOLDER}}` fields or unsupported empty sections.
- Human review recorded before final status.
- Headless tests run without Streamlit import.

## Pilot company categories (E6)

Automotive; electronics; logistics; industrial materials/manufacturing; retail. Company selection and source evidence will be documented at execution time, not invented in the plan.

## Evaluation rubric (proposed)

Evaluate each proposal on a 0–4 scale per dimension, with reviewer rationale:
1. Fact accuracy and sourcing.
2. BAJA relevance and demonstrated needs.
3. Company-specific arguments versus generic template content.
4. Commercial safety and feasibility.
5. Source PPTX fidelity and editability.
6. Clarity and review effort.

No global acceptance score is fixed yet. **Critical factual, business-rule and fidelity violations are automatic fail regardless of scores.**

## Reproducibility evidence

Record source template hash/version, BAJA knowledge version, research fixture IDs, model/provider settings, generation timestamp, test command and actual results, output presentation checksum, and unresolved limitations.
