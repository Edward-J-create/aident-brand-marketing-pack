# Evidence and Research

Use this reference whenever the pack depends on URLs, social profiles, external documents, or claims that can change.

## Source hierarchy

Use the narrowest reliable source for each fact:

1. User-approved facts, copy, and uploaded assets.
2. Official product pages, company pages, documentation, pricing pages, release notes, app-store listings, and press rooms.
3. Official social profiles and official creator or partner materials.
4. Reputable third-party reporting for context only.
5. Search snippets only as discovery leads, never as final evidence when the source cannot be opened.

“Official” does not mean “current.” Record retrieval date and any visible publication or update date.

## Efficient collection

- Start from the exact URLs the user supplied.
- For a website, extract homepage, product or service pages, about page, documentation, pricing, case studies, press or newsroom, and contact or social links only when relevant.
- For social profiles, prefer a native platform action. Sample enough recent posts to detect recurring language and content patterns; do not treat a small sample as a complete strategy.
- For documents, preserve headings, tables, links, and media references. Inventory embedded files separately when they cannot be downloaded or previewed.
- Avoid crawling an entire domain before a focused extraction proves insufficient.

## Evidence ledger

Maintain one row per consequential claim:

| Field | Meaning |
|---|---|
| Claim ID | Stable identifier such as `FACT-001` |
| Claim | Atomic factual statement |
| Source | Exact document or URL |
| Source type | user, official-site, official-doc, official-social, third-party |
| Retrieved | ISO date |
| Status | verified, user-supplied, inferred, stale, conflicting, unknown |
| Confidence | high, medium, low |
| Used in | Asset IDs or sections that depend on the claim |
| Notes | Scope, date, conflict, or wording constraint |

Do not put creative proposals in the evidence ledger. Track them in the asset matrix as `proposed`.

## Conflict rules

- Prefer a user-confirmed correction over older published copy and record the correction as user-supplied.
- Prefer current official product documentation over marketing summaries for technical behavior.
- Prefer a current pricing page over old blog posts for pricing, but warn that pricing is time-sensitive.
- Do not combine incompatible numbers into a new claim.
- If two first-party sources disagree and recency or scope is unclear, mark the claim conflicting and omit it from public copy until resolved.

## High-risk claims

Require direct evidence and conservative wording for:

- customer, revenue, growth, usage, performance, savings, or market-share numbers;
- security, privacy, compliance, certification, medical, legal, or financial claims;
- “free,” “unlimited,” “best,” “guaranteed,” “secure,” or “fully automated” claims;
- compatibility, integration, model, pricing, availability, and geographic coverage;
- testimonials, named customers, awards, quotes, and endorsements.

## Brand voice inference

Infer voice only from a meaningful first-party sample. Record both positive and negative evidence:

- sentence length and rhythm;
- vocabulary and technical density;
- level of directness, humor, urgency, and formality;
- how proof and calls to action are presented;
- words or frames that repeatedly appear or are conspicuously avoided.

Describe inferred voice as a proposal until the user approves it.

## Research stop condition

Stop collecting when each required asset has enough verified facts and tone evidence to draft, and new sources are repeating the same information. Continue only when a material gap, conflict, or time-sensitive claim remains.
