# Scope and Modules

Choose a profile before drafting. Add or remove modules only when the request makes that necessary.

| Profile | Modules | Minimum result |
|---|---|---|
| `snapshot` | core, delivery | Evidence-backed brand core and guardrails |
| `copy-pack` | core, copy, delivery | Canonical narrative plus requested channel copy |
| `asset-inventory` | core, inventory, delivery | Existing-asset index with provenance, rights, gaps, and reuse notes |
| `visual-kit` | core, copy when text is present, inventory, visual-spec, delivery | Selected static-asset briefs and all dependent copy |
| `video-kit` | core, copy, inventory, video-spec, delivery | Selected video briefs, scripts, on-screen copy, and shot plans |
| `campaign-kit` | core, copy, optional inventory, selected spec modules, delivery | One campaign system, not an evergreen library dump |
| `full-library` | all relevant modules | Complete reusable library with manifests and gaps |
| `refresh` | affected modules, delivery | Diff-led update that preserves stable approvals |

## Granularity rules

- One asset ID represents one independently reusable deliverable.
- One channel, locale, or aspect-ratio variant may be a child of a master asset; do not duplicate the full strategy in every child.
- A logo lockup, banner, poster, ad unit, social card, carousel, thumbnail, video master, cutdown, and subtitle file are distinct deliverables when they can be approved or delivered separately.
- Keep copy as separate assets even when destined for an image or video.
- Do not create empty sections for unselected modules.
- Do not treat a list of prompts as a visual kit unless each prompt is attached to a complete brief.

## Mode rules

### Library

Default. Create reusable copy, inventory records, and production briefs. No rendering or paid media calls.

### Handoff

Use after scope and dependencies are reviewed. Freeze copy IDs, supplied brand assets, formats, variants, rights, and acceptance criteria. If the user requests handoff before approval or rights are complete, create a `blocked` handoff draft that names every missing dependency; do not label it frozen or production-ready. No rendering occurs here.

### Refresh

Compare source dates and manifest states. Revalidate changed facts, identify dependent assets, revise only affected content, preserve approved unchanged copy, and append a change log.

## Scope declaration

At the start of substantive work, state:

```text
Profile: {profile}
Mode: {library | handoff | refresh}
Modules: {selected modules}
Locales: {selected locales}
Channels: {selected channels}
Destination: {one destination}
Excluded: {explicit exclusions}
```
