---
name: no-slops
description: >
  The AI-tell filter. Reads a draft for the patterns that make writing sound machine-made
  (stock phrases, tiered vocabulary, structural reflexes, flat rhythm, missing texture), fixes
  them in place, and scores the result out of 50 with 35 as the bar. Use after drafting
  anything, and as a drafting constraint before. Trigger on "no-slops", "noslops", "slop
  check", "stop slop", "AI tells", "does this sound like AI", "de-AI this", "clean up the copy",
  or "audit this draft". Runs on any prose: posts, emails, pages, essays, scripts.
---

# No-slops

A single filter for everything that makes copy read as generated. It is also a rulebook: craft and blog hand it to the writer before the first sentence (prose-craft pass 0), so by the time the audit runs it should come back nearly empty.

How to run it: one read, every section at once, fixing as you go. Don't produce a list of problems for later; produce the repaired text.

## 0. Fingerprint check (mechanical, first)

Some artifacts are proof on their own that a machine touched the text and nobody read it after. Sweep for these before reading for meaning. They need no judgment, only search:

| Artifact | What it looks like |
|---|---|
| Template residue | Square-bracket blanks, "[Client name]", "TBD-link", dates like 2026-MM-DD |
| Citation debris | Tool tokens such as `oaicite`, `contentReference`, `turn0search`, `grok_card`, or a stray `attached_file` |
| Tracking tails | `utm_source=chatgpt.com` or another assistant's name in a link |
| Model disclaimers | "As of my training data...", "I can't browse the web..." |
| Assistant manners | "Hope that's useful!", "Happy to adjust!", "Great question", "Absolutely!" |
| Leaked reasoning | "Let me work through this", "First, I'll outline", "Okay, so the user wants" |
| Invisible characters | Zero-width spaces, lookalike letters from other alphabets, odd unicode from a paste. Strip them as hygiene; never add unicode to dodge a detector. |

One of these in published copy costs more credibility than every other finding combined.

**The mechanical sweep.** When another skill asks for "no-slops's mechanical sweep" (on short copy, or after any rewrite), it means this list, run by search and not by eye: the §0 artifacts, Tier 1 vocabulary (`${CLAUDE_PLUGIN_ROOT}/skills/no-slops/references/banned.md`), the kill-on-sight phrases in that same file, em dashes, and adverbs. No score; scoring is §7.

## 1. Kill dead language

`${CLAUDE_PLUGIN_ROOT}/skills/no-slops/references/banned.md` holds the catalog. Two different rules apply:

- **Phrases** are never acceptable. Stalling openers, borrowed authority ("research suggests"), assistant manners, recap endings, crystal-ball closers, everyone-and-their-dog breadth: delete or replace every one.
- **Words** are tiered by how much it takes to make them a problem. Tier 1 is a finding the first time it appears. Tier 2 is fine alone and a finding when two land in one paragraph. Tier 3 only counts in bulk, three or more in roughly 300 words.

The test for any phrase you aren't sure about: could it sit in an article on any subject without changing a word? Then it's carrying nothing. Cut it.

## 2. Fix the structure

Models reach for a handful of sentence shapes so often that the shapes themselves become the tell. Individually each looks fine; in aggregate they read as a template. The full catalog, with repairs, is `${CLAUDE_PLUGIN_ROOT}/skills/no-slops/references/structures.md`. The six that matter most:

### Binary contrasts / negation-reframes
Setting up a wrong idea just to knock it down: "It's not a tool, it's a teammate." "Forget speed. Think trust." Say the second half and skip the straw man.

### Dramatic fragmentation
Single nouns as drumbeats: "Fast. Private. Yours." "One click. Done." Write the sentence the fragments were avoiding.

### Rhetorical setups
Lines that promise a reveal instead of making the point: "Here's the twist." "Picture this:" "Once you notice it, it's everywhere." Make the point; the reader will notice on their own.

### False agency
Objects doing what people do: "The data tells a story." "The roadmap decided." "Churn is asking us something." Find who actually acted and name them, or address the reader as "you."

### Narrator-from-a-distance
Commentary from above the scene: "Teams often find..." "There's a reason this keeps happening." Put the reader inside it with a specific person, place, or moment.

