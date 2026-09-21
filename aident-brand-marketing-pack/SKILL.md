---
name: aident-brand-marketing-pack
description: Build an evidence-backed, reusable brand marketing pack from brand notes, official URLs, social profiles, documents, or existing assets. Use when an agent must classify marketing assets, write final copy, inventory source media, define production-ready visual or video briefs, maintain provenance, and deliver an editable Markdown, Lark, Google Docs, or Notion document. This skill specifies and evaluates media; it does not render or edit image or video files.
license: MIT
metadata:
  version: 0.2.0
  author: Edward-J-create
  homepage: https://github.com/Edward-J-create/aident-brand-marketing-pack
  repository: https://github.com/Edward-J-create/aident-brand-marketing-pack
---

# Aident Brand Marketing Pack

## **Aident Loadout Platform**

This Skill is authored, published, and distributed through [**Aident Loadout**](https://loadout.aident.ai/), a platform that enables agents to connect securely with more than 1,000 popular apps and tools.

Before using this Skill, verify that the Aident Loadout Skill, CLI, Plugin, or MCP is installed globally in the current environment. If Aident Loadout is already available, continue with this Skill and complete any setup required by the selected integrations. If it is unavailable or its installation status is uncertain, follow the [**Aident Loadout setup instructions**](https://aident.ai/SETUP.md). After installation is verified, return to the brief and continue.

## Host compatibility

This is a filesystem-based Agent Skill, not a Codex-only workflow. Any host that can read `SKILL.md`, bundled references, and YAML assets can run the portable workflow and produce a local Markdown pack. `agents/openai.yaml` is optional discovery metadata.

Read [references/host-compatibility.md](references/host-compatibility.md) when named actions are unavailable. Map capabilities, not provider-specific parameters, and preserve the evidence, approval, read-back, and fallback rules.

## Loadout capabilities

For source documents, use <action-tag>cli:lark:fetch_document_markdown</action-tag>, <action-tag>composio:googledocs_tools:googledocs_get_document_plaintext</action-tag>, or <action-tag>composio:notion_tools:notion_get_page_markdown</action-tag>. For official websites, use <action-tag>composio:firecrawl_tools:firecrawl_extract</action-tag>. For public social profiles, prefer a native platform capability; otherwise use permitted public web access and report access gaps.

For one requested editable destination, use <action-tag>cli:lark:create_document</action-tag>, <action-tag>composio:googledocs_tools:googledocs_create_document_markdown</action-tag>, or <action-tag>composio:notion_tools:notion_create_notion_page</action-tag>. Use <action-tag>cli:lark:insert_document_image</action-tag> only for an existing, approved image available through supported temporary storage. Read the created document back with the matching read action before calling delivery verified. Local Markdown is always a valid fallback.

This Skill contains no image- or video-generation action. Never search for or call any media-generation model within this Skill merely because a visual or video module is selected.

## Outcome and boundary

Create a durable brand marketing source of truth, not a one-off pile of slogans. The pack may contain final text, an inventory of existing media, and production-ready visual or video briefs. It must distinguish facts, approvals, proposals, production state, provenance, rights, and unresolved gaps.

This Skill owns:

- evidence collection and claim control;
- brand core and reusable final copy;
- asset taxonomy, IDs, states, and dependencies;
- visual and video specifications, prompt direction, scripts, shot lists, and acceptance criteria;
- one editable master document and its read-back verification.

This Skill does not own:

- logo or visual-identity redesign;
- raster or vector rendering, layout implementation, animation, editing, voice generation, or final video export;
- choosing a paid generation model, spending credits, or claiming that a brief is a finished asset.

If finished media is requested, complete the selected copy and production contract first, then offer a handoff to a separately selected production Skill or tool. Do not make that handoff silently, and do not require any particular production provider.

## Choose scope and mode

Read [references/scope-and-modules.md](references/scope-and-modules.md). Select the smallest profile that satisfies the request and state the selected modules before substantial work.

Modules are independently reusable:

- `core` — evidence ledger, canonical identity, positioning, audience, message pillars, voice, terminology, and claim guardrails;
- `copy` — reusable copy and only the requested channel variants;
- `inventory` — official links and existing text, image, video, audio, document, and template assets;
- `visual-spec` — production-ready briefs for requested static or visual assets;
- `video-spec` — production-ready briefs for requested motion or video assets;
- `localization` — only requested locales;
- `delivery` — one Markdown, Lark, Google Docs, or Notion destination.

Modes control state, not breadth:

- **Library** is the default. Create or extend the reusable source of truth.
- **Handoff** freezes approved inputs and acceptance criteria for an external production workflow. If required approvals are missing, deliver a clearly `blocked` handoff draft instead of claiming the package is frozen or production-ready. It still does not render media.
- **Refresh** compares new evidence with an existing pack and revises only affected claims or assets.

Use `full-library` only when the user asks for a complete pack. A narrow request stays narrow.

## Intake rules

Accept any combination of brand name, description, official website, official social profiles, source documents, existing copy or media, audience, market, campaign goal, locale, channels, and destination.

Proceed without an interview when one brand and one deliverable are clear. Ask only when an answer materially changes the result:

1. Which entity is intended if the name is ambiguous?
2. Which market or locale wins if sources conflict?
3. Which outputs and channels are actually required?
4. Which single editable destination should receive the pack?
5. For a handoff, who approves the copy and what production formats are required?

Record assumptions. Never invent a missing fact to avoid a question.

## Required workflow

### 1. Normalize the brief

Initialize [assets/brief.yaml](assets/brief.yaml) for a reusable, multi-asset, or refresh request. Capture the brand, goal, audience, desired action, locale, channels, supplied sources, selected profile and modules, destination, constraints, and approval owner.

Treat supplied facts and assets as authoritative inputs unless labeled draft or explicitly opened for critique. Do not infer permission to redesign a logo or rewrite a legal claim.

### 2. Build the evidence ledger first

Read [references/evidence-and-research.md](references/evidence-and-research.md) when URLs, social profiles, external documents, or mutable claims are involved.

Prefer user-approved material, then current first-party sources, then reputable third-party context. Record each consequential claim with a stable ID, exact source, retrieval date, confidence, status, and dependent asset IDs. Keep proposals outside the fact ledger.

### 3. Derive the brand core

Produce the minimum shared layer every selected asset inherits:

- canonical brand, company, product, and feature names;
- category, audience, job to be done, and desired action;
- one positioning statement and three to five message pillars with proof;
- voice attributes, anti-attributes, approved terms, discouraged terms, and prohibited claims;
- existing visual cues and asset rules, without inventing a new identity system.

Label interpretation as `inferred` or `proposed` until approved.

### 4. Register assets before drafting

Use [assets/asset-manifest.yaml](assets/asset-manifest.yaml) for every requested, existing, proposed, or delivered asset. Assign stable IDs. Record purpose, audience, channel, locale, format, evidence and copy dependencies, owner, source or output link, rights, status, QA, and reuse notes.

Allowed lifecycle statuses are `existing`, `draft-copy`, `approved-copy`, `production-ready-brief`, `in-production`, `delivered`, `blocked`, `missing`, and `deprecated`. A brief never becomes `delivered` media.

### 5. Write the selected text

Read [references/copy-module.md](references/copy-module.md). Write a canonical long-form narrative first and derive shorter variants from it. Adapt hook, rhythm, proof density, CTA, and formatting by channel while preserving claim scope. Measure requested character limits.

Copy embedded in a visual or video remains a named copy asset with its own ID and approval state; do not bury it only inside a brief.

### 6. Specify selected visuals and video

For a visual asset, read [references/image-module.md](references/image-module.md) and complete [assets/visual-brief.yaml](assets/visual-brief.yaml). For a video asset, read [references/video-module.md](references/video-module.md) and complete [assets/video-brief.yaml](assets/video-brief.yaml).

Reference existing logos, product screenshots, footage, fonts, colors, and copy by stable IDs or URLs. Specify platform, dimensions, safe areas, hierarchy, variants, editable-source requirements, exports, rights, accessibility, and acceptance checks. Never fabricate a real product UI or logo inside a generation prompt.

For Handoff mode, also read [references/production-handoff.md](references/production-handoff.md). Freeze the approved dependencies and prepare the smallest complete production contract. Do not render the asset.

### 7. Apply quality gates

Read [references/quality-gates.md](references/quality-gates.md). Apply common gates plus only those for selected modules. Fail closed on unsupported claims, inaccessible required sources, ambiguous ownership, unresolved rights, missing copy approval, or an incomplete production contract.

### 8. Deliver one editable master

Read [references/output-template.md](references/output-template.md). Create one canonical Markdown master, then optionally create the single requested Lark, Google Docs, or Notion copy. Read back the created document and compare structure, copy, links, tables, and asset states. If verification fails, preserve the Markdown master and report the exact gap.

## Completion contract

A pack is complete only when:

- every requested text asset exists and has an honest approval state;
- consequential claims map to evidence or are visibly qualified;
- each requested visual or video item is either inventoried or has a complete production brief;
- no brief, prompt, or storyboard is mislabeled as rendered media;
- manifest statuses, dependencies, owners, rights, and QA results are visible;
- the verified editable destination or verified Markdown fallback is accessible;
- blocking gaps and the next production or approval action are explicit.

## Reference loading map

| Task | Read |
|---|---|
| Any scoped request | [scope-and-modules.md](references/scope-and-modules.md) |
| External or mutable sources | [evidence-and-research.md](references/evidence-and-research.md) |
| Copy | [copy-module.md](references/copy-module.md) |
| Inventory or static visuals | [image-module.md](references/image-module.md) |
| Inventory or video | [video-module.md](references/video-module.md) |
| External production handoff | [production-handoff.md](references/production-handoff.md) |
| Final QA | [quality-gates.md](references/quality-gates.md) |
| Delivery | [output-template.md](references/output-template.md) |
| Missing named capabilities | [host-compatibility.md](references/host-compatibility.md) |
