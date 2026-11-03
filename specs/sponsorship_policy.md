# Sponsorship policy — hybrid model

**Status:** Hybrid model APPROVED. Tier values, intervals, benefits, owners and commitments PENDING current BAJA UEA confirmation.

## Modes

- `official_tier`: tier ID from a human-maintained and approved tier table; exact price and benefits cannot be invented or adjusted by the model.
- `financial_custom`: negotiated financial support outside standard tier; requires manual approval of amount and associated benefits.
- `in_kind`: components, materials, tools, logistics or services suggested based on current verified needs; quantity and compatibility require technical review.
- `technical`: mentorship, workshop, engineering or validation support; proposed, not presumed available.
- `institutional`: joint presence/events, relationships and recognition; subject to brand and event approvals.
- `mixed`: combination of the above with approval for each non-standard commitment.

## Business constraints

1. The model proposes; the team approves.
2. No fabricated price, return-on-investment figure, media reach forecast, product compatibility or exclusivity.
3. A suggestion to provide hardware must refer to an approved need and cannot infer product donations from a company catalog.
4. Sponsor logos, vehicle branding, test-drive, factory visits or speaker access are not automatically granted. Use only approved benefits and availability.
5. National event sponsorship does not imply direct existing team sponsorship.
6. An optional sponsorship value recommendation must be a **draft requiring explicit approval**, not an automatic quotation.
7. Do not assert tax deductibility, fiscal incentives or legal eligibility without case-specific review.

## Required reviewed datasets

- `tiers`: unique ID, label, value range, currency, valid_from/to, valid benefits, approval authority.
- `benefits`: deliverable description, conditions, visibility class, owner, availability.
- `needs`: team subsystem, requested items/services, urgency, restrictions, owner and update date.
- `exceptions`: scope/approver/expires_at for negotiated special arrangements.

## Acceptance condition

Tier ranges and values must be internally consistent, have no unintended gaps/overlaps, and match the current approved commercial policy before any automated tier recommendation is enabled.
