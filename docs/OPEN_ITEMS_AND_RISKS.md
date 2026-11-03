# Open items and risks

## Inputs awaiting review

| Item | Why it matters | Status |
|---|---|---|
| Original editable sponsorship PPTX | Defines actual source design, layouts, master, slide order and renderer compatibility | RECEIVED — 15 slides; final design fidelity checks pending |
| Current sponsorship tiers and benefits | Prevents fabricated prices and conflicting offers | OPEN — team approval |
| Current technical needs | Makes in-kind and technical offers concrete and useful | OPEN — team approval |
| Institutional data owners and sign-off | Ensures historical metrics are not mistaken for current claims | OPEN |
| Deck/logo publication rights | Controls private/public repository and document exports | OPEN |
| License and GitHub visibility | GitHub is PUBLIC; source files must stay restricted until explicit authorization; license still open | OPEN |

## Newly confirmed E0 issues

- `Poppins`, `Anton` and `Arimo Bold` are absent on the test machine; the exported presentation exhibits text fallback and clipping.
- PowerPoint slide 12 contains an OLE/Excel embedded table that LibreOffice fails to render correctly.
- Original company-specific commercial terms on slide 13 require removal/replacement for every new prospect.
- Public repository was created; source proposals include business content, so keep them out of Git and external assets until rights review.

## Project risks

| Risk | Impact | Mitigation |
|---|---|---|
| Source PPTX cannot be safely round-tripped by chosen library | High | E0 fidelity spike; alternative renderer if needed |
| AI invents sponsorship history or eligibility | High | Evidence-per-claim; primary-source preference; human approval |
| Model promises unavailable benefits or arbitrary funding values | High | Separate approved commercial rules and manual exception workflow |
| Company name resolves to wrong legal entity | High | Canonical identity and ambiguity checkpoint |
| Different sectors receive generic cloned text | Medium | Distinctiveness rubric across five-sector pilot |
| Template overflow / font mismatch | Medium | Field budgets, visual comparisons and reviewer check |
| Costs/latency grow with research depth | Medium | Bounded search budget, caching, provider accounting |
| Historical team metrics treated as current | High | Cycle/version tagging and review expiry |
| Unlicensed brand/image use | High | Asset source/permissions checklist |

## Recommended first next action

Review `docs/E0_PPTX_AUDIT.md` and resolve font/embedded-table visual fidelity, plus slide-13 commercial placeholders. Do not claim E0 acceptance until the missing approvals are completed.
