# Original PowerPoint extension contract

## Binding product requirement

The editable BAJA UEA sponsorship PowerPoint, once supplied, is the **base and source of truth for presentation design**. New company proposals are **extensions of that file**, not replacements or newly designed short decks.

## Inspected source (E0)

- Original editable **2026 company-specific sponsorship PPTX** received: **15 slides**, **20 × 11.25 in (16:9)**, **one master/theme**.
- Source SHA-256: `527caecd04f8e917da2e18d3a51c944995698774df694e47edc853014337aa8f`.
- The original deck's **slide 13 is already a company-specific commercial request**; it cannot remain unchanged in a proposal to another company.
- Slide 12 has an embedded **OLE/Excel table** which did not render correctly in LibreOffice PDF conversion.
- Observed fonts: Poppins family, Anton, Arimo Bold. Original fonts were absent in the test environment, leading to fallback-renderer text issues.
- First `python-pptx` round-trip and one-slide append tests preserved all 15 original slides pixel-for-pixel **in the same LibreOffice renderer**. Native PowerPoint fidelity approval remains pending.

See `docs/E0_PPTX_AUDIT.md`. The candidate data map is `specs/template_manifest.candidate.json`, not yet an approved template manifest.

## Proposed rules

1. Keep the source PPTX immutable and preserve its unmodified copy/checksum.
2. Each run opens a copy, verifies `template_version` and produces a distinct artifact.
3. Retain all approved institutional content. Insert new company-fit slide(s) before the company-specific commercial section if approved, and **parameterize existing slide 13**. Never leave the sample company-specific price/benefit content in an unrelated deck.
4. Reuse the existing master/layout/theme where technically feasible. No arbitrary redesign, recoloring or flattened screenshots in place of editable content.
5. Company-specific slides may contain strategic fit, documented shared themes, proposed support, sponsorship benefits and CTA. Final contents/number depend on PPTX inventory.
6. Keep images/brand elements within authorized use. Logo retrieval never implicitly licenses commercial reuse.
7. The final proposal is editable PPTX. PDF is a secondary export only, and export must avoid the known unsupported OLE rendering path.
8. Maintain source-to-output mapping (slide index, title, shape IDs when feasible, insertion point).

## Fidelity spike — mandatory before implementation

- Extract source deck metadata, fonts, layouts and slide inventory.
- Save an unchanged copy with candidate library and verify that original content can still be opened and edited.
- Render/inspect original and regenerated slides at matching resolution.
- Check text wraps, missing fonts, duplicated/lost elements, images, diagrams, headers/footers and links.
- Attempt a representative extension slide in the source theme.
- Record capability limits; change renderer if preservation is unacceptable.

`python-pptx` can load/save existing files and append slides with available layouts, but does not generally support flawless cloning of arbitrary source slides. This must be tested against the actual deck, not assumed.

## Template manifest (future)

The **inspected** source is mapped in `specs/template_manifest.candidate.json`. After design and commercial review, promote it to normative `specs/template_manifest.json`, adding explicit shape IDs, insertion logic, character limits, required fonts, and accepted render/export procedures.

## Acceptance checks

- Unmodified source file SHA-256 matches original after a generation run.
- Institutional slide count/content maintained; no unintended loss of slide parts/relationships.
- Generated extension slides visually align with source design and remain editable.
- Required placeholders filled; no unsupported fields/claims; text fits the layout.
- Output opens in a standard PPTX viewer and survives round-trip.
- Visual comparison plus human reviewer sign-off for at least one generated example.
