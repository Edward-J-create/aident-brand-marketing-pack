# Host Compatibility

Use this reference when the current Agent host does not expose the exact Aident actions named in `SKILL.md`, or when network, provider, or file access is limited.

## Portable core

With only the Skill files and a writable location, an agent can perform scope selection, brief normalization, evidence work from supplied material, brand core creation, final copy, asset inventory, visual and video briefs, manifests, quality checks, and local Markdown drafting. This is not equivalent to the default online-document delivery.

Do not block these outputs because a connector is unavailable. Narrow the evidence base and disclose the gap.

## Capability mapping

| Need | Preferred route | Acceptable equivalent | Invariant |
|---|---|---|---|
| Read official URL | Aident website extraction | Native web fetch, browser, or approved connector | Record URL, retrieval date, status, and access gaps |
| Read Lark, Google Docs, or Notion | Matching Aident read action | Native authenticated connector | Never infer inaccessible private content |
| Create editable cloud document | Matching Aident create action, after current Vault check | Native provider action only when Aident is unavailable or cannot perform it | Create one native document and read it back; disclose any route change |
| Insert existing approved image in Lark | Aident Lark image action | Native document image insertion | Preserve rights and source record; verify placement |
| Store final result files | Matching Aident Drive, Lark, or Notion upload action | Native provider storage when Aident is unavailable | Keep full-quality PNG/JPEG/SVG and MP4/MOV exports; verify file identity and audience access; exclude editable projects by default |
| Deliver locally | File write | Any host file tool | Verify the Markdown file exists and is readable |
| Produce final media | Separate user-selected production workflow | Any authorized production Skill or tool | Use frozen brief; return outputs and QA; never run implicitly |

Equivalent tools are interchangeable only at the capability level. Inspect the live schema available in the current host.

## Degradation rules

1. If public research is unavailable, use supplied material and mark unsupported external facts as unknown.
2. If a private document is inaccessible, request an export or permission; do not reconstruct it from hints.
3. If no cloud provider is writable, preserve the Markdown draft and permitted final result files but mark online delivery incomplete and ask for a connection or explicit local-only change of scope.
4. If the document is writable but no route can store the actual result files, mark media delivery incomplete; do not call a link-only document a ready pack.
5. If read-back is unavailable, do not report cloud delivery as verified.
6. If no production workflow is available, deliver the complete brief and label media as not produced.
7. If files cannot persist, return complete Markdown in the conversation and disclose that neither an online document nor a durable local library was created.

## Host-specific metadata

Files under `agents/` are optional adapters. The portable contract is the folder containing `SKILL.md`, `references/`, and `assets/`.
