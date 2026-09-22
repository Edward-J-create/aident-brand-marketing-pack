# Visual Asset Module

Use this module to inventory and package permitted existing visuals, then specify missing static marketing assets. It does not render, edit, or redesign media. Read [original-media-delivery.md](original-media-delivery.md) before labeling an image ready.

## Inventory existing assets

Capture usable logo exports and lockups, icons, product screenshots, photography, illustrations, diagrams, social posts, ad creative, event graphics, and prior final exports. Prefer full-resolution finished PNG/JPEG/SVG files over website renditions. Record exact source page and actual result file separately, owner, rights, recency, MIME type, dimensions, size/hash when accessible, durable pack location, and reuse restrictions. Inspect each member of an official brand archive before claiming it contains a particular variant. Do not place PSD, AI, Figma, or other editable design projects in the default pack.

Do not infer a logo variant, font license, partner lockup, or image right from appearance alone.

The document may display a high-quality derivative when the provider cannot render a final SVG export, but the full-quality result file must remain available separately. If only a CDN thumbnail or resized image is accessible, label it `Website rendition only`, not a ready export. Do not publish a private file at a public URL just to satisfy an image-insertion API.

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

Fail the brief if required copy, logo source, rights, dimensions, or approval owner is missing. A valid brief is `production-ready-brief`; it is never `delivered` until a separate workflow returns an inspected output. An existing-image item is ready only when the original file, rights, durable location, and intended-audience access are verified; a source-page link alone is not enough.