### Overly smooth connectors
Openers that fake continuity: "That same energy carries into...", "This is where it gets personal." If the paragraph follows, it needs no bridge; if it needs one, use a word you'd say out loud.

The catalog also covers, at the same severity: rebuttals to objections nobody raised, relationships asserted without being named ("tied to"), runs of identical sentence openings, a first sentence that repeats its heading, trailing "-ing" commentary (", underscoring the need for..."), ranges with no real scale ("from solo founders to global enterprises"), rotating synonyms for one thing, stock conclusions, inflated significance, formatting reflexes (wall-of-bold bullets, decorative emoji, arrow chains, colon stacks), documents that narrate their own edits, abrupt register changes, and question-shaped headers (a tell in ordinary prose; the point of the exercise in search-weave).

## 3. Enforce voice rules

### Active voice
Sentences should have someone doing something. "The pricing page was rewritten" hides who did it; "Priya rewrote the pricing page" doesn't. Passive is a choice you can make on purpose, when the thing acted on matters more than who acted ("Every account was migrated by Friday"), but it is never the default.

### No adverbs
Cut them, -ly words and the unmarked ones too: softeners (just, really, simply), boosters (truly, deeply, incredibly), and fake candor (honestly, frankly, actually). When an adverb is holding a verb up, the verb is wrong: "walked slowly" is "trudged"; "very important" is either a better word or a reason.

### No em dashes
None in final copy. Rebuild the sentence with a comma, a period, a colon, a semicolon, or parentheses, whichever fits its rhythm. (House style, including en dashes in ranges, is in tone-and-guidelines under Dashes.)

### Copula inflation
"Is" is a fine verb. "Serves as," "stands as," "functions as," "represents," "boasts" are usually "is" or "has" in costume. "The dashboard serves as the team's source of truth" is "the dashboard is the team's source of truth."

### Contractions
Use them where a person would: don't, it's, we'll. Stiffness isn't rigor.

### Specificity over declaration
A sentence that announces weight without carrying any ("The impact was substantial." "There are deeper forces at work.") gets replaced by the impact or the force. If you can't name it, you haven't earned the sentence. Sweeping quantifiers (always, never, everyone, no one) get the same treatment: swap in the real scope.

### Uncertainty
Real doubt is allowed and should be plain ("probably," "I'm not sure yet," "my guess"). Doubt sprinkled over things you know is not humility; it's noise. State the known things flatly.

## 4. Check the rhythm

### Sentence length
The rule itself lives in craft's prose-craft §5. What to catch here: a pair of short sentences can land; three short ones in a row start to sound like a drum solo.

### Lists
Models love threes. Default to two items, or to however many actually exist. One deliberate triplet per piece is fine; a habit of them is a tell.

### Punctuation displacement
Without em dashes, drafts tend to swap in colons and semicolons for every hinge. Allow one colon-hinged sentence per paragraph at most. When every sentence pivots, none of them do.

### Paragraph endings
If every paragraph lands on a short zinger, the zingers become wallpaper. Let some paragraphs stop plainly or run into the next.

### Sentence starters
Watch for crutch openers: "What's interesting is", "The thing about X is", "So," at the top of a paragraph, "Look," anywhere. Start with the subject.

### Quotability
A line built to be screenshotted ("Clarity is a kindness you pay forward") is usually empty. Rewrite it as something specific or cut it.

## 5. Catch the second-generation tells

Once the obvious tells are gone, a cleaner but still synthetic layer shows up. Look for it on the second read.

- **Performed cleverness:** odd adjective-noun pairings that sound literary and mean little ("honest chaos," "a gentle brutality"). Replace with the fact underneath.
- **Wisdom-shaped objects:** sentences with the cadence of insight and no claim anyone could dispute ("Some lessons only arrive late."). Make it specific enough to argue with, or delete it.
- **Perfect balance:** every point qualified, every section the same size, every argument resolved. People write unevenly; they linger where they care.
- **Omniscient casual:** a relaxed voice that is never wrong and never unsure. Real experts show the edges of what they know.

