---
name: tone-and-guidelines
description: >
  Taylor's tone of voice, style guide, and quality standards, in three registers: personal
  voice, professional voice (career pieces under Taylor's name), and the B2B tech buyer voice
  (product, sales, and technical-marketing content). The register is picked by content type.
  Use alongside any writing workflow unless a specific person's profile is loaded from
  voice-profiles; it defines HOW to write, not WHAT to write.
---

# Tone of Voice & Style Guide

This is the single source of truth for the default written voice. Every piece of content passes through these guidelines before it ships, unless a specific person's profile from `voice-profiles` is loaded instead. The voice comes in three registers, picked by content type (below); the Editorial Guidelines and Writing Tips apply to all three.

Read this entire file before producing any written output.

This guide governs HOW to write. WHO you're writing for (register, reading level, jargon tolerance): ask directly if the brief doesn't already say. There's no persona library here; name the specific reader and calibrate to them.

---

## Choosing a register

Pick the register from the content type before drafting. If the type sits between two rows, or the brief points somewhere the table doesn't, ask, with your recommendation.

| Register | Use it for |
|---|---|
| **Personal** | Personal essays, memoir, fiction, letters, personal social posts |
| **Professional** | Cover letters, resumes and bios, LinkedIn About sections and posts under Taylor's name, bylines and op-eds under Taylor's name, pitches to editors, professional email |
| **B2B tech buyer** | Website, landing, and product copy for technical products; sales enablement (battle cards, objection handlers, one-sheets); executive briefs and 1-pagers written for buyers; whitepapers, ebooks, and reports; technical blog posts; customer stories aimed at technical buyers; webinars; ads to technical buyers |

A profile from `voice-profiles` replaces the register's personality for that person's pieces, but not the register's limits: a CTO's battle card still follows the B2B tech buyer rules on proof, tradeoffs, and hype.

---

## Register 1: Personal voice

Full strength. This is how Taylor writes when the piece is hers and nobody is buying anything.

The point of the written word is to engage the reader, to spark their curiosity and get them to ask "what happens next," even in something as plain as a work email.

What you say is as important as how you say it.

### Core tenets

**Unsanitized.**
Put the grit next to the beauty and don't clean either one up for the other. Name the smell, the mess, the vulgar line. If a sentence flinches away from a real detail to stay polite, put the detail back in.

**Self-aimed first, and fair game.**
When something's funny at someone's expense, aim it at yourself before anyone else. Report your own bad calls and embarrassments flat, like data, not with an apology or a punchline announcing itself. When the target shifts to someone else, it's someone who can take it, delivered with real affection underneath, never at someone vulnerable.

**Earnest underneath.**
The jokes never replace the stakes. Say what you actually want, actually believe, actually care about, then let the humor sit next to it, not instead of it. A piece that's all bit and no stake is unfinished.

**Concrete over stated.**
Don't name the feeling; show the gesture that carries it. The way someone reshelves a book tells the reader more than "he was thoughtful" ever could. This is the three-rules test's older sibling: specifics over declarations, always.

**Metaphor that argues.**
Reach for a metaphor when it does real work explaining a structure or a feeling ("a first-timer's dinghy" for a first novel), not to decorate a sentence. If you can cut it and lose nothing, cut it.

**Escalate in specifics, not adjectives.**
Build a comic or dramatic moment through a sequence of concrete, itemized beats (a numbered ritual, an escalating list of bad exes), not one adjective doing all the work.

### Sentence mechanics
- Long, clause-stacked sentences are fine, even good: build with dashes, semicolons, and commas toward the sharpest clause at the end. (See Dashes, below, for where this runs into the em-dash rule: use semicolons, colons, and commas to get the same stacking effect.)
- State hyperbole flat. No exclamation points doing the emphasis for you.
- Vary rhythm: drop a short, declarative sentence between the long ones.
- Let dialogue and quoted voices stay unpolished and profane when the person would actually talk that way. Don't sand someone's real voice smooth.

### What to avoid
- Sanitizing real detail out of politeness
- Whimsy with no real stake underneath it
- Naming an emotion instead of showing what it looked like
- Hedged, neutral reactions dressed up as balance

**Voice in 5 words:** Wry. Sensory. Self-deprecating. Ambitious. Generous.

---

## Register 2: Professional voice

Taylor's voice, wearing work clothes. Same person, same instincts, dialed for a reader who is deciding something about her: a hiring manager, an editor, a conference organizer, a client.

**What carries over:** concrete over stated, earnest underneath, metaphor that argues, escalation in specifics. Self-aimed humor survives in small doses: one light beat per piece is plenty, and it should never undercut a claim she needs the reader to believe.

**What changes:**
- **Grit becomes candor.** No vulgarity and no profane dialogue. The unsanitized instinct shows up as naming the real problem plainly: the traffic deficit, the team of one, the thing that failed first.
- **Proof before personality.** Lead with the result and its number, then the color. A hiring manager skims for evidence; give them the evidence, then make them like the person behind it.
- **Mid-length sentences.** Keep the rhythm varied, but trade the long clause-stacked builds for sentences a skimmer can take in one pass.
- **Confident, not modest.** State what she did in the first person and active voice ("I grew the team from one writer to nine"), never "was responsible for" or "helped to."

**Voice in 5 words:** Candid. Specific. Warm. Confident. Brief.

---

## Register 3: B2B tech buyer voice

For readers evaluating a technical product: CTOs, VPs of engineering, platform and infrastructure leads, security reviewers, IT, technical PMs, developers running a trial, and the procurement person who has to sign. They are skeptical by profession, short on time, and they will check what you say. Write so they never have to.

### Core tenets

**Answer first.**
The reader is evaluating, not browsing. Open with what it does, who it's for, and what changes for them. Context and story come after the answer, never instead of it.

**Precise over impressive.**
Name the mechanism, not the adjective. "Runs entirely in the browser, so nothing executes on a remote server" beats "blazing fast and secure." Name integrations, protocols, versions, limits, and units. If a claim can't survive a technical reader asking "how, exactly?", rewrite it until it can.

**Receipts on every claim.**
Benchmarks state their conditions. Customer claims name the customer (with consent) or say why they can't. Security claims name the certification (SOC 2 Type II, ISO 27001) or the control (SSO via SAML, audit logs, data residency), never "enterprise-grade" or "bank-level." Link the docs, the security page, the methodology.

**Name the tradeoffs.**
Say where it doesn't fit, what it doesn't do yet, and what it costs. Technical buyers trust a vendor that tells them the limits, because they'll find the limits anyway, and they remember who told them first.

**Write for the whole committee.**
A technical purchase has a champion, an economic buyer, and a reviewer whose job is to say no (security, legal, IT). Each section should answer at least one of their three questions: does it work, what does it cost, what's the risk.

**Peer to peer.**
Write like a senior practitioner explaining the product to another one, not a vendor pitching a prospect. Plain verbs, no hype, second person ("you," "your team"). Humor is rare and dry, and never at the reader's expense.

### Sentence mechanics
- Shorter sentences than the personal register; one claim per sentence in any proof-heavy section.
- Numbers carry units and conditions ("p95 latency under 200 ms at 1,000 requests per second").
- Jargon the reader uses is fine; jargon they might not, define on first use (see Acronyms).
- Comparisons go in tables, preceded by one plain sentence saying what the table shows.
- Specific beats complete: three concrete integrations named beat "integrates with your entire stack."

### What to avoid
- Superlatives without a benchmark ("fastest," "most secure," "best-in-class")
- Category hype standing in for a mechanism ("AI-powered," "next-gen," "enterprise-grade," "revolutionary")
- Hiding pricing, limits, or roadmap status; never present a beta or planned feature as shipped
- Fear-selling ("don't get left behind")
- Vague security language that a security reviewer would bounce
- Vulgarity, profane dialogue, and the personal register's long comic builds

**Before and after** (illustrative, invented for teaching; never reuse as a real claim):

> Hype: "Our revolutionary AI-powered platform delivers blazing-fast deployments with enterprise-grade security."
>
> Buyer voice: "Deploys finish in about 90 seconds on a median 40-service repo (our benchmark, March 2026; methodology linked). SSO via SAML, audit logs, and SOC 2 Type II cover every plan. On-prem isn't supported yet."

**What carries over from Taylor's voice:** concrete over stated, earnest underneath (say the real problem plainly), and self-aimed candor, which here means admitting the product's limits before a competitor does.

**Voice in 5 words:** Precise. Candid. Evidence-first. Peer-level. Unhyped.


---


## Editorial Guidelines

### Active vs. passive voice
Active by default; passive only on purpose. The rule and its one exception live in no-slops §3 (Active voice).

### Oxford comma
Use the Oxford comma in all content, all the time.

### Headlines and subheads
All headlines, headers, and subheads use sentence casing. Exception: heroes and certain creative assets may use headline casing.

### Bibliography and attribution
**Always cite the origin, not the middleman.** Direct quotes and statistics are attributed to their original source. If you found a statistic in Forbes from a Forrester report, confirm it at the source and cite the Forrester report, not the Forbes article. Prefer primary sources and first-party data.

**Citation format depends on the content type:**

- **Long-form** (ebook, whitepaper, guide, manual, report): superscript in-text numbers tied to a **Works Cited appendix** at the end, formatted in **Chicago Manual of Style**. These are downloadable assets, so the academic treatment fits, and they are exempt from the inline-attribution rule below.
- **All web copy (blog and website):** the two-part inline citation below. Never superscripts, footnotes, or a works-cited block.

**The two-part inline citation.** Every sourced claim in web copy carries both halves:

1. **Hyperlink the phrase that carries the statistic**, not the publisher's name. The anchor text is the claim itself.
2. **Close the sentence with a plain-text parenthetical: (Publisher Name, date).** It is not hyperlinked; the link is already on the phrase.

> Software spend per employee [rose 27% in 2025](https://zylo.com/research/saas-management-index) (Zylo, 2026).

Both halves earn their place. The anchor text tells search and answer engines what the linked source actually says, which a bare publisher name never does. And when an AI engine lifts a passage it usually strips the markup, so the plain parenthetical is what keeps the attribution attached to the claim. Link on the phrase, name in the parens.

**Per-channel notes:**

- **Blog:** cite freely. Sourced statistics are the strongest AI-citation lever.
- **Website:** cite sparingly on conversion pages (hero, pricing, landing) and more freely on content-style pages. Label and link first-party data. Rare page-level exceptions (e.g., a gated-asset download page) are deliberate one-offs, decided per piece.

### Naming competitors or comparable work
Write comparison content like you're confident, because the receipts back it up:
- Name names plainly. No coy "other tools in the space."
- Every comparative claim carries a receipt: a benchmark, a price, a dated screenshot, a cited limitation.
- Critique the product or the work, never the person. No punching down, no dunking.
- Date competitive claims in the sentence ("as of June 2026"): things change monthly, and a stale swipe damages the writer, not the target.

### US vs. UK spelling
Use US spelling as the default for all content. Exception: copy written for a UK/EMEA audience uses UK spelling.

### Numbers
- Spell out one through ten.
- Use numerals for 11 and up.
- Always use numerals with units, symbols, and data: 3%, $5, 8 GB, 10M+ users.
- Large round figures take numerals + abbreviation in data-forward contexts (10M users, $8K); narrative prose may spell them out (ten million) when the rhythm wants it.
- Don't open a sentence with a numeral: restructure, or spell it out if you can't.
- Ranges repeat the unit on both ends with an en dash: $8K–$22K, 2–4 pm.

### Bulleted lists
- Always introduce bulleted lists with a colon (not a semicolon).
- Phrase-based lists: all lowercase, no period at the end of each bullet.
- Sentence-based lists: sentence casing and proper punctuation.

If you're repeating the same phrase in each bullet, rewrite the intro snippet to eliminate the repetition.

### Date and time
For designed collateral, use date and time formats appropriate to the target region.

**US:** Thursday, Dec 19 | Thursday, Dec 19, 2019 | Dec 19, 2019
**Non-US:** Thursday 19 Dec | Thursday 19 Dec 2019 | 19 Dec 2019
**12-hour clock:** 2:00 pm EST | 1:00 am
**24-hour clock:** 14:00 GMT

### Percent or %
Use numerals with the % symbol for all percentages, everywhere: body text, pull quotes, headers ("cut onboarding time by 40%"). Specific figures are what readers believe. If a percentage would open a sentence, restructure the sentence.

### Acronyms and initialisms
Spell out the full name or process followed by the abbreviation in parentheses the first time it appears in text.

Exceptions:
- You can use acronyms in headlines and primary headers. Spell them out early in the body.
- Well-established acronyms (like DVD) don't need to be spelled out if doing so would confuse the reader.

### Product and brand names
Use the subject's full name on first mention on the page (including when that first mention is a headline or hero), then its short form everywhere after, unless the brief sets a different convention. Never use the short form before the full name has appeared. Give the full name again to any passage that may be lifted on its own: a pull quote, a standalone FAQ answer, a definitional block.

### Dashes
Don't use em dashes (—). They read as an AI tell, and they're cut here. Use a comma, colon, semicolon, parentheses, or two sentences instead. (Enforced in the no-slops filter.)

En dashes (–) are allowed in ranges only: Jun 15–18, 2–4 pm, $8K–$22K. Never as a stand-in for an em dash.

### Currency symbols
Use the appropriate symbols or currency code for all currencies.

### Inclusive language
Write for the whole audience without announcing that you're doing it:
- Plain language is the inclusive default: jargon excludes more readers than any other choice.
- Use "they" for an unspecified person; name roles, not genders ("the developer... they").
- Swap loaded metaphors for plain ones: "gut check" or "coherence check" over "sanity check," "gap" over "blind spot," "allowlist/blocklist" over "whitelist/blacklist," "primary/replica" over "master/slave," "legacy" over "grandfathered."
- "Team," "folks," or "everyone" over "guys" in copy.
- Describe people the way they describe themselves; when in doubt, ask or omit.


---


## Writing Tips

These are the line-level rules every piece follows. The full drafting craft (leads, sentence engineering, rhythm, kickers, the 10% cut) lives in craft's `${CLAUDE_PLUGIN_ROOT}/skills/craft/references/prose-craft.md`: writers work those passes at draft time, then these rules and the no-slops filter gate what ships.

### The three-rules test
Run every line that carries weight (headlines, claims, openers, CTAs) through three questions:
1. **Can I picture it?** "Streamline your workflow" shows nothing. "Cut your Monday report from four hours to 15 minutes" shows a clock.
2. **Can I prove it true or false?** "Industry-leading" is unfalsifiable. "Used by 12 of the top 20 Shopify stores" is checkable.
3. **Could anyone else write the same sentence?** "We help businesses grow" fits any logo. "1,000 songs in your pocket" belongs to one product.
Three yeses, keep it. Two, sharpen it. One or none, rewrite it. Specificity is what passes this test, and specificity is what readers believe. For worked examples, see `${CLAUDE_PLUGIN_ROOT}/skills/no-slops/references/slop-vs-gold.md`.

### Murder your darlings
Make sure everything in a content piece works together. Don't keep an analogy or explanation just because you like how it sounds. If a phrase or concept weakens the cohesion of the piece: kill it.

### Keep it tidy
Deliver your thesis in a tidy package. Reread every draft and ask:
- Is any of this repetitive?
- Are there any mixed metaphors or flowery language?
- Is this an appropriate length for the content type?

If the answer is "yes" to any of these: cut and revise.

### Word usage: business/company vs. organization
Use "business" or "company" most of the time. Exception: when using "enterprise" as a descriptor or writing about large, global entities where "organization" makes more sense.

### Adjectives (adverbs: see no-slops)
Adverbs are cut outright; that rule lives in no-slops §3 (No adverbs). Adjectives are allowed, sparingly. If one is redundant, delete it. If it's propping up a weak noun, find a stronger noun.

Bad: "The massive sea beast aggressively broke the boat."
Better: "The leviathan destroyed the schooner."

Cut the chaff. Use direct, accurate language.

### Compound modifiers
Compound modifiers: two words that function as one descriptor, connected by a hyphen. Without the hyphen, the meaning could be interpreted separately.

- Don't hyphenate adverbs ending in -ly.
- Use a hyphen only when the two words precede a noun. After the noun, no hyphen needed.

### Exclamation points, italics, and "emphasis quotes"
Don't lean on these to spice up your piece. Rely on the strength of your language to add texture and interest.

### That
- **Overuse:** Is every instance of "that" required? Cut it when you don't need it.
- **Who vs. that:** Use "who" when talking about a person or people, not "that."
- **That vs. which:** Use "that" in defining clauses (essential info). Use "which" in non-defining clauses (extra detail that can be removed).

### Common writing errors
- **Then/than:** "Then" shows order of events. "Than" makes comparisons.
- **Affect/effect:** "Affect" is a verb (causes change). "Effect" is a noun (result of change).
- **Between/among:** "Between" for two things. "Among" for more than two.
- **Loose/lose:** "Lose" is a verb (fail, misplace). "Loose" is an adjective (not attached, too large).

### Homonym check
Read through your copy to make sure you've got the correct version of all homographs and homophones. Frequent offenders: accept/except, compliment/complement, to/too/two, you're/your, their/they're/there.


---


## No-slops: AI writing quality filter

Every draft passes through the no-slops filter before it ships. That filter lives in one place now: the **`no-slops`** skill (`${CLAUDE_PLUGIN_ROOT}/skills/no-slops/SKILL.md`). It is the single source of truth for killing dead language, fixing AI structural patterns, the voice rules (active voice, no adverbs, no em dashes, no copula inflation, contractions, specificity over declaration), the second-generation tells, the build-texture rules, the rhythm checks, and the 35/50 scoring rubric. Run it on every piece.

Worked examples of specific-beats-slop live in `${CLAUDE_PLUGIN_ROOT}/skills/no-slops/references/slop-vs-gold.md`.
