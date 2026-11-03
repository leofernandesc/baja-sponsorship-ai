# Data contracts — design stage

These are conceptual typed contracts, not implementation claims. Exact JSON Schema/Pydantic types will be frozen during E1–E3.

## CompanyIdentity

`company_id`, `input_name`, `canonical_name`, `jurisdiction`, `business_unit`, `sector`, `official_domain`, `aliases`, `identification_state` (`resolved | ambiguous | unresolved`).

## Evidence

`evidence_id`, `company_id`, `claim`, `source_url`, `source_title`, `source_type`, `published_at?`, `captured_at`, `verification_state` (`verified | conflicting | uncertain | rejected`), `notes?`, `used_in_claim_ids[]`.

**Constraint:** facts with `verification_state != verified` cannot be stated as established facts in the outbound deck.

## BajaInstitutionalFact

`fact_id`, `topic`, `statement`, `source_asset`, `effective_period`, `approved_by`, `approval_date`, `version`, `active`, `review_due?`.

## TechnicalNeed

`need_id`, `subsystem`, `description`, `priority`, `quantities?`, `compatible_items?`, `owner`, `approved`, `valid_until?`.

## PartnershipOpportunity

`opportunity_id`, `mode` (`official_tier | financial_custom | in_kind | technical | institutional | mixed`), `rationale`, `evidence_ids[]`, `need_ids[]`, `benefit_ids[]`, `requested_commitments[]`, `approval_required`, `status` (`proposed | reviewed | approved | rejected`).

## ProposalSection

`section_id`, `purpose`, `title`, `body`, `company_claim_ids[]`, `baja_fact_ids[]`, `opportunity_ids[]`, `character_budget?`, `layout_id?`, `review_state`.

## ProposalDraft

`draft_id`, `company_id`, `template_version`, `baja_knowledge_version`, `research_run_id`, `sections[]`, `commercial_recommendation`, `review_state` (`draft | review_required | approved | rejected`), `reviewer?`, `approved_at?`.

## GenerationRun

`run_id`, `company_input`, `started_at`, `completed_at?`, `pipeline_stage`, `status` (`running | blocked | failed | review_required | approved | exported`), `provider`, `model`, `source_template_sha256`, `source_template_version`, `artifact_paths[]`, `validation_issues[]`, `approved_by?`.

## Validation invariants

- The original template is never an artifact output path.
- Proposal section claims must trace to verified external evidence or approved BAJA facts; proposals must read as proposals.
- An approved proposal must have no outstanding critical validation issues.
- Custom commitments and unapproved benefits cannot enter an approved state.
- A final deck must reference the exact template version and source SHA-256.

## Initial UI view model

Input: `company_name: str`. Output after each stage: progress status, company identity, selected evidence, qualification notes, recommended modes, editable proposal sections, validation alerts and approve/export actions.
