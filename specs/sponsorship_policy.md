# Sponsorship policy — hybrid model (E1)

**Policy status:** Sponsorship taxonomy and approval roles **APPROVED 2026-11-03**. Official tier labels and existing plan benefits are retained. Detailed tier boundaries, specific amounts and benefit entitlements are awaiting validated private records.

## Separate dimensions: contribution versus commercial arrangement

**Contribution type** (`support_type`, one per contribution):
1. `money` — financial support.
2. `materials` — donated/supplied parts, tools, consumables, materials or equipment.
3. `services` — logistics, manufacturing, maintenance, training or other services.

**Commercial arrangement** (`arrangement`):
- `official_tier`: current approved tier plan (Diamante, Ouro, Prata, Bronze, Apoio);
- `custom`: specifically negotiated terms or deliverables, subject to operational-management approval;
- `mixed`: two or more contribution types and/or official-tier plus individually approved custom terms.

A technical or institutional opportunity is a partnership theme, **not an additional primary support type**. The same proposal can contain multiple contribution line items with distinct types.

## Commercial governance

- **Institutional data owner, commercial approver, final reviewer:** BAJA UEA operational management.
- The model **may suggest** monetary amounts or custom commercial packages, but cannot issue final offers or guarantee benefits without management approval.
- Existing plan benefits are the sole initial authorized benefit catalog; additional benefits must be explicitly requested and approved.
- Materials and services are classified **separately**, not automatically converted to money or tier status. Where equivalence or cost valuation is relevant, it requires a documented management decision.
- Provisional technical needs extracted from the PPTX are discovery aids, not validated procurement requirements. Do not promise availability, product compatibility, quantities or prices.
- The legacy annual budget is excluded from scoring, calculations, proposed monetary amounts and institutional narrative, regardless of its presence in the visual template.
- Use historical 2025/2026 achievements only with their period label within 2026/2027 proposals.
- No fabricated reach/ROI, contracts, exclusivity, legal eligibility, tax deductions or third-party commitments.
- National Baja SAE sponsorship does not constitute direct BAJA UEA sponsorship.
- Logos, test drives, presentation appearances and factory visits require approved entitlement and any necessary permissions.

## Required private reviewed datasets

- `tiers`: `tier_id`, `label`, `currency`, `min_amount?`, `max_amount?`, inclusivity, `effective_cycle`, `benefit_ids`, `approved_by_role`, `approved_at`.
- `benefits`: `benefit_id`, description, allowed tiers, conditions, asset permissions, delivery owner, valid period.
- `needs`: `need_id`, subsystem, support type, item/service, technical constraints, quantity if approved, `provisional|approved|expired`, update date.
- `support_lines`: `support_type`, proposed commitment, monetary amount if applicable, linked needs and benefits, review state.
- `exceptions`: scope, negotiated proposal ID, authorized benefit/amount, authorizing management role, expiry.

## Commercial gates

1. Do not auto-match a value to any tier if the tier ranges have gaps, overlaps or inclusive-end ambiguity. Route to management review.
2. Do not set final approval unless all applicable amounts, terms, benefits, brand uses and technical needs are approved.
3. Draft suggestions may omit amounts until a valid official price table exists.
4. Never auto-send, submit or publish a proposal to companies in MVP v1.

## Publication policy

Store private commercial catalogs, contacts, proprietary presentations and draft proposals only in controlled non-public storage. The public repository contains rules, schemas and sanitized synthetic tests. See `docs/PRIVACY_AND_DATA_HANDLING.md`.

**Reference:** `docs/E1_DECISIONS.md`.
