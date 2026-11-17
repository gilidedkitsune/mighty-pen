---
name: blog
description: >
  Blog posts and SEO blog content: write a post from scratch, produce a brief or outline,
  optimize an existing draft for search, or analyze a competitor's page and write one that
  outranks it. Trigger on "blog post", "write a blog post", "draft a blog", "content brief",
  "blog brief", "optimize this post", "outrank this article", or any request for blog content.
  Not for other types (social, email, ads, landing pages, one-pagers), which route through craft.
  Runs its own promise step and research, drafts in the register the post calls for, and checks
  the result with no-slops before presenting it.
---

# Blog

The blog skill owns the blog's shape: its four workflows, its structure, its brief template, on-page SEO, and its edit order. Everything else is shared with craft and linked, not repeated: the promise questions, the research and sourcing rules, the drafting craft, the voice, and the review passes. Read those in their homes:

- Drafting craft: `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/prose-craft.md`
- Voice and citation format: `${CLAUDE_PLUGIN_ROOT}/skills/tone-and-guidelines/SKILL.md`
- The filter: `${CLAUDE_PLUGIN_ROOT}/skills/no-slops/SKILL.md`, which runs on every output, including briefs, outlines, FAQs, and meta copy. Zero em dashes.
- The shared workflow and promise steps: `${CLAUDE_PLUGIN_ROOT}/skills/craft/SKILL.md`

## Four workflows

| The user has | Workflow |
|---|---|
| A topic or keyword | 1. Write from scratch (or 2 first, if they want to approve an outline) |
| A brief, or asks for an outline first | 2. Outline and brief |
| An existing draft | 3. Optimize |
| A competitor URL | 4. Outrank (analyze, brief, then write) |

If it's unclear which one they want, ask: "Do you want a full post, an outline, or an optimization pass?"

---

## Step 1: Promise and blog specifics

Run craft's promise step first: who the post is for, what it's for (most blog posts serve search and AI answers and a buyer stage, so name both), and why the reader should care, confirmed in one round. If there's no answer to "why should they care," the post has no thesis yet, so stop there.

Then one more round, for what only a blog needs:
1. **Target keyword:** the primary phrase, plus any secondaries. search-weave asks for questions and citations later, so collect them now if the user has them.
2. **Style:** thought leadership, how-to, or product-led.
3. **Length:** let the topic decide. Don't pad or trim to hit a number.
4. **Call to action:** the specific next step (sign up, subscribe, open a feature page).

---

## Step 2: Research

Follow craft's research step. Web research for the current conversation and figures. Internal material only from connectors that actually exist. Every figure, quote, or claim goes to **cited-works**, or, if it isn't installed, gets traced to its origin by hand.

Two rules specific to blogs:
- At least two credible sources per post, internal or external.
- Citations use the two-part inline format from tone-and-guidelines: the claim hyperlinked to its source, then a plain "(Publisher, year)" closing the sentence. No footnotes, bibliography, or works-cited list. Chicago belongs to long-form, which goes through craft. Ask cited-works to return citations in this format.

Before drafting, position the post: searchable, shareable, or both (most are searchable first); the buyer stage; pillar and internal-link opportunities; and the gap competing posts leave open. For a series or a backlog, use craft's ideation workflow.

---

## Workflow 1: Write from scratch

Draft with craft's Step 4, prose-craft first and then the voice. The structure below is the frame; prose-craft is how each section gets written.

### Post structure

```
[Title] under 60 characters, sentence case, keyword included
[Intro] a hook in the first sentence, at the point within two sentences, no preamble
[Sections] each one a single move, named, with a specific it carries; joined by "but" or "therefore"
[FAQ] three to five adjacent questions (see below)
[Kicker, then call to action] a fact, image, or consequence, then the next step
```

The intro never announces the post. Avoid "This post covers," "In this blog we'll," "Read on to learn," "By the end of this article," or any variant. Start in the topic. Don't justify why the subject matters; the reader already clicked.

### On-page SEO, every post
- The target keyword in the title, within the first 100 words, in at least one H2, and in the meta description.
- Internal link opportunities marked `[INTERNAL LINK: anchor text, target topic]`.
- A meta title of 60 characters or fewer, a meta description of 160 or fewer, and a slug, all suggested at the end.

Question-shaped headers, answer-first sections, the definitional block, placing secondary keywords, and checking the FAQ are search-weave's work after the draft. Don't duplicate them here.

