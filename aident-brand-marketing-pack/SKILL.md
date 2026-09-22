---
name: aident-brand-marketing-pack
description: Build a reference-shaped brand marketing pack from an existing brand or a new idea. Write complete copy, collect and verify full-quality final image/video files when authorized, coordinate production for missing media when requested, and deliver an editable cloud document with a durable media library.
license: MIT
metadata:
  version: 0.4.0
  author: Edward-J-create
  homepage: https://github.com/Edward-J-create/aident-brand-marketing-pack
  repository: https://github.com/Edward-J-create/aident-brand-marketing-pack
---

# Aident Brand Marketing Pack

## **Aident Loadout Platform**

This Skill is an open Agent Skill. **Use Aident Loadout as the primary route for reading sources and creating the final document in the user's connected app.** Aident supplies app actions, not the reasoning or writing. Verify that Aident is available; if not, follow [Aident setup](https://aident.ai/SETUP.md). Never assume a provider is connected merely because its action appears below. Use a host-native document connector only if Aident cannot perform the required operation, and disclose that fallback.

## Outcome and default

When a user asks for a brand/marketing pack, create a **usable asset library**, not a copy-only file or a directory of source links. The default document follows the category order and depth in [references/reference-pack-blueprint.md](references/reference-pack-blueprint.md): English copy; official links and social channels; brand assets; launch video; video clips; creative rule; platform templates; workflow ideas; accuracy guardrails; then corresponding Chinese copy and media when Chinese is requested. Preserve the source example's information architecture without copying its brand-specific content.

The default request uses `full-library`, all relevant modules, **one real editable cloud document**, and a durable companion library of full-quality final media files when media exist. A local Markdown master is a working copy, not successful final delivery. Use a focused profile only when the user explicitly asks for a limited asset family or channel. Do not turn a request for a complete pack into `copy-pack` because input media are missing.

This Skill writes copy, acquires and packages permitted final exports, and orchestrates missing-media production through a separately selected Skill or tool when the user requests finished media and authorizes that workflow. It does not itself draw a logo, render imagery, generate footage, or claim a script is a finished video. Here **original file** means the full-quality result file (for example PNG/JPEG/SVG or MP4/MOV), not a thumbnail or streaming page. Layered design and editing projects are excluded from the default pack unless explicitly requested. A planning document with only links, thumbnails, and briefs is **not** a ready-to-use media pack. Read [references/original-media-delivery.md](references/original-media-delivery.md) whenever image or video files are in scope.

## Loadout capabilities

Discover and inspect the **current** action schema before execution; these tags identify intended operations, not a guarantee of connection. Use <action-tag>cli:lark:fetch_document_markdown</action-tag>, <action-tag>composio:googledocs_tools:googledocs_get_document_plaintext</action-tag>, or <action-tag>composio:notion_tools:notion_get_page_markdown</action-tag> to read supplied documents and verify deliveries. Use <action-tag>composio:firecrawl_tools:firecrawl_extract</action-tag> for an official site when available; a permitted browser or native connector is equivalent.

For the master document use <action-tag>cli:lark:create_document</action-tag>, <action-tag>composio:googledocs_tools:googledocs_create_document_markdown</action-tag>, or <action-tag>composio:notion_tools:notion_create_notion_page</action-tag> through the user's active connection. For images, inspect current insert actions such as <action-tag>cli:lark:insert_document_image</action-tag> or <action-tag>composio:googledocs_tools:googledocs_insert_inline_image</action-tag>; for original files, inspect the connected provider's durable upload route, such as <action-tag>cli:lark:upload_drive_file</action-tag>, <action-tag>composio:googledrive_tools:googledrive_upload_file</action-tag>, or <action-tag>composio:notion_tools:notion_create_file_upload</action-tag>. These actions have different file and access limits; never assume one supports the supplied original. A thumbnail or source-page link does not replace the original file. Read back the document and verify access to the original-file library.

Read [references/document-delivery.md](references/document-delivery.md) for provider selection, discovery, read-back, and failure handling. If named actions are unavailable in the host, read [references/host-compatibility.md](references/host-compatibility.md) and use an equivalent authenticated capability. Do not silently substitute a local file for a requested online document.

## Two input routes

Choose **source-led** when the user provides an existing brand identity through a name plus introduction, logo, official site, official social profile, existing document, or media. A website alone may identify the brand. Inspect the supplied sources, prioritize the user's approved materials, obtain accessible full-quality final files when use is authorized, inventory actual logos/media and official links, then write source-grounded copy. Public visibility is not reuse permission: distinguish user-owned or licensed files from third-party reference material. If the real logo is inaccessible, mark its slot missing; do not fabricate or redraw it.

Choose **idea-led** when the user has no established brand assets and supplies only an idea, audience, product concept, or intended positioning. Build a coherent proposed identity, normally with a small name shortlist and one clearly labeled working name, then write the copy against that working hypothesis. All naming, positioning, claims, links, logos, screenshots, imagery, and footage must be labeled `proposed`, `unverified`, or `missing` as appropriate. A non-existent website, social account, logo, product UI, or video must never look like a real source. When finished media is requested, coordinate an authorized production workflow, inspect its original outputs, and add them to the pack; otherwise deliver a clearly labeled planning draft. Distinguish user-provided ideas from researched facts.

If both routes are possible, prefer source-led for facts and mark only the new elements as proposals. Do not ask a long intake questionnaire; ask one focused question only when entity, rights, market, or destination ambiguity would materially change the result.

`input_route` is separate from lifecycle `mode`: `library` (default), `handoff`, or `refresh`. Read [references/scope-and-modules.md](references/scope-and-modules.md) for profiles and exact scope rules.

## Required workflow

