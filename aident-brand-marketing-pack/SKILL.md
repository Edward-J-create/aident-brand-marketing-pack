---
name: aident-brand-marketing-pack
description: Build a reference-shaped, bilingual-ready brand marketing asset library and deliver it as a verified editable Lark, Google Docs, or Notion document. Use with an existing brand name/logo/introduction/official URL, or with only a new brand idea. Write complete marketing copy, classify and link real media, and specify missing visual/video assets without pretending concepts are finished files.
license: MIT
metadata:
  version: 0.3.0
  author: Edward-J-create
  homepage: https://github.com/Edward-J-create/aident-brand-marketing-pack
  repository: https://github.com/Edward-J-create/aident-brand-marketing-pack
---

# Aident Brand Marketing Pack

## **Aident Loadout Platform**

This Skill is an open Agent Skill. Aident Loadout supplies connected app actions, not the reasoning or writing. Verify that Aident Loadout is available; if not, follow [Aident setup](https://aident.ai/SETUP.md). Never assume a provider is connected merely because its action appears below.

## Outcome and default

When a user asks for a brand/marketing pack, create an **asset library document**, not a copy-only file. The default result follows the category order and depth in [references/reference-pack-blueprint.md](references/reference-pack-blueprint.md): English copy; official links and social channels; brand assets; launch video; video clips; creative rule; platform templates; workflow ideas; accuracy guardrails; then corresponding Chinese copy and media when Chinese is requested. Its table cells contain usable text or exact asset links, while absent media remain visibly marked as missing or proposed. Preserve the source example's information architecture without copying its brand-specific content.

The default request uses `full-library`, all relevant modules, and **one real editable cloud document**. A local Markdown master is a working copy, not successful final delivery. Use a focused profile only when the user explicitly asks for a limited asset family or channel. Do not turn a request for a complete pack into `copy-pack` because input media are missing.

This Skill writes the copy and asset production contracts. It inventories and embeds or links approved existing media; it does not draw a logo, render imagery, generate footage, or claim a script is a finished video. If actual media production is requested, prepare the pack and offer a separate authorized production workflow.

## Loadout capabilities

Discover and inspect the **current** action schema before execution; these tags identify intended operations, not a guarantee of connection. Use <action-tag>cli:lark:fetch_document_markdown</action-tag>, <action-tag>composio:googledocs_tools:googledocs_get_document_plaintext</action-tag>, or <action-tag>composio:notion_tools:notion_get_page_markdown</action-tag> to read supplied documents and verify deliveries. Use <action-tag>composio:firecrawl_tools:firecrawl_extract</action-tag> for an official site when available; a permitted browser or native connector is equivalent.

For the master document use <action-tag>cli:lark:create_document</action-tag>, <action-tag>composio:googledocs_tools:googledocs_create_document_markdown</action-tag>, or <action-tag>composio:notion_tools:notion_create_notion_page</action-tag> through the user's active connection. Use <action-tag>cli:lark:insert_document_image</action-tag> only for an existing, approved image when the current schema and storage flow support it. A provider link or an explicit unembedded asset link is preferable to a broken image. Read back the created document; never report cloud delivery as verified merely because a create call returned success.

Read [references/document-delivery.md](references/document-delivery.md) for provider selection, discovery, read-back, and failure handling. If named actions are unavailable in the host, read [references/host-compatibility.md](references/host-compatibility.md) and use an equivalent authenticated capability. Do not silently substitute a local file for a requested online document.

## Two input routes

Choose **source-led** when the user provides an existing brand identity through a name plus introduction, logo, official site, official social profile, existing document, or media. A website alone may identify the brand. Inspect the supplied sources, prioritize the user's approved materials, inventory actual logos/media and official links, then write source-grounded copy. If the real logo is inaccessible, mark its slot missing; do not fabricate or redraw it.

Choose **idea-led** when the user has no established brand assets and supplies only an idea, audience, product concept, or intended positioning. Build a coherent proposed identity, normally with a small name shortlist and one clearly labeled working name, then write the complete pack against that working hypothesis. All naming, positioning, claims, links, logos, screenshots, imagery, and footage must be labeled `proposed`, `unverified`, or `missing` as appropriate. A non-existent website, social account, logo, product UI, or video must never look like a real source. Distinguish user-provided ideas from researched facts.

If both routes are possible, prefer source-led for facts and mark only the new elements as proposals. Do not ask a long intake questionnaire; ask one focused question only when entity, rights, market, or destination ambiguity would materially change the result.

`input_route` is separate from lifecycle `mode`: `library` (default), `handoff`, or `refresh`. Read [references/scope-and-modules.md](references/scope-and-modules.md) for profiles and exact scope rules.

## Required workflow

1. **Normalize input.** Initialize [assets/brief.yaml](assets/brief.yaml). Record route, existing sources or idea, market, requested locales, audience, channels, goal, source cutoff, destination, and assumptions. If locales are unspecified, use the input language plus an English version when meaningfully useful; for a bilingual request, deliver full English and Chinese sections rather than scattered translations. Do not invent a locale requirement the user explicitly excluded.
2. **Collect evidence and inventory.** Read [references/evidence-and-research.md](references/evidence-and-research.md). Inspect official website/social/documents and supplied media where accessible. Build a provenance ledger for consequential facts and a link inventory. Record source, owner, rights, freshness, and access limitations. In idea-led mode, the user's idea is a brief, not evidence that a product or URL exists.
3. **Derive the brand core.** Set canonical or working names, category, audience, positioning, message pillars, voice, terminology, desired action, and claim guardrails. Identify actual visual cues only from supplied assets. Keep approval states visible.
4. **Register the complete taxonomy before drafting.** Use [assets/asset-manifest.yaml](assets/asset-manifest.yaml). Create stable IDs for every reference-pack category, including image and video slots even when no file exists. Status must distinguish `existing`, `draft-copy`, `approved-copy`, `proposed-concept`, `production-ready-brief`, `missing`, `blocked`, and `delivered`. A brief or placeholder is never delivered media.
5. **Write full copy, then compress and localize.** Read [references/copy-module.md](references/copy-module.md). Draft a canonical narrative and all default reference-pack copy rows, including measured short/medium/long variants, feature and value bullets, use cases, how it works, and platform-ready examples. The actual wording belongs in the document, not just in a manifest or outline. Derive Chinese copy by meaning, not mechanical translation, when Chinese is in scope.
6. **Populate media sections.** Read [references/image-module.md](references/image-module.md) and [references/video-module.md](references/video-module.md). Place approved existing media in the document where supported; otherwise give a visible exact link and format. For missing assets, provide purpose, format/placement, required source, one concise creative direction, owner/rights/approval gap, and next action. For a launch video, include a usable concept, script/beat sheet, shot-source labels, cover, subtitle/locale variants, and status. Do not use empty headings or generic prompt lists.
7. **Run QA.** Read [references/quality-gates.md](references/quality-gates.md). Compare the finished draft against every category and ordering requirement in the blueprint. Check provenance, copy quality, link validity, media truthfulness, status consistency, rights, and localization. An asset can remain missing, but its slot and next action cannot disappear.
8. **Deliver the cloud document.** Read [references/output-template.md](references/output-template.md) and [references/document-delivery.md](references/document-delivery.md). Choose the user-named provider; otherwise prefer connected Lark, then Google Docs, then Notion. Discover and inspect the live action and connection, create one readable/editable document, and read back its title, headings, representative copy, links, and asset labels. Return the real document URL and a short ready/missing summary. Keep local Markdown as a backup or explicit fallback only. If no provider can create/read back, report that the online deliverable is incomplete and ask for connection or another destination.

For a production handoff, also read [references/production-handoff.md](references/production-handoff.md). Freeze only approved inputs; if approvals or rights are missing, label the handoff blocked.

## Completion contract

The default pack is complete only if its reference-shaped category coverage is intact, requested copy is actually written, each media slot links a real approved file or clearly states its missing/proposed status and production requirement, and the editable online document has been read back. No claimed output may rely on an invented URL, logo, screenshot, endorsement, product behavior, or completed media file. Put evidence and manifest detail in appendices or companion files so the main document remains browsable like the reference.

## Reference loading map

| Task | Read |
|---|---|
| Every complete pack | [reference-pack-blueprint.md](references/reference-pack-blueprint.md), [scope-and-modules.md](references/scope-and-modules.md) |
| External sources | [evidence-and-research.md](references/evidence-and-research.md) |
| Copy | [copy-module.md](references/copy-module.md) |
| Visual and video slots | [image-module.md](references/image-module.md), [video-module.md](references/video-module.md) |
| Handoff | [production-handoff.md](references/production-handoff.md) |
| QA | [quality-gates.md](references/quality-gates.md) |
| Online document | [output-template.md](references/output-template.md), [document-delivery.md](references/document-delivery.md) |
| Missing named actions | [host-compatibility.md](references/host-compatibility.md) |
