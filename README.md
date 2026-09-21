# Brand Marketing Pack Skill

Build a sourced, reusable library of brand and marketing content from a brand name, notes, official website, social profiles, source documents, or existing media.

The Skill focuses on content operations: brand facts, positioning, reusable copy, existing-asset inventory, image briefs, video scripts, generated-media routing, evidence, and editable delivery. It does not replace a visual identity or brand-guideline design workflow.

## Why this Skill is modular

The agent selects the smallest useful module set instead of generating a large pack every time:

| Profile | Best for |
|---|---|
| `snapshot` | A compact, evidence-backed brand core |
| `copy-pack` | Reusable descriptions and selected channel copy |
| `asset-inventory` | Organizing existing links, images, and videos |
| `image-kit` | Image briefs, prompts, or explicitly approved generation |
| `video-kit` | Concepts, scripts, shot lists, or explicitly approved generation |
| `campaign-kit` | Copy and media for one campaign |
| `full-library` | A complete reusable brand marketing library |
| `refresh` | Updating only affected modules in an existing pack |

Scope and execution mode are separate. Library mode creates reviewed copy and production briefs without paid media calls. Production mode generates only the exact approved image or video deliverables. Refresh mode preserves stable approvals and revisits changed evidence.

## Install

Copy the [`build-brand-marketing-pack`](build-brand-marketing-pack/) directory into the skills directory used by your agent environment.

For Codex, a typical location is:

```text
~/.codex/skills/build-brand-marketing-pack
```

The Skill can always deliver a local Markdown pack. Lark, Google Docs, Notion, website extraction, and media generation use Aident Loadout capabilities and require the relevant connection or credit approval. Follow the [Aident Loadout setup instructions](https://aident.ai/SETUP.md) when those actions are needed.

## Example requests

```text
Use $build-brand-marketing-pack to create an English copy pack from our website.
Deliver it as a local Markdown file. Only include website, LinkedIn, and YouTube copy.
```

```text
Use $build-brand-marketing-pack to inventory the images and videos in this Lark brand document.
Do not generate new media. Save the result to Google Docs.
```

```text
Use $build-brand-marketing-pack in Production mode to create one 16:9 hero image and
one 15-second launch-video concept from our approved brand core. Show cost and model choices first.
```

```text
Use $build-brand-marketing-pack in Refresh mode. Compare our current pack with these updated
official URLs and revise only facts and assets affected by the changes.
```

## Package structure

```text
build-brand-marketing-pack/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── asset-manifest.yaml
│   └── brief.yaml
└── references/
    ├── copy-module.md
    ├── evidence-and-research.md
    ├── image-module.md
    ├── output-template.md
    ├── quality-gates.md
    ├── scope-and-modules.md
    └── video-module.md
```

The entrypoint contains routing, boundaries, and the shared workflow. Supporting references are loaded only for the selected modules.

Two machine-readable templates make repeated runs deterministic:

- [`assets/brief.yaml`](build-brand-marketing-pack/assets/brief.yaml) fixes scope, mode, module, channel, locale, count, and destination decisions before production.
- [`assets/asset-manifest.yaml`](build-brand-marketing-pack/assets/asset-manifest.yaml) gives every requested, proposed, or generated asset a stable status and provenance record.

The [`examples/copy-pack.yaml`](examples/copy-pack.yaml) example shows how to request only one channel without triggering unrelated image or video work.

## Reliability model

- Evidence is collected before copy is drafted.
- Verified facts, user-supplied facts, inferences, proposals, and approved assets have distinct statuses.
- Short copy is derived from one source-of-truth narrative.
- Paid generation never runs merely because an image or video module was selected.
- Generated media is not called complete until its output is accessible and inspected.
- Lark, Google Docs, and Notion deliveries are read back before completion.
- Narrow requests stay narrow; omitted modules are not silently reintroduced during delivery.

## Validation status

The package passes the Codex Skill structure validator and the deterministic Aident Loadout packager. Its referenced Loadout Action names were resolved from live capability discovery. Protected Aident curator validation and publication are separate admin steps and are not performed by this repository.

Run the repository-level checks locally with:

```bash
python3 scripts/validate_package.py
```

The same dependency-free check runs in GitHub Actions. It validates package limits, required metadata, local links, placeholder hygiene, and exact parity between referenced Aident capability tags and [`loadout/metadata.json`](loadout/metadata.json).

## License

[MIT](LICENSE.md)
