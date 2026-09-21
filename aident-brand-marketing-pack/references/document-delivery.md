# Online Document Delivery

The default final artifact is **one editable online document**. Local Markdown is an intermediate master/backup. Use the user's explicit provider if given. Otherwise choose the first connected, writable option in this order: Lark, Google Docs, Notion. If the source is already a Lark/Google/Notion document, prefer that provider unless the user asks otherwise. Never create three redundant documents merely because three actions exist.

## Provider workflow

1. Discover the exact provider action in Aident Loadout (`capabilities search`), inspect its live schema (`capabilities get`), and check the current connection/account (`vault status` or host equivalent). Do this in the run. **Connected/readable does not prove writable**: a provider app may still lack document-create scopes or a permitted parent location.
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

If a create action fails, diagnose schema, account, app scopes, permission, parent location, size, and content conversion once. An error such as Lark `app_scope_not_applied` requires the app developer/administrator to grant the named scopes; it is not fixed by retrying or by assuming the user's login is bad. Try a connected alternate provider only if the user did not mandate a provider. Do not silently switch from an explicitly requested provider. Preserve the local draft and status, but say **online delivery incomplete**, give the precise blocker, and request the required connection or destination choice. If create succeeds but read-back fails, share the link as unverified and do not label the task complete. Never paste credentials or private document contents into logs.
