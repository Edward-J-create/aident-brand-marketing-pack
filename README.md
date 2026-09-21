![Aident Brand Marketing Pack](docs/assets/readme-hero.png)

# Aident Brand Marketing Pack

An open, cross-agent Skill for turning brand notes, official sites, social profiles, documents, and existing media into an evidence-backed marketing source of truth.

It writes the actual copy. For visual and video assets, it creates precise production contracts—briefs, copy dependencies, formats, source requirements, rights, and quality gates—without pretending that a prompt is a finished design.

## The contract

```text
BRAND SOURCES
     │
     ▼
FACT LEDGER ──► BRAND CORE ──► FINAL COPY
     │               │              │
     └───────────────┴──────► ASSET MANIFEST
                                      │
                         ┌────────────┴────────────┐
                         ▼                         ▼
                   VISUAL BRIEFS              VIDEO BRIEFS
                         │                         │
                         └────────────┬────────────┘
                                      ▼
                            EXTERNAL PRODUCTION
                         (a separate Skill or tool)
```

| This Skill owns | A separate production Skill owns |
|---|---|
| Brand facts, positioning, message pillars, voice, terminology | Rendering and editing |
| Final website, social, ad, email, event, partner, and video copy | Model or renderer selection |
| Existing-asset inventory and rights state | Layout implementation and animation |
| Visual and video briefs, prompts, scripts, shots, formats, safe areas | Working design or editing projects |
| Asset IDs, dependencies, status, acceptance criteria, QA contract | Final exports and render inspection |

This split is intentional. Stable brand governance should not be coupled to a fast-changing image model, video generator, editor, or paid API.

## Modular profiles

| Profile | Use it for |
|---|---|
| `snapshot` | Compact brand core and claim guardrails |
| `copy-pack` | Canonical narrative and selected channel copy |
| `asset-inventory` | Existing logo, image, video, audio, document, and template index |
| `visual-kit` | Static-asset briefs with dependent copy and source assets |
| `video-kit` | Video concepts, scripts, shots, captions, and delivery contracts |
| `campaign-kit` | One campaign across selected copy and media formats |
| `full-library` | A complete reusable content and asset system |
| `refresh` | Evidence-aware updates that preserve stable approvals |

Operating modes are separate: `library` builds the source of truth, `handoff` freezes production contracts, and `refresh` revises only affected records. None of them renders media.

## Why visual and video templates stay here

The reusable templates in [`assets/visual-brief.yaml`](aident-brand-marketing-pack/assets/visual-brief.yaml) and [`assets/video-brief.yaml`](aident-brand-marketing-pack/assets/video-brief.yaml) describe what a good asset must communicate and how it will be accepted. Those contracts belong beside the brand facts and copy.

Actual Figma layouts, Canvas code, image-model recipes, motion components, editing timelines, caption pipelines, audio mixing, and export logic should live in independent Skills such as a future `aident-brand-visual-production` or `aident-brand-video-production`. This repository can hand off to either without becoming dependent on it.

## Reliability rules

- Evidence precedes copy.
- Every consequential claim carries a source, retrieval date, confidence, and dependent asset IDs.
- Short copy derives from one canonical narrative.
- Visual and video copy remains independently reviewable.
- Logo files, product UI, footage, rights, and approval ownership are explicit.
- Prompts, concepts, scripts, and storyboards are never labeled as delivered media.
- Lark, Google Docs, and Notion deliveries are read back before verification.
- Narrow requests do not silently expand into a full library.

## Cross-agent installation

The repository follows the open filesystem-based Agent Skills layout. The portable package is [`aident-brand-marketing-pack/`](aident-brand-marketing-pack/) and is not tied to Codex or one model.

Install with the open [`skills`](https://github.com/vercel-labs/skills) CLI:

```bash
npx skills add Edward-J-create/aident-brand-marketing-pack \
  --skill aident-brand-marketing-pack
```

Or install globally for detected agents:

```bash
npx skills add Edward-J-create/aident-brand-marketing-pack \
  --skill aident-brand-marketing-pack \
  --global \
  --agent codex claude-code cursor opencode \
  --yes
```

For manual installation, copy the complete package directory—not only `SKILL.md`—to the host's personal or project Skill directory. Hosts may ignore [`agents/openai.yaml`](aident-brand-marketing-pack/agents/openai.yaml); it is optional discovery metadata.

The portable core can always produce a local Markdown pack from accessible inputs. Connected Lark, Google Docs, Notion, and website extraction use Aident Loadout capabilities or equivalent host-native tools. Follow the [Aident Loadout setup instructions](https://aident.ai/SETUP.md) when those routes are selected.

## Example requests

```text
Use $aident-brand-marketing-pack to build an English copy pack from our website.
Include only the website one-liner, LinkedIn launch post, and three ad variants.
Deliver a local Markdown file and show the evidence behind factual claims.
```

```text
Use $aident-brand-marketing-pack to inventory the assets in this Lark document.
Create production-ready briefs for one 16:9 hero banner, one 1:1 ad, and one
15-second launch video. Write all required copy, but do not render media.
```

```text
Use $aident-brand-marketing-pack in handoff mode. Freeze the approved copy,
logo sources, formats, and acceptance checks for the three selected assets.
Prepare the package for a separate visual/video production workflow.
```

## Package structure

```text
aident-brand-marketing-pack/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── asset-manifest.yaml
│   ├── brief.yaml
│   ├── video-brief.yaml
│   └── visual-brief.yaml
└── references/
    ├── copy-module.md
    ├── evidence-and-research.md
    ├── host-compatibility.md
    ├── image-module.md
    ├── output-template.md
    ├── production-handoff.md
    ├── quality-gates.md
    ├── scope-and-modules.md
    └── video-module.md
```

## Design references

The architecture borrows two strong patterns while keeping a narrower contract:

- [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills): task-specific marketing modules, evidence-grounded creative batches, channel-aware copy, and concrete creative QA.
- [anthropics/skills](https://github.com/anthropics/skills): concise `SKILL.md` routing, progressive reference loading, reusable assets, and explicit boundaries between guidance and production.

Their rendering-oriented visual workflows informed the separation documented above: this Skill controls the brand and production contract; renderer-specific implementation stays independent.

## Validation

Run the dependency-free repository checks:

```bash
python3 scripts/validate_package.py
```

The same check runs in GitHub Actions. It validates the public package limits, frontmatter, local links, placeholder hygiene, YAML/JSON syntax, banned media-generation capability tags, and exact parity between Aident action tags and [`loadout/metadata.json`](loadout/metadata.json).

## License

[MIT](LICENSE.md)
