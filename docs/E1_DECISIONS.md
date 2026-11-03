# E1 — Institutional knowledge and sponsorship decisions

**Decision date:** 2026-11-03  
**Approving role:** BAJA UEA operational management  
**Scope:** 2026/2027 sponsorship cycle  
**Status:** Business rules approved; structured source data and price-band validation still in progress.

## Explicitly approved inputs (answers 1–14)

| Topic | Approved decision | Implementation consequence |
|---|---|---|
| Planning cycle | 2026/2027 | New proposals use the current cycle; never relabel historic results as current |
| 2025/2026 reported team achievements | Yes, previously published metrics approved | Use approved historic performance facts with their original period/source |
| Institutional data approver | Operational management | Only this role may approve/update authoritative records |
| Sponsorship tiers | Existing five named tiers remain valid | Preserve tier catalog from the source presentation; confirm ambiguous numeric boundaries before automatic amount classification |
| AI-generated financial suggestions | Allowed | Draft only; amount and commercial terms require operational-management sign-off |
| Main sponsorship types | Money, materials/inputs, services | Distinct classification per provided contribution, combinable within a mixed proposal |
| Custom proposal approver | Operational management | Any exception to a standard tier is gated |
| Current technical-needs source | Existing 2026 PPTX materials initially | Seed only as `provisional`; do not describe as current purchasing authorization |
| Annual budget from presentations | Do **not** consider | No arithmetic, needs prioritization, score, recommendation, or AI text grounded in legacy annual budget |
| Standard sponsor benefits | Only those in approved tier plans | Do not invent benefits; additional benefit requires explicit new instruction and approval |
| Tailored sponsor benefits | Allowed | Must be approved individually; do not promise first |
| Contact details in 2026 source | Confirmed current | Store **privately**; public code/repo uses roles/placeholders only |
| Final proposal reviewer | Operational management | No unattended final publication, company outreach or binding proposal |
| Sensitive data | Never publicly exposed | No names/contact fields, contract details, proposal files, internal financial/need documents, source PPTXs or private research logs in public Git history |

## Three main sponsorship types

- `money`: monetary contribution. May use an approved standard tier or a proposed custom amount, with explicit commercial approval.
- `materials`: goods, equipment, consumables and components delivered to the team. Technical fit, quantities, and receipt are subject to review.
- `services`: provided work or services, including manufacturing, logistics, training, maintenance and professional support. Define scope/availability before approval.

**Mixed** means any combination of these three types, not a fourth contribution type. A standard tier is a *commercial plan*, not a contribution type. Technical/institutional collaboration is expressed through services or a separately approved activity/benefit where no item is being transferred.

Do **not** automatically convert materials/services into a cash tier. If accounting valuation or equivalent tier recognition is later required, operational management must approve the method and assessment for each case.

## Source and display policy

- The supplied 2026 sponsorship PowerPoint is the visual/document source. The company-specific slide is never reused verbatim.
- The 2026 portfolio contributes reference information, not a transferable slide layout.
- The 2025 document is a historical comparison only.
- Source-year performance is kept under its original cycle (2025/2026), while the proposal is for 2026/2027.
- The source PPTX has a legacy annual-budget slide. **Do not ingest it into the AI knowledge base or infer money requests from it.** Decide its inclusion/omission in output decks during E4, without altering the original source file.
- Confirmed source contacts may be used only by the private proposal-generation environment, not in public example files.

## Open E1 data gates

1. **Tier boundaries:** the legacy table has apparent pricing gaps/ambiguous boundaries; names stay valid, but the matching engine cannot auto-classify uncovered amounts until a rule is approved.
2. **Benefits:** the source PPTX is the only initial benefits catalog. Transcribe and cross-check the embedded table, including conditional benefits and visibility levels; no additions are auto-approved.
3. **Technical needs:** extract candidate categories from the PPTX, label `provisional_source_only`, and obtain technical team approval before requesting specific models, quantities or prices.
4. **Private source of truth:** decide controlled private data storage and revision/backup workflow. Public repo must contain schema/examples only, never personal data or commercial exhibits.
5. **Brand permissions:** validate sponsor-logo inclusion and rights/approval process prior to any deck export.

## Acceptance

E1 may be called **policy approved / knowledge inventory provisional**, but is not fully closed until the tier table and benefits are formally transcribed/validated, eligible current needs are approved, and the private master data workflow is documented and tested. The service must block unsupported commercial commitments.
