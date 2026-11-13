# SEO/GEO Toolkit — workflow orchestration map

Which SEO/GEO skill to run at which stage of a content project. This reference owns the **choreography**; the skill's `SKILL.md` owns **what data is connected and how to pull it**.

**Before running anything, check "What's connected" in seo-geo's SKILL.md**, the one list of what's wired and what's gated. Every trigger below assumes that check: if its backend isn't connected, skip it (say so in one line) or ask the user for the data, and skip any trigger whose data the user already handed you.

---

## Workflow triggers (availability-checked)

These fire when their stage and conditions are met **and** the data backend each one needs is connected.

### During research (Step 2)

| Condition | Action |
|-----------|--------|
| Content type is blog, long-form, or website copy AND the user hasn't provided target keywords | Run `/keyword-research` for the topic. Use results to inform the outline. *(Needs DataForSEO — gated. Ask the user for target keywords instead.)* |
| Content type is blog or long-form AND this is a Content Bonanza workflow | Run `/serp-analysis` on the primary keyword to see what Google rewards (format, depth, features, AI Overviews). *(Needs DataForSEO — gated.)* |
| The user mentions a competitor by name or asks to differentiate | Run `/competitor-analysis` on the named competitor. *(Data-heavy parts need DataForSEO; the strategic read does not.)* For AI share of voice against the named competitor, run `aeo-insights` (its competitor view). |
| Content type is blog and the piece is part of a series or hub | Run `/seo-cluster` to validate the topic-cluster structure and internal-link plan. *(Intent-only mode is safe with no backend; SERP-overlap mode needs DataForSEO.)* |
| You need the site's current traffic or search performance to ground the piece | Pull it with this skill's `ga4` / `gsc` commands (connected). |
| GEO priority is high, the user asks where the subject shows up in AI answers, or an idea's "GEO opportunity" needs grounding | Run `aeo-insights` (named versus cited, per topic and per engine, competitors) and state the window. If it reports it isn't connected, say so. Never guess. |

### During drafting (Step 4)

| Condition | Action |
|-----------|--------|
| Content type is blog, long-form, or website copy | fresh-ink applies its SEO/GEO drafting rules (craft's SEO-GEO-drafting reference) while drafting. A drafting rule, not a post-draft skill. |

### After drafting (Step 5–6)

| Condition | Action |
|-----------|--------|
| Content will be published (blog, landing page, website copy) | Generate meta title + description. Offer `/meta-tags-optimizer` for alternatives. |
| Content includes FAQ or how-to sections | Offer `/schema-markup-generator` for FAQ, Article, or HowTo JSON-LD. |
| Content is a blog referencing other content on the same site | Run `/internal-linking-optimizer` to validate link structure and anchor text. |
| GEO priority is high (user stated it, or topic targets question/definition/comparison queries) — and by default for every published blog or website piece | fresh-ink runs `search-weave` after the no-slops gate, weaving the target keywords, questions, and citations into the structure. Hand it what this plugin found: GSC queries the page already ranks for, and `aeo-insights`'s named-vs-cited read and engine sub-questions for the topic. For definitional or comparison pieces, run `aeo-insights`'s winnability check BEFORE the outline is locked. |

---

## Offer-based triggers

Don't auto-run these. Present them as options (AskUserQuestion with `multiSelect: true`) at the right stage, and only surface ones that match the content type and context. Don't dump the full list.

### After outline approval (before drafting)

| Skill | When to offer | What it does |
|-------|--------------|-------------|
| `/seo-content-brief` | User wants a competitive brief (target word count, keyword density, heading structure) | Data-backed brief from SERP analysis *(needs DataForSEO)* |
| `/content-gap-analysis` | User is unsure of the angle, or wants gaps competitors miss | Surfaces topics/formats/angles competitors cover that this site doesn't |
| `/content-strategy` | The piece is part of a larger campaign or pillar | Pillars, clusters, prioritization framework *(safe with no backend)* |
| `/seo-plan` | User asks for a full SEO roadmap (rare in single-piece work) | Strategic plan: keyword priorities, calendar, technical recs |

### After presenting the draft (Step 6)

| Skill | When to offer | What it does |
|-------|--------------|-------------|
| `/content-quality-auditor` | User wants a quality score or publish-readiness check | 80-item CORE-EEAT audit with fixes |
| `/on-page-seo-auditor` | User wants a technical on-page review | On-page audit against the target keyword |
| `/seo-images` | Content has images, or user asks about image SEO | Alt text, file size, format, placement |
| `/seo-image-gen` | Content needs OG/hero/visual assets | Image generation plan with prompts (does not auto-generate) |
| `/entity-optimizer` | User wants stronger brand/author recognition in AI systems | Knowledge Graph and entity signal recs |
| `socialize` (fresh-ink) | User wants to repurpose the piece for other channels | Native versions for each platform (LinkedIn, X, Threads, Bluesky, Reddit, newsletter, email, and more) from the finished piece, citations intact |

### After publish

Offer when the user shares a live URL or asks about performance:

| Skill | When to offer | What it does |
|-------|--------------|-------------|
| `/performance-reporter` | User wants a report/dashboard on content performance | SEO/GEO report with KPI tracking: **feed it real numbers from this skill's `ga4`/`gsc` pulls, and AI-answer KPIs from `aeo-insights`, each labeled with its window** |
| `/content-refresher` | Published content is aging or losing traffic | What to update: stale stats, new competitors, decayed sections — **ground it in this skill's GSC trend pull** |
| `/seo-audit` | User shares a live URL and wants a full audit | Comprehensive page audit *(crawl steps need Firecrawl — gated)* |
| `/seo-page` | User wants a deep single-page analysis | One URL: content, keywords, links, schema, performance |
| `/rank-tracker` | User wants to track keyword positions over time | Monitors SERP positions *(needs DataForSEO; for this site's own queries, GSC position data via this skill is the connected alternative)* |
| `/seo-drift` | User wants to detect regressions on a page that was performing | Captures baselines and compares against stored snapshots |

---

## Data integrations

Connection status for every source (Google, DataForSEO, Firecrawl, PageSpeed, authority data) lives in seo-geo's "What's connected". AI-answer visibility is `aeo-insights`.

---

## Quick decision tree

```
RESEARCH PHASE
  └─ Need the site's current numbers? → seo-geo: ga4 / gsc  (connected once configured)
  └─ Need AI-answer visibility (GEO)? → aeo-insights  (Cairrot, where set up)
  └─ Do we have keywords?
       ├─ No → /keyword-research  (DataForSEO gated → ask user for keywords)
       └─ Yes → Do we know what's ranking?
            ├─ No → /serp-analysis  (DataForSEO gated)
            └─ Yes → proceed to outline

OUTLINE APPROVED
  └─ Want deeper research? → offer /seo-content-brief, /content-gap-analysis

DRAFT COMPLETE
  └─ Will this be published (blog, landing page, website copy)?
       ├─ Yes → meta tags, internal links
       │    ├─ AEO structure (default for published pieces) → fresh-ink's search-weave, fed by aeo-insights if connected
       │    └─ Has FAQ/HowTo? → /schema-markup-generator
       └─ No (social, email, internal) → skip SEO/GEO skills

POST-PUBLISH
  └─ Tracking performance? → seo-geo ga4/gsc (live) + aeo-insights (where wired) → /performance-reporter, /content-refresher
  └─ User shares live URL? → offer /seo-audit (crawl gated) or /seo-page
```
