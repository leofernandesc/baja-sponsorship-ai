# Product scope

## User story

As a BAJA UEA sponsorship coordinator, I want to enter a company name and receive a verified prospecting report plus a customizable, editable extension of the approved sponsorship presentation, so I can pursue better-aligned partnerships without rewriting the deck manually.

## MVP in scope

- Identify the target company and handle necessary disambiguation.
- Research public sources with source, capture date and confidence/verification state.
- Use only approved BAJA UEA facts from a versioned institutional knowledge base.
- Recommend hybrid sponsorship alternatives: official tiers, financial, in-kind, technical, institutional or combination.
- Show reasoning summaries and sources in an internal report, not hidden inside the proposal.
- Generate a company-specific deck **from the original PPTX**, preserving original institutional slides and extending them with native editable slides when technically feasible.
- Inspect, edit and approve the draft before finalizing.
- Record generation metadata, source version, model configuration and approvals.

## Explicitly out of scope for MVP

- Automatic sending to target companies or submitting third-party forms.
- Company contact scraping behind authentication or privacy boundaries.
- Autonomous negotiation, contract signature or sponsorship approval.
- Fully autonomous visual design replacing the supplied source deck.
- Sales CRM, multiuser access, roles/permissions and automatic follow-up reminders.
- Arbitrary slide cloning across unrelated PowerPoint themes as an untested requirement.

## Success definition

One company name → sourced company profile → defensible hybrid strategy → editable presentation with unchanged institutional prefix and reviewed company-specific extension → approved deliverables.

## Important constraints

The number of appended slides, layout mapping and some commercial field constraints remain OPEN until the source PPTX and current sponsorship policy are inspected and approved.
