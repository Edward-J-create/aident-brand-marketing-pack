# Original Media Acquisition and Delivery

Use for every source-led pack with existing media and every idea-led pack that returns newly produced media. In this Skill, **original file** means the full-quality **finished result file** supplied or exported for use, such as a full-resolution PNG/JPEG/SVG or final MP4/MOV. It does **not** mean an editable PSD/AI/Figma file, animation project, or editing timeline. The default deliverable is an editable document plus the actual result files where the document cannot retain them. Keep production source files out of the default pack unless the user explicitly requests a source-file handoff. A small preview, source page, ZIP URL, playlist, temporary URL, or script is not an original-file deliverable.

## Decide what may be collected

Classify each source as `user-supplied/owned`, `licensed or explicitly approved`, `public third-party reference`, or `permission unknown`. Public visibility or a first-party website does not grant the agent redistribution, modification, or advertising rights. Respect provider terms, authentication, robots/access controls, and the brand's published usage rules. Do not bypass restrictions or publish private files to make an image-insertion action work. If copying into the pack is not authorized, show a cited reference and mark `reference-only / rights blocked`; ask for approval or owner-provided originals when necessary.

## Acquire the best permitted source

1. Prefer the user's supplied full-quality final export or connected brand asset library. Next prefer an official downloadable asset package. Inspect archive members safely and select its **result files**; the archive link itself is not the file inventory. Put a vector logo export in the pack when that is the usable logo result, but do not add unrelated design projects by default.
2. Preserve the exact bytes of the selected final result file whenever possible. For video, prefer an approved high-quality master/export, not its editing project; a streaming page or playlist is not a raw video file. Do not manufacture an "original" by upscaling, screenshotting, or transcoding a preview.
3. If the website exposes only a resized CDN image or streaming rendition, label it `website rendition`, record its real resolution and source page, and seek a higher-fidelity file. The highest obtainable rendition is not silently promoted to an original.
4. Inspect MIME type, file size, pixel dimensions for raster media, duration and resolution for video, and a SHA-256 digest when bytes are accessible. Check that the file opens. Record retrieval date and any expiry. Do not count HEAD success or a page URL as a downloaded, inspected asset.

## Pack record and user-facing labels

For each media ID record the source page, direct original-file source if known, filename/format, dimensions or duration, bytes/hash when available, ownership and rights, original-verification result, persistent pack location, intended audience access check, and document placement. Keep source evidence separate from delivery location.

Use these labels consistently:

- `Original file — ready`: original bytes inspected, rights match the stated use, durable file is accessible to the intended audience, and the document points to it.
- `Original file — review required`: bytes inspected and stored, but publication or modification rights remain unapproved. It is available for review, not an approved campaign asset.
- `Reference only`: an official page, streaming item, or file is visible, but copying or reuse is not authorized or the original is unavailable.
- `Website rendition only`: the inspected file is an optimized page asset, not an original export.
- `Missing / proposed / production blocked`: no real file passed the original-file and rights checks.

The legacy manifest `status: existing` means only that a source exists. It does not satisfy `Original file — ready` without the separate media fields.

## Deliver through a real provider

Before choosing Lark, Google Docs, or Notion, inspect the connected provider's current document-image, file-upload, storage, and read-back actions. Check size, format, public-URL, account, and folder constraints against actual files. For example, the current Google Docs inline-image action accepts a direct public PNG/JPEG/GIF URL with limits; it cannot embed an SVG master or an MP4. A document-rendered image may be a high-quality display rendition, while the vector or high-resolution original stays in the companion library. Do not make a private original public merely to satisfy image insertion.

Use durable, user-controlled cloud storage for originals, preferably alongside the document in the same provider. Keep the original filename and exact bytes; create a derivative only for display, label it as a derivative, and link it back to the original. For video, place a poster and direct file/open action in the document if native video embedding is unavailable; the underlying MP4/MOV/master file must still be available in the companion library. A streaming playlist alone does not satisfy this contract. Verify the destination ID, access for the intended audience, file size or digest when the provider exposes it, and the document entry after write. Temporary Aident file-storage URLs are a transfer route, not final asset locations.

Do not impose a universal 5 MB limit. Many finished images and short clips may fit under it, but preserve file quality and inspect the actual provider cap for each upload. If a result exceeds a chosen route's cap, use a compatible durable storage route or ask for a destination; do not silently recompress it to satisfy the cap.

If no connected provider can store or expose the original because of file size, permission, schema, or audience access, stop before claiming a ready pack. Keep any permitted local originals as a recoverable working set, report the exact limitation, and ask for an acceptable durable destination. Do not silently downsize or substitute links.

## Missing-media production

When the user wants finished media but none exists, this Skill owns the brief, authorized handoff, return inspection, original-file registration, and final pack integration. Choose a separate production Skill/tool that fits the medium; inspect its current instructions and cost/permission requirements. Do not run paid generation or external publication on the user's behalf without the needed authorization. If production is not authorized or feasible, deliver the copy and briefs as an explicitly incomplete planning draft, not a finished media pack.
