# SEO and GEO toolkit: which tool, which stage

This file covers the order of work: which tool to reach for at which stage of a content project. seo-geo's SKILL.md covers what is connected and how to pull data.

**Before running anything, check "What's connected" in seo-geo's SKILL.md.** Each trigger below assumes that check passed. If a tool's data source isn't connected, skip it and say so in one line, or ask the user for the data. Also skip any trigger whose data the user already supplied.

---

## Automatic triggers

These fire when their stage and conditions match and the data source is connected.

### Research

| When | Do this |
|---|---|
| A blog, long-form, or website piece has no target keywords from the user | Run `/keyword-research` on the topic and use the results for the outline. *(Needs DataForSEO. Otherwise ask the user for keywords.)* |
| A blog or long-form piece is part of an ongoing workflow (not a one-off) | Run `/serp-analysis` on the main keyword to see what results reward: format, depth, features, AI overviews. *(Needs DataForSEO.)* |
| The user names a competitor or asks how to differ from one | Run `/competitor-analysis` on that competitor. The strategic read works without data; the data parts need DataForSEO. For AI share of voice against the competitor, use `aeo-insights`' competitor view. |
| A blog is one piece of a series or hub | Run `/seo-cluster` to check the cluster structure and the internal-link plan. Intent-only mode works with no backend; SERP overlap needs DataForSEO. |
| The piece needs the site's current traffic or search performance | Pull it with `ga4` or `gsc`. |
| AI answer visibility matters, or an idea's "GEO opportunity" has to be grounded | Run `aeo-insights` (named versus cited, per topic and per engine, plus competitors) and state the time window. If it isn't connected, say so. Never guess. |

### Drafting

| When | Do this |
|---|---|
| A blog, long-form, or website piece is being drafted | fresh-ink applies its search and AI writing rules as it drafts. That's a drafting rule, not a separate step. |

### After drafting

| When | Do this |
|---|---|
| The piece will be published (blog, landing page, website copy) | Write a meta title and description. Offer `/meta-tags-optimizer` for alternatives. |
| The piece has an FAQ or how-to section | Offer `/schema-markup-generator` for FAQ, article, or how-to structured data. |
| A blog links to other pages on the same site | Run `/internal-linking-optimizer` to check the links and their anchor text. |
| Citation structure matters (a question-led topic, or every published blog and web piece by default) | fresh-ink runs `search-weave` after the no-slops gate. Give it what this plugin found: the queries the page already ranks for, and `aeo-insights`' named-versus-cited reading and the sub-questions engines asked. For definition or comparison pieces, run `aeo-insights`' winnability check before the outline is set. |

---

## Offered options

Don't run these automatically. Offer them as choices (AskUserQuestion, `multiSelect: true`) at the right stage, and only the ones that fit. Don't list them all at once.

### Before drafting (after the outline is approved)

| Skill | Offer it when | What it does |
|---|---|---|
| `/seo-content-brief` | The user wants a competitive brief with a target length, keyword density, and heading structure | Data-backed brief from SERP analysis *(needs DataForSEO)* |
| `/content-gap-analysis` | The angle is unclear, or the user wants gaps competitors leave open | Topics, formats, and angles competitors cover that this site doesn't |
| `/content-strategy` | The piece belongs to a larger campaign or pillar | Pillars, clusters, and a prioritization framework *(works with no backend)* |
| `/seo-plan` | The user asks for a full SEO roadmap (rare for a single piece) | A strategy with keyword priorities, a calendar, and technical recommendations |

### After the draft

| Skill | Offer it when | What it does |
|---|---|---|
| `/content-quality-auditor` | The user wants a quality score or a publish-readiness check | An 80-item audit with fixes |
| `/on-page-seo-auditor` | The user wants a technical on-page review | An on-page audit against the target keyword |
| `/seo-images` | The content has images, or image SEO comes up | Alt text, file size, format, placement |
| `/seo-image-gen` | The content needs social or hero images | An image plan with prompts (prompts only; nothing is generated automatically) |
| `/entity-optimizer` | The user wants stronger brand and author recognition in AI systems | Recommendations on entity signals |
| `socialize` (fresh-ink) | The user wants the piece repurposed for other channels | Native versions for each platform, citations kept |

### After publishing

Offer these when the user shares a live URL or asks how something performs:

| Skill | Offer it when | What it does |
|---|---|---|
| `/performance-reporter` | The user wants a report or dashboard on content performance | An SEO and GEO report with KPIs. **Feed it real numbers from `ga4` and `gsc`, and AI-answer KPIs from `aeo-insights`, each with its window.** |
| `/content-refresher` | Published content is aging or losing traffic | What to update: stale figures, new competitors, decayed sections. **Ground it in the GSC trend pull.** |
| `/seo-audit` | The user shares a live URL and wants a full audit | A full page audit. *(The crawl steps need Firecrawl.)* |
| `/seo-page` | The user wants a deep look at one page | Content, keywords, links, schema, and performance for one URL |
| `/rank-tracker` | The user wants keyword positions tracked over time | Position monitoring. *(Needs DataForSEO. For this site's own queries, the GSC position data is the connected alternative.)* |
| `/seo-drift` | A page that used to perform has slipped | Compares the page with stored baselines to catch regressions |

---

## Data sources

Connection status for every source lives in seo-geo's "What's connected." Summary:

| Source | What it covers | Status | Use it for |
|---|---|---|---|
| **seo-geo** (this plugin) | GA4 and Search Console for the configured site | Connected once set up | Real traffic and search numbers. The default for "our actual data." |
| **aeo-insights** (this plugin) | AI-answer visibility across the major answer engines | Connected where set up | Named versus cited, per topic and per engine, competitor standing, sentiment, and crawler activity. |
| `/seo-google` | Search Console, PageSpeed, CrUX, GA4 (generic) | Partial | PageSpeed and CrUX angles. For GA4 and Search Console, prefer this plugin's puller. |
| `/seo-dataforseo` | Live SERP data, keyword metrics, backlinks | Gated | Search volume, difficulty, SERP features, and competitor data, if the DataForSEO extension is installed. |
| `/seo-firecrawl` | Full-site crawl | Gated | Site crawl and internal-link inventory, if Firecrawl is installed. |
| `/seo-backlinks` | Backlink profile | Gated | Link signals. The data parts need DataForSEO. |
| `/domain-authority-auditor` | Domain authority and competitive position | Gated | How aggressively to target keywords. Needs an external authority source. |

---

## Decision tree

```
RESEARCH
  Need the site's current numbers?       seo-geo ga4 / gsc (once set up)
  Need AI-answer visibility?             aeo-insights (where set up)
  Have target keywords?
    No  -> /keyword-research (gated: ask the user for keywords)
    Yes -> Know what ranks?
             No  -> /serp-analysis (gated)
             Yes -> go to the outline

OUTLINE APPROVED
  Want deeper research? -> offer /seo-content-brief or /content-gap-analysis

DRAFT COMPLETE
  Will it be published (blog, landing page, website copy)?
    Yes -> meta tags and internal links
           Citation structure -> fresh-ink's search-weave, fed by aeo-insights if set up
           Has FAQ or how-to? -> /schema-markup-generator
    No  (social, email, internal) -> skip the SEO and GEO tools

AFTER PUBLISHING
  Tracking performance? -> seo-geo ga4 / gsc, and aeo-insights, into /performance-reporter or /content-refresher
  User shares a live URL? -> offer /seo-audit (crawl steps gated) or /seo-page
```
