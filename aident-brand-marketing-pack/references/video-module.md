# Video Asset Module

Use this module to inventory and package permitted existing footage and define production-ready video contracts. It produces concepts, scripts, copy, shot plans, and acceptance criteria; a separate authorized production workflow generates, edits, voices, or exports new video. Read [original-media-delivery.md](original-media-delivery.md) before labeling a video ready.

## Inventory existing assets

Record finished product captures, interviews, testimonials, demos, launch films, logo motion, captions, posters, masters, and cutdowns. Prefer an approved full-quality MP4/MOV export to a social stream or low-resolution preview. Capture the actual result file separately from its watch page, owner, rights, release status, size/hash when accessible, duration, resolution, aspect ratio, locale, durable pack location, and reuse limits. Editing timelines, animation projects, and raw source footage are not default pack deliverables; include them only in a separately requested source-file handoff. A YouTube/Vimeo playlist is not an inventory of verified video files; identify each relevant finished clip and its file availability.

## Video brief contract

Complete [../assets/video-brief.yaml](../assets/video-brief.yaml) for every requested master or cutdown family. Define:

- objective, audience, channel, placement, desired action, and success condition;
- format type, master ID, cutdown IDs, duration, aspect ratio, resolution, frame rate, and safe areas;
- hook, story beats, payoff, and CTA with timestamps or time budgets;
- voiceover, on-screen copy, captions, and end-card copy by asset ID;
- shot or scene list with source type: supplied footage, real capture required, licensed stock, or generated concept;
- real product behavior that must be shown accurately;
- visual treatment, motion behavior, logo entry and exit, transitions, and poster frame;
- voice, music, sound design, caption format, loudness or delivery requirements when known;
- source rights, releases, accessibility, editable project, export variants, owners, and acceptance checks.

## Script rules

- Put the product, problem, or tension early enough for the target channel.
- One scene should perform one communication job.
- Time narration at a realistic speaking rate and reserve room for pauses.
- Keep on-screen copy shorter than voiceover; specify reading time.
- Do not invent a customer quote, result, product action, or screen flow.
- Mark conceptual scenes so they cannot be mistaken for product footage.

## Shot-source labels

Every shot must use one of:

- `supplied` — exact provided file;
- `capture-required` — a real product or environment capture must be produced;
- `licensed-stock` — search and license separately;
- `generated-concept` — synthetic visual is allowed, subject to an external production workflow;
- `motion-design` — built from approved graphic assets in an editable project.

## Acceptance baseline

Fail the brief if duration or platform is unknown, a real product action lacks a capture source, copy is unapproved, rights are unresolved, or deliverables and review owner are missing. A storyboard is not a rendered video. A finished video is ready in the pack only when its original export, rights, durable file location, intended-audience access, and document entry are verified; a streaming page or poster alone is reference-only.
