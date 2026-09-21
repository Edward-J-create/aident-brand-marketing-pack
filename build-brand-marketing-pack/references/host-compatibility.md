# Host Compatibility

Use this reference only when the current Agent host does not expose the exact Aident Loadout actions named in `SKILL.md`, or when its sandbox limits network, file, or provider access.

## Portable core

The following work is host-neutral and requires only access to the Skill files plus a writable output location:

- scope and module selection;
- brief normalization;
- evidence ledger construction from user-supplied material;
- brand core, copy, image briefs, prompts, video concepts, scripts, and shot lists;
- asset-manifest maintenance;
- local Markdown delivery and local read-back verification.

Do not block these outputs because an external connector is unavailable. Reduce the scope to the evidence that can actually be read and disclose the gap.

## Capability mapping

| Need | Preferred packaged route | Acceptable host equivalent | Required invariant |
|---|---|---|---|
| Read an official URL | Aident website extraction | Native web fetch, browser, or approved connector | Record URL, retrieval date, status, and access gaps |
| Read Lark, Google Docs, or Notion | Matching Aident read action | Native authenticated connector | Never infer inaccessible private content |
| Deliver an editable cloud document | Matching Aident create action | Native provider action | Create exactly one requested destination and read it back |
| Generate an image or video | Aident media action | Native generation tool | Production mode, exact approved count, cost/rights check, inspect output |
| Deliver locally | File write | Any host file tool | Verify the Markdown file exists and is readable |

Equivalent tools are interchangeable only at the capability level. Do not copy Aident-specific parameters into an unrelated provider call. Inspect the live schema or tool documentation available in the current host.

## Degradation rules

1. If public research is unavailable, use supplied material and mark external facts as unverified or missing.
2. If a cloud document provider is unavailable, preserve the verified Markdown master and state the exact connection requirement.
3. If media generation is unavailable, deliver reviewed briefs and prompts; do not call them finished media.
4. If the host cannot read back an external document, do not report delivery as verified.
5. If the host cannot persist files, return the complete Markdown in the conversation and disclose that no durable asset library was created.

## Host-specific metadata

Files under `agents/` are optional adapters for a particular host. The portable contract is the folder containing `SKILL.md`, `references/`, and `assets/`. A host may ignore metadata it does not recognize, but it must not ignore the workflow and safety boundaries in `SKILL.md`.