Worked pairs (machine version against the human original, with what changed) are in `${CLAUDE_PLUGIN_ROOT}/skills/no-slops/references/slop-vs-gold.md`.

## 6. Build texture, don't just strip tells

A draft with every tell removed can still read as generated, because it's too even. After cleaning, add back the unevenness a person leaves:

- **Spend unevenly.** Give the part that matters the most room, and squeeze or drop the parts that don't.
- **Mix registers.** A precise term next to a casual one ("the p99 latency, which is to say the bad days") is how people actually talk.
- **Vary shape on purpose, not on a schedule.** A long paragraph because there was more to say; a one-liner because there wasn't. Alternating long and short by rule is its own pattern.
- **Take positions that could be wrong.** "Promising, with caveats" is a dodge. "The benchmark only holds on warm caches" is a position. If there's no take to have, say that instead of inventing balance.
- **Use "I" for real thoughts.** Not "what strikes me is", but "I tried the import twice and it dropped the same three rows both times."

## 7. Score it

Score each dimension from 1 to 10:

| Dimension | Ask |
|---|---|
| Directness | Does it say things, or say that it's about to? |
| Rhythm | Does the length and shape vary like speech, or tick like a metronome? |
| Trust | Does it assume a smart reader, or explain what they already know? |
| Authenticity | Could a specific person have written this, or anyone? |
| Density | Is there a sentence you could delete without losing anything? |

**Under 35 out of 50 doesn't ship.** Revise the lowest-scoring dimension first, then score again.

## 8. Second pass and self-audit

Reread the revised text, not the original: rewrites introduce their own tells (a fresh "furthermore," a copula that crept back, a new Tier 2 pair). Ask yourself, "What here would still make a reader suspect a model?" Write two or three blunt answers, fix them, then score. Stop after one corrective round; a third pass rarely finds anything and usually flattens the voice.

## 9. Severity, channels, and what to preserve

**Severity** (lines up with red-pen's Red, Yellow, Blue):
- **P0 / Red:** §0 artifacts, and vague attribution holding up a factual claim. Never ships.
- **P1 / Yellow:** Tier 1 words, kill-on-sight phrases, and the §2 structures. Fixed before anyone sees the draft.
- **P2 / Blue:** Tier 2 and 3 density, rhythm, texture (§4 to §6). Fixed in revision, with judgment.

**By channel** (em dashes are zero in all of them):

| Channel | How the rules flex |
|---|---|
| Blog, long-form, web pages | Everything at full strength |
| Social | Fragments and platform emoji conventions are allowed; the vocabulary tiers still apply |
| Email | Full strength, except subject lines may be fragments |
| Docs and technical writing | Tier 2 terms with a precise technical meaning (robust, scalable, ecosystem, comprehensive) are fine; the rest at full strength |

**Never add a fact while fixing a tell.** A repair can delete, merge, reorder, or simplify. It can't introduce a name, number, date, quote, source, or claim that the writer or the source didn't provide. Missing a detail? Ask, or write the plainer sentence. An invented specific is worse than the tell it replaced.

**Protect these on sight:**
- Details that are hard to fake: names, figures, dates, things the writer saw
- Ambivalence that the writer didn't resolve
- References that date the piece, and a right word repeated on purpose
- Real asides, self-corrections, and lopsided emphasis

If a cleanup leaves the draft smoother but deader, it went too far; put the life back.

## 10. Sources

The structural and vocabulary catalog started from Wikipedia's "Signs of AI writing" page, maintained by WikiProject AI Cleanup (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), and was checked for gaps against two MIT-licensed humanizer catalogs on GitHub (blader/humanizer and Aboudjem/humanizer-skill). Entries were selected, reorganized, and rewritten for this rulebook's stricter house rules; the worked examples are original.

Re-check the catalog every few months. Tells shift as models change, and a fixed list goes stale.

## 11. The editorial judgment call

The question is never whether a pattern appears. It's whether the writer chose it or the model fell into it. A keynote or a manifesto can carry more rhetoric than a product email. What gives a draft away is density: patterns stacked closer together than a person would ever stack them.

So audit for density first, single instances second. Then read the whole draft aloud, and cut any line that sounds rehearsed.
