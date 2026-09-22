# Scope and Modules

Choose the input route (`source-led` or `idea-led`) first, then the scope profile. A request for a "brand pack", "marketing assets", or this Skill without a narrow deliverable defaults to `full-library`. Missing source media do not narrow the scope. Add or remove modules only when the user explicitly limits the deliverable.

| Profile | Modules | Minimum result |
|---|---|---|
| `snapshot` | core, delivery | Evidence-backed brand core and guardrails |
| `copy-pack` | core, copy, delivery | Canonical narrative plus requested channel copy |
| `asset-inventory` | core, inventory, delivery | Existing-asset index with provenance, rights, gaps, and reuse notes |
| `visual-kit` | core, copy when text is present, inventory, visual-spec, delivery | Selected static-asset briefs and all dependent copy |
| `video-kit` | core, copy, inventory, video-spec, delivery | Selected video briefs, scripts, on-screen copy, and shot plans |
| `campaign-kit` | core, copy, optional inventory, selected spec modules, delivery | One campaign system, not an evergreen library dump |
| `full-library` | core, copy, inventory, visual-spec, video-spec, requested localization, delivery | Reference-shaped bilingual-ready document, collected full-quality final result files where available, briefs for gaps, manifest and evidence appendix |
| `refresh` | affected modules, delivery | Diff-led update that preserves stable approvals |

## Granularity rules

- One asset ID represents one independently reusable deliverable.
- One channel, locale, or aspect-ratio variant may be a child of a master asset; do not duplicate the full strategy in every child.
- A logo lockup, banner, poster, ad unit, social card, carousel, thumbnail, video master, cutdown, and subtitle file are distinct deliverables when they can be approved or delivered separately.
- Keep copy as separate assets even when destined for an image or video.
- In the default `full-library`, retain every category in the reference blueprint. Use `Missing`, `Proposed`, or `Not applicable — reason` instead of an empty section.
- In an explicitly focused profile, omit unrelated categories and state that the result is not a complete reference-shaped pack.
- Do not treat a list of prompts as a visual kit unless each prompt is attached to a complete brief.

## Mode rules

### Library

Default. Create reusable copy, inventory records, and production briefs; collect and deliver permitted existing full-quality final media files. Do not include editable design or editing projects by default. No rendering or paid media calls occur implicitly; if the user requests finished media that is missing, coordinate a separate authorized production workflow and add only its inspected final result files to the pack.

### Handoff

Use after scope and dependencies are reviewed. Freeze copy IDs, supplied brand assets, formats, variants, rights, and acceptance criteria. If the user requests handoff before approval or rights are complete, create a `blocked` handoff draft that names every missing dependency; do not label it frozen or production-ready. No rendering occurs here.

### Refresh

Compare source dates and manifest states. Revalidate changed facts, identify dependent assets, revise only affected content, preserve approved unchanged copy, and append a change log.

## Scope declaration

At the start of substantive work, state:

```text
Input route: {source-led | idea-led}
Profile: {full-library by default, or explicit focused profile}
Mode: {library | handoff | refresh}
Modules: {selected modules}
Locales: {selected locales}
Channels: {selected channels}
Destination: {connected editable cloud document; provider or connection status}
Excluded: {explicit exclusions}
```
