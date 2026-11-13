---
name: blog
description: >
  Write blog posts and SEO blog content. Use this skill for any blog content task: write a post from scratch, produce a content brief or outline, optimize an existing draft, or analyze a competitor URL and write a post to outrank it. Trigger on "blog post", "write a blog post", "draft a blog", "content brief", "blog brief", "optimize this post", "outrank this article", or any request for blog content. Do NOT trigger for other content types (social posts, emails, ads, landing pages, 1-pagers); those route through craft. This skill runs robust intake and research, drafts to the locked SEO-blog shape with the default voice from tone-and-guidelines in the register the post calls for (B2B tech buyer for technical-product posts, personal for Taylor's own), and audits with no-slops before presenting clean copy.
---

# Blog Writer

You write blog content. craft delegates every blog request here, so this skill owns the blog's shape: the four workflows, the post structure, the brief template, on-page SEO, and the citation format. Everything that isn't blog-specific (the promise, research, drafting craft, voice, and the edit order) follows craft's workflow in `${CLAUDE_PLUGIN_ROOT}/skills/craft/SKILL.md`; this file points there instead of repeating it, so the two can't drift apart.

**Before writing anything,** read the craft passes in `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/prose-craft.md` (pass 0 puts no-slops's rulebook in front of you as drafting constraints) and the voice in `${CLAUDE_PLUGIN_ROOT}/skills/tone-and-guidelines/SKILL.md`, in the register the post calls for. **No-slops runs on every output,** briefs, outlines, FAQs, and meta copy included: the 35/50 gate, zero em dashes.

## Four workflows

| Input | Workflow |
|---|---|
| Topic or keyword | 1. Write from scratch (outline first if the user wants to approve one) |
| A brief, or "outline this first" | 2. Outline & brief |
| An existing draft | 3. Optimize |
| A competitor URL | 4. Outrank (analyze, brief, then write) |

If it isn't clear which one they want, ask: "Do you want a full post, an outline, or an optimization pass?"

---

## Step 1: The promise, then the blog specifics

Run craft's promise module first (craft Step 1, "The promise"): who it's for, what it's for, and why they should care, confirmed in one round. Most blogs are AEO/GEO with a buyer stage; name both. No answer to "why should they care" means no thesis yet; stop.

Then one more round for what only a blog needs:
1. **Target keyword**, primary plus any secondaries (search-weave will ask for questions and citations later; collect them now if the user has them)
2. **Content style:** thought leadership, how-to, or product-led
3. **Target length:** let the topic decide; don't pad or cut to a number
4. **CTA:** the specific next step (signup, newsletter, a feature page)

## Step 2: Research

Follow craft Step 2: web research, internal context only from connectors that are actually there, and every stat or quote handed to **cited-works** by name (or cited origin-first by hand if it isn't installed). Two blog-specific rules on top:

- **At least two credible sources** per post, internal or external.
- **Citations use the two-part inline format** (the stat phrase hyperlinked, then a plain "(Publisher, date)" closing the sentence), defined in tone-and-guidelines, Bibliography and attribution (`${CLAUDE_PLUGIN_ROOT}/skills/tone-and-guidelines/SKILL.md`). No footnotes or works-cited block on a blog. Ask cited-works to return citations in this format.

**Position the post** before drafting: searchable, shareable, or both; buyer stage; pillar and internal-link opportunities; and the gap it fills that competitors haven't. For a series or a backlog, use craft's ideation workflow.

---

## Workflow 1: Write from Scratch

Draft with craft Step 4: prose-craft passes 0 through 8, then the voice. The structure below is the skeleton; prose-craft is how each section gets written.

### Post structure
```
[Title]: includes the target keyword, sentence case, under 60 characters
[Intro]: hook in the first sentence (a sharp observation, a direct claim, a question, or a scenario the reader recognizes), at the point within two sentences. No preamble and no meta-commentary ("This post covers", "In this blog we'll", "Read on to learn", "By the end of this article", "We're going to walk you through", or any variant). Don't justify why the topic matters; the reader clicked.
[H2 sections]: keyword-aligned, logical flow, each with a clear point
[CTA or closing]: direct, purposeful
```

### On-page SEO, every post
- Target keyword in the title, the first 100 words, at least one H2, and the meta description
- Internal link opportunities marked `[INTERNAL LINK: suggested anchor + topic]`
- Meta title (60 characters or fewer), meta description (160 or fewer), and a slug, suggested at the end

Question-shaped headers, answer-first sections, the definitional block, secondary-keyword placement, and the FAQ's citability are search-weave's job after the draft; don't duplicate them here.

---

## Workflow 2: Outline & Brief

Deliver a structured brief the user can approve before full writing begins. What they are approving is the promise, the intro angle, and the section moves, not just a list of headers.

```
## Content Brief: [Working Title]

**The promise:** [one sentence: who this is for, beyond the keyword, and what they walk away with. Carried forward from the Step 1 promise module, not re-asked. Every section below is checked against it: anything that doesn't serve it is cut here, before it costs a draft.]
**Purpose:** [AEO/GEO, awareness, consideration, or decision. From Step 1. Most posts are AEO/GEO with a stage, so name both.]

**Target keyword:** [primary]
**Secondary keywords:** [2-4 related terms]
**Content style:** [thought leadership / how-to / product-led]
**Target length:** [word count]
**Audience:** [who this is for]
**Search intent:** [informational / navigational / commercial / transactional]
**Goal / CTA:** [what the post should drive]

---

### Proposed structure:

**Title:** [SEO title, sentence case, ≤60 chars]

**Highlights:**
A scannable summary block placed before the intro. Gives the reader an instant read on what the post covers and why it's worth their time. Keep it tight, 3 to 5 bullets, each one a concrete takeaway or key point from the post. No vague teasers. No "in this article we'll explore..." Write it like a TL;DR the reader would actually want.

- [Concrete takeaway or key point from the post]
- [Concrete takeaway or key point]
- [Concrete takeaway or key point]
- [Add a 4th or 5th if the post warrants it]

**Product callout** *(include when it fits naturally, skip if forced)*:
If any highlight directly connects to something the subject does or solves, add a one-sentence callout tied to that bullet. Format: a short, specific statement, not a sales pitch, e.g. "[Product] lets you ship this without writing a line of backend code." Only include if it earns its place. One callout per highlights block maximum.

**Intro angle:** [1-2 sentences on the hook/angle]

The intro follows the Post structure rule in Workflow 1 and prose-craft pass 2 (the lead): a hook in the first sentence, no announcing or meta-commentary, at the point within two sentences.

**H2: [Section title]** *(the move: states a claim / proves a claim / turns the argument)*
- Key point to cover
- The specific it carries: the number, name, quote, or artifact

**H2: [Section title]** *(the move)*
- Key point to cover
- The specific it carries

[...continue]

Each section is one named move carrying one specific, connected to the last by *but* or *therefore* (prose-craft §4 and §6, `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/prose-craft.md`).

**Kicker:** [the fact, image, or consequence the post lands on, never a summary (prose-craft §7). Naming it now stops the post ending on a wrap-up.]

**Closing / CTA:** [what action the reader should take. The kicker sets it up: the CTA is not the ending, the line before it is.]

---

### On-page SEO recommendations:

**Recommended slug:** [lowercase, hyphen-separated, keyword-first, no stop words, e.g. /prompt-coding-enterprise]
**Meta title:** [≤60 chars, includes primary keyword near the front, sentence case]
**Meta description:** [≤160 chars, includes primary keyword, clear value prop or CTA]

**Semantically related terms to include:**
- [LSI / related term 1]: suggested placement (e.g. intro, H2, body)
- [LSI / related term 2]: suggested placement
- [LSI / related term 3]: suggested placement
- [LSI / related term 4]: suggested placement
- [LSI / related term 5]: suggested placement

Derive these from: the target keyword's topic cluster, terms that appear across competitor pages, and natural synonyms a reader would expect. Don't force them, note where they fit naturally. These carry forward as search-weave's secondary keywords, so it places them after the draft rather than you forcing them in while writing.

---

### Competitor context:
[If a competitor URL was provided, note their angle, gaps, and how this post will differ]

### Internal linking opportunities:
[Suggested content to link to, if known]

---

### FAQs:
Follow search-weave's FAQ rules (pass 7, `${CLAUDE_PLUGIN_ROOT}/skills/search-weave/SKILL.md`): adjacent questions, edge cases, and objections, phrased the way people ask, each answered in a self-contained 40 to 60 words. Draft them here so the user approves them with the brief; search-weave checks them after the draft. Blog-only addition: if a question connects naturally to a product use case, one sentence of product tie-in in the answer, only if it fits.

**Q: [Question]**
A: [Answer]

**Q: [Question]**
A: [Answer]

**Q: [Question]**
A: [Answer]
```

---

## Workflow 3: Optimize Existing Draft

1. **On-page check.** Run the Workflow 1 On-page SEO list against the draft, plus the citation format (flag a link on the publisher's name instead of the claim, a missing date, and any footnotes or bibliography) and thin sections. Report as ✅ Pass / ⚠️ Fix needed / ❌ Missing, with the fix inline.
2. **The edit passes** below, in order, on the existing draft. Deliver the revised post with a short summary of what changed.

---

## Workflow 4: Outrank Competitor

Read `${CLAUDE_PLUGIN_ROOT}/skills/blog/references/competitor-research.md` in full before starting this workflow.

1. **Analyze the competitor URL** using the full 5-step process in the reference. Use web search for SERP results and competitor pages, or Insights' connected tools if that plugin is installed and wired.
2. **Propose a differentiated angle**, don't write the same post longer. The reference outlines six strategies; pick the right one.
3. **Deliver a brief first** (Workflow 2 format) with the Competitive Brief Summary Block filled in.
4. **Write the post** once the brief is approved, following Workflow 1 requirements.

---

## Present

Deliver clean, ready-to-publish copy: title (sentence case), the full body, the meta description, and the slug. If the user wants a file, ask where it should go and in what format (craft Step 6).

### Edit passes

The same Step 5 menu and order as craft: the no-slops gate, then the Schwartz re-angle and Ogilvy (on request; `headline-lab` when only the headline is in question), then **search-weave** (default for every published post), then **red-pen** (default, always last), then the final no-slops mechanical sweep. Skip what the post doesn't need; never reorder what runs. Full descriptions are in craft Step 5.

**Data, if you have it.** Keywords, questions, and citations come from the user's brief by default. If the Insights plugin is installed and wired, its `seo-geo` skill can supply real Search Console queries and the stage-by-stage SEO tool map, and `aeo-insights` the AI-answer baseline; both stay dormant otherwise. Never fabricate metrics.

## Brand reminder

Full name first, short form after, and the full name again in any passage that may be lifted alone (tone-and-guidelines, Product and brand names).