### FAQ
Draft three to five questions for the end of the post. Follow search-weave's FAQ rules (pass 7): adjacent questions, edge cases, and objections, phrased the way people ask, each answered in 40 to 60 words. Draft them now so the user approves them with the brief. search-weave checks them after the draft. One blog-only addition: where a question connects naturally to a product use case, one sentence of product mention in the answer, only if it fits.

---

## Workflow 2: Outline and brief

The user approves the promise, the intro angle, and the section moves. A list of headings alone isn't enough.

```
## Brief: [working title]

**Promise:** one sentence, carried from Step 1. Every section below is checked against it. Anything that doesn't serve it gets cut here.
**Stage and purpose:** from Step 1
**Primary keyword:** ...
**Secondary keywords:** two to four related phrases
**Style:** thought leadership, how-to, or product-led
**Length:** a word target
**Reader:** who they are
**Search intent:** informational, navigational, commercial, or transactional
**Call to action:** what the post should drive

### Title
Sentence case, 60 characters or fewer, with the keyword near the front.

### Highlights
Three to five concrete takeaways, placed before the intro. Each one is a specific point from the post, not a teaser. Write them the way a reader would want a summary.

### Product mention (optional)
If a highlight connects to what the product does, one sentence tied to it, and only if it reads naturally. At most one per brief.

### Intro
- The hook (a sharp observation, a claim, a question, or a scenario the reader knows).
- Get to the point within two sentences of the opening.
- No announcing, no meta-commentary, no justification.

### Sections
For each section: the heading, the move it makes (states, proves, or turns), the points it covers, and the specific it carries (a number, a name, a quote, or an artifact).
Joins: each section follows from the one before with *but* or *therefore*.
Weight: the section you care most about gets the most room.

### Kicker and call to action
The kicker is the fact, image, or consequence the post ends on. Name it now, so the draft doesn't end on a summary. The call to action comes after it.

### On-page SEO
- Slug: lowercase, hyphenated, keyword first
- Meta title and meta description (within their limits)
- Related terms, with a suggested place for each. Only the ones that fit naturally. These carry forward to search-weave as secondary keywords.

### Competitor context
If a competitor URL was given, its angle, its gaps, and how this post differs.

### Internal links
Existing content on the site to link to, if known.

### FAQ
Three to five questions and short answers, using the rules in Workflow 1.
```

---

## Workflow 3: Optimize an existing draft

1. **On-page check.** Run the on-page list from Workflow 1 against the draft, plus the citation check: flag any link on a publisher's name rather than the claim, any missing date, and any footnote or bibliography left over from another format. Also flag thin sections. Report each item as ✅ pass, ⚠️ fix needed, or ❌ missing, with the fix next to it.
2. **Edit passes**, below, in order. Deliver the revised post with a short list of what changed.

---

## Workflow 4: Outrank a competitor

Read `${CLAUDE_PLUGIN_ROOT}/skills/blog/references/competitor-research.md` in full before starting.

1. **Analyze the competitor page**, following the reference's steps. Use web search for the results and pages, or Insights' connected tools if the plugin is installed and wired.
2. **Choose a differentiated angle.** Don't write the same post longer. The reference lists six strategies; pick the one that fits the gap.
3. **Deliver the brief first** (Workflow 2), with the competitor block filled in.
4. **Write the post** once the brief is approved, following Workflow 1.

---

## Present

Deliver ready-to-publish copy: a title in sentence case, the full body with headers, a meta description, and the slug. If the user wants a file, ask where to save it and in what format (craft's Step 6).

### Edit passes

These are the same passes, in the same order, as craft's Step 5. Structure first, sentences last.

1. **Schwartz re-angle**, when the substance is right and the opening isn't. Rewrite the headline, lead, and structure to the reader's position. If only the headline needs work, use `headline-lab` instead.
2. **Ogilvy review**, on request. Run the diagnostic questions against the finished post. This is an edit of the post, not a second draft.
3. **search-weave**, for every published post. It works the keywords, questions, and citations into the structure.
4. **red-pen**, for anything going to publish, always last. It handles the line-level copyedit and readability against the reader's band.
5. **Final sweep**, whenever any of the passes above ran: no-slops's mechanical sweep on the final text.

Skip any pass the post doesn't need, but never change the order of the ones that run.

### Data

Keywords, questions, and citations come from the brief by default. If Insights is installed and wired, its `seo-geo` skill can supply Search Console queries and its tool map, and `aeo-insights` can supply the AI-answer baseline. Both stay dormant otherwise. Never invent metrics.

---

## Names

Give the full name on first mention in the post, then the short form. Repeat the full name in any passage that might be quoted alone: a pull quote, a standalone FAQ answer, a definition. Rule and reasons: tone-and-guidelines, Product and brand names.