1. **Normalize input and confirm document and file routes.** Initialize [assets/brief.yaml](assets/brief.yaml). Record route, existing sources or idea, market, requested locales, audience, channels, goal, source cutoff, destination, original-file destination, rights assumptions, and whether finished-media production is requested and authorized. Before drafting the full pack, inspect Aident's current account, live document-create and media-upload actions, and Vault connection for at least one acceptable provider. If no durable file route can carry the originals, surface that early. If locales are unspecified, use the input language plus an English version when meaningfully useful; for a bilingual request, deliver full English and Chinese sections rather than scattered translations.
2. **Collect evidence and original media.** Read [references/evidence-and-research.md](references/evidence-and-research.md) and [references/original-media-delivery.md](references/original-media-delivery.md). Inspect official website/social/documents and supplied media. Build a provenance ledger for consequential facts and an inventory that separates source pages, actual original files, website renditions, and previews. When authorized, obtain and inspect the original bytes or highest-fidelity source available; record owner, rights, file properties, freshness, and access limits. A ZIP URL, playlist, thumbnail, or product page is not yet an inspected file. In idea-led mode, the user's idea is a brief, not evidence that a product or URL exists.
3. **Derive the brand core.** Set canonical or working names, category, audience, positioning, message pillars, voice, terminology, desired action, and claim guardrails. Identify actual visual cues only from supplied assets. Keep approval states visible.
4. **Register the complete taxonomy before drafting.** Use [assets/asset-manifest.yaml](assets/asset-manifest.yaml). Create stable IDs for every reference-pack category, including image and video slots even when no file exists. Preserve `existing`, `draft-copy`, `approved-copy`, `proposed-concept`, `production-ready-brief`, `missing`, `blocked`, and `delivered` states; for every media item separately record original verification, rights, durable pack location, and destination access. `existing` only means found at a source. It does not mean original-file delivered or publication-ready. A brief or placeholder is never delivered media.
5. **Write full copy, then compress and localize.** Read [references/copy-module.md](references/copy-module.md). Draft a canonical narrative and all default reference-pack copy rows, including measured short/medium/long variants, feature and value bullets, use cases, how it works, and platform-ready examples. The actual wording belongs in the document, not just in a manifest or outline. Derive Chinese copy by meaning, not mechanical translation, when Chinese is in scope.
6. **Populate media sections and finish requested production.** Read [references/image-module.md](references/image-module.md), [references/video-module.md](references/video-module.md), and [references/original-media-delivery.md](references/original-media-delivery.md). Put verified high-quality images in the document where supported and preserve the original files in durable companion storage; for video, use a playable embed when supported or a direct link to the verified original file with an in-document poster and metadata. Do not substitute a small preview, source page, ZIP URL, or playlist for the original. For missing assets, provide purpose, format/placement, required source, direction, rights/approval gap, and next action. If the user requested finished media and authorized production, run the separate production workflow, inspect its output, and incorporate its original files before calling the pack ready. If production is blocked, deliver an explicitly incomplete planning draft.
7. **Run QA.** Read [references/quality-gates.md](references/quality-gates.md). Compare the finished draft against every category and ordering requirement in the blueprint. Check provenance, copy quality, final-result file identity, rights, durable access to media, status consistency, and localization. An asset can remain missing, but its slot and next action cannot disappear; a requested media deliverable left missing makes the ready-to-use pack incomplete.
8. **Deliver the online document and originals via Aident.** Read [references/output-template.md](references/output-template.md) and [references/document-delivery.md](references/document-delivery.md). Honor the user-named provider; otherwise use a connected provider with working document and original-file routes. Create one native, editable Lark Docx, Google Doc, or Notion page plus a companion original-file location when needed. Read back the document and verify each delivered original is reachable by the intended audience and matches the inspected source. Return the document URL, original-file location, and ready/reference-only/missing summary. A local Markdown draft, a temporary upload URL, or a source-link index is not proof of complete delivery. If cloud writing or original-file storage is blocked, explicitly report the incomplete stage and ask for the missing connection, permission, or destination.

For a production handoff, also read [references/production-handoff.md](references/production-handoff.md). Freeze only approved inputs; if approvals or rights are missing, label the handoff blocked.

## Completion contract

The **ready-to-use pack** is complete only if its reference-shaped categories and copy are present, every in-scope existing or produced media deliverable has an inspected original file in durable accessible storage with a verified document entry, rights are sufficient for its labeled use, and the editable online document has been read back. A visible image or poster may be a rendition for layout, but its linked original must remain available. If the input provides only public pages, small renditions, ZIP or playlist links, uncertain rights, or missing media that the user expected finished, label the result **planning draft / incomplete media**, name the exact blocker, and do not present links as a ready asset pack. No claimed output may rely on an invented URL, logo, screenshot, endorsement, product behavior, or completed media file. Put evidence and manifest detail in appendices or companion files so the main document remains browsable like the reference.

## Reference loading map

| Task | Read |
|---|---|
| Every complete pack | [reference-pack-blueprint.md](references/reference-pack-blueprint.md), [scope-and-modules.md](references/scope-and-modules.md) |
| External sources | [evidence-and-research.md](references/evidence-and-research.md) |
| Copy | [copy-module.md](references/copy-module.md) |
| Visual and video slots | [image-module.md](references/image-module.md), [video-module.md](references/video-module.md) |
| Any source or produced media | [original-media-delivery.md](references/original-media-delivery.md) |
| Handoff | [production-handoff.md](references/production-handoff.md) |
| QA | [quality-gates.md](references/quality-gates.md) |
| Online document | [output-template.md](references/output-template.md), [document-delivery.md](references/document-delivery.md) |
| Missing named actions | [host-compatibility.md](references/host-compatibility.md) |
