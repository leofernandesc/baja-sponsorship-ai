# E0 — PowerPoint source audit (03 Nov 2026)

**Status:** Structural inventory and basic save/append feasibility checks completed. **E0 structurally feasible for planning:** source/editability check complete. Font/OLE fidelity still requires E4 acceptance. Business rules moved to E1; the original budget must not feed any calculation or recommendation.

## Files evaluated (not committed to the public repository)

| Source | Slides | Format | Canvas | SHA-256 |
|---|---:|---|---|---|
| Sponsorship deck 2026, company-specific example | 15 | PPTX | 20 × 11.25 in (16:9) | `527caecd04f8e917da2e18d3a51c944995698774df694e47edc853014337aa8f` |
| BAJA UEA Portfolio 2026 | 16 | PPTX | 8.264 × 11.694 in (portrait) | `93174462edd7620f277605756a6c25a1622cbd656878132c32fb8a5d57fd581e` |
| Sponsorship request 2025 | 20 | PDF | landscape slides | Historical reference only |

The company-specific deck is **the designated baseline for generated PowerPoint proposals**. The portfolio is a knowledge/reference source and optional attachment; its portrait aspect ratio is not interchangeable with the proposal's wide format.

## 2026 sponsorship deck slide inventory

| Slide | Identified content | Generation treatment |
|---:|---|---|
| 1 | Capa / ciclo 2026 | Institutional; brand/year may require new-cycle review |
| 2 | Sobre nós | Institutional |
| 3 | Objetivos e missão | Institutional |
| 4 | Veículo BAJA | Institutional |
| 5 | Competição Baja SAE | Institutional |
| 6 | História (1) | Institutional |
| 7 | História (2) | Institutional |
| 8 | Resultados 25/26 | Historical facts, cycle-fixed; require update only at new cycle |
| 9 | Áreas técnicas e operacionais | Institutional |
| 10 | Orçamento anual | Excluded from AI data/recommendations by E1 approval; output display to be decided in E4 |
| 11 | Patrocínio & apoio | Institutional |
| 12 | Cotas e contrapartidas | OLE/Excel object: review/fix before automation |
| 13 | Proposta e justificativa de patrocínio | COMPANY-SPECIFIC 2026 example; never reuse numeric terms by default |
| 14 | Contatos | Team-confirmed contact details; may change |
| 15 | Patrocinadores | Historical/current branding: must validate before any new proposal |

**Key finding:** slide 13 already contains a bespoke financial request/justification for one company, so the product needs to **replace or parameterize that company-specific content and optionally insert supporting fit/opportunity slides**. Simply appending company material after a still-personalized example would be wrong. Existing contract language, brand logos and other prospective claims must be validated by the BAJA team.

## Technical inventory

- 15 slides, one slide master, one theme, all using `Blank` slide layout.
- 20 × 11.25 inch wide presentation; approximately 31.7 MB source file.
- PowerPoint package: 166 ZIP parts, including 91 media files (77 PNG, 9 SVG, 5 JPEG) and **one embedded OLE object** (`ppt/embeddings/oleObject1.bin`).
- Identified text font families: **Poppins, Poppins Bold, Poppins Ultra-Bold, Anton, Arimo Bold**. These are not installed in the test environment; fallback was Noto Sans. Do **not** redistribute bundled font files.
- Many images/ornaments are stored as freeform and grouped shapes; visual/editable preservation matters. The original file contains native text boxes, not merely rendered images.
- Slide 12 contains an embedded OLE/Excel table of sponsorship tiers; under LibreOffice PDF export the displayed table was not rendered correctly. **PDF export through LibreOffice is not accepted as proof of accurate pricing-table output** until that object is normalized or an alternative export pipeline is verified.
- Slides 1 and some other slides show text wrapping/clipping in the available fallback-font renderer. This is an environment/font issue observed even on the unmodified original. The PowerPoint-native output must be inspected on a system with the intended fonts.

## Feasibility tests conducted

1. Load/save an unedited copy using `python-pptx`: 166 original package parts preserved by name; no ZIP corruption detected.
2. Render original and saved copy via LibreOffice: 15 pages each, **zero pixel differences on all 15 rendered pages at the tested resolution**.
3. Add one simple native/editable slide to a copy: output has 16 slides; original first 15 slides again showed **zero pixel differences** in the same renderer.
4. This is a technical feasibility spike, not a full fidelity guarantee: none of the tests proves that PowerPoint/Google Slides will render the source identically, nor that arbitrary complex slide cloning works.

## Recommended extension strategy (candidate; requires review)

- Treat slides 1–12 and 14–15 as the original institutional deck, *subject to current-content checks*.
- Introduce 1–2 new native slides after slide 12 for company-fit and collaboration opportunities, following the existing black/yellow/white design. Decide final count after a visual prototype.
- Parameterize original slide 13 for the agreed hybrid proposal terms, replacing all example-company-specific amounts, needs and procurement screenshots; when terms are unapproved, render only a negotiation-oriented non-numeric proposal.
- Keep contacts and current sponsor listing only after validating their freshness; do not infer a company is an existing team sponsor from its logo appearing in a sample deck.
- Use an immutable PPTX base identified by checksum, a versioned template manifest, and source-to-output slide mapping; keep research citation links in the internal report rather than overloading slides.
- Prefer `python-pptx` for editing native text and appending simple native slides; use a designed slide library or controlled OOXML cloning only after regression tests. Preserve the embedded table carefully or replace it using a team-approved native PowerPoint table.

## E0 exit blockers

- [ ] Visually inspect original/saved/generated deck in Microsoft PowerPoint (or an environment with correct fonts); approve typography and clipping.
- [ ] Resolve embedded sponsorship-table OLE behavior and validate prices/benefits with the team.
- [ ] Approve exact insertion order, number of personalized slides, and fallback for no financial quote.
- [ ] Confirm sponsor logos, internal contacts, brand assets and sample commercial terms suitable for redistribution.
- [ ] Approve final manifest (`template_manifest.json`) instead of the current candidate version.

## Disclosure / public repository

Source PPTX/PDF files contain logos, contacts and company-specific commercial content. They are not uploaded to the public GitHub repository by this audit. Only source hashes, structural findings and generic implementation rules belong here until rights and team approvals are resolved.
