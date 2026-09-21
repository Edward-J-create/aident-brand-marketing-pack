# Host Compatibility

Use this reference when the current Agent host does not expose the exact Aident actions named in `SKILL.md`, or when network, provider, or file access is limited.

## Portable core

With only the Skill files and a writable location, an agent can perform scope selection, brief normalization, evidence work from supplied material, brand core creation, final copy, asset inventory, visual and video briefs, manifests, quality checks, and local Markdown delivery.

Do not block these outputs because a connector is unavailable. Narrow the evidence base and disclose the gap.

## Capability mapping

| Need | Preferred route | Acceptable equivalent | Invariant |
|---|---|---|---|
| Read official URL | Aident website extraction | Native web fetch, browser, or approved connector | Record URL, retrieval date, status, and access gaps |
| Read Lark, Google Docs, or Notion | Matching Aident read action | Native authenticated connector | Never infer inaccessible private content |
| Create editable cloud document | Matching Aident create action | Native provider action | Create one requested destination and read it back |
| Insert existing approved image in Lark | Aident Lark image action | Native document image insertion | Preserve rights and source record; verify placement |
| Deliver locally | File write | Any host file tool | Verify the Markdown file exists and is readable |
| Produce final media | Separate user-selected production workflow | Any authorized production Skill or tool | Use frozen brief; return outputs and QA; never run implicitly |

Equivalent tools are interchangeable only at the capability level. Inspect the live schema available in the current host.

## Degradation rules

1. If public research is unavailable, use supplied material and mark unsupported external facts as unknown.
2. If a private document is inaccessible, request an export or permission; do not reconstruct it from hints.
3. If a cloud provider is unavailable, preserve the verified Markdown master.
4. If read-back is unavailable, do not report cloud delivery as verified.
5. If no production workflow is available, deliver the complete brief and label media as not produced.
6. If files cannot persist, return complete Markdown in the conversation and disclose that no durable library was created.

## Host-specific metadata

Files under `agents/` are optional adapters. The portable contract is the folder containing `SKILL.md`, `references/`, and `assets/`.
