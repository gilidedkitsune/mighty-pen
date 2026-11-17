---
name: search-weave
description: >
  The SEO and AEO structural pass for a finished draft. Give it the target keywords, the
  questions the piece should answer, and the sources or citations to work in, and it weaves them
  into the copy where they fit: question-shaped headers, answer-first sections, a definitional
  block, attributed receipts, liftable tables and steps, an FAQ, and dated facts, so search
  engines rank the piece and AI answer engines (ChatGPT, Perplexity, AI Overviews, Gemini,
  Claude) can lift and credit it. Never keyword-stuffs; voice and accuracy win every
  disagreement. Runs by default on every blog post and web page bound for publication, after the
  no-slops gate and before red-pen. Trigger on "SEO pass", "AEO pass", "GEO pass", "work in
  these keywords", "optimize for AI citations", "make this citable", "is this AEO-ready", or
  "search-weave". Needs no data connection; uses the Insights plugin's data when it's installed
  and wired.
---

# Search Weave

Other skills make the prose good. This one makes it **findable and citable**: ranked by search, extractable in standalone passages, and safe for an engine to quote with your name on it. It works on a finished draft, with inputs you supply. It doesn't research keywords and doesn't measure anything; it structures.

**The rulebook** is `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/SEO-GEO-drafting.md`: the shared spine, the three tensions, and the engine notes (its FAST-MOVING section is the single source for engine behavior; read it there, don't restate it here). The draft should already have passed the no-slops gate: structuring slop makes citable slop.

## Step 1: Collect the inputs

One AskUserQuestion round, asking only for what the brief and the draft don't already show:

| Input | What to ask for | If they don't have it |
|---|---|---|
| **Primary keyword or term** | The one phrase this piece should own | Propose one from the draft's promise and the reader's likely words, and confirm |
| **Secondary keywords** | 3 to 8 related phrases, in the reader's words | Skip; don't invent a list |
| **Questions to answer** | What the reader types into Google or asks an assistant | Draft 5 from the brief and the reader named in craft Step 1, and confirm |
| **Citations to work in** | Sources, stats, or pages that must be cited, plus internal pages to link | Use what's already in the draft; send any new stat need to cited-works |
| **Who already owns the answer** | Optional: competitors or sources that win this query today | Skip |

**If the Insights plugin is installed and wired,** offer to pull from it instead of asking: `seo-geo` for the Search Console queries the page or site already ranks for, and `aeo-insights` for the winnability verdict, the named-versus-cited baseline, and the sub-questions engines actually ran. If Insights isn't installed, or it reports it isn't connected, don't mention it again; work from the user's inputs.

Never invent search volumes, rankings, or citation numbers. A keyword list the user didn't give you and no tool returned is a guess, so label it as one.

## Step 2: Weave

Work through the draft in this order. The writing rules themselves live in the rulebook (SEO-GEO-drafting, "The shared spine"); each pass below says which rule it enforces and what weaving adds on top. Apply fixes in place unless the user asked for audit-only.

### 1. The term
Pick the phrasing the piece can actually win. A brand-new term nobody owns yet gets the bare question ("What is X?"). An established term, a competitor's brand, or a saturated head query can't be won head-on; scope it to the entity ("What is the message queue in [Product]?"). If aeo-insights returned a winnability verdict, follow it. Then place the term in the title, the first 100 words, and at least one H2, in natural language.

### 2. The question tree (spine §2)
Map the supplied questions and secondary keywords onto the headers. Where a keyword doesn't fit a header naturally, it goes in the body or nowhere. One non-question H2 for a closing section is fine.

### 3. Answer-first sections (spine §1, and tension 1)
Check every section against the screenshot test and the 40 to 60 word answer up top. Move brand energy below the answer where it's sitting on top.

### 4. The definitional block (spine §5)
For anything the piece defines, one sentence cluster carries four things together: the **term**, the **entity tied to its category** ("[Product], a [category]"), the **claim**, and the **date** ("as of [Month Year]"). Engines lift definitions whole; one missing its entity gets lifted without credit, and one missing its date rots silently.

### 5. Receipts (spine §3)
Work the supplied citations into the claims they support, and check every existing claim has one, in the two-part format from tone-and-guidelines (long-form keeps Chicago). Any claim without a verified origin goes to cited-works (job 5) rather than shipping. Named customers need consent on record. Two of the site's own pages contradicting each other on a number is a Red.

### 6. Liftable formats (spine §7)
Turn comparisons into tables, processes into numbered steps, and fragment bullets into standalone ones, wherever the content already has that shape.

### 7. The FAQ (spine §7)
Five to eight questions at the end, taken from the supplied questions that didn't become headers, plus adjacent questions, edge cases, and objections. No repeats of the body's H2s, and no duplicates of a sibling page's FAQ. Note that it's ready for FAQPage schema.

### 8. Freshness and trust (spine §8)
Dates in sentences, current numbers, a named author, at least one real example, links to the docs and to related pages on the same site (and a note to add a link back from those pages when they're next edited).

### 9. The glaze (when a claim can't be confirmed in time)
If a factual claim can't be verified before publishing (a feature awaiting confirmation, a number pending review), don't guess and don't cut the section. Rewrite it to phrasing that's true in every possible outcome, and bank the stronger version as a clearly marked note at the end of the draft, so the post-confirmation edit is a paste, not a rewrite.

## The weaving rules
- **Natural or nowhere.** A keyword goes where a person would use the phrase. If it reads forced, leave it out and say so; a stuffed page loses both the reader and the ranking.
- **Voice wins.** When structure and the voice guide disagree, the voice guide wins. When either disagrees with accuracy, accuracy wins.
- **Protect what's load-bearing:** honest "what's hard about this" sections, deliberate refrains, verbatim quotes. They're citation magnets and trust builders; sanding them off makes the piece worse.
- **Readability still gates.** The piece stays inside the target reader's Flesch band. red-pen checks it next.

## Output
1. **Inputs used:** the term, keywords, questions, and citations, and where each came from (the user, the draft, cited-works, or Insights). If Insights supplied a baseline, state it with its window.
2. **Numbered findings** in red-pen's format (🔴 Red 1 / 🟡 Yellow 2 / 🔵 Blue 3, stable numbers), tagged by pass: Term, Tree, Answer-first, Definition, Receipts, Liftable, FAQ, Freshness, Glaze. Red: it can't rank or be cited, or it makes an unsafe claim. Yellow: a lever left unpulled. Blue: polish.
3. **Where each keyword landed**, and any you left out because it didn't fit.
4. **The checklist:** each pass as pass, warn, or fail, with one line of detail.
5. **What was protected.**
6. If Insights' aeo-insights is wired, offer to set the baseline now and re-measure after the engines re-crawl.
