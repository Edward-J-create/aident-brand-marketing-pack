# Quality Gates

Apply common gates plus gates for selected modules before delivery and after provider read-back.

## Common gates

- Scope matches the selected profile. A generic pack request remains `full-library`; only an explicitly narrow request may omit categories.
- Canonical names, audience, primary value, CTA, locale, and terminology are consistent.
- Every consequential factual claim maps to a source or is visibly qualified.
- Time-sensitive sources include retrieval dates; conflicts and inaccessible sources remain visible.
- Asset IDs, dependencies, owner, rights, status, and source or output location are complete.
- `delivered` is used only for an accessible external output, never for a prompt, concept, script, or brief.
- A source page, ZIP URL, streaming playlist, temporary transfer URL, or small preview is not counted as an inspected original file. `existing` does not by itself mean ready to use.

## Original-media gates

- Every media item promised as ready has inspected original bytes, format, size/dimensions or duration, source provenance, rights for the stated use, a durable pack location, and a verified intended-audience access path. Compare a digest or file size with the source when the provider exposes it.
- Full-quality finished image/vector files and final video masters/exports are retained where available. Display renditions link back to the final result file and are never mislabeled as it. Editable design or editing projects are excluded from the default pack unless the user explicitly requests a separate source-file handoff.
- Media visible only on a public third-party website is `reference-only` or `website rendition only` until acquisition and reuse rights are established; it is not a cleared ad asset.
- For requested finished media, a separate authorized production workflow returned and inspected the actual file before the pack is marked ready. Otherwise the result is an incomplete planning draft with the blocker named.

## Copy gates

- Final requested text exists rather than only an outline.
- Short versions derive from the canonical narrative and preserve claim scope.
- Channel adaptation changes form, not facts.
- Character-limited text includes measured counts.
- Variants are meaningfully distinct and label the changed strategic axis.
- No invented testimonial, endorsement, customer, partnership, metric, urgency, or regulated claim appears.
- Visual and video copy exists as separately reviewable copy assets.

## Visual-brief gates

- Platform, placement, master size, aspect ratio, variants, and safe areas are explicit.
- Copy and source visuals are referenced by stable IDs or exact links.
- Logo lockup, placement, clear space, partner treatment, and prohibited modifications are explicit when relevant.
- Product UI is supplied, capture-required, or clearly conceptual; it is never silently fabricated.
- Composition, hierarchy, focal point, crop behavior, editable source, export formats, alt text, and accessibility are defined.
- Rights and approval ownership are resolved or the brief is `blocked`.
- Acceptance checks are observable, not adjectives such as “premium” alone.

## Video-brief gates

- Platform, placement, master duration, aspect ratio, resolution, frame rate when relevant, and cutdowns are explicit.
- Hook, story beats, CTA, and time budget fit the requested duration.
- Voiceover, on-screen copy, captions, and end card reference approved copy assets.
- Every shot has a source label and product actions requiring real capture are identified.
- Logo behavior, poster frame, audio, accessibility, editable project, exports, and rights are defined.
- Acceptance checks cover message accuracy, readability, timing, brand use, captions, and delivery format.
- A concept, script, animatic brief, or storyboard is not labeled as a final video.

## Handoff gates

- Brief version and dependencies are frozen.
- All required copy has an approval state and exact text.
- Inputs are accessible to the production workflow.
- Creative latitude and prohibited changes are explicit.
- Return contract requires output, editable source, deviations, rights, and QA evidence.
- Paid or externally mutating execution remains separately authorized.

## Document gates

- The main document follows the [reference blueprint](reference-pack-blueprint.md) category order for every requested locale; missing media families have status and actionable briefs, not disappeared headings.
- The first screen shows usable brand copy/assets and route/status, not a process ledger.
- All requested copy rows contain real wording; required length variants have measured counts or an explained unmet constraint.
- Each real visual/video has a verified original-file location and a document entry. Images are displayed at useful quality when supported; video has a player or poster plus direct access to the original file. Each non-real item is visibly missing/proposed. No placeholder, source-page link, or thumbnail is presented as completed media.
- Tables, links, copy, status labels, and requested locale headings survived provider conversion.
- One editable online document was created and read back, and the companion original-file library was checked where applicable. Local Markdown or a link-only document is an incomplete default media delivery; if the provider is blocked, state the blocker explicitly.

## Completion rule

Complete as a **ready-to-use pack** means selected copy and media exist, original files and rights are verified, and the editable document plus companion file library are accessible. A pack containing only source references and production contracts is a **planning draft**, even when its document is editable. Requested media are not produced unless a separate authorized workflow returned inspected files that passed acceptance checks.
