# Production Handoff

Use this reference only when a visual or video brief must move into a separate production workflow.

## Separation of responsibilities

This Skill owns the production contract. The selected production Skill or tool owns rendering, editing, iteration files, exports, and output inspection. The user owns approvals and any paid execution authorization.

Do not hard-code a dependency on a named model, vendor, design app, or video editor. Select an available production workflow after the contract is complete and only when the user has asked for execution. If approval, rights, or required source assets are missing, return a `blocked` handoff draft rather than a frozen handoff.

## Handoff package

Provide:

1. Handoff ID, date, brand, campaign, owner, and approval owner.
2. Frozen brief version and selected deliverable IDs.
3. Approved copy IDs and exact text.
4. Source asset links or file paths, rights, and required real captures.
5. Master and variant specifications.
6. Editable-source and export requirements.
7. Acceptance checklist and prohibited changes.
8. Open blockers, optional creative latitude, and return format.

## Return contract

Ask the production workflow to return, per asset:

- output and editable-source links or paths;
- production tool or method and version when relevant;
- source assets actually used and rights notes;
- deviations from the brief;
- QA evidence, including dimensions or duration and visual inspection;
- status: `in-production`, `blocked`, or `delivered`.

On return, update the manifest. Do not automatically approve a delivered file; verify it against the frozen acceptance criteria and flag subjective approvals for the named owner.

## When separate production Skills are justified

Create a separate production Skill when the workflow contains renderer-specific implementation, model selection, design-system components, animation code, editing timelines, caption burning, audio mixing, or export logic. Those concerns change faster than the stable brand-pack contract and should be versioned independently.
