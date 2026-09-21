# Scope and Modules

Choose the smallest profile that satisfies the request. Scope profiles are presets, not rigid product tiers; add or remove modules when the user is explicit.

## Profiles

| Profile | Modules | Typical request | Default output |
|---|---|---|---|
| `snapshot` | core, delivery | “Summarize our brand for future marketing work.” | Brand core, evidence ledger, guardrails, gaps |
| `copy-pack` | core, copy, delivery | “Create reusable brand and channel copy.” | Length variants plus requested channels |
| `asset-inventory` | core, inventory, delivery | “Organize what brand media we already have.” | Official links and existing asset index |
| `image-kit` | core, images, delivery | “Plan or create marketing images.” | Requested image briefs; files only in Production mode |
| `video-kit` | core, video, delivery | “Plan or create marketing videos.” | Requested concepts, scripts, shot lists; files only in Production mode |
| `campaign-kit` | core, copy, selected images or video, delivery | “Prepare assets for this campaign.” | Campaign-specific copy and media deliverables |
| `full-library` | all relevant modules | “Build the complete reusable brand marketing pack.” | Full reusable library without arbitrary filler |
| `refresh` | only changed modules plus delivery | “Update our existing pack.” | Versioned changes with preserved approvals |

When the user asks for one concrete item, do not expand to a profile that adds unrelated assets. When the user asks for a “complete brand pack,” use `full-library` but still omit channels, locales, or formats with no plausible use.

## Scope controls

Record these before production:

| Control | Examples |
|---|---|
| audiences | product teams, buyers, creators |
| channels | website, LinkedIn, YouTube |
| locales | `en`, `zh-CN` |
| copy assets | positioning, three taglines, LinkedIn launch post |
| image assets | one hero, three social cards |
| video assets | one 30-second launch video, two 9:16 cutdowns |
| generation | briefs only, or exact generated count |
| destination | local Markdown, Lark, Google Docs, Notion |
| version intent | new, campaign variant, refresh |

If counts are absent, use one strong draft per requested placement plus up to three meaningful creative options where choice is useful. Do not multiply aspect ratios, languages, or variants silently.

## Module dependencies

- Every profile includes `core`; it prevents downstream assets from drifting.
- `copy`, `images`, and `video` may reuse the same core independently.
- `localization` applies after the source-language asset is stable and only to selected asset IDs.
- `delivery` assembles selected modules and must not reintroduce omitted ones.
- Production mode changes only selected `images` or `video` items from brief to generated output.

## Scope changes

If new evidence changes the core, recheck every selected downstream asset. If the user adds a channel or locale later, extend the current asset matrix instead of regenerating the entire pack.
