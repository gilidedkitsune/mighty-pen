---
name: tone-and-guidelines
description: >
  The voice and house style for written content, in three registers: personal (essays and
  personal posts), professional (career pieces under the author's name), and B2B tech buyer
  (product, sales, and technical-marketing content). The register is picked by content type.
  Covers the voice rules, citation format, numbers, dates, dashes, brand names, and the
  line-level writing rules. Applies to every writing workflow unless a specific person's profile
  is loaded from voice-profiles. It defines how to write, not what to write.
---

# Tone of voice and house style

The source for the default written voice and the house style. Every piece follows these rules before it ships, unless a person's profile from `voice-profiles` is loaded instead. The voice comes in three registers, chosen by content type. The house style and the writing rules apply to all three.

Read this file before producing written output.

This file governs how to write. Who the writing is for (the register, reading level, jargon tolerance) is a question to ask unless the brief already answers it. Name the specific reader and calibrate to them.

---

## Choosing a register

Choose the register from the content type before drafting. If a type falls between two rows, or the brief points somewhere the table doesn't cover, ask and give a recommendation.

| Register | Use it for |
|---|---|
| **Personal** | Personal essays, memoir, fiction, letters, personal social posts |
| **Professional** | Cover letters, resumes and bios, LinkedIn About sections and posts under the author's name, bylines and op-eds under the author's name, editor pitches, professional email |
| **B2B tech buyer** | Website, landing, and product copy for technical products; sales enablement (battle cards, objection handlers, one-sheets); executive briefs and one-pagers for buyers; whitepapers, ebooks, and reports; technical blog posts; customer stories for technical buyers; webinars; ads aimed at technical buyers |

A profile from `voice-profiles` replaces the register's personality for that person's pieces, but not its limits. A CTO's battle card still follows the B2B tech buyer rules on proof, tradeoffs, and hype.

---

## Register 1: Personal voice

Full strength. This is the register for pieces that belong to the author, where nothing is being sold.

The purpose of the writing is to hold the reader and make them want the next line, even in something as ordinary as a work email. What you say matters as much as how you say it.

### Core tenets

**Leave the grit in.** Keep the smell, the mess, and the crude line when they're true. If a sentence flinches from a real detail to stay polite, put the detail back.

**Aim the joke at yourself first.** When something is funny at someone's expense, the author goes first. Report your own mistakes and embarrassments plainly, like data, without an apology or a punchline announcing itself. If the target moves to someone else, it has to be someone who can take it, and the affection underneath has to be real. Never punch down.

**Keep the stakes under the jokes.** The humor sits beside what the author actually wants, believes, and cares about. A piece that is all bit and no stake isn't finished.

**Show the gesture, not the feeling.** Don't name the emotion. Show what it looked like: how someone reshelves a book says more than "he was thoughtful." This is the older sibling of the three-rules test (below): specific beats declared.

**Let metaphors argue.** Use a metaphor when it explains a structure or a feeling ("a first-timer's dinghy" for a first novel). Don't use one only for decoration. If you can cut it and lose nothing, cut it.

**Escalate with specifics, not adjectives.** Build a comic or dramatic moment from a run of concrete, itemized beats: a numbered ritual, an escalating list of bad dates. One adjective can't carry it.

### Sentence mechanics
- Long, clause-stacked sentences are fine, even welcome. Build toward the sharpest clause at the end, using semicolons, colons, and commas for the stacking (the dash ban is covered under Dashes).
- State exaggeration flatly. Let the content carry emphasis, not exclamation points.
- Vary the rhythm: put a short declarative between the long sentences.
- Let quoted speech stay rough and profane when the speaker would talk that way. Don't smooth out someone's real voice.

### Avoid
- Sanitizing real detail out of politeness
- Whimsy with no stake under it
- Naming an emotion instead of showing it
- Hedged, neutral reactions presented as balance

**Voice in five words:** Wry. Sensory. Self-deprecating. Ambitious. Generous.

---

## Register 2: Professional voice

The same voice, dressed for work. The reader is deciding something about the author: a hiring manager, an editor, a conference organizer, a client.

**What carries over:** concrete over stated, earnest underneath, metaphors that argue, escalation through specifics. Self-aimed humor survives in small doses: one light moment per piece, and never one that undercuts a claim the reader has to believe.

**What changes:**
- **Candor replaces grit.** No profanity, and no crude dialogue. The unsanitized instinct becomes plain naming of the real problem: the traffic gap, the team of one, the thing that broke first.
- **Proof comes before personality.** Lead with the result and its number, then the color. A hiring manager skims for evidence, so give them the evidence first and let the personality follow.
- **Medium-length sentences.** Keep the rhythm varied, but drop the long clause-stacked builds in favor of sentences a skimmer can take in at one pass.
- **Confident, not modest.** Say what the author did, in the first person and the active voice ("I grew the team from one writer to nine"). Never "was responsible for" or "helped to."

**Voice in five words:** Candid. Specific. Warm. Confident. Brief.

---

## Register 3: B2B tech buyer voice

For readers evaluating a technical product: CTOs, engineering VPs, platform and infrastructure leads, security reviewers, IT, technical product managers, developers running a trial, and the procurement person who signs. They're skeptical by trade, short on time, and they check what you say. Write so they never need to.

### Core tenets

**Answer first.** The reader is evaluating, not browsing. Open with what the product does, who it's for, and what changes for them. Context and story come after the answer, never in its place.

**Mechanism over adjective.** Say how it works. "It runs entirely in the browser, so nothing executes on a remote server" beats "fast and secure." Name integrations, protocols, versions, limits, and units. If a claim can't survive a technical reader asking "how, exactly?", rewrite it until it can.

**Receipts on every claim.** Benchmarks state their conditions. Customer claims name the customer (with consent) or say why they can't. Security claims name the certification (SOC 2 Type II, ISO 27001) or the control (SSO via SAML, audit logs, data residency), never "enterprise-grade" or "bank-level." Link the documentation, the security page, the methodology.

**Name the tradeoffs.** Say where the product doesn't fit, what it doesn't do yet, and what it costs. Technical buyers trust a vendor who tells them the limits, because they'll find the limits anyway, and they remember who said so first.

**Write for the whole committee.** A technical purchase has a champion, an economic buyer, and a reviewer whose job is to say no (security, legal, IT). Each section should answer at least one of their questions: does it work, what does it cost, what's the risk?

**Peer to peer.** Write like a senior practitioner explaining the product to another practitioner, not a vendor pitching a prospect. Plain verbs, no hype, second person. Humor is rare and dry, and never at the reader's expense.

### Sentence mechanics
- Shorter sentences than the personal register. One claim per sentence in any section full of proof.
- Numbers carry units and conditions: "p95 latency under 200 ms at 1,000 requests per second."
- Define any term the reader might not know, on first use (see Acronyms).
- Put comparisons in tables, introduced by one plain sentence saying what the table shows.
- Specific beats complete: three named integrations beat "integrates with your whole stack."

### Avoid
- Superlatives without a benchmark ("fastest," "most secure," "best-in-class")
- Category hype in place of a mechanism ("AI-powered," "next-gen," "enterprise-grade," "revolutionary")
- Hiding pricing, limits, or roadmap status. A beta or planned feature is never presented as shipped.
- Fear selling ("don't get left behind")
- Vague security language a security reviewer would reject
- Profanity, crude dialogue, and the personal register's long comic builds

**An illustrative before and after** (invented for teaching; never reuse as a real claim):

> Hype: "Our revolutionary AI-powered platform delivers blazing-fast deployments with enterprise-grade security."
>
> Buyer voice: "Deploys finish in about 90 seconds on a median 40-service repo (our benchmark, March 2026; methodology linked). SSO via SAML, audit logs, and SOC 2 Type II cover every plan. On-prem isn't supported yet."

**What carries over from the personal voice:** concrete over stated, earnest underneath (name the real problem plainly), and candor about yourself, which here means admitting the product's limits before a competitor does.

**Voice in five words:** Precise. Candid. Evidence-first. Peer-level. Unhyped.

---

## Editorial guidelines

### Active and passive voice
Active by default; passive only on purpose. The rule and its one exception are in no-slops §3 (Active voice).

### Serial comma
Use it everywhere.

### Headlines and subheads
Sentence case for all headlines, headers, and subheads. Heroes and some creative assets may use title case.

### Bibliography and attribution
**Cite the origin, not the middleman.** Quotes and statistics go back to their source. If a figure appears in a business magazine but came from an analyst report, check the report and cite the report, not the magazine. Prefer primary sources and first-party data.

**Citation format depends on the content type:**

- **Long-form** (ebook, whitepaper, guide, manual, report): superscript numbers in the text, tied to a **Works Cited** list at the end in **Chicago Manual of Style**. These are downloadable documents, so the academic format fits, and they're exempt from the inline rule below.
- **All web copy (blog and website):** the two-part inline citation below. No superscripts, footnotes, or works-cited blocks.

**The two-part inline citation.** Every sourced claim in web copy has both parts:

1. **Hyperlink the phrase that carries the figure**, not the publisher's name. The link text is the claim.
2. **Close the sentence with a plain-text "(Publisher Name, year)".** It's not linked; the link already sits on the claim.

> Software spend per employee [rose 27% in 2025](https://zylo.com/research/saas-management-index) (Zylo, 2026).

Both parts do work. The link text tells search and answer engines what the source says, which a bare publisher name never does. And when an AI engine lifts a passage, it usually strips links, so the plain parenthetical keeps the attribution with the claim. Link the claim, name the source in the parentheses.

**Per-channel notes:**
- **Blog:** cite freely. Sourced figures are the strongest lever for AI citation.
- **Website:** cite sparingly on conversion pages (hero, pricing, landing) and more freely on content pages. Label first-party data and link it. Exceptions, like a gated download page, are one-off decisions made per piece.

### Naming competitors or comparable work
Write comparisons with confidence, backed by receipts:
- Name them plainly. No coy "other tools in the space."
- Every comparative claim has a receipt: a benchmark, a price, a dated screenshot, a cited limitation.
- Criticize the product or the work, never the person. No punching down.
- Date competitive claims in the sentence ("as of June 2026"). Things change monthly, and a stale comparison hurts the writer more than the target.

### Spelling
US spelling by default. Copy for a UK or EMEA audience uses UK spelling.

### Numbers
- Spell out one through ten. Use numerals from 11 up.
- Numerals always go with units, symbols, and data: 3%, $5, 8 GB, 10M+ users.
- In data-forward writing, large round figures take numerals and an abbreviation (10M users, $8K). Narrative prose can spell them out when the rhythm calls for it.
- Don't begin a sentence with a numeral. Rewrite the sentence, or spell the number out.
- Ranges repeat the unit at both ends and use an en dash: $8K–$22K, 2–4 pm.

### Bulleted lists
- Introduce every bulleted list with a colon, not a semicolon.
- Phrase lists: lowercase, no period at the end of each item.
- Sentence lists: sentence case and full punctuation.

If every bullet starts with the same words, rewrite the lead-in to remove the repetition.

### Dates and times
For designed collateral, use the format for the audience's region.

**US:** Thursday, Dec 19 | Thursday, Dec 19, 2019 | Dec 19, 2019
**Non-US:** Thursday 19 Dec | Thursday 19 Dec 2019 | 19 Dec 2019
**12-hour clock:** 2:00 pm EST | 1:00 am
**24-hour clock:** 14:00 GMT

### Percentages
Use a numeral and the % sign everywhere, including pull quotes and headers ("cut onboarding time by 40%"). If a percentage would open a sentence, restructure the sentence.

### Acronyms
Spell out the term and put the abbreviation in parentheses at first use in the body. Headlines and primary headers may use the acronym; spell it out early in the body. Very familiar acronyms (like DVD) can stand alone when spelling them out would confuse.

### Product and brand names
Use the full name on first mention on the page, including a headline or hero mention, then the short form everywhere after, unless the brief sets a different convention. Never use the short form before the full name has appeared. Repeat the full name in any passage that may be lifted alone: a pull quote, a standalone FAQ answer, a definition.

### Dashes
No em dashes (the long dash character). They read as an AI tell, and no-slops enforces the ban. Use a comma, colon, semicolon, parentheses, or two sentences.

En dashes (–) are for ranges only: Jun 15–18, 2–4 pm, $8K–$22K. Never as a replacement for an em dash.

### Currency
Use the right symbol or currency code for every amount.

### Inclusive language
Write for the whole audience without making a show of it:
- Plain language is the inclusive default. Jargon shuts out more readers than anything else.
- Use "they" for an unspecified person, and name roles rather than genders.
- Choose plain metaphors: "coherence check" over "sanity check," "gap" over "blind spot," "allowlist and blocklist" over "whitelist and blacklist," "primary and replica" over "master and slave," "legacy" over "grandfathered."
- Write "team," "folks," or "everyone" in place of "guys."
- Describe people the way they describe themselves. When unsure, ask or leave it out.

---

## Writing rules

These line-level rules apply to every piece. Full drafting craft (leads, sentence construction, rhythm, endings, the cut) is in craft's `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/prose-craft.md`. The no-slops filter checks the result.

### The three-rules test
Run every line that carries weight (headlines, claims, openers, calls to action) through three questions:
1. **Can you picture it?** "Streamline your workflow" shows nothing. "Cut your Monday report from four hours to 15 minutes" shows a clock.
2. **Can it be shown true or false?** "Industry-leading" can't be checked. "Used by 12 of the top 20 Shopify stores" can.
3. **Could anyone else have written it?** "We help businesses grow" fits any logo. "1,000 songs in your pocket" belongs to one product.

Three yeses: keep it. Two: sharpen it. One or none: rewrite it. Specificity is what passes this test, and specificity is what readers believe. Worked examples are in `${CLAUDE_PLUGIN_ROOT}/skills/no-slops/references/slop-vs-gold.md`.

### Cut what doesn't serve the piece
If a line or idea weakens the piece's coherence, cut it, even if you like it. Everything in a piece should work together.

### Reread for shape
Before delivering, ask: is anything repetitive? Are there mixed metaphors or decorative language? Is the length right for this content type? If any answer is yes, cut and revise.

### Business or company, not organization
Use "business" or "company" by default. Use "enterprise" as a descriptor, or "organization," when writing about large, global entities.

### Adjectives and adverbs
Adverbs are cut outright (no-slops §3, No adverbs). Use adjectives sparingly, and delete any that repeat what the noun already says. If one is propping up a weak noun, find a stronger noun.

Weak: "The massive sea beast aggressively broke the boat."
Stronger: "The leviathan destroyed the schooner."

### Compound modifiers
Hyphenate two words that act as one descriptor before a noun ("a high-quality report"). Don't hyphenate after the noun ("the report is high quality"), and don't hyphenate adverbs ending in -ly.

### Emphasis devices
Exclamation points, italics, and scare quotes shouldn't do the work of the language. Let the wording carry the emphasis.

### "That"
- Cut it when the sentence works without it.
- "Who" for people, "that" or "which" for things.
- "That" introduces essential clauses; "which" introduces extra detail that can be removed.

### Commonly confused words
- **Then / than:** "then" is sequence; "than" is comparison.
- **Affect / effect:** "affect" is a verb (to influence); "effect" is a noun (the result).
- **Between / among:** "between" for two things; "among" for more than two.
- **Lose / loose:** "lose" is the verb; "loose" is the adjective (not tight).

### Homonym check
Before delivering, check the frequent offenders: accept or except, compliment or complement, to, too, or two, you're or your, their, they're, or there.

---

## No-slops

Every draft goes through the no-slops filter before it ships. That skill (`${CLAUDE_PLUGIN_ROOT}/skills/no-slops/SKILL.md`) is the single source for the AI-tell rules: dead language, structural tells, the voice rules (active voice, no adverbs, no em dashes, no copula inflation, contractions, specificity over declaration), second-generation tells, texture, rhythm, and the 35/50 score. Worked examples of specificity beating slop are in `${CLAUDE_PLUGIN_ROOT}/skills/no-slops/references/slop-vs-gold.md`.
