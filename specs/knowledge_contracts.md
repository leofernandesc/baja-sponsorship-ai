# E1 data model — conceptual contracts

**Status:** Public schema proposal. No live, private institutional database is being published.

## Institutional facts

`InstitutionalFact`: `id`, `claim_type`, `statement`, `cycle`, `source_ref`, `review_status`, `approver_role`, `approved_at`, `valid_from`, `review_due`, `sensitivity`.

Approved prior-cycle facts must not be relabeled as 2026/2027 achievements.

## Funding and benefits

`SponsorTier`: `id`, `label`, `currency`, `amount_min?`, `amount_max?`, `min_inclusive`, `max_inclusive`, `benefit_ids[]`, `cycle`, `approval_status`, `approved_by_role`.

`Benefit`: `id`, `description`, `tier_ids[]`, `conditions[]`, `brand_permission_status`, `availability`, `approval_status`.

`Contribution`: `id`, `type: money|materials|services`, `description`, `amount?` (money only by default), `quantity?`, `related_need_ids[]`, `technical_validation_status`, `commercial_validation_status`.

`SponsorshipProposal`: `arrangement: official_tier|custom|mixed`, `contributions[]`, `tier_id?`, `benefit_ids[]`, `requested_exceptions[]`, `approval_state`, `approved_by_role`, `approved_at?`.

**Invariant:** no implicit valuation equivalence between materials/services and monetary tier; no live tier allocation where amount bands are unresolved.

## Technical needs

`TechnicalNeed`: `id`, `subsystem`, `support_type`, `description`, `source_asset`, `source_cycle`, `technical_constraints?`, `approval_status: provisional_source_only|approved|expired`, `reviewer_role?`, `review_date?`.

The supplied PPTX is a **provisional** source. Named items in historical company-specific requests are **examples**, not current verified demand.

## Private fields

Contact names, phone numbers, email addresses, internal budgets, negotiated prices, originals and proposal outputs belong only in private storage. In a public schema, use type names/placeholders instead of authentic values.

## Approval gates

Only `operational_management` may mark institutional data, custom commercial conditions and final generated proposals as approved. This is a role name, not an assertion about the person's identity. Log time and source version privately.

## Migration compatibility

These contracts are transport-neutral: Python core and future FastAPI/React adapters must share the same semantics. Persist version and confidentiality metadata; do not import Streamlit in core models.
