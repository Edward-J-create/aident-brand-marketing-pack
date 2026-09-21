# Online Document Delivery

The default final artifact is **one native, editable online document created through Aident Loadout**. Local Markdown is an intermediate drafting buffer/backup, never a successful default handoff. Use the user's explicit provider if given. Otherwise select a connected provider whose create action can write in the current run; prefer the provider holding the source document when appropriate. Do not keep retrying a provider already shown to lack write permission. Never create three redundant documents merely because three actions exist.

## Provider workflow

1. Discover the exact provider action in Aident Loadout (`capabilities search`), inspect its live schema (`capabilities get`), and check the current account and connection (`whoami` and `vault status`, or the matching Aident host tools). Do this before the full drafting pass. **Connected/readable does not prove writable**: a provider app may still lack document-create scopes or a permitted parent location. A connection installed after an earlier check must be detected by a fresh Vault read, not ruled out by stale state.
2. Prepare Markdown for the [output template](output-template.md). For Lark, check that the create action accepts the content format and that tables/links/images will survive conversion. For Google Docs or Notion, respect the live action's parent/location requirements and do not invent one.
3. Create **one** master document with a brand-specific title. If the action returns `requires-user-acknowledgement`, request explicit approval for this exact write; only then retry the identical action/input with the one-time acknowledgement scope. Never self-acknowledge or request an indefinite scope merely to make delivery automatic. Record the returned document/page ID and URL. A local file path does not satisfy this step.
4. Read the document back with the matching provider read action. Verify title; English/Chinese headings as requested; first, middle, and last copy rows; representative official/source links; visible image/video references or missing-status labels; and the asset index. If conversion strips a table or image, repair through an available document action or reformat as plain headings and links, then read back again.
5. Report the URL and verification state. If the user must grant access, say so. Do not assert the document is editable by others unless sharing permissions were actually checked.

## Media in the document

- Existing approved image: embed with a supported provider action if available; otherwise place its exact accessible source URL and label it `Existing — linked, not embedded`. Keep rights and source in the asset index.
- Existing video: embed or link only if the provider and permissions support it. A source link with a preview description is acceptable; never claim an embedded player that was not verified.
- Missing visual/video: use a clearly styled concept/brief card with status `Missing` or `Proposed`; no synthetic placeholder masquerading as a rendered asset.
- If the source is a private file and the destination's audience cannot access it, the item remains blocked for sharing. Do not publish a private URL as if public.

## Failure recovery

If a create action fails, diagnose schema, account, app scopes, permission, parent location, size, and content conversion once. A Lark `app_scope_not_applied` error names an **application-level** permission: the app developer/administrator must grant the stated scopes. Browser login, local CLI user login, and Aident Vault `connected` do not themselves repair that bot-app permission. Do not retry the identical failing action without a changed permission state. If the user did not mandate Lark, try a fresh Vault check and one connected Google Docs or Notion action. Do not silently switch from an explicitly requested provider. Preserve the local draft and status, but say **online delivery incomplete**, give the precise blocker, and request the required connection or destination choice. If create succeeds but read-back fails, share the link as unverified and do not label the task complete. Never paste credentials or private document contents into logs.
