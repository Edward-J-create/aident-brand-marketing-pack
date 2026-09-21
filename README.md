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

## Agent compatibility

This repository follows the open, filesystem-based Agent Skills layout: a skill directory with `SKILL.md`, progressively loaded references, and reusable assets. It is not tied to Codex or to one model.

The package can be installed in Codex, Claude Code, Cursor, OpenCode, Gemini CLI, GitHub Copilot, and other environments that support Agent Skills. The [`agents/openai.yaml`](build-brand-marketing-pack/agents/openai.yaml) file is only optional OpenAI discovery metadata; other hosts can ignore it.

Compatibility has two levels:

| Level | Requirement | Available result |
|---|---|---|
| Portable core | Read `SKILL.md` and bundled files; write a local file | Scope selection, research from supplied files, copy, image/video briefs, manifest, local Markdown |
| Connected production | Web/provider/media tools through Aident Loadout or equivalent native capabilities | Live website research, Lark/Google Docs/Notion delivery, generated images or video |

Missing provider access degrades to a verified Markdown master or production brief. It must not cause fabricated research, silent provider switching, or a false claim that media was generated.

## Install

The simplest cross-agent installation uses the [open `skills` CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add Edward-J-create/brand-marketing-pack-skill --skill build-brand-marketing-pack
```

The installer lets the user choose one or more detected Agent environments. A non-interactive global example is:

```bash
npx skills add Edward-J-create/brand-marketing-pack-skill \
  --skill build-brand-marketing-pack \
  --global \
  --agent codex claude-code cursor opencode \
  --yes
```

For manual installation, copy the complete [`build-brand-marketing-pack`](build-brand-marketing-pack/) directory—not only `SKILL.md`—to the host's personal or project Skill directory:

| Host | Example personal directory |
|---|---|
| Codex | `~/.codex/skills/build-brand-marketing-pack/` |
| Claude Code | `~/.claude/skills/build-brand-marketing-pack/` |
| Gemini CLI | `~/.gemini/skills/build-brand-marketing-pack/` or `~/.agents/skills/build-brand-marketing-pack/` |
| OpenCode | `~/.config/opencode/skills/build-brand-marketing-pack/` or `~/.agents/skills/build-brand-marketing-pack/` |
| GitHub Copilot | `~/.copilot/skills/build-brand-marketing-pack/` or `~/.agents/skills/build-brand-marketing-pack/` |

The Skill can always deliver a local Markdown pack. Lark, Google Docs, Notion, website extraction, and media generation use Aident Loadout capabilities or equivalent host-native tools and require the relevant connection or credit approval. Follow the [Aident Loadout setup instructions](https://aident.ai/SETUP.md) when those routes are selected.

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
    ├── host-compatibility.md
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
