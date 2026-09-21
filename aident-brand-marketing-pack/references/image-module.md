# Visual Asset Module

Use this module to inventory existing visuals and specify static marketing assets. It does not render, edit, or redesign media.

## Inventory existing assets

Capture logo source files and lockups, icons, product screenshots, photography, illustrations, diagrams, social posts, ad creative, decks, event graphics, templates, and prior exports. Record exact source, owner, rights, recency, editable-source availability, file type, dimensions when known, and reuse restrictions.

Do not infer a logo variant, font license, partner lockup, or image right from appearance alone.

## Visual brief contract

Complete [../assets/visual-brief.yaml](../assets/visual-brief.yaml) for every requested deliverable. A production-ready brief must define:

- objective, audience, channel, placement, locale, CTA, and success condition;
- master and variant IDs, dimensions, aspect ratio, crop behavior, and platform safe areas;
- approved copy asset IDs and text hierarchy;
- exact logo file or lockup, minimum size, clear space, placement, and partner-logo rules;
- approved colors, fonts, UI screenshots, photography, illustrations, and prohibited treatments;
- composition, focal point, reading order, visual direction, and negative space;
- required editable source and export formats;
- rights, accessibility, alt text, owners, approvals, and acceptance checks.

## Logo and product rules

- Prefer supplied vector logos for lockups; never redraw a real logo with an image model.
- Combine logos only when both parties, order, scale, divider, and clear-space rules are known.
- Use real product screenshots or clearly label conceptual UI. Never fabricate a screenshot as evidence of actual behavior.
- Keep important copy editable. A prompt may describe background imagery but must not be the sole source of critical typography.
- Do not extract a complete design system from one screenshot. Record only observed cues.

## Common asset patterns

### Social card or ad

Define platform placement, master ratio, crop variants, primary copy ID, optional support copy, CTA treatment, subject or product, logo placement, disclaimer area, and file-size limit.

### Website hero or banner

Define responsive crops, text-safe zones, focal point, light or dark mode, overlay contrast, CTA relationship, and whether imagery may sit behind live HTML text.

### Poster or event graphic

Define physical or digital size, viewing distance, information hierarchy, date and venue sources, sponsor lockups, bleed when relevant, QR destination, and print/export profile.

### Logo combination

Define source files, optical sizing, order, separator, monochrome fallback, minimum size, clear space, background restrictions, and approval owner. The brief cannot authorize a new logo.

## Acceptance baseline

Fail the brief if required copy, logo source, rights, dimensions, or approval owner is missing. A valid brief is `production-ready-brief`; it is never `delivered` until a separate workflow returns an inspected output.
